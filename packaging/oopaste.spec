Name:           oopaste
Version:        0.1.0
Release:        1%{?dist}
Summary:        Merges lines of corresponding files sequentially using user-specified delimiters.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oopaste
Source0:        oopaste-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oopaste is a sovereign, capability-bounded STREAM MERGER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oopaste
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oopaste-uninstall

%files
/usr/bin/oopaste
/usr/bin/oopaste-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
