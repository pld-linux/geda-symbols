Summary:	symbols of electronic devices
Summary(pl):	symbole elementów elektronicznych
Name:		geda-symbols
Version:	20010304
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Source0:	ftp://ftp.geda.seul.org/pub/geda/devel/symbols-%{version}.tar.gz
URL:		http://www.geda.seul.org/
# FIXME. It should be noarch but rpm breaks attr() then.
# BuildArch:	noarch
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
%setup  -q -n symbols

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

gzip -9nf TODO AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*-config
%{_datadir}/gEDA
