# Generated by go2rpm 1.15.0
%bcond check 0
%bcond bootstrap 0

%if %{with bootstrap}
%global debug_package %{nil}
%endif

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# Naming variable as something other than "commit" is necessary
# to stop %%gometa from putting commit hash in release
%global commit_hash c93747926d2e5ead9adf0039f6bf34f48ba3263d
%global commit_date 20250225
%global shortcommit %{sub %{commit_hash} 1 7}
%global ver 2.0.14

# https://github.com/zyedidia/micro
%global goipath         github.com/zyedidia/micro
Version:                %{ver}^%{commit_date}git.%{shortcommit}

%gometa -f

%global common_description %{expand:
micro is a terminal-based text editor that aims to be easy to use and intuitive, while also taking advantage of the capabilities of modern terminals. It strives to be enjoyable as a full-time editor for people who prefer to work in a terminal, or those who regularly edit files over SSH.}

%global golicenses      LICENSE LICENSE-THIRD-PARTY
%global godocs          README.md runtime/help/colors.md runtime/help/commands.md\\\
                        runtime/help/copypaste.md runtime/help/defaultkeys.md\\\
                        runtime/help/help.md runtime/help/keybindings.md\\\
                        runtime/help/options.md runtime/help/plugins.md\\\
                        runtime/help/tutorial.md

Name:           micro.nightly
Release:        2%{?dist}
Summary:        A modern and intuitive terminal-based text editor

License:        MIT
URL:            %{gourl}
Packager:       sadlerm <lerm@chromebooks.lol>

BuildRequires:  anda-srpm-macros

Recommends:     wl-clipboard
Recommends:     (xclip or xsel)

Provides:       micro-nightly = %{version}-%{release}
Provides:       micro
Conflicts:      micro

%description %{common_description}

%gopkg

%global buildsubdir micro-%{version}

%prep
git clone --recurse-submodules -q %{gourl} micro-%{version}
cd %{builddir}/micro-%{version} && git checkout -q %{commit_hash}
%gomkdir
%go_prep_online

%build
%if %{without bootstrap}
go generate ./runtime

MICRO_VERSION=$(go run ./tools/build-version.go)
MICRO_DATE=$(date --date=%{commit_date} +"%%B %%d, %%Y")

LDFLAGS="-X internal/util.version=${MICRO_VERSION} \
         -X internal/util.hash=%{shortcommit} \
         -X 'internal/util.date=${MICRO_DATE}'"

%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/micro ./cmd/micro
%endif

%install
%if %{without bootstrap}
install -Dm755 %{gobuilddir}/bin/micro        -t %{buildroot}%{_bindir}
install -Dm644 assets/packaging/micro.1       -t %{buildroot}%{_mandir}/man1
install -Dm644 assets/packaging/micro.desktop -t %{buildroot}%{_datadir}/applications
install -Dm644 assets/micro-logo-mark.svg        %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/micro.svg

# for %%doc packaging
mv -v ./runtime/help .
%endif

%if %{without bootstrap}
%if %{with check}
%check
%gotest ./internal/... ./cmd/micro/...
%endif
%endif

%if %{without bootstrap}
%files
%license LICENSE LICENSE-THIRD-PARTY
%doc README.md help
%{_bindir}/micro
%{_mandir}/man1/micro.1.gz
%{_datadir}/applications/micro.desktop
%{_datadir}/icons/hicolor/scalable/apps/micro.svg
%endif

%changelog
%autochangelog
