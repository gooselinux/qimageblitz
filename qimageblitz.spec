Summary: Interim image effect library for KDE 4.0
Name:    qimageblitz
Version: 0.0.4
Release: 1%{?dist}

Group:   System Environment/Libraries
License: BSD and ImageMagick
URL:     http://qimageblitz.sourceforge.net/
Source0: http://garr.dl.sourceforge.net/project/qimageblitz/qimageblitz/'QImageBlitz %{version}'/qimageblitz-%{version}.tar.bz2
Patch0:  qimageblitz-0.0.4-noexecstack.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: cmake
BuildRequires: qt4-devel

%description
Blitz is an interim image effect library that people can use until KDE 4.1 is
released. KImageEffect, the old image effect class is being dropped for KDE 4.0
and the replacement, Quasar, won't be ready until KDE 4.1. Blitz gives people
something to use in the meantime.

%package devel
Summary: Developer files for %{name}
Group:   Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: qt4-devel pkgconfig
%description devel
%{summary}.

%package examples
Summary: Example programs for %{name}
Group:   System Environment/Libraries
%description examples
This package contains the blitztest example program for %{name}.

%prep
%setup -q
%patch0 -p1

%build
%cmake .
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc Changelog COPYING README*
%{_libdir}/libqimageblitz.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libqimageblitz.so
%{_libdir}/pkgconfig/qimageblitz.pc
%{_includedir}/qimageblitz/

%files examples
%defattr(-,root,root,-)
%{_bindir}/blitztest

%changelog
* Tue Jan 05 2010 Than Ngo <than@redhat.com> - 0.0.4-1
- use the official 0.0.4

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-0.6.svn706674
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-0.5.svn706674
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 7 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.0.4-0.4.svn706674
- Fix noexecstack patch to disable execstack also on x86_64 (#428036).

* Tue Jan 8 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.0.4-0.3.svn706674
- Apply Debian patch by Sune Vuorela to fix executable stack (#428036).

* Wed Sep 19 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.0.4-0.2.svn706674
- Move blitztest example to its own subpackage.

* Fri Aug 3 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.0.4-0.1.svn706674
- First Fedora package
