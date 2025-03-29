# Generated by go2rpm 1.15.0
%bcond check 1
%bcond bootstrap 0

# https://github.com/nektos/act
%global goipath         github.com/nektos/act
Version:                0.2.75

%gometa -f

%global common_description %{expand:
Run your GitHub Actions locally
}

%global golicenses      LICENSE pkg/lookpath/LICENSE
%global godocs          README.md

Name:           act
Release:        %autorelease
Summary:        None

License:        MIT AND ISC AND BSD-3-Clause AND Apache-2.0 AND BSD-2-Clause
URL:            %{gourl}
BuildRequires:  anda-srpm-macros
BuildRequires:  bash
BuildRequires:  golang
BuildRequires:  go-rpm-macros
BuildRequires:  make
BuildRequires:  nodejs-npm
Packager:       xiaoshihou <xiaoshihou@tutamail.com>

%description %{common_description}

%gopkg

%prep
%git_clone https://github.com/nektos/act v%{version}
%go_prep_online -A

%build

%install
cd %{_builddir}
mkdir -p %{buildroot}%{_bindir}
%make_install PREFIX=%{buildroot}%{_prefix}

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE pkg/lookpath/LICENSE
%doc .markdownlint.yml CONTRIBUTING.md IMAGES.md README.md
%{_bindir}/act

%changelog
%autochangelog
