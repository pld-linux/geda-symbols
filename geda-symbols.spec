Summary:	Symbols of electronic devices
Summary(pl):	Symbole elementów elektronicznych
Name:		geda-symbols
Version:	20030901
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.geda.seul.org/devel/%{version}/geda-symbols-%{version}.tar.gz
# Source0-md5:	5d5c3d58ce99d233d662378bb6ba40cf
URL:		http://www.geda.seul.org/
#BuildArch:	noarch
Requires:	libgeda
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a bunch of symbols of electronic devices used by
gschem, the gEDA project schematic editor.

%description -l pl
Pakiet zawiera du¿± ilo¶æ symboli elementów elektronicznych, które s±
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
%{_datadir}/gEDA/sym
%{_datadir}/gEDA/system-commonrc
