#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2EFC7FF0D416E014 (Michal.Trojnara@mirt.net)
#
Name     : stunnel
Version  : 5.69
Release  : 25
URL      : https://www.stunnel.org/downloads/stunnel-5.69.tar.gz
Source0  : https://www.stunnel.org/downloads/stunnel-5.69.tar.gz
Source1  : https://www.stunnel.org/downloads/stunnel-5.69.tar.gz.asc
Summary  : An TLS-encrypting socket wrapper
Group    : Development/Tools
License  : GPL-2.0
Requires: stunnel-bin = %{version}-%{release}
Requires: stunnel-lib = %{version}-%{release}
Requires: stunnel-man = %{version}-%{release}
Requires: stunnel-services = %{version}-%{release}
BuildRequires : net-tools
BuildRequires : nmap
BuildRequires : nmap-extras
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(systemd)
BuildRequires : procps-ng
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Prepare-systemd-service.patch

%description
Stunnel is a socket wrapper which can provide TLS (Transport Layer Security) support to ordinary applications. For example, it can be used
in conjunction with imapd to create an TLS secure IMAP server.

%package bin
Summary: bin components for the stunnel package.
Group: Binaries
Requires: stunnel-services = %{version}-%{release}

%description bin
bin components for the stunnel package.


%package doc
Summary: doc components for the stunnel package.
Group: Documentation
Requires: stunnel-man = %{version}-%{release}

%description doc
doc components for the stunnel package.


%package lib
Summary: lib components for the stunnel package.
Group: Libraries

%description lib
lib components for the stunnel package.


%package man
Summary: man components for the stunnel package.
Group: Default

%description man
man components for the stunnel package.


%package services
Summary: services components for the stunnel package.
Group: Systemd services

%description services
services components for the stunnel package.


%prep
%setup -q -n stunnel-5.69
cd %{_builddir}/stunnel-5.69
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1677980849
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static --disable-libwrap \
--disable-fips
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1677980849
rm -rf %{buildroot}
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/bin/stunnel3
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system
mv %{buildroot}/usr/share/doc/stunnel/examples/stunnel.service %{buildroot}/usr/lib/systemd/system/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/stunnel

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/stunnel/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/stunnel/libstunnel.so

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/stunnel.8
/usr/share/man/man8/stunnel.pl.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/stunnel.service
