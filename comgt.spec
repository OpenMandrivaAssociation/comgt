%define name comgt
%define old_name gcom
%define version 0.32
%define release %mkrel 2

Summary: GPRS/EDGE/3G/HSDPA datacard control tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.pharscape.org/3G/%{name}/%{name}.%{version}.tgz
License: GPL
Group: Communications
Url: http://www.pharscape.org/content/view/46/70/
Provides: %{old_name}
Obsoletes: %{old_name}

%description
comgt is a datacard control tool for Option GlobeTrotter
GPRS/EDGE/3G/HSDPA and Vodafone 3G/GPRS.

It is a scripting language interpreter useful for establishing
communications on serial lines and through PCMCIA modems as well as
GPRS and 3G datacards.

comgt has some features that are rarely found in other utilities of the
same type.

%prep
%setup -q -n %{name}.%{version}

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_sbindir}
install -m 755 %{name} $RPM_BUILD_ROOT%{_sbindir}
install -d -m 755 $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 644 %{name}.1 $RPM_BUILD_ROOT/%{_mandir}/man1
ln -s %{_sbindir}/%{name} $RPM_BUILD_ROOT%{_sbindir}/%{old_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGELOG gprs.txt TODO umts.txt
%{_sbindir}/%{name}
%{_sbindir}/%{old_name}
%{_mandir}/man1/%{name}.1*
