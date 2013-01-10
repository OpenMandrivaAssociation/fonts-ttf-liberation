%define pkgname liberation-fonts-ttf
%define date 20091227

Summary:		Fonts to replace commonly used Microsoft Windows Fonts
Name:			fonts-ttf-liberation
Version:		2.00.1
Release:		1
# The license of the Liberation Fonts is a EULA that contains 
# GPLv2 and two exceptions:
# The first exception is the standard FSF font exception.
# The second exception is an anti-lockdown clause somewhat like
# the one in GPLv3. This license is Free, but GPLv2 and GPLv3
# incompatible.
License:		GPLv2 + font exception
Group:			System/Fonts/True type
URL:			https://fedorahosted.org/liberation-fonts/
Source0:		https://fedorahosted.org/releases/l/i/liberation-fonts/%{pkgname}-%{version}.tar.gz
BuildArch:		noarch
BuildRequires:	fontconfig
BuildRequires:	freetype-tools

%description
The Liberation Fonts are intended to be replacements for the three
most commonly used fonts on Microsoft systems: Times New Roman,
Arial, and Courier New.

%prep
%setup -q -n %{pkgname}-%{version}

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



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.05.2-6mdv2011.0
+ Revision: 675421
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.05.2-5
+ Revision: 675185
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.05.2-4
+ Revision: 664334
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.05.2-3mdv2011.0
+ Revision: 605200
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.05.2-2mdv2010.1
+ Revision: 494151
- fc-cache is now called by an rpm filetrigger

* Tue Jan 19 2010 Frederik Himpe <fhimpe@mandriva.org> 1.05.2-1mdv2010.1
+ Revision: 493789
- Update to new version 1.05.2.20091227

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.04-2mdv2009.1
+ Revision: 351079
- rebuild

* Wed Aug 27 2008 Frederic Crozat <fcrozat@mandriva.com> 1.04-1mdv2009.0
+ Revision: 276484
- Release 1.04
- Remove source1, integrated in tarball now

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0-2mdv2009.0
+ Revision: 220953
- rebuild

* Thu Mar 06 2008 Frederic Crozat <fcrozat@mandriva.com> 1.0-1mdv2008.1
+ Revision: 180881
- Release 1.0 (fully hinted)

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.2-2mdv2008.1
+ Revision: 149817
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Aug 28 2007 Frederic Crozat <fcrozat@mandriva.com> 0.2-1mdv2008.0
+ Revision: 72692
- Update tarball to -3 release

* Fri Jul 06 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.1-3mdv2008.0
+ Revision: 49020
- fontpath.d conversion (#31756)

* Tue May 22 2007 Frederic Crozat <fcrozat@mandriva.com> 0.1-2mdv2008.0
+ Revision: 29693
- New upstream tarball
- Fix license
- drop fontconfig dependency

* Fri May 11 2007 Frederic Crozat <fcrozat@mandriva.com> 0.1-1mdv2008.0
+ Revision: 26348
- Initial package
- Import fonts-ttf-liberation







* Sun Apr 29 2007 Funda Wang <fundawang@mandriva.org> 2.16-1mdv2008.0
+ Revision: 19133
- New upstream version 2.16

  + Mandriva <devel@mandriva.com>


* Thu Mar 15 2007 Olivier Blin <oblin@mandriva.com> 2.15-2mdv2007.1
+ Revision: 144604
- drop huge status.txt file (853k of not useful character/version table)

* Mon Feb 26 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.15-1mdv2007.1
+ Revision: 125924
- new release

* Fri Jan 26 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.14-1mdv2007.1
+ Revision: 113950
- new release

* Mon Nov 20 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.12-1mdv2007.1
+ Revision: 85530
- new release

* Thu Nov 16 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.11-1mdv2007.1
+ Revision: 84975
- new release

* Wed Oct 18 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.10-1mdv2007.1
+ Revision: 66059
- new release

* Wed Sep 06 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.9-1mdv2007.0
+ Revision: 60114
- new release (fix cyrillic issue #25216)

* Sat Aug 05 2006 Helio Chissini de Castro <helio@mandriva.com> 2.8-1mdv2007.0
+ Revision: 52886
- Normalize fonts with new paths
- import fonts-ttf-dejavu-2.8-1mdv2007.0

* Fri Jul 28 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.8-1mdv2007.0
- new release

* Fri Jul 07 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.7-1mdv2007.0
- new release

* Tue May 16 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.6-1mdk
- new release

* Wed Apr 26 2006 Frederic Crozat <fcrozat@mandriva.com> 2.5-1mdk
- Release 2.5 (fix ligature bug with latest pango)

* Tue Mar 07 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.3-1mdk
- new release

* Thu Feb 02 2006 Frederic Crozat <fcrozat@mandriva.com> 2.2-2mdk
- Never ship fonts.cache-2
- fix prereq

* Wed Jan 18 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.2-1mdk
- new release

* Tue Nov 15 2005 Frederic Crozat <fcrozat@mandriva.com> 2.0-2mdk
- fontconfig cache name has changed

* Tue Nov 15 2005 Thierry Vignaud <tvignaud@mandriva.com> 2.0-1mdk
- new release

* Wed Jul 27 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.11-1mdk
- new release

* Thu May 26 2005 Abel Cheung <deaddog@mandriva.org> 1.10-1mdk
- New release 1.10

* Wed May 04 2005 Abel Cheung <deaddog@mandriva.org> 1.9-1mdk
- New release 1.9
- Mark attributes for various files

* Wed Feb 16 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.7-1mdk
- new release

* Tue Nov 02 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.4-1mdk
- new release (merged with Owen & BePa fonts)
- fix package (enable to rebuild on version bumping)

* Tue Aug 10 2004 Robert Vojta <robert.vojta@mandrake.org> 1.1-2mdk
- README file added
- better description (based on the README file)

* Fri Aug 06 2004 Petr Spatka <petr.spatka@kamarad.cz> 1.1-1mdk
- Initial build. Based on fonts-ttf-vera.spec from Mandrake.
