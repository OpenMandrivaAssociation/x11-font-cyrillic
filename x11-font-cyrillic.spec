Name: x11-font-cyrillic
Version: 1.0.0
Release: %mkrel 9
Summary: X11 fonts cyrillic
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPL
BuildArch: noarch
BuildRequires: fontconfig

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
