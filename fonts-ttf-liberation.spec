%define pkgname liberation-fonts-ttf
%define date 20091227

Summary: Fonts to replace commonly used Microsoft Windows Fonts
Name: fonts-ttf-liberation
Version: 1.05.2
Release: %mkrel 5
# The license of the Liberation Fonts is a EULA that contains 
# GPLv2 and two exceptions:
# The first exception is the standard FSF font exception.
# The second exception is an anti-lockdown clause somewhat like
# the one in GPLv3. This license is Free, but GPLv2 and GPLv3
# incompatible.
License: GPLv2 + font exception
Group: System/Fonts/True type
URL: https://fedorahosted.org/liberation-fonts/
Source0: https://fedorahosted.org/releases/l/i/liberation-fonts/%{pkgname}-%{version}.%{date}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: freetype-tools

%description
The Liberation Fonts are intended to be replacements for the three
most commonly used fonts on Microsoft systems: Times New Roman,
Arial, and Courier New.

%prep
%setup -q -c -n %{pkgname}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

pushd ttf
mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/liberation

install -m 644 *.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/liberation
ttmkfdir $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/liberation > $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/liberation/fonts.dir
ln -s fonts.dir $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/liberation/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/liberation \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-liberation:pri=50
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc License.txt COPYING
%dir %{_datadir}/fonts/TTF/liberation
%{_datadir}/fonts/TTF/liberation/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/liberation/fonts.dir
%{_datadir}/fonts/TTF/liberation/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-liberation:pri=50

