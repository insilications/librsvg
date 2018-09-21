#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : librsvg
Version  : 2.42.0
Release  : 27
URL      : https://github.com/GNOME/librsvg/archive/2.42.0.tar.gz
Source0  : https://github.com/GNOME/librsvg/archive/2.42.0.tar.gz
Source1  : http://localhost/cgit/projects/cargo-librsvg/snapshot/cargo-librsvg-2.42.0.tar.gz
Summary  : library that renders svg files
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause GPL-2.0 LGPL-2.0 MIT MPL-2.0-no-copyleft-exception Unlicense
Requires: librsvg-bin
Requires: librsvg-lib
Requires: librsvg-data
Requires: librsvg-doc
BuildRequires : atk-dev
BuildRequires : atk-dev32
BuildRequires : cargo
BuildRequires : docbook-xml
BuildRequires : freetype-dev
BuildRequires : freetype-dev32
BuildRequires : fribidi-dev
BuildRequires : fribidi-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : gtk3-dev
BuildRequires : gtk3-dev32
BuildRequires : libpng-dev
BuildRequires : libpng-dev32
BuildRequires : libxslt-bin
BuildRequires : pango-dev
BuildRequires : pango-dev32
BuildRequires : pkgconfig(32cairo)
BuildRequires : pkgconfig(32cairo-png)
BuildRequires : pkgconfig(32fontconfig)
BuildRequires : pkgconfig(32gdk-pixbuf-2.0)
BuildRequires : pkgconfig(32gio-2.0)
BuildRequires : pkgconfig(32gio-unix-2.0)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32gmodule-2.0)
BuildRequires : pkgconfig(32gthread-2.0)
BuildRequires : pkgconfig(32libcroco-0.6)
BuildRequires : pkgconfig(32libxml-2.0)
BuildRequires : pkgconfig(32pangocairo)
BuildRequires : pkgconfig(32pangoft2)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-png)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(libcroco-0.6)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(pangoft2)
BuildRequires : rust-std32
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
Patch1: 0001-Add-cargo-config-file.patch

%description
Test data was taken from the Go distribution, which was in turn taken from the
testregex test suite:

%package bin
Summary: bin components for the librsvg package.
Group: Binaries
Requires: librsvg-data

%description bin
bin components for the librsvg package.


%package data
Summary: data components for the librsvg package.
Group: Data

%description data
data components for the librsvg package.


%package dev
Summary: dev components for the librsvg package.
Group: Development
Requires: librsvg-lib
Requires: librsvg-bin
Requires: librsvg-data
Provides: librsvg-devel

%description dev
dev components for the librsvg package.


%package dev32
Summary: dev32 components for the librsvg package.
Group: Default
Requires: librsvg-lib32
Requires: librsvg-bin
Requires: librsvg-data
Requires: librsvg-dev

%description dev32
dev32 components for the librsvg package.


%package doc
Summary: doc components for the librsvg package.
Group: Documentation

%description doc
doc components for the librsvg package.


%package lib
Summary: lib components for the librsvg package.
Group: Libraries
Requires: librsvg-data

%description lib
lib components for the librsvg package.


%package lib32
Summary: lib32 components for the librsvg package.
Group: Default
Requires: librsvg-data

%description lib32
lib32 components for the librsvg package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n librsvg-2.42.0
mkdir -p %{_topdir}/BUILD/librsvg-2.42.0/rust/vendor
mv %{_topdir}/BUILD/cargo-librsvg-2.42.0/* %{_topdir}/BUILD/librsvg-2.42.0/rust/vendor
%patch1 -p1
pushd ..
cp -a librsvg-2.42.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526071522
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%autogen --disable-static --enable-introspection
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%autogen --disable-static --enable-introspection  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags} CARGO_TARGET_ARGS=--target=i586-unknown-linux-gnu RUST_LIB=rust/target/i586-unknown-linux-gnu/release/librsvg_internals.a
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1526071522
rm -rf %{buildroot}
pushd ../build32/
%make_install32  RUST_LIB=rust/target/i586-unknown-linux-gnu/release/librsvg_internals.a
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)
/usr/lib32/girepository-1.0/Rsvg-2.0.typelib

%files bin
%defattr(-,root,root,-)
/usr/bin/rsvg-convert
/usr/bin/rsvg-view-3

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Rsvg-2.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/thumbnailers/librsvg.thumbnailer

%files dev
%defattr(-,root,root,-)
/usr/include/librsvg-2.0/librsvg/librsvg-enum-types.h
/usr/include/librsvg-2.0/librsvg/librsvg-features.h
/usr/include/librsvg-2.0/librsvg/rsvg-cairo.h
/usr/include/librsvg-2.0/librsvg/rsvg.h
/usr/lib64/librsvg-2.so
/usr/lib64/pkgconfig/librsvg-2.0.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/librsvg-2.so
/usr/lib32/pkgconfig/32librsvg-2.0.pc
/usr/lib32/pkgconfig/librsvg-2.0.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/librsvg/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.so
/usr/lib64/librsvg-2.so.2
/usr/lib64/librsvg-2.so.2.42.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.so
/usr/lib32/librsvg-2.so.2
/usr/lib32/librsvg-2.so.2.42.0
