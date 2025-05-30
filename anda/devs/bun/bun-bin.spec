%define debug_package %nil
%ifarch x86_64
%global a x64-baseline
%elifarch aarch64
%global a aarch64
%endif

Name:			bun-bin
Version:		1.2.15
Release:		1%?dist
Summary:		Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one
License:		MIT
URL:			https://bun.sh
Source0:		https://github.com/oven-sh/bun/releases/download/bun-v%version/bun-linux-%a.zip
BuildRequires:	unzip

%description
%summary.


%package bash-completion
Summary:		Bash completion for %{name}
Requires:		%{name} = %{version}-%{release}
Requires: 		bash-completion
Supplements:	(%{name} and bash-completion)

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:		Fish completion for %{name}
Requires:		%{name} = %{version}-%{release}
Requires:		fish
Supplements:	(%{name} and fish)

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:		Zsh completion for %{name}
Requires:		%{name} = %{version}-%{release}
Requires:		zsh
Supplements:	(%{name} and zsh)

%description zsh-completion
Zsh command line completion support for %{name}.


%prep
%autosetup -n bun-linux-%a
cat<<EOF > LICENSE
MIT License

Copyright (c) Jarred Sumner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

%install
declare -a shells=("zsh" "bash" "fish")
for s in "${shells[@]}"; do
	SHELL=$s ./bun completions > bun.$s
done

install -Dpm755 bun -t %buildroot%_bindir
install -Dm644 bun.zsh %buildroot%zsh_completions_dir/_bun
install -Dm644 bun.bash -t %buildroot%bash_completions_dir
install -Dm644 bun.fish -t %buildroot%fish_completions_dir
ln -s bun %buildroot%_bindir/bunx

%files
%license LICENSE
%_bindir/bun
%_bindir/bunx

%files bash-completion
%bash_completions_dir/bun.bash

%files fish-completion
%fish_completions_dir/bun.fish

%files zsh-completion
%zsh_completions_dir/_bun
