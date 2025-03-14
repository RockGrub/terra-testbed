Name:           umdive
Version:        0.1.3
Release:        1%?dist
Summary:        Chroot utility (just like arch-chroot)
License:        MIT
URL:            https://github.com/Ultramarine-Linux/dive
Source0:		%url/archive/refs/tags/v%version.tar.gz
Requires:       (%_bindir/chroot or %_sbindir/chroot)
Requires:       %_bindir/mount
BuildRequires:  anda-srpm-macros nim mock
Provides:       dive = %version-%release

%description
%summary.

%prep
%autosetup -n dive-%version
%nim_prep

%build
%nim_c src/dive

%install
install -Dpm755 src/dive %buildroot%_bindir/dive

%files
%doc README.md
%license LICENSE
%_bindir/dive
