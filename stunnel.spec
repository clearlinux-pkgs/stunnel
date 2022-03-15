#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2EFC7FF0D416E014 (Michal.Trojnara@mirt.net)
#
Name     : stunnel
Version  : 5.63
Release  : 18
URL      : https://www.stunnel.org/downloads/stunnel-5.63.tar.gz
Source0  : https://www.stunnel.org/downloads/stunnel-5.63.tar.gz
Source1  : https://www.stunnel.org/downloads/stunnel-5.63.tar.gz.asc
Summary  : An TLS-encrypting socket wrapper
Group    : Development/Tools
License  : GPL-2.0
Requires: stunnel-bin = %{version}-%{release}
Requires: stunnel-data = %{version}-%{release}
Requires: stunnel-lib = %{version}-%{release}
Requires: stunnel-license = %{version}-%{release}
Requires: stunnel-man = %{version}-%{release}
Requires: stunnel-services = %{version}-%{release}
BuildRequires : net-tools
BuildRequires : nmap
BuildRequires : nmap-extras
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(systemd)
BuildRequires : procps-ng
Patch1: 0001-Prepare-systemd-service.patch

%description
Stunnel is a socket wrapper which can provide TLS (Transport Layer Security) support to ordinary applications. For example, it can be used
in conjunction with imapd to create an TLS secure IMAP server.

%package bin
Summary: bin components for the stunnel package.
Group: Binaries
Requires: stunnel-data = %{version}-%{release}
Requires: stunnel-license = %{version}-%{release}
Requires: stunnel-services = %{version}-%{release}

%description bin
bin components for the stunnel package.


%package data
Summary: data components for the stunnel package.
Group: Data

%description data
data components for the stunnel package.


%package doc
Summary: doc components for the stunnel package.
Group: Documentation
Requires: stunnel-man = %{version}-%{release}

%description doc
doc components for the stunnel package.


%package lib
Summary: lib components for the stunnel package.
Group: Libraries
Requires: stunnel-data = %{version}-%{release}
Requires: stunnel-license = %{version}-%{release}

%description lib
lib components for the stunnel package.


%package license
Summary: license components for the stunnel package.
Group: Default

%description license
license components for the stunnel package.


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
%setup -q -n stunnel-5.63
cd %{_builddir}/stunnel-5.63
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647381706
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
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
export SOURCE_DATE_EPOCH=1647381706
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/stunnel
cp %{_builddir}/stunnel-5.63/COPYING.md %{buildroot}/usr/share/package-licenses/stunnel/b258a68362e907b7c6e543832c211402035fd121
cp %{_builddir}/stunnel-5.63/tools/stunnel.license %{buildroot}/usr/share/package-licenses/stunnel/bca24c139b07290a4d4ca3445bac1e3ddf5653fb
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

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/stunnel.bash

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/stunnel/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/stunnel/libstunnel.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/stunnel/b258a68362e907b7c6e543832c211402035fd121
/usr/share/package-licenses/stunnel/bca24c139b07290a4d4ca3445bac1e3ddf5653fb

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/stunnel.8
/usr/share/man/man8/stunnel.pl.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/stunnel.service
