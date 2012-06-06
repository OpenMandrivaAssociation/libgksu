%define fakename gksu2.0

%define major 0
%define libname %mklibname %{fakename}_ %major
%define devname %mklibname %{fakename} -d

Name: libgksu
Summary: GKSu libraries
Version: 2.0.12
Release: 4
License: LGPLv2+
Group: System/Libraries
Url: http://www.nongnu.org/gksu/
Source0: http://people.debian.org/~kov/gksu/%{name}-%{version}.tar.gz
Patch0:	libgksu-2.0.12-fix-str-fmt.patch
Patch1:	libgksu-2.0.9-fix_lib64_detection.patch
Patch2: libgksu-2.0.12-fix-build.patch
Patch3:	libgksu-2.0.12-ru.patch

BuildRequires:	desktop-file-utils
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(gnome-keyring-1)

Provides:	libgksu
Provides:	libgksu2
Obsoletes:	libgksu1.2

%description
GKSu is a library that provides a Gtk+ frontend to su and sudo. It 
supports login shells and preserving environment when acting as a su
 frontend. It is useful to menu items or other graphical programs 
that need to ask a user's password to run another program as another user.

%package -n gksu-utils
Summary:	Utilities package for %{name}
Group:		System/Base
Requires:	%{libname} = %{version}

%description -n gksu-utils
Utilities package for %{name}

GKSu is a library that provides a Gtk+ frontend to su and sudo. It
supports login shells and preserving environment when acting as a su
 frontend. It is useful to menu items or other graphical programs
that need to ask a user's password to run another program as another user.

%package -n %{libname}
Summary:	GKSu libraries
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Development package for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides:	%{name}-devel
Obsoletes:	libgksu1.2-devel
Obsoletes:	%{_lib}gksu2.0_0-devel

%description -n %{devname}
Development package for %{name}

%prep
%setup -q 
%patch0 -p0 -b .str
%patch1 -p0
%patch2 -p0
%patch3 -p0
touch README NEWS

intltoolize --force

%build
%configure2_5x \
	--disable-static

# fix single spaces for tabbed indent
sed -i "s|^        if|	if|g" \
	Makefile

# autoreconf for patch1 fails
sed -i "s|@LIB@|%{_lib}|g" \
	libgksu/libgksu.c

%make LIBS='-lX11 -lgtk-x11-2.0'

%install
%makeinstall_std

desktop-file-install --vendor="" \
	--remove-category="Application" \
	--remove-category="AdvancedSettings" \
	--add-category="Settings" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%files -n gksu-utils -f %{name}.lang
%{_sysconfdir}/gconf/schemas/gksu.schemas
%{_bindir}/gksu-properties
%{_datadir}/applications/gksu-properties.desktop
%{_datadir}/libgksu/gksu-properties.ui
%{_datadir}/pixmaps/gksu.png
#{_datadir}/locale/*
%{_mandir}/man1/gksu-properties.1*

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/%{name}

%files -n %{devname}
%doc INSTALL ChangeLog AUTHORS
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/gtk-doc/html/%{name}

