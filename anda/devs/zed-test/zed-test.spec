%global commit 931a6d6f407b294004d091fea780d3a061cfe091
%global crate zed
%global debug_package %{nil}

Name: zed-test
Version: 0.1.0
Release: 2%?dist
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
script/generate-licenses

%install
# The license generation script doesn't generate licenses for ALL compiled dependencies, just direct deps of Zed, and it does not "group" licenses
# There is also some horrible issue with --no-dedupes with Zed so we have to work around this
%{__cargo} tree                                                 \
    -Z avoid-dev-deps                                               \
    --workspace                                                     \
    --edges no-build,no-dev,no-proc-macro                           \
    --target all                                                    \
    %{__cargo_parse_opts %{-n} %{-a} %{-f:-f%{-f*}}}                \
    --prefix none                                                   \
    --format "{l}: {p}"                                             \
    | sed -e "s: ($(pwd)[^)]*)::g" -e "s: / :/:g" -e "s:/: OR :g"   \
    | sort -u                                                       \
> LICENSE.dependencies
# Remove duplicate entries
sed -i 's/.*(\*).*//d' LICENSE.dependencies
# Remove GitHub links
sed -i 's/(https.*//g' LICENSE.dependencies
# Add license to Microsoft crates hosted on GitHub
sed -i '/^: pet/ s/./MIT&/' LICENSE.dependencies
# Remove empty lines
#sed -ir '/^\s*$/d' LICENSE.dependencies
mv assets/icons/LICENSES LICENSE.icons
mv assets/themes/LICENSES LICENSE.themes
mv assets/fonts/plex-mono/license.txt LICENSE.fonts

%files
%doc CODE_OF_CONDUCT.md
%doc README.md
%license LICENSE-AGPL
%license LICENSE-APACHE
%license LICENSE-GPL
%license LICENSE.dependencies
%license LICENSE.icons
%license LICENSE.fonts
%license LICENSE.themes
%license assets/licenses.md

%changelog
* Wed Mar 26 2025 John Doe <packager@example.com>
- Test package
