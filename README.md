# Obsidian RPM for Fedora

Build a native Fedora RPM from Obsidian’s official Linux tarball, without Flatpak.

This repository contains the RPM spec file and build instructions. 

**No pre-built binaries are distributed.** 

The build repackages Obsidian’s official binaries; it does not compile Obsidian from source.

Run the commands below from the directory containing `obsidian.spec`.

## Install build tools

```bash
sudo dnf install rpmdevtools
```

## Prepare the build directories

```bash
rpmdev-setuptree
cp obsidian.spec ~/rpmbuild/SPECS/
```

## Download the official tarball
```bash
wget https://github.com/obsidianmd/obsidian-releases/releases/download/v{versoin_you_need}/obsidian-{versoin_you_need}.tar.gz"
```

## Build the RPM

Install any dependencies declared by the spec, then build as your regular user:

```bash
sudo dnf builddep ~/rpmbuild/SPECS/obsidian.spec
rpmbuild -ba ~/rpmbuild/SPECS/obsidian.spec
```

**Do not run `rpmbuild` with `sudo`.**

The installable RPM is written to:

```text
~/rpmbuild/RPMS/x86_64/
```

## Install

```bash
sudo dnf install ~/rpmbuild/RPMS/x86_64/obsidian-*.rpm
```

If that directory contains several builds, specify the exact RPM filename.

Launch Obsidian from your application menu or terminal:

```bash
obsidian
```

## Updating

Update `Version` in `obsidian.spec`, then repeat the preparation, download, build, and installation steps.

When changing **only** the packaging without changing the Obsidian version, increment `Release` so DNF recognises the new RPM as an upgrade.

## Notes

Obsidian remains proprietary software, subject to its own licence terms. This repository provides packaging instructions, not an alternative licence for Obsidian.

Using an RPM avoids the Flatpak runtime and sandbox.
