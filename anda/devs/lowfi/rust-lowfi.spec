# Generated by rust2rpm 27
%global crate lowfi

Name:           rust-lowfi
Version:        1.6.0
Release:        1%?dist
Summary:        Extremely simple lofi player

License:        MIT
URL:            https://crates.io/crates/lowfi
Source:         %{crates_source}

Packager:       sadlerm <lerm@chromebooks.lol>

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  anda-srpm-macros
BuildRequires:  mold
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(openssl)

%global _description %{expand:
An extremely simple lofi player.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR MIT OR Apache-2.0) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND ISC AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/lowfi

%prep
%autosetup -n %{crate}-%{version}
%cargo_prep_online

%build
%cargo_build
%{cargo_license_summary_online}
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm755 target/rpm/%{crate} %{buildroot}%{_bindir}/%{crate}
