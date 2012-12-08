%define old_name gcom

Summary:	GPRS/EDGE/3G/HSDPA datacard control tool
Name:		comgt
Version:	0.32
Release:	%mkrel 13
Source0:	http://www.pharscape.org/3G/%{name}/%{name}.%{version}.tgz
Patch0:		comgt-0.32-string-format.patch
Patch1:		comgt-0.32-fix-man-page-typo.patch
License:	GPLv2+
Group:		Communications
URL:		http://pharscape.org/comgt.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:	%{old_name}
Obsoletes:	%{old_name}
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
%patch0 -p1 -b .str_format~
%patch1 -p1 -b .man_typo~

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
%defattr(644,root,root,755)
%doc CHANGELOG gprs.txt TODO umts.txt
%{_mandir}/man1/%{name}.1*
%defattr(755,root,root,755)
%{_sbindir}/%{name}
%{_sbindir}/%{old_name}


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.32-13mdv2011.0
+ Revision: 663391
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.32-12mdv2011.0
+ Revision: 603842
- rebuild

* Wed May 19 2010 Olivier Blin <oblin@mandriva.com> 0.32-11mdv2010.1
+ Revision: 545448
- require usb_modeswitch since most modems needs to switched explicitely to 3G mode nowadays (#57544)

* Mon Mar 29 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.32-10mdv2010.1
+ Revision: 528749
- fix permissions of docs
- fix typo in man page (P1)
- update URL
- build with %%optflags & %%ldflags
- fix build with -Werror=format-security (P0)
- be more accurate on GPL versioning for license
- don't define name, version & release on top of spec
- cosmetics

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.32-9mdv2010.1
+ Revision: 520030
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.32-8mdv2010.0
+ Revision: 413258
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.32-7mdv2009.1
+ Revision: 350729
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.32-6mdv2009.0
+ Revision: 220507
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.32-5mdv2008.1
+ Revision: 149125
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jun 26 2007 Adam Williamson <awilliamson@mandriva.org> 0.32-2mdv2008.0
+ Revision: 44575
- restore gcom (needed for drakconnect)

* Wed Jun 20 2007 Adam Williamson <awilliamson@mandriva.org> 0.32-1mdv2008.0
+ Revision: 41675
- new release 0.32; rebuild for 2008
- Import comgt



* Thu Sep  7 2006 Olivier Blin <blino@seggie.mandriva.com> 0.3-2mdv2007.0
- gcom has changed name to comgt

* Thu Apr 20 2006 Olivier Blin <oblin@mandriva.com> 0.3-1mdk
- initial release
