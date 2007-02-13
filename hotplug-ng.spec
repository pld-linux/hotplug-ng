# TODO
# - link with klibc + bcond
#
# Conditional build:
%bcond_with	verbose		# verbose build (V=1)
#
Summary:	hotplug-ng - /sbin/hotplug replacement and auto module loader in C
Summary(pl.UTF-8):	hotplug-ng - zamiennik /sbin/hotplug i automatyczny loader do modułów w C
Name:		hotplug-ng
Version:	002
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://kernel.org/pub/linux/utils/kernel/hotplug/%{name}-%{version}.tar.bz2
# Source0-md5:	a302ec0a7110c4f598f655d877eb8875
Patch0:		%{name}-Makefile.patch
Provides:	hotplug = 2005
Obsoletes:	hotplug
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
hotplug-ng - a /sbin/hotplug replacement and auto module loader in C.
It currently provides the following:
- a /sbin/hotplug multiplexer. Works identical to the existing bash
  /sbin/hotplug.
- autoload programs for usb, scsi, and pci modules. These programs
  determine what module needs to be loaded when the kernel emits a
  hotplug event for these types of devices. This works just like the
  existing linux-hotplug scripts, with a few exceptions.

%description -l pl.UTF-8
hotplug-ng to zamiennik /sbin/hotplug i program do automatycznego
ładowania modułów napisany w C. Aktualnie dostarcza:
- multiplekser /sbin/hotplug - działa tak samo, jak istniejący
  /sbin/hotplug w bashu,
- programy do automatycznego ładowania modułów usb, scsi i pci -
  określają, który moduł musi być załadowany, kiedy jądro generuje
  zdarzenie hotplug dla tych rodzajów urządzeń; działa to tak, jak
  istniejące skrypty linux-hotplug, z paroma wyjątkami.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	HOSTCC="%{__cc}" \
	DEBUG=%{!?debug:false}%{?debug:true} \
	OPTIMIZATION="%{rpmcflags}" \
	USE_LOG=true \
	%{?with_verbose:V=1}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/hotplug.d/default

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_sbindir}/*
%{_sysconfdir}/hotplug.d
%{_mandir}/man8/*
