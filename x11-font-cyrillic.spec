Name: x11-font-cyrillic
Version: 1.0.0
Release: 16
Summary: X11 fonts cyrillic
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPL
BuildArch: noarch

Obsoletes: xorg-x11-cyrillic-fonts

Requires: x11-font-alias
Requires: x11-font-cronyx-cyrillic
Requires: x11-font-misc-cyrillic
Requires: x11-font-screen-cyrillic
Requires: x11-font-winitzki-cyrillic

%description
The Cyrillic fonts included with Xorg. Those who use a language requiring the
Cyrillic character set should install this package.

%files
%defattr(-,root,root)


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0.0-10mdv2011.0
+ Revision: 675583
- rebuild
- br fontconfig for fc-query used in new rpm-setup-build

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-9
+ Revision: 671203
- mass rebuild

* Fri Feb 05 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.0-8mdv2011.0
+ Revision: 501206
- Obsolete xorg-x11-cyrillic-fonts and fix description

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-7mdv2009.0
+ Revision: 225987
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-6mdv2008.1
+ Revision: 179651
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-5mdv2008.0
+ Revision: 75828
- rebuild


* Mon Sep 18 2006 Pixel <pixel@mandriva.com>
+ 2006-09-18 16:20:28 (61945)
- do not obsolete/provide Obsoletes: xorg-x11-cyrillic-fonts <= 6.9.0xorg-x11-server which is still a package in 2007.0

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 19:54:51 (26912)
- fixed more dependencies

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

