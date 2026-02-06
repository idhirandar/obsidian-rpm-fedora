# Obsidian native RPM for Fedora (no Flatpak lag)

This repo contains only the `.spec` file and instructions to build a clean, native Obsidian RPM yourself.

**No pre-built binary is distributed** — you download the official tarball directly from Obsidian.

### How to build (takes 30 seconds)

```bash
# 1. Download official tarball
wget https://github.com/obsidianmd/obsidian-releases/releases/download/v1.11.7/obsidian-1.11.7.tar.gz

# 2. Install build tools (once)
sudo dnf install rpmdevtools

# 3. Build the RPM
rpmdev-setuptree
cp Obsidian-1.11.3.tar.gz obsidian.spec ~/.rpmmacros
spectool -g -R obsidian.spec
rpmbuild -ba obsidian.spec

# 4. Install
sudo dnf install ~/rpmbuild/RPMS/x86_64/obsidian-*.rpm
