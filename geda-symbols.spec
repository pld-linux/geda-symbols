Summary:	symbols of electronic devices
Summary(pl):	symbole elementów elektronicznych
Name:		geda-symbols
Version:	20021103
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.geda.seul.org/devel/%{version}/geda-symbols-%{version}.tar.gz
URL:		http://www.geda.seul.org/
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This package contains a bunch of symbols of electronic devices used by
gschem, the gEDA project schematic editor.

%description -l pl
Pakiet zawiera du¿± ilo¶æ symboli elementów elektronycznych, które s±
u¿ywane w edytorze schematów gschem.

%prep
%setup  -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*-config
%{_datadir}/gEDA
