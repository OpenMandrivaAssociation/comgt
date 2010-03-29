%define old_name gcom

Summary:	GPRS/EDGE/3G/HSDPA datacard control tool
Name:		comgt
Version:	0.32
Release:	%mkrel 10
Source0:	http://www.pharscape.org/3G/%{name}/%{name}.%{version}.tgz
Patch0:		comgt-0.32-string-format.patch
License:	GPLv2+
Group:		Communications
Url:		http://www.pharscape.org/content/view/46/70/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:	%{old_name}
Obsoletes:	%{old_name}

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
%patch0 -p1 -b .str_format~

%build
%make CFLAGS="-c %{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}
install -m755 %{name} -D %{buildroot}%{_sbindir}/%{name}
install -m644 %{name}.1 -D %{buildroot}%{_mandir}/man1/%{name}.1
ln -s %{_sbindir}/%{name} %{buildroot}%{_sbindir}/%{old_name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG gprs.txt TODO umts.txt
%{_sbindir}/%{name}
%{_sbindir}/%{old_name}
%{_mandir}/man1/%{name}.1*
