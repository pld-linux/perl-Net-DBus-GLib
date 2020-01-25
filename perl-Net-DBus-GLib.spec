#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%define		pdir	Net
%define		pnam	DBus-GLib
Summary:	Net::DBus::GLib - Perl extension for the DBus GLib bindings
Summary(pl.UTF-8):	Net::DBus::GLib - rozszerzenie Perla do dowiązań DBus GLib
Name:		perl-Net-DBus-GLib
Version:	0.33.0
Release:	1
# "same as perl", but GPL in version 2+ is specified afterwards
License:	GPL v2+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d86fac8abef6781e7f652b1062f474ff
URL:		http://search.cpan.org/dist/Net-DBus-GLib/
BuildRequires:	dbus-glib-devel >= 0.33
BuildRequires:	perl-Glib
BuildRequires:	perl-Net-DBus >= 0.33.2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Net-DBus >= 0.33.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::DBus::GLib provides an extension to the Net::DBus module allowing
integration with the GLib mainloop.

%description -l pl.UTF-8
Moduł Net::DBus::GLib udostępnia rozszerzenie modułu Net::DBus
umożliwiające integrację z główną pętlą GLib.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README
%{perl_vendorarch}/Net/DBus/GLib.pm
%dir %{perl_vendorarch}/auto/Net/DBus/GLib
%attr(755,root,root) %{perl_vendorarch}/auto/Net/DBus/GLib/GLib.so
%{_mandir}/man3/Net::DBus::GLib.3pm*
