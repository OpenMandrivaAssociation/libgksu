%define sname	gksu
%define api	2
%define major	0
%define libname %mklibname %{sname} %{api} %{major}
%define devname %mklibname %{sname} -d

Summary:	GKSu libraries
Name:		libgksu
Version:	2.0.12
Release:	7
Url:		http://www.nongnu.org/gksu/
Group:		System/Libraries
License:	LGPLv2+
Source0:	http://people.debian.org/~kov/gksu/%{name}-%{version}.tar.gz
Patch0:		libgksu-2.0.12-fix-str-fmt.patch
Patch1:		libgksu-2.0.9-fix_lib64_detection.patch
Patch2:		libgksu-2.0.12-fix-build.patch
Patch3:		Makefile.am.patch
Patch4:		libgksu-automake-1.13.patch

BuildRequires:	desktop-file-utils
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)

%description
GKSu is a library that provides a Gtk+ frontend to su and sudo. It 
supports login shells and preserving environment when acting as a su
 frontend. It is useful to menu items or other graphical programs 
that need to ask a user's password to run another program as another user.

%package -n gksu-utils
Summary:	Utilities package for %{name}
Group:		System/Base
Requires:	%{libname} = %{version}-%{release}

%description -n gksu-utils
Utilities package for %{name}

%package -n %{libname}
Summary:	GKSu libraries
Group:		System/Libraries
Obsoletes:	%{_lib}gksu2.0_0 < 2.0.12-6

%description -n %{libname}
GKSu is a library that provides a Gtk+ frontend to su and sudo. It 
supports login shells and preserving environment when acting as a su 
frontend. It is useful to menu items or other graphical programs 
that need to ask a user's password to run another program as another user.

%package -n %{devname}
Summary:	Development package for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}gksu2.0_0-devel < 2.0.12-6
Obsoletes:	%{_lib}gksu2.0-devel < 2.0.12-6

%description -n %{devname}
Development package for %{name}

%prep
%setup -q 
%apply_patches
touch README NEWS
autoreconf -fi

%build
%configure2_5x \
	--disable-static \
	LIBS="-lX11"
%make

%install
%makeinstall_std

desktop-file-install --vendor="" \
	--remove-category="Application" \
	--remove-category="AdvancedSettings" \
	--add-category="Settings" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%preun -n gksu-utils
%preun_uninstall_gconf_schemas gksu

%files -n gksu-utils
%{_sysconfdir}/gconf/schemas/gksu.schemas
%{_bindir}/gksu-properties
%{_datadir}/applications/gksu-properties.desktop
%{_datadir}/libgksu/gksu-properties.ui
%{_datadir}/pixmaps/gksu.png
%{_mandir}/man1/gksu-properties.1*

%files -n %{libname} 
%{_libdir}/libgksu2.so.%{major}*
%{_libdir}/%name

%files -n %{devname}
%doc INSTALL ChangeLog AUTHORS
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%doc %{_datadir}/gtk-doc/html/%name

