#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : librsvg
Version  : 2.51.2
Release  : 301
URL      : https://download-fallback.gnome.org/sources/librsvg/2.51/librsvg-2.51.2.tar.xz
Source0  : https://download-fallback.gnome.org/sources/librsvg/2.51/librsvg-2.51.2.tar.xz
Summary  : library that renders svg files
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 LGPL-2.1
Requires: librsvg-bin = %{version}-%{release}
Requires: librsvg-data = %{version}-%{release}
Requires: librsvg-lib = %{version}-%{release}
Requires: librsvg-man = %{version}-%{release}
Requires: glib
Requires: pango
Requires: regex
BuildRequires : asciidoctor
BuildRequires : asciidoctor-bin
BuildRequires : asciidoctor-dev
BuildRequires : atk-dev
BuildRequires : autoconf-archive-dev
BuildRequires : binutils-dev
BuildRequires : binutils-extras
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-gnome
BuildRequires : ca-certs
BuildRequires : ca-certs-static
BuildRequires : cairo-dev
BuildRequires : cargo-edit
BuildRequires : docbook-xml
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : fontconfig-dev
BuildRequires : freetype-dev
BuildRequires : freetype-staticdev
BuildRequires : fribidi-dev
BuildRequires : fribidi-staticdev
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-go
BuildRequires : gcc-go-lib
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gdk-pixbuf
BuildRequires : gdk-pixbuf-dev
BuildRequires : gettext
BuildRequires : git
BuildRequires : glib
BuildRequires : glib-dev
BuildRequires : glib-dev32
BuildRequires : glibc
BuildRequires : glibc-bin
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-doc
BuildRequires : glibc-extras
BuildRequires : glibc-lib-avx2
BuildRequires : glibc-libc32
BuildRequires : glibc-locale
BuildRequires : glibc-nscd
BuildRequires : glibc-staticdev
BuildRequires : glibc-utils
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : googletest-dev
BuildRequires : grep
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : gtk3-dev
BuildRequires : harfbuzz-dev
BuildRequires : harfbuzz-staticdev
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : just
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libpng-dev
BuildRequires : libpng-dev32
BuildRequires : libstdc++
BuildRequires : libstdc++-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt-bin
BuildRequires : llvm
BuildRequires : llvm-bin
BuildRequires : llvm-data
BuildRequires : llvm-dev
BuildRequires : llvm-lib
BuildRequires : llvm-libexec
BuildRequires : llvm-man
BuildRequires : llvm-staticdev
BuildRequires : ncurses-dev
BuildRequires : ninja
BuildRequires : openssl
BuildRequires : openssl-dev
BuildRequires : openssl-dev32
BuildRequires : pandoc
BuildRequires : pandocfilters
BuildRequires : pango
BuildRequires : pango-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkg-config
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-gobject)
BuildRequires : pkgconfig(cairo-png)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(harfbuzz)
BuildRequires : pkgconfig(libcroco-0.6)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(pangoft2)
BuildRequires : regex
BuildRequires : ruby
BuildRequires : rust-std32
BuildRequires : rust-std32-dev
BuildRequires : rustc
BuildRequires : rustc-bin
BuildRequires : rustc-data
BuildRequires : rustc-dev
BuildRequires : rustc-doc
BuildRequires : rustc-libexec
BuildRequires : rustc-man
BuildRequires : rustc-staticdev
BuildRequires : termcolor
BuildRequires : time
BuildRequires : vala
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Test data was taken from the Go distribution, which was in turn taken from the
testregex test suite:

%package bin
Summary: bin components for the librsvg package.
Group: Binaries
Requires: librsvg-data = %{version}-%{release}

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
Requires: librsvg-lib = %{version}-%{release}
Requires: librsvg-bin = %{version}-%{release}
Requires: librsvg-data = %{version}-%{release}
Provides: librsvg-devel = %{version}-%{release}
Requires: librsvg = %{version}-%{release}

%description dev
dev components for the librsvg package.


%package doc
Summary: doc components for the librsvg package.
Group: Documentation
Requires: librsvg-man = %{version}-%{release}

%description doc
doc components for the librsvg package.


%package lib
Summary: lib components for the librsvg package.
Group: Libraries
Requires: librsvg-data = %{version}-%{release}

%description lib
lib components for the librsvg package.


%package man
Summary: man components for the librsvg package.
Group: Default

%description man
man components for the librsvg package.


%package staticdev
Summary: staticdev components for the librsvg package.
Group: Default
Requires: librsvg-dev = %{version}-%{release}

%description staticdev
staticdev components for the librsvg package.


%prep
%setup -q -n librsvg-2.51.2
cd %{_builddir}/librsvg-2.51.2

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622625686
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fPIC -Wl,-z,max-page-size=0x1000 -fvisibility=hidden -flto-partition=none
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common -funroll-loops
export CXXFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export FCFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -Wl,--build-id=sha1"
export CFFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export LDFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread -Wl,--build-id=sha1"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags1 end
%configure  --enable-shared --enable-static --enable-introspection --enable-vala
make  %{?_smp_mflags}    V=1 VERBOSE=1


%install
export SOURCE_DATE_EPOCH=1622625686
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rsvg-convert

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Rsvg-2.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/thumbnailers/librsvg.thumbnailer
/usr/share/vala/vapi/librsvg-2.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/librsvg-2.0/librsvg/rsvg-cairo.h
/usr/include/librsvg-2.0/librsvg/rsvg-features.h
/usr/include/librsvg-2.0/librsvg/rsvg-version.h
/usr/include/librsvg-2.0/librsvg/rsvg.h
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.so
/usr/lib64/librsvg-2.so
/usr/lib64/pkgconfig/librsvg-2.0.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/librsvg/*
/usr/share/gtk-doc/html/rsvg-2.0/RsvgHandle.html
/usr/share/gtk-doc/html/rsvg-2.0/annotation-glossary.html
/usr/share/gtk-doc/html/rsvg-2.0/api-index-full.html
/usr/share/gtk-doc/html/rsvg-2.0/ch01.html
/usr/share/gtk-doc/html/rsvg-2.0/ch02.html
/usr/share/gtk-doc/html/rsvg-2.0/home.png
/usr/share/gtk-doc/html/rsvg-2.0/index.html
/usr/share/gtk-doc/html/rsvg-2.0/left-insensitive.png
/usr/share/gtk-doc/html/rsvg-2.0/left.png
/usr/share/gtk-doc/html/rsvg-2.0/licence.html
/usr/share/gtk-doc/html/rsvg-2.0/object-tree.html
/usr/share/gtk-doc/html/rsvg-2.0/recommendations-assets.html
/usr/share/gtk-doc/html/rsvg-2.0/right-insensitive.png
/usr/share/gtk-doc/html/rsvg-2.0/right.png
/usr/share/gtk-doc/html/rsvg-2.0/rsvg-2.0.devhelp2
/usr/share/gtk-doc/html/rsvg-2.0/rsvg-Using-RSVG-with-GIO.html
/usr/share/gtk-doc/html/rsvg-2.0/rsvg-Using-RSVG-with-GdkPixbuf.html
/usr/share/gtk-doc/html/rsvg-2.0/rsvg-Using-RSVG-with-cairo.html
/usr/share/gtk-doc/html/rsvg-2.0/rsvg-Version-checks.html
/usr/share/gtk-doc/html/rsvg-2.0/rsvg.html
/usr/share/gtk-doc/html/rsvg-2.0/style.css
/usr/share/gtk-doc/html/rsvg-2.0/up-insensitive.png
/usr/share/gtk-doc/html/rsvg-2.0/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/librsvg-2.so.2
/usr/lib64/librsvg-2.so.2.48.0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/rsvg-convert.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.a
/usr/lib64/librsvg-2.a
