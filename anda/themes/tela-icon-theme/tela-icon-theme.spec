%global commit 69d31d1067916e5ac3694d311c73b6f3515991ed
%global commit_date 20250503
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           tela-icon-theme
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Tela icon theme for linux desktops

License:        GPL-3.0-only
URL:            https://github.com/vinceliuice/Tela-icon-theme/
Source0:        %url/archive/%commit/Tela-icon-theme-%commit.tar.gz

BuildArch:      noarch
BuildRequires:  gtk-update-icon-cache fdupes

%description
Tela icon theme for linux desktops.

%prep
%autosetup -n Tela-icon-theme-%{commit}

%build

%install
mkdir -p %{buildroot}%{_datadir}/themes
./install.sh -c -d %{buildroot}%{_datadir}/icons

%fdupes %buildroot%_datadir/icons/

%files
%license COPYING
%doc README.md

%{_datadir}/icons/Tela*/

%changelog
%autochangelog
