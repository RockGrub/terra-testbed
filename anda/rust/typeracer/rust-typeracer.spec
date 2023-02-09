# Generated by rust2rpm 23
%bcond_without check

%global crate typeracer

Name:           rust-typeracer
Version:        2.1.2
Release:        %autorelease
Summary:        Terminal typing game

License:        GPL-3.0
URL:            https://crates.io/crates/typeracer
Source:         %{crates_source}

BuildRequires:  anda-srpm-macros rust-packaging >= 21

%global _description %{expand:
Terminal typing game. Race to see the fastest time you can get!.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
# FIXME: no license files detected
%doc README.md
%{_bindir}/typeracer

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
