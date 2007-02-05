Summary:	Symbols of electronic devices
Summary(pl):	Symbole elementów elektronicznych
Name:		geda-symbols
Version:	20061020
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.geda.seul.org/devel/%{version}/geda-symbols-%{version}.tar.gz
# Source0-md5:	a05c9bb11a31c246be3c9a799685bb0e
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
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO AUTHORS ChangeLog NEWS README
%{_datadir}/gEDA/sym
%{_datadir}/gEDA/system-gafrc
