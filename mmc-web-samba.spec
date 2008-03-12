%define _requires_exceptions pear(graph\\|pear(includes\\|pear(modules
%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	SAMBA module for the MMC web interface
Name:		mmc-web-samba
Version:	2.3.0
Release:	%mkrel 1
License:	GPL
Group:		System/Servers
URL:		http://mds.mandriva.org/
Source0:	%{name}-%{version}.tar.gz
Patch0:		mmc-web-samba-Makefile_fix.diff
Requires:	samba-server samba-vscan-clamav
Requires:	mmc-web-base >= 2.3.0
Requires:	nss_ldap
BuildArch:      noarch
Buildroot:	%{_tmppath}/%{name}-buildroot

%description
Mandriva Management Console web interface designed by Linbox.

This is the SAMBA module.

%prep

%setup -q -n %{name}-%{version}

for i in `find . -type d -name .svn`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%patch0 -p0

%build

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc COPYING Changelog
%{_datadir}/mmc/modules/samba
