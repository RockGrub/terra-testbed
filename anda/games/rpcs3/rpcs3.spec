Name:           rpcs3
Version:        0.0.35
Release:        1%?dist
Summary:        PlayStation 3 emulator and debugger
License:        GPL-2.0-only
URL:            https://github.com/RPCS3/rpcs3
%dnl Source0:        %url/archive/refs/tags/v%version.tar.gz
BuildRequires:  glew openal-soft cmake vulkan-validation-layers gcc gcc-c++ git-core
BuildRequires:  cmake(FAudio)
BuildRequires:  cmake(OpenAL)
BuildRequires:  cmake(OpenCV)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  pkgconfig(sdl3)
BuildRequires:  pkgconfig(sndio)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  doxygen
BuildRequires:  qt6-qtbase-private-devel vulkan-devel jack-audio-connection-kit-devel llvm-devel

%description
%summary.

%prep
%git_clone %url v%version

%build
%ifarch aarch64
EXTRA=-DUSE_NATIVE_INSTRUCTIONS=OFF
%else
EXTRA=
%endif
%cmake -DDISABLE_LTO=TRUE -DZSTD_BUILD_SHARED=ON -DZSTD_BUILD_STATIC=OFF $EXTRA
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
