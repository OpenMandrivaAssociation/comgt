%define old_name gcom

Summary:	GPRS/EDGE/3G/HSDPA datacard control tool
Name:		comgt
Version:	0.32
Release:	17
License:	GPLv2+
Group:		Communications
Url:		http://pharscape.org/comgt.html
Source0:	http://www.pharscape.org/3G/%{name}/%{name}.%{version}.tgz
Patch0:		comgt-0.32-string-format.patch
Patch1:		comgt-0.32-fix-man-page-typo.patch
Requires:	usb_modeswitch

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
%apply_patches

%build
%make CFLAGS="-c %{optflags}" LDFLAGS="%{ldflags}"

%install
install -m755 %{name} -D %{buildroot}%{_sbindir}/%{name}
install -m644 %{name}.1 -D %{buildroot}%{_mandir}/man1/%{name}.1
ln -s %{_sbindir}/%{name} %{buildroot}%{_sbindir}/%{old_name}

%files
%doc CHANGELOG gprs.txt TODO umts.txt
%{_mandir}/man1/%{name}.1*
%{_sbindir}/%{name}
%{_sbindir}/%{old_name}

