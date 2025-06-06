# Generated by rust2rpm 26
%bcond_with check
# aarch64 dist is not available
%ifarch aarch64
%bcond_with dist_server
%else
%bcond_without dist_server
%endif

# Don't mangle shebangs
%global __brp_mangle_shebangs %{nil}

%global crate sccache

Name:           rust-sccache
Version:        0.10.0
Release:        1%?dist
Summary:        Ccache-like tool

License:        Apache-2.0
URL:            https://crates.io/crates/sccache
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          sccache-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  anda-srpm-macros
BuildRequires:  openssl-devel
BuildRequires:  gcc
BuildRequires:  perl
BuildRequires:  rust-packaging
BuildRequires:  mold

%global _description %{expand:
Sccache is a ccache-like tool. It is used as a compiler wrapper and
avoids compilation when possible. Sccache has the capability to utilize
caching in remote storage environments, including various cloud storage
options, or alternatively, in local storage.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        MIT

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
#license LICENSE.dependencies
%doc CODE_OF_CONDUCT.md
%doc README.md
%{_bindir}/sccache
%if %{with dist_server}
%{_bindir}/sccache-dist
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sccache) = 0.7.4
Requires:       cargo
Requires:       rust >= 1.67.1

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CODE_OF_CONDUCT.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sccache/default) = 0.7.4
Requires:       cargo
Requires:       crate(sccache) = 0.7.4
Requires:       crate(sccache/all) = 0.7.4

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+all-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+all-devel %{_description}

This package contains library source intended for building other packages which
use the "all" feature of the "%{crate}" crate.

%files       -n %{name}+all-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+azure-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+azure-devel %{_description}

This package contains library source intended for building other packages which
use the "azure" feature of the "%{crate}" crate.

%files       -n %{name}+azure-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dist-client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dist-client-devel %{_description}

This package contains library source intended for building other packages which
use the "dist-client" feature of the "%{crate}" crate.

%files       -n %{name}+dist-client-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dist-server-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dist-server-devel %{_description}

This package contains library source intended for building other packages which
use the "dist-server" feature of the "%{crate}" crate.

%files       -n %{name}+dist-server-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dist-tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dist-tests-devel %{_description}

This package contains library source intended for building other packages which
use the "dist-tests" feature of the "%{crate}" crate.

%files       -n %{name}+dist-tests-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+flate2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+flate2-devel %{_description}

This package contains library source intended for building other packages which
use the "flate2" feature of the "%{crate}" crate.

%files       -n %{name}+flate2-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gcs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gcs-devel %{_description}

This package contains library source intended for building other packages which
use the "gcs" feature of the "%{crate}" crate.

%files       -n %{name}+gcs-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gha-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gha-devel %{_description}

This package contains library source intended for building other packages which
use the "gha" feature of the "%{crate}" crate.

%files       -n %{name}+gha-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http-body-util-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http-body-util-devel %{_description}

This package contains library source intended for building other packages which
use the "http-body-util" feature of the "%{crate}" crate.

%files       -n %{name}+http-body-util-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+hyper-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hyper-devel %{_description}

This package contains library source intended for building other packages which
use the "hyper" feature of the "%{crate}" crate.

%files       -n %{name}+hyper-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+hyper-util-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hyper-util-devel %{_description}

This package contains library source intended for building other packages which
use the "hyper-util" feature of the "%{crate}" crate.

%files       -n %{name}+hyper-util-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+jwt-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+jwt-devel %{_description}

This package contains library source intended for building other packages which
use the "jwt" feature of the "%{crate}" crate.

%files       -n %{name}+jwt-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+libmount-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libmount-devel %{_description}

This package contains library source intended for building other packages which
use the "libmount" feature of the "%{crate}" crate.

%files       -n %{name}+libmount-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+memcached-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+memcached-devel %{_description}

This package contains library source intended for building other packages which
use the "memcached" feature of the "%{crate}" crate.

%files       -n %{name}+memcached-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+native-zlib-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+native-zlib-devel %{_description}

This package contains library source intended for building other packages which
use the "native-zlib" feature of the "%{crate}" crate.

%files       -n %{name}+native-zlib-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nix-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nix-devel %{_description}

This package contains library source intended for building other packages which
use the "nix" feature of the "%{crate}" crate.

%files       -n %{name}+nix-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+opendal-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+opendal-devel %{_description}

This package contains library source intended for building other packages which
use the "opendal" feature of the "%{crate}" crate.

%files       -n %{name}+opendal-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+openssl-devel %{_description}

This package contains library source intended for building other packages which
use the "openssl" feature of the "%{crate}" crate.

%files       -n %{name}+openssl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+oss-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+oss-devel %{_description}

This package contains library source intended for building other packages which
use the "oss" feature of the "%{crate}" crate.

%files       -n %{name}+oss-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+redis-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+redis-devel %{_description}

This package contains library source intended for building other packages which
use the "redis" feature of the "%{crate}" crate.

%files       -n %{name}+redis-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+reqsign-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+reqsign-devel %{_description}

This package contains library source intended for building other packages which
use the "reqsign" feature of the "%{crate}" crate.

%files       -n %{name}+reqsign-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+reqwest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+reqwest-devel %{_description}

This package contains library source intended for building other packages which
use the "reqwest" feature of the "%{crate}" crate.

%files       -n %{name}+reqwest-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rouille-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rouille-devel %{_description}

This package contains library source intended for building other packages which
use the "rouille" feature of the "%{crate}" crate.

%files       -n %{name}+rouille-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+s3-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+s3-devel %{_description}

This package contains library source intended for building other packages which
use the "s3" feature of the "%{crate}" crate.

%files       -n %{name}+s3-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sha2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sha2-devel %{_description}

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%files       -n %{name}+sha2-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+syslog-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+syslog-devel %{_description}

This package contains library source intended for building other packages which
use the "syslog" feature of the "%{crate}" crate.

%files       -n %{name}+syslog-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%files       -n %{name}+unstable-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+url-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+url-devel %{_description}

This package contains library source intended for building other packages which
use the "url" feature of the "%{crate}" crate.

%files       -n %{name}+url-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+vendored-openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+vendored-openssl-devel %{_description}

This package contains library source intended for building other packages which
use the "vendored-openssl" feature of the "%{crate}" crate.

%files       -n %{name}+vendored-openssl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+version-compare-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+version-compare-devel %{_description}

This package contains library source intended for building other packages which
use the "version-compare" feature of the "%{crate}" crate.

%files       -n %{name}+version-compare-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+webdav-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+webdav-devel %{_description}

This package contains library source intended for building other packages which
use the "webdav" feature of the "%{crate}" crate.

%files       -n %{name}+webdav-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online


%build
%if %{with dist_server}
%cargo_build -f dist-server
%else
%cargo_build
%endif

%install
rm -rf .git || true
%if %{with dist_server}
%cargo_install -f dist-server
%else
%cargo_install
%endif

%if %{with check}
%check
%if %{with dist_server}
%cargo_test -f dist-server
%else
%cargo_test
%endif

%endif

%changelog
* Mon Dec 18 2023 Cappy Ishihara <cappy@cappuchino.xyz> - 0.7.4-1
- Initial package
