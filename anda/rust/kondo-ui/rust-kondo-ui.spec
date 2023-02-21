# Generated by rust2rpm 23
%global crate kondo-ui

Name:           rust-kondo-ui
Version:        0.2.0
Release:        %autorelease
Summary:        Filesystem cleaning tool that recursively searches directories for known project structures and allows you to clean them of unnecessary files like build artifacts

License:        MIT
URL:            https://crates.io/crates/kondo-ui
Source:         %{crates_source}

BuildRequires:  pkgconfig(glib-2.0) anda-srpm-macros rust-packaging >= 21

%global _description %{expand:
Filesystem cleaning tool that recursively searches directories for known
project structures and allows you to clean them of unnecessary files like build
artifacts.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
# FIXME: no license files detected
%{_bindir}/kondo-ui

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
