%global commit e117986715e1e9ef955009ad7f03ec110aa14940
%global commit_date 20250303
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%if 0%{?rhel}
%global debug_package %{nil}
%endif

Name:           envision-nightly
Version:        %commit_date.%shortcommit
Release:        2%?dist
Summary:        UI for building, configuring and running Monado, the open source OpenXR runtime
License:        AGPL-3.0-or-later
URL:            https://gitlab.com/gabmus/envision/
Source0:        %url/-/archive/%commit/envision-%commit.tar.gz
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  ninja-build
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gio-2.0) >= 2.66
BuildRequires:  pkgconfig(gtk4) >= 4.10.0
BuildRequires:  pkgconfig(vte-2.91-gtk4) >= 0.72.0
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  openssl-devel-engine
BuildRequires:  openxr-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  git-core
Recommends:     android-tools
Conflicts:      envision

%description
%summary.

%prep
%autosetup -n envision-%commit
%cargo_prep_online

%build
%meson
%meson_build

%install
%meson_install
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%_bindir/envision
%_datadir/applications/org.gabmus.envision.Devel.desktop
%_datadir/envision/
%_iconsdir/hicolor/scalable/apps/org.gabmus.envision.Devel.svg
%_iconsdir/hicolor/symbolic/apps/org.gabmus.envision.Devel-symbolic.svg
%_metainfodir/org.gabmus.envision.Devel.appdata.xml
