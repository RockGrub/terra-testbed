# Generated by go2rpm 1.15.0
%bcond check 0
%bcond bootstrap 0

# https://github.com/twpayne/chezmoi
%global goipath         github.com/twpayne/chezmoi
Version:                2.61.0

%gometa -f

%global common_description %{expand:
Manage your dotfiles across multiple diverse machines, securely.}

%global golicenses      LICENSE assets/chezmoi.io/docs/license.md\\\
                        assets/chezmoi.io/docs/reference/commands/license.md
%global godocs          .markdownlint-cli2.yaml README.md docs\\\
                        assets/chezmoi.io/snippets/config-format.md\\\
                        assets/chezmoi.io/snippets/common-flags/exclude.md\\\
                        assets/chezmoi.io/snippets/common-flags/format.md\\\
                        assets/chezmoi.io/snippets/common-flags/include.md\\\
                        assets/chezmoi.io/snippets/common-flags/init.md\\\
                        assets/chezmoi.io/snippets/common-flags/nul-path-\\\
                        separator.md assets/chezmoi.io/snippets/common-\\\
                        flags/parent-dirs.md\\\
                        assets/chezmoi.io/snippets/common-flags/path-style.md\\\
                        assets/chezmoi.io/snippets/common-flags/recursive.md\\\
                        assets/chezmoi.io/snippets/common-flags/tree.md

Name:           chezmoi
Release:        1%?dist
Summary:        Manage your dotfiles across multiple diverse machines, securely

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

#gopkg

%prep
%goprep

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/chezmoi .

%install
#gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/chezmoi

#gopkgfiles
