%define pkgname liberation-fonts-ttf
%define oname liberation-fonts
%define archivename %{oname}-%{version}
%define catalogue %{_sysconfdir}/X11/fontpath.d
%define fontname liberation
%define _fondir  %{_datadir}/fonts/TTF/liberation

Summary: Fonts to replace commonly used Microsoft Windows Fonts
Name: fonts-ttf-liberation
Version: 1.07.2
Release: %mkrel 1
# The license of the Liberation Fonts is a EULA that contains 
# GPLv2 and two exceptions:
# The first exception is the standard FSF font exception.
# The second exception is an anti-lockdown clause somewhat like
# the one in GPLv3. This license is Free, but GPLv2 and GPLv3
# incompatible.
License: GPLv2 + font exception
Group: System/Fonts/True type
URL: https://fedorahosted.org/liberation-fonts/
Source0: https://fedorahosted.org/releases/l/i/liberation-fonts/%{archivename}.tar.gz
Source1:  generate.pe
BuildArch: noarch
BuildRequires: ttmkfdir
BuildRequires: fontforge
BuildRequires: mkfontdir
BuildRequires: mkfontscale

%description
The Liberation Fonts are intended to be replacements for the three
most commonly used fonts on Microsoft systems: Times New Roman,
Arial, and Courier New.

%prep
%setup -q -n %{archivename}
rm -rf scripts
mv src/* .
rm -rf src
cp %{SOURCE1} .
chmod 755 generate.pe

%build
./generate.pe *.sfd
mv LiberationMono.ttf LiberationMono-Regular.ttf
mv LiberationSerif.ttf LiberationSerif-Regular.ttf
mv LiberationSans.ttf LiberationSans-Regular.ttf

%install
%__rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/liberation
install -m 644 *.ttf %{buildroot}%{_datadir}/fonts/TTF/liberation
ttmkfdir %{buildroot}%{_datadir}/fonts/TTF/liberation > %{buildroot}%{_datadir}/fonts/TTF/liberation/fonts.dir
ln -s fonts.dir %{buildroot}%{_datadir}/fonts/TTF/liberation/fonts.scale

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/liberation \
    %{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-liberation:pri=50

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/liberation \
    %{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-liberation:pri=50

# fonts.{dir,scale}
mkfontdir %{buildroot}%{_fontdir}
mkfontscale %{buildroot}%{_fontdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc License.txt COPYING
%dir %{_datadir}/fonts/TTF/liberation
%{_datadir}/fonts/TTF/liberation/liberation
%{_datadir}/fonts/TTF/liberation/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/liberation/fonts.dir
%{_datadir}/fonts/TTF/liberation/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-liberation:pri=50

