%define pkgname liberation-fonts-ttf
%define date 20091227

Summary:	Fonts to replace commonly used Microsoft Windows Fonts
Name:		fonts-ttf-liberation
Version:	2.00.1
Release:	6
# The license of the Liberation Fonts is a EULA that contains 
# GPLv2 and two exceptions:
# The first exception is the standard FSF font exception.
# The second exception is an anti-lockdown clause somewhat like
# the one in GPLv3. This license is Free, but GPLv2 and GPLv3
# incompatible.
License:	GPLv2 + font exception
Group:		System/Fonts/True type
Url:		https://fedorahosted.org/liberation-fonts/
Source0:	https://fedorahosted.org/releases/l/i/liberation-fonts/%{pkgname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	freetype-tools

%description
The Liberation Fonts are intended to be replacements for the three
most commonly used fonts on Microsoft systems: Times New Roman,
Arial, and Courier New.

%prep
%setup -qn %{pkgname}-%{version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/liberation

install -m 644 *.ttf %{buildroot}%{_datadir}/fonts/TTF/liberation
ttmkfdir %{buildroot}%{_datadir}/fonts/TTF/liberation > %{buildroot}%{_datadir}/fonts/TTF/liberation/fonts.dir
ln -s fonts.dir %{buildroot}%{_datadir}/fonts/TTF/liberation/fonts.scale

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/liberation \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-liberation:pri=50

%files
%doc README AUTHORS LICENSE TODO
%dir %{_datadir}/fonts/TTF/liberation
%{_datadir}/fonts/TTF/liberation/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/liberation/fonts.dir
%{_datadir}/fonts/TTF/liberation/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-liberation:pri=50

