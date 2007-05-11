%define pkgname dejavu-ttf

Summary: Liberation ttf Fonts
Name: fonts-ttf-liberation
Version: 0.1
Release: %mkrel 1
License: GPL
Group: System/Fonts/True type
URL: https://www.redhat.com/promo/fonts/
Source0: https://www.redhat.com/f/fonts/liberation-fonts-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires(post): fontconfig 
Requires(postun): fontconfig 
Requires(post): chkfontpath
Requires(postun): chkfontpath
BuildArch: noarch
Requires: freetype-tools

%description
The Liberation Fonts are intended to be replacements for the three
most commonly used fonts on Microsoft systems: Times New Roman,
Arial, and Courier New.

%prep
%setup -q -c 

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/liberation

install -m 644 *.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/liberation
ttmkfdir $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/dejavu > $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/liberation/fonts.dir
ln -s fonts.dir $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/liberation/fonts.scale

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x %{_sbindir}/chkfontpath ] && %{_sbindir}/chkfontpath -q -a %{_datadir}/fonts/TTF/liberation
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 

%postun
if [ "$1" = "0" ]; then
  [ -x %{_sbindir}/chkfontpath ] && %{_sbindir}/chkfontpath -q -r %{_datadir}/fonts/TTF/liberation
  [ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 
fi


%files
%defattr(-,root,root,-)
%doc License.txt
%dir %{_datadir}/fonts/TTF/liberation
%{_datadir}/fonts/TTF/liberation/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/liberation/fonts.dir
%{_datadir}/fonts/TTF/liberation/fonts.scale
