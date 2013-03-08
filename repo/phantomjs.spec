Summary:	a headless WebKit with JavaScript API
Name:		phantomjs
Version:	%(cat /var/lib/dinamize/base/%{name}/VERSION)
Release:	%(cat /var/lib/dinamize/base/%{name}/RELEASE)
License:	BSD
Packager:	Matthew Barr <mbarr@snap-interactive.com>
Group:		Utilities/Misc
BuildRoot:	%{_tmppath}/%{name}-root
Source0:        %{name}-%{version}-%{release}.tar.gz

Requires:	xorg-x11-fonts-Type1

%description
PhantomJS is a headless WebKit with JavaScript API. It has fast and native
support for various web standards: DOM handling, CSS selector, JSON,
Canvas, and SVG. PhantomJS is created by Ariya Hidayat.

%prep
%setup -q

%clean
rm -rf $RPM_BUILD_ROOT

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin/
cp bin/%{name} $RPM_BUILD_ROOT/usr/bin/ 

%files
%defattr(0777,root,root)
/usr/bin/%{name}
