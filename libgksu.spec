%define name libgksu
%define version 2.0.12
%define release %mkrel 4

%define fakename gksu2.0

%define major 0
%define libname %mklibname %{fakename}_ %major
%define libnamedev %mklibname %{fakename}_ %major -d

Name: %{name}
Summary: GKSu libraries
Version: %{version}
Release: %{release}
Source: http://people.debian.org/~kov/gksu/%{name}-%{version}.tar.gz
Patch0:	libgksu-2.0.12-fix-str-fmt.patch
Patch1:	libgksu-2.0.9-fix_lib64_detection.patch
Patch2: libgksu-2.0.12-fix-build.patch
Patch3: Makefile.am.patch
Patch4: libgksu-automake-1.13.patch
Url: http://www.nongnu.org/gksu/
Group: System/Libraries
License: LGPLv2+
BuildRequires: gtk-doc
BuildRequires: libgtop2.0-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: startup-notification-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libGConf2-devel
BuildRequires: gtk+2-devel
BuildRequires: perl-XML-Parser
BuildRequires: desktop-file-utils
BuildRequires: dbus-glib-devel
BuildRequires: intltool
BuildRequires: libx11
BuildRequires: pkgconfig(pkg-config)
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
%patch0 -p0 -b .str
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p1 -b .am113~
touch README NEWS
#sed -i 's:dist_pkglibexec_SCRIPTS:dist_pkgdata_SCRIPTS:g' \
#                $(grep -l dist_pkglibexec_SCRIPTS $(find . -name Makefile.am))

%build
autoreconf -fi
%configure2_5x LIBS="-lX11"
%make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="AdvancedSettings" \
  --add-category="Settings" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%clean
rm -rf %{buildroot}

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

%files -n %libname 
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*
%_libdir/%name

%files -n %libnamedev
%defattr(-,root,root)
%doc INSTALL ChangeLog AUTHORS
%{_libdir}/lib*.a
%{_libdir}/*.so
%{_includedir}/*
%_libdir/pkgconfig/*
%_datadir/gtk-doc/html/%name

%files -n gksu-utils
%{_sysconfdir}/gconf/schemas/gksu.schemas
%{_bindir}/gksu-properties
%{_datadir}/man/man1/gksu-properties.1*
%{_datadir}/applications/gksu-properties.desktop
%{_datadir}/libgksu/gksu-properties.ui
%{_datadir}/pixmaps/gksu.png





%changelog
* Wed Feb 22 2012 abf
- The release updated by ABF

* Wed Feb 22 2012 abf
- The release updated by ABF

* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 2.0.12-2mdv2011.0
+ Revision: 677115
- rebuild to add gconf2 as req

* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 2.0.12-1mdv2011.0
+ Revision: 565336
- new version 2.0.12

* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 2.0.11-2mdv2010.0
+ Revision: 438606
- rebuild

  + Frederik Himpe <fhimpe@mandriva.org>
    - Update to new version 2.0.11

* Mon Apr 13 2009 Michael Scherer <misc@mandriva.org> 2.0.9-2mdv2009.1
+ Revision: 366765
- fix gksu on 64b system, as this was using the wrong path
- fix the license

* Sat Mar 07 2009 Emmanuel Andry <eandry@mandriva.org> 2.0.9-1mdv2009.1
+ Revision: 352670
- BR intltool
- New version 2.0.9
- diff P0 to fix string format not literal

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.7-2mdv2009.1
+ Revision: 301581
- rebuilt against new libxcb

* Thu Aug 14 2008 Emmanuel Andry <eandry@mandriva.org> 2.0.7-1mdv2009.0
+ Revision: 271961
- BR dbus?\195-glib-devel
- New version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jul 03 2007 Emmanuel Andry <eandry@mandriva.org> 2.0.5-1mdv2008.0
+ Revision: 47621
- new version

* Fri Jun 22 2007 Thierry Vignaud <tv@mandriva.org> 2.0.4-2mdv2008.0
+ Revision: 43013
- remove "AdvancedSettings" category from menu
- kill X-MandrivaLinux-System-Configuration-Other
- fix group


* Tue Mar 06 2007 Emmanuel Andry <eandry@mandriva.org> 2.0.4-1mdv2007.0
+ Revision: 134081
- New version 2.0.4
- disable gtk-doc (build problem)

* Tue Feb 20 2007 Götz Waschk <waschk@mandriva.org> 2.0.3-5mdv2007.1
+ Revision: 123029
- fix scripts

* Sat Jan 27 2007 Emmanuel Andry <eandry@mandriva.org> 2.0.3-4mdv2007.1
+ Revision: 114416
- xdg menu
  handles gconf schemas

* Sat Jan 06 2007 Emmanuel Andry <eandry@mandriva.org> 2.0.3-3mdv2007.1
+ Revision: 104863
- fix provides

* Sat Jan 06 2007 Emmanuel Andry <eandry@mandriva.org> 2.0.3-2mdv2007.1
+ Revision: 104797
- rebuild

* Sat Jan 06 2007 Emmanuel Andry <eandry@mandriva.org> 2.0.3-1mdv2007.1
+ Revision: 104663
- buildrequires perl-XML-Parser
- buildrequires libglade2.0-devel
- buildrequires libGConf2-devel
  buildrequires gtk+2-devel
- buildrequires startup-notification-devel
  gnome-keyring-devel
- New version 2.0.3
  fix provides
  buildrequires libgtop2.0-devel

  + Jérôme Soyer <saispo@mandriva.org>
    - Import libgksu

