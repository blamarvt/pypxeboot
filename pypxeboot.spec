Summary: A simple python-based bootloader to fake PXE booting for Xen DomUs.
Name:    pypxeboot
Version: 0.0.3
Release: 1
Group:   System Environment/Daemons
License: GPL
Vendor: Grid-Ireland
URL: http://grid.ie/pypxeboot
Source0: pypxeboot-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
#BuildRequires: 
Requires: udhcp == 0.9.8-1usermac, python-tftpy
#ExclusiveArch: i386 i686 x86_64

%description
pypxeboot uses a modified version of udhcpc that allows MAC address to be passed on
the command line. Also uses tftpy to download configuration and images.

%prep 
%setup -q

%build
# nothing to build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/udhcpc
mkdir -p %{buildroot}/usr/share/pypxeboot
install pypxeboot %{buildroot}/usr/bin/pypxeboot
install README %{buildroot}/usr/share/pypxeboot/README
install COPYING %{buildroot}/usr/share/pypxeboot/COPYING
install AUTHORS %{buildroot}/usr/share/pypxeboot/AUTHORS
install outputpy.udhcp.sh %{buildroot}/usr/share/udhcpc/outputpy.udhcp.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/*
/usr/share/udhcpc/outputpy.udhcp.sh
/usr/share/pypxeboot/*

%changelog
* Wed Feb  17 2009 David O'Callaghan <david.ocallaghan@cs.tcd.ie> - [0.0.3-1]
- incorporated new version from Magnus Leuthner, Aethernet
* Fri Feb  16 2007 Stephen Childs <childss@cs.tcd.ie> - [0.0.2-1]
- better management of downloaded kernels
- changed requirement to require modified udhcp
* Tue Feb  6 2007 Kurt Hackel <kurt.hackel@oracle.com> - [0.0.1-1]
- initial version of specfile
