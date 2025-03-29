Name:           rpcs3
Version:        0.0.35
Release:        1%?dist
Summary:        PlayStation 3 emulator and debugger
License:        GPL-2.0-only
URL:            https://github.com/RPCS3/rpcs3
Source0:        %url/archive/refs/tags/v%version.tar.gz
BuildRequires:  glew openal-soft cmake vulkan-validation-layers gcc
BuildRequires:  qt6-qtbase qt6-qtdeclarative qt6-qtmultimedia qt6-qtsvg
BuildRequires:  pkgconfig(sdl3)
BuildRequires:  pkgconfig(sndio)
BuildRequires:  pkgconfig(jack)

%description
%summary.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
