# Credit to LionHeartP from Nobara for most of the spec and letting me know about the need for this package <3
%global origname mesa
%global ver 25.0.4

Name:           %{origname}-compat
Summary:        Mesa graphics libraries - legacy compatibility libraries
Version:        %{lua:ver = string.gsub(rpm.expand("%{ver}"), "-", "~"); print(ver)}
Release:        1%{?dist}
Epoch:          1
License:        MIT AND BSD-3-Clause AND SGI-B-2.0
URL:            http://www.mesa3d.org

Source0:        https://archive.mesa3d.org/mesa-%{ver}.tar.xz
# src/gallium/auxiliary/postprocess/pp_mlaa* have an ... interestingly worded license.
# Source1 contains email correspondence clarifying the license terms.
# Fedora opts to ignore the optional part of clause 2 and treat that code as 2 clause BSD.
Source1:        Mesa-MLAA-License-Clarification-Email.txt
# Keep Mesa builds relatively the same
Patch0:         bazzite.patch

BuildRequires:  meson >= 1.3.0
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
%if 0%{?with_hardware}
BuildRequires:  kernel-headers
%endif
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(zlib) >= 1.2.3
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig(libelf)
BuildRequires:  llvm-devel >= 7.0.0
BuildRequires:  libdrm-devel
BuildRequires:  python3-devel
BuildRequires:  python3-mako
BuildRequires:  python3-pycparser
BuildRequires:  python3-pyyaml

%description
%{summary}.

%package libOSMesa
Summary:        Mesa offscreen rendering libraries
Provides:       libOSMesa
Provides:       libOSMesa%{?_isa}
# New things should not rely on this as this library is dead upstream
Provides:       deprecated()

%description libOSMesa
%{summary}.

%package libOSMesa-devel
Summary:        Mesa offscreen rendering development package
Requires:       %{name}-libOSMesa%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# New things should not rely on this as this library is dead upstream
Provides:       deprecated()

%description libOSMesa-devel
%{summary}.

%prep
%autosetup -n %{origname}-%{ver} -p1
cp %{SOURCE1} docs/

%build
# We've gotten a report that enabling LTO for mesa breaks some games. See
# https://bugzilla.redhat.com/show_bug.cgi?id=1862771 for details.
# Disable LTO for now
%define _lto_cflags %{nil}

%meson \
  -Dplatforms= \
  -Dosmesa=true \
  -Dgallium-drivers=llvmpipe \
  -Dgallium-vdpau=disabled \
  -Dgallium-va=disabled \
  -Dgallium-xa=disabled \
  -Dgallium-nine=false \
  -Dgallium-opencl=disabled \
  -Dgallium-rusticl=false \
  -Dvulkan-drivers= \
  -Dshared-glapi=enabled \
  -Dgles1=disabled \
  -Dgles2=disabled \
  -Dopengl=true \
  -Dgbm=disabled \
  -Dglvnd=disabled \
  -Dglx=disabled \
  -Degl=disabled \
  -Dllvm=enabled \
  -Dshared-llvm=enabled \
  -Dvalgrind=disabled \
  -Dbuild-tests=false \
  -Dmesa-clc=auto \
  -Dmicrosoft-clc=disabled \
  -Dxlib-lease=disabled \
  -Dandroid-libbacktrace=disabled \
  -Dlibunwind=disabled \
  -Dlmsensors=disabled \
%ifarch %{ix86}
  -Dglx-read-only-text=true \
%endif
  %{nil}
%meson_build

%install
%meson_install

# trim some garbage, the mesa base package handles these
rm -rf %{buildroot}%{_datadir}/drirc.d
rm -rf %{buildroot}%{_includedir}/GL/gl*.h
rm -rf %{buildroot}%{_includedir}/KHR

%files libOSMesa
%{_libdir}/libOSMesa.so.8*
%files libOSMesa-devel
%dir %{_includedir}/GL
%{_includedir}/GL/osmesa.h
%{_libdir}/libOSMesa.so
%{_libdir}/pkgconfig/osmesa.pc

%changelog
* Thu Apr 24 2025 Neal Gompa <ngompa@fedoraproject.org> - 25.0.4-1
- Initial split from mesa for compat libraries (rhbz#2362203)
