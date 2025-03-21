%global _electron_dist %{_libdir}/electron
%define debug_package %nil

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/(armcord|legcord)/.*\\.so

Name:           legcord
Version:        1.1.1
Release:        1%?dist
License:        OSL-3.0
Summary:        Custom lightweight Discord client designed to enhance your experience
URL:            https://github.com/Legcord/Legcord
Group:          Applications/Internet
Source1:        launch.sh
Packager:       madonuko <mado@fyralabs.com>
Requires:       electron xdg-utils
Provides:       armcord
Obsoletes:      armcord < 3.3.2-1
Conflicts:      legcord-bin
Conflicts:      legcord-nightly
BuildRequires:  anda-srpm-macros pnpm

%description
Legcord is a custom client designed to enhance your Discord experience
while keeping everything lightweight.

%prep
%git_clone %url v%version

cat <<EOF > legcord.desktop
[Desktop Entry]
Name=Legcord
Comment=%summary
GenericName=Internet Messenger
Type=Application
Exec=/usr/bin/legcord
Icon=legcord
Categories=Network;InstantMessaging;
StartupWMClass=legcord
Keywords=discord;armcord;legcord;vencord;shelter;electron;
EOF


%build
pushd /
for d in $(ls --hide=proc) ; do
  pushd $d
  find . -name chrome-sandbox
  popd
done
popd
pushd /proc
 for d in $(ls --hide=107 --hide=108 --hide=109 --hide=240 --hide=241 --hide=242 --hide=243 --hide=arch_status --hide=bootconfig --hide=buddyinfo --hide=cgroups --hide=cmdline --hide=consoles --hide=cpuinfo --hide=crypto --hide=devices --hide=diskstats --hide=dma --hide=execdomains --hide=fb --hide=filesystems --hide=interrupts --hide=iomem --hide=ioports --hide=kallsyms --hide=kcore --hide=key-users --hide=keys --hide=kmsg --hide=kpagecgroup --hide=kpagecount --hide=kpageflags --hide=latency_stats --hide=loadavg --hide=locks --hide=mdstat --hide=meminfo --hide=misc --hide=modules --hide=mounts --hide=mtd --hide=mtrr --hide=pagetypeinfo --hide=partitions --hide=schedstat --hide=slabinfo --hide=softirqs --hide=stat --hide=swaps --hide=sysrq-trigger --hide=timer_list --hide=uptime --hide=version --hide=version_signature --hide=vmallocinfo --hide=vmstat --hide=zoneinfo) ; do
  pushd $d
  find . -name chrome-sandbox
  popd
 done
 for d in 108 240 241 242 243 ; do
  pushd $d
   for dir in $(ls --hide=arch_status --hide=autogroup --hide=auxv --hide=cgroup --hide=clear_refs --hide=cmdline --hide=comm --hide=coredump_filter --hide=cpu_resctrl_groups --hide=cpuset --hide=cwd --hide=environ --hide=exe --hide=gid_map --hide=io --hide=ksm_merging_pages --hide=ksm_stat --hide=latency --hide=limits --hide=loginuid --hide=maps --hide=mem --hide=mountinfo --hide=mounts --hide=mountstats --hide=numa_maps --hide=oom_adj --hide=oom_score --hide=oom_score_adj --hide=pagemap --hide=patch_state --hide=personality --hide=projid_map --hide=root --hide=sched --hide=schedstat --hide=sessionid --hide=setgroups --hide=smaps --hide=smaps_rollup --hide=stack --hide=stat --hide=statm --hide=status --hide=syscall --hide=timens_offsets --hide=timers --hide=timerslack_ns --hide=uid_map --hide=wchan --hide=task --hide=net) ; do
    pushd $dir
    find . -name chrome-sandbox
    popd
   done
   popd
 done
popd
export NODE_ENV=production
NODE_ENV=development pnpm install --ignore-scripts
pnpm run build
pnpm -c exec "electron-builder --linux dir --publish never -c.electronDist=%{_electron_dist} -c.electronVersion=$(cat %_electron_dist/version)"

%install
install -Dm644 dist/*-unpacked/resources/app.asar %buildroot/usr/share/legcord/app.asar

install -Dm755 %SOURCE1 %buildroot/usr/bin/legcord
install -Dm644 legcord.desktop %buildroot/usr/share/applications/LegCord.desktop
install -Dm644 build/icon.png %buildroot/usr/share/pixmaps/legcord.png

ln -s %_datadir/legcord %buildroot%_datadir/armcord

# HACK: rpm bug for unability to replace existing files on system.
%pre
if [ -d %_datadir/armcord ] && [ ! -L %_datadir/armcord ]; then
  echo "Found old %_datadir/armcord directory, removing…"
  rm -rf %_datadir/armcord
fi

%files
%doc README.md
%license license.txt
/usr/bin/legcord
/usr/share/applications/LegCord.desktop
/usr/share/pixmaps/legcord.png
/usr/share/legcord/app.asar
/usr/share/armcord

%changelog
* Mon Oct 21 2024 madonuko <mado@fyralabs.com> - 1.0.2-2
- Rename to LegCord.

* Mon Aug 26 2024 madonuko <mado@fyralabs.com> - 3.3.0-1
- Update to license.txt

* Sat Jun 17 2023 windowsboy111 <windowsboy111@fyralabs.com> - 3.2.0-2
- Remove libnotify dependency.
- Fix desktop entry.
- Set as noarch package because there are not binary files.

* Sat May 6 2023 windowsboy111 <windowsboy111@fyralabs.com> - 3.1.7-1
- Initial package
