%define name nethserver-delegation

%define version 0.1.10
%define release 1
Summary: Delegate the usage of  panels to users or groups
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Distribution: NethServer
License: GNU GPL version 2
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz
BuildArchitectures: noarch
BuildRoot: /var/tmp/%{name}-%{version}-buildroot
BuildRequires: nethserver-devtools
AutoReqProv: no

%description
Delegate the usage of  panels to users or groups

%prep
%setup
%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
     > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update

%pre

%post


%changelog
* Fri Oct 5 2018 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.10-1.ns7
- Subscribed to the nethserver-sssd-event

* Fri Aug 24 2018 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.9-1.ns7
- Use sam.ldb to authenticate in samba ldap

* Mon Sep 18 2017 stephane de LAbrusse <stephdl@de-labrusse.fr> 0.1.8-1.ns7
- Allow Admin todo by default

* Sat Sep 09 2017 stephane de LAbrusse <stephdl@de-labrusse.fr> 0.1.7-1.ns7
- ldif file creation with a random name
- chmod ldif file 0600
- remove the key name when the user/group is deleted

* Fri Sep 08 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.6-1.ns7
- Automatic activation of the shell access if the sudo power is enabled

* Sun Aug 06 2017 stephane de labrusse <stephdl@de-labrusse.fr> 0.1.5-1.ns7
- fix unix permissions to sudoers file

* Tue Aug 01 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.4-1.ns7
- The path to the binary is sanitised
- New UI

* Fri Jul 28 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.3-1.ns7
- Sudo delegation per group and user
- values of properties are visible directly in the Table form
- Json check all added, thank nethesis

* Thu Jul 20 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.2-1.ns7
- First release to NS7
- New UI (FIELDSET_EXPANDABLE)

* Wed Jul 12 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.5-1
- start by denying access

* Wed Jun 28 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.4-1
- Created a new specific file DelegatedPanel.json
- Added COPYING
- Created translation files for user and group plugin

* Sun Nov 11 2015 stephane de labrusse <stephdl@de-labrusse.fr> 0.0.3-1
- Added a plugin of delegation in User and Group panel

* Thu Nov 05 2015 stephane de labrusse <stephdl@de-labrusse.fr> 0.0.2-1
- corrected path to template

* Fri Oct 23 2015 stephane de labrusse <stephdl@de-labrusse.fr> 0.0.1-1
- First commit

