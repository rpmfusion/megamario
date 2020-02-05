Name:           megamario
Version:        1.7
Release:        7%{?dist}
Summary:        Well known platform game clone
Group:          Amusements/Games
License:        LGPLv2
URL:            http://mmario.sourceforge.net/
Source0:        http://downloads.sourceforge.net/mmario/MegaMario_v%{version}_full.zip
Source1:        %{name}.desktop
Patch0:         megamario-1.5-compile-fix.patch

BuildRequires:  gcc-c++
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
MegaMario is a clone of a well know platform game, featuring 25 new levels. In
the game you play Mario and your task is to free his brother Luigi, who was
captured by the evil Bowser.


%prep
%setup -q -c
%patch0 -p1
sed -i 's/\r//' *.txt
sed -i -e 's@Canyon.jpg@canyon.jpg@g' data/levels/grasslevels/grassland


%build
%make_build PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char" \
  LDFLAGS="-lSDL -lSDL_mixer -lSDL_ttf -lSDL_image -lGL $RPM_LD_FLAGS"
convert -transparent '#FF00FF' data/gfx/characters/small/player1r.PNG \
  %{name}.png


%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}
# cruft removal
rm $RPM_BUILD_ROOT%{_datadir}/megamario/levels/1/1
rm $RPM_BUILD_ROOT%{_datadir}/megamario/levels/11/mai
rm $RPM_BUILD_ROOT%{_datadir}/megamario/save.sav


# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor dribble           \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%doc CONTROLS.txt readme.txt fixes_v%{version}.txt
%license licence.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/dribble-%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.7-2
- Fix canyon file name (rfbz #4526)

* Sun Oct 22 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.7-1
- New upstream release 1.7 (rfbz #4526)
- Clean up spec file

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.5-6
- Mass rebuilt for Fedora 19 Features

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.5-5
- Rebuilt for c++ ABI breakage

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.5-3
- rebuild for new F11 features

* Thu Jul 24 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.5-2
- Release bump for rpmfusion

* Tue Jun  5 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.5-1%{?dist}
- New upstream release 1.5

* Sat Mar 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3-3%{?dist}
- Fixup .desktop file categories for games-menus usage
- No longer use preconverted .png as RH bug 196010 is fixed

* Sun Jul  9 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3-2%{?dist}
- Use a preconverted .png as icon to work around RH bug 196010

* Thu Jun 15 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3-1%{?dist}
- Initial Fedora Extras package
