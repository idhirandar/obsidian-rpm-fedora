Name:           obsidian
Version:        1.10.3
Release:        1%{?dist}
Summary:        Obsidian - A powerful knowledge base on top of local Markdown files

License:        Commercial (Obsidian EULA)
URL:            https://obsidian.md
# Direct official download (no rename needed)
Source0:        https://github.com/obsidianmd/obsidian-releases/releases/download/v%{version}/Obsidian-%{version}.tar.gz

BuildArch:      x86_64
AutoReqProv:    no

# Minimal runtime dependencies
Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       libX11
Requires:       alsa-lib
Requires:       nss

%description
Obsidian is a powerful and extensible knowledge base that works on top of a local
folder of plain text Markdown files.

%prep
%autosetup -n obsidian-%{version}

%install
# App
install -Dm755 -d %{buildroot}%{_datadir}/obsidian
cp -a * %{buildroot}%{_datadir}/obsidian/

# Binary symlink
install -Dm755 -d %{buildroot}%{_bindir}
ln -s ../share/obsidian/obsidian %{buildroot}%{_bindir}/obsidian

# Desktop file (Fedora guidelines compliant)
install -Dm644 %{buildroot}%{_datadir}/obsidian/resources/app.desktop \
               %{buildroot}%{_datadir}/applications/md.obsidian.Obsidian.desktop
# Fix Exec= and Icon= paths (they point to relative paths inside the tarball)
sed -i 's|Exec=.*|Exec=obsidian %U|' \
       %{buildroot}%{_datadir}/applications/md.obsidian.Obsidian.desktop
sed -i 's|Icon=.*|Icon=obsidian|' \
       %{buildroot}%{_datadir}/applications/md.obsidian.Obsidian.desktop

# Icon (official 512×512)
install -Dm644 resources/icon.png \
               %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/obsidian.png

# Update desktop database and icon cache at install/remove
%post
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor 2>/dev/null || :
%{_bindir}/update-desktop-database -q %{_datadir}/applications 2>/dev/null || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor 2>/dev/null || :
%{_bindir}/update-desktop-database -q %{_datadir}/applications 2>/dev/null || :

%files
%license LICENSE.electron.txt LICENSES.chromium.html
%{_bindir}/obsidian
%{_datadir}/obsidian/
%{_datadir}/applications/md.obsidian.Obsidian.desktop
%{_datadir}/icons/hicolor/512x512/apps/obsidian.png

%changelog
* Mon Nov 24 2025 Dhirandar <idhirandar@example.com> - 1.10.3-1
- Initial native RPM package
