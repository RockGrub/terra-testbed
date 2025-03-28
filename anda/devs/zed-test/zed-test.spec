%global commit 931a6d6f407b294004d091fea780d3a061cfe091
%global crate zed

Name: zed-test
Version: 0.1.0
Release: 1%?dist
Summary: Zed license generator
License: MIT
URL:            https://zed.dev/
Source0:        https://github.com/zed-industries/zed/archive/%{commit}.tar.gz
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  anda-srpm-macros
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  clang
BuildRequires:  mold
BuildRequires:  cmake
BuildRequires:  alsa-lib-devel
BuildRequires:  fontconfig-devel
BuildRequires:  wayland-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  libzstd-devel
BuildRequires:  perl-FindBin
BuildRequires:  perl-IPC-Cmd
BuildRequires:  perl-File-Compare
BuildRequires:  perl-File-Copy
BuildRequires:  perl-lib
BuildRequires:  rust2rpm
BuildRequires:  vulkan-loader

%description
Generate licenses

%prep
%autosetup -n %{crate}-%{commit} -p1
%cargo_prep_online

%build

%install
export CARGOFLAGS="-vv --verbose"
cargo tree                                                 \
    -Z avoid-dev-deps                                               \
    --workspace                                                     \
    --edges no-build,no-dev,no-proc-macro                           \
    --no-dedupe                                                     \
    --target all                                                    \
    --prefix none                                                   \
    --format "{l}: {p}"                                             
  

%files
%license LICENSE.dependencies

%changelog
* Wed Mar 26 2025 John Doe <packager@example.com>
- Test package
