Name:           cutter-re
Version:        1.9.0
Release:        2%{?dist}
Summary:        GUI for radare2 reverse engineering framework

# CC-BY-SA: src/img/icons/
# CC0: src/fonts/Anonymous Pro.ttf
License:        GPLv3 and CC-BY-SA and CC0

URL:            https://cutter.re/
Source0:        https://github.com/radareorg/cutter/archive/v%{version}/cutter-%{version}.tar.gz

BuildRequires:  radare2-devel >= 3.8.0
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  file-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
%ifarch %{qt5_qtwebengine_arches}
BuildRequires:  qt5-qtwebengine-devel
%endif
Requires:       python3-jupyter-client
Requires:       python3-notebook
Requires:       hicolor-icon-theme

%description
Cutter is a Qt and C++ GUI for radare2. Its goal is making an advanced,
customizable and FOSS reverse-engineering platform while keeping the user
experience at mind. Cutter is created by reverse engineers for reverse
engineers.


%prep
%autosetup -p1 -n cutter-%{version}


%build
mkdir build
cd build
%ifarch %{qt5_qtwebengine_arches}
%cmake -DCMAKE_BUILD_WITH_INSTALL_RPATH=TRUE -DCUTTER_ENABLE_QTWEBENGINE=ON ../src
%else
%cmake -DCMAKE_BUILD_WITH_INSTALL_RPATH=TRUE -DCUTTER_ENABLE_QTWEBENGINE=OFF ../src
%endif
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_bindir}
install build/Cutter %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
        src/org.radare.Cutter.desktop

mkdir -p %{buildroot}%{_metainfodir}
install -pm644 src/org.radare.Cutter.appdata.xml \
        %{buildroot}%{_metainfodir}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -pm644 src/img/cutter.svg \
        %{buildroot}%{_datadir}/icons/hicolor/scalable/apps


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml


%files
%{_bindir}/Cutter
%{_datadir}/applications/*.desktop
%{_metainfodir}/*.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%license COPYING src/img/icons/Iconic-LICENSE
%doc README.md


%changelog
* Fri Oct 11 2019 Riccardo Schirone <rschirone91@gmail.com> - 1.9.0-2
- Rebuilt for radare2-3.9.0-3

* Mon Sep 30 2019 Riccardo Schirone <rschirone91@gmail.com> - 1.9.0-1
- rebase to cutter 1.9.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Riccardo Schirone <rschirone91@gmail.com> - 1.8.3-1
- rebase to cutter 1.8.3

* Wed Jun 26 2019 Riccardo Schirone <rschirone91@gmail.com> - 1.8.0-4
- recompile for radare2 3.6.0

* Mon Apr 15 2019 Riccardo Schirone <rschirone91@gmail.com> - 1.8.0-3
- recompile for radare2 3.4.1

* Tue Apr 09 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.8.0-2
- Update to radare2 3.4.1

* Thu Mar 21 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.8.0-1
- Update to 1.8.0
- Require hicolor-icon-theme
- Move appdata to a correct location
- Fix license field (Robert-André Mauchin, #1690050)

* Thu Mar 14 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.7.4-1
- Initial packaging
