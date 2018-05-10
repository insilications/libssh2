#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libssh2
Version  : 1.8.0
Release  : 7
URL      : https://www.libssh2.org/download/libssh2-1.8.0.tar.gz
Source0  : https://www.libssh2.org/download/libssh2-1.8.0.tar.gz
Summary  : Library for SSH-based communication
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libssh2-lib
Requires: libssh2-doc
BuildRequires : cmake
BuildRequires : pkgconfig(openssl)

%description
libssh2 - SSH2 library
======================
libssh2 is a library implementing the SSH2 protocol, available under
the revised BSD license.

%package dev
Summary: dev components for the libssh2 package.
Group: Development
Requires: libssh2-lib
Provides: libssh2-devel

%description dev
dev components for the libssh2 package.


%package doc
Summary: doc components for the libssh2 package.
Group: Documentation

%description doc
doc components for the libssh2 package.


%package lib
Summary: lib components for the libssh2 package.
Group: Libraries

%description lib
lib components for the libssh2 package.


%prep
%setup -q -n libssh2-1.8.0

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
