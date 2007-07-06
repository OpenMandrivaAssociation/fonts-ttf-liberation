%define tarball_version 2
Summary: Liberation ttf Fonts
Name: fonts-ttf-liberation
Version: 0.1
Release: %mkrel 3
License: GPL + font exception
Group: System/Fonts/True type
URL: https://www.redhat.com/promo/fonts/
Source0: https://www.redhat.com/f/fonts/liberation-fonts-ttf-%{tarball_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: freetype-tools

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
ttmkfdir $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/liberation > $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/liberation/fonts.dir
ln -s fonts.dir $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/liberation/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/liberation \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-liberation:pri=50

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 

%postun
if [ "$1" = "0" ]; then
  [ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 
fi


%files
%defattr(-,root,root,-)
%doc License.txt
%dir %{_datadir}/fonts/TTF/liberation
%{_datadir}/fonts/TTF/liberation/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/liberation/fonts.dir
%{_datadir}/fonts/TTF/liberation/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-liberation:pri=50

