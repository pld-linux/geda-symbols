Summary:	Symbols of electronic devices
Summary(pl.UTF-8):	Symbole elementów elektronicznych
Name:		geda-symbols
Version:	1.4.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.geda.seul.org/release/v1.4/%{version}/geda-symbols-%{version}.tar.gz
# Source0-md5:	212f390e71d0fb4188b3a48d5bd8c076
URL:		http://www.geda.seul.org/
#BuildArch:	noarch
Requires:	libgeda
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a bunch of symbols of electronic devices used by
gschem, the gEDA project schematic editor.

%description -l pl.UTF-8
Pakiet zawiera dużą ilość symboli elementów elektronicznych, które są
używane w edytorze schematów gschem.

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
%{_datadir}/gEDA/scheme
%{_datadir}/gEDA/sym
%{_docdir}/geda-doc/nc.pdf
