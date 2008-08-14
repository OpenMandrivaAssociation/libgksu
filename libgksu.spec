%define name libgksu
%define version 2.0.7
%define release %mkrel 1

%define fakename gksu2.0

%define major 0
%define libname %mklibname %{fakename}_ %major
%define libnamedev %mklibname %{fakename}_ %major -d

Name: %{name}
Summary: GKSu libraries
Version: %{version}
Release: %{release}
Source: http://people.debian.org/~kov/gksu/libgksu/%{name}-%{version}.tar.gz
Url: http://www.nongnu.org/gksu/
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
License: GPL
BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: libgtop2.0-devel
BuildRequires: startup-notification-devel
BuildRequires: gnome-keyring-devel
BuildRequires: libGConf2-devel
BuildRequires: gtk+2-devel
BuildRequires: libglade2.0-devel
BuildRequires: perl-XML-Parser
BuildRequires: desktop-file-utils
BuildRequires: dbus-glib-devel
Provides: libgksu
Provides: libgksu2
Obsoletes: libgksu1.2

%description
GKSu is a library that provides a Gtk+ frontend to su and sudo. It 
supports login shells and preserving environment when acting as a su
 frontend. It is useful to menu items or other graphical programs 
that need to ask a user's password to run another program as another user.

%package -n %libname
Summary: GKSu libraries
Group: System/Libraries

%description -n %libname
GKSu is a library that provides a Gtk+ frontend to su and sudo. It 
supports login shells and preserving environment when acting as a su 
 frontend. It is useful to menu items or other graphical programs 
that need to ask a user's password to run another program as another user.

%package -n %libnamedev
Summary: Development package for %{name}
Group: Development/Other
Requires: %libname = %version
Provides: libgksu2.0-devel = %version-%release
Provides: libgksu2-devel = %version-%release
Provides: libgksu-devel
Obsoletes: libgksu1.2-devel

%description -n %libnamedev
Development package for %{name}

GKSu is a library that provides a Gtk+ frontend to su and sudo. It 
supports login shells and preserving environment when acting as a su 
 frontend. It is useful to menu items or other graphical programs 
that need to ask a user's password to run another program as another user.

%package -n gksu-utils
Summary: Utilities package for %{name}
Group: System/Base
Requires: %libname = %version

%description -n gksu-utils
Utilities package for %{name}

GKSu is a library that provides a Gtk+ frontend to su and sudo. It
supports login shells and preserving environment when acting as a su
 frontend. It is useful to menu items or other graphical programs
that need to ask a user's password to run another program as another user.

%prep
%setup -q 

%configure2_5x

%build

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="AdvancedSettings" \
  --add-category="Settings" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%post -n gksu-utils
%post_install_gconf_schemas gksu

%preun -n gksu-utils
%preun_uninstall_gconf_schemas gksu

%files -n %libname -f %name.lang
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*
%_libdir/%name

%files -n %libnamedev
%defattr(-,root,root)
%doc INSTALL ChangeLog AUTHORS
%{_libdir}/lib*.a
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/lib*.la
%{_includedir}/*
%_libdir/pkgconfig/*
%_datadir/gtk-doc/html/%name

%files -n gksu-utils
%{_sysconfdir}/gconf/schemas/gksu.schemas
%{_bindir}/gksu-properties
%{_datadir}/applications/gksu-properties.desktop
%{_datadir}/libgksu/gksu-properties.glade
%{_datadir}/pixmaps/gksu.png



