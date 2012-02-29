%define fakename gksu2.0

%define major 0
%define libname %mklibname %{fakename}_ %major
%define develname %mklibname %{fakename} -d

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

BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: libgtop2.0-devel
BuildRequires: startup-notification-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libGConf2-devel
BuildRequires: gtk+2-devel
BuildRequires: perl-XML-Parser
BuildRequires: desktop-file-utils
BuildRequires: dbus-glib-devel
BuildRequires: intltool
Provides: libgksu
Provides: libgksu2
Obsoletes: libgksu1.2

%description
GKSu is a library that provides a Gtk+ frontend to su and sudo. It 
supports login shells and preserving environment when acting as a su
 frontend. It is useful to menu items or other graphical programs 
that need to ask a user's password to run another program as another user.

%package -n %{libname}
Summary: GKSu libraries
Group: System/Libraries

%description -n %{libname}
GKSu is a library that provides a Gtk+ frontend to su and sudo. It 
supports login shells and preserving environment when acting as a su 
 frontend. It is useful to menu items or other graphical programs 
that need to ask a user's password to run another program as another user.

%package -n %{develname}
Summary: Development package for %{name}
Group: Development/Other
Requires: %{libname} = %{version}
Provides: libgksu-devel
Obsoletes: libgksu1.2-devel
Obsoletes: %{_lib}gksu2.0_0-devel

%description -n %{develname}
Development package for %{name}

GKSu is a library that provides a Gtk+ frontend to su and sudo. It 
supports login shells and preserving environment when acting as a su 
 frontend. It is useful to menu items or other graphical programs 
that need to ask a user's password to run another program as another user.

%package -n gksu-utils
Summary: Utilities package for %{name}
Group: System/Base
Requires: %{libname} = %{version}

%description -n gksu-utils
Utilities package for %{name}

GKSu is a library that provides a Gtk+ frontend to su and sudo. It
supports login shells and preserving environment when acting as a su
 frontend. It is useful to menu items or other graphical programs
that need to ask a user's password to run another program as another user.

%prep
%setup -q 
%patch0 -p0 -b .str
%patch1 -p0
%patch2 -p0
%patch3 -p0
touch README NEWS

%build
autoreconf -fi
intltoolize --force
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install --vendor="" \
	--remove-category="Application" \
	--remove-category="AdvancedSettings" \
	--add-category="Settings" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%files -n %{libname} -f %{name}.lang
%{_libdir}/*.so.%{major}*
%{_libdir}/%{name}

%files -n %{develname}
%doc INSTALL ChangeLog AUTHORS
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/gtk-doc/html/%{name}

%files -n gksu-utils
%{_sysconfdir}/gconf/schemas/gksu.schemas
%{_bindir}/gksu-properties
%{_datadir}/man/man1/gksu-properties.1*
%{_datadir}/applications/gksu-properties.desktop
%{_datadir}/libgksu/gksu-properties.ui
%{_datadir}/pixmaps/gksu.png
%{_datadir}/locale/*

