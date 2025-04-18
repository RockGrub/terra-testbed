%global commit 63ff648bb64c23023a0047ea3ff2c0b6b1fd3caf
%global commit_date 20250404
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-magnetar
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Workspaces client for Stardust XR.
URL:            https://github.com/StardustXR/magnetar
Source0:        %url/archive/%commit/magnetar-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold libudev-devel g++ libinput-devel libxkbcommon-x11-devel

Provides:       magnetar stardust-magnetar
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary

%prep
%autosetup -n magnetar-%commit
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
%cargo_install


%files
%_bindir/magnetar
%license LICENSE
%doc README.md

%changelog
* Wed Sep 11 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR magnetar

