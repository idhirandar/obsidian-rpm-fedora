Name:           obsidian
Version:        1.11.7
Release:        1%{?dist}
Summary:        Obsidian - A powerful knowledge base on top of local Markdown files

License:        Commercial
URL:            https://obsidian.md
Source0:        Obsidian-%{version}.tar.gz

BuildArch:      x86_64
AutoReqProv:    no

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
# App itself
install -Dm755 -d %{buildroot}%{_datadir}/obsidian
cp -a * %{buildroot}%{_datadir}/obsidian/

# Binary symlink
install -Dm755 -d %{buildroot}%{_bindir}
ln -s ../share/obsidian/obsidian %{buildroot}%{_bindir}/obsidian

# Create the applications directory first
install -Dm755 -d %{buildroot}%{_datadir}/applications

# Create a proper .desktop file (Obsidian stopped shipping one)
cat > %{buildroot}%{_datadir}/applications/md.obsidian.Obsidian.desktop <<'DESK'
[Desktop Entry]
Name=Obsidian
Comment=A powerful knowledge base on top of local Markdown files
Exec=obsidian %U
Terminal=false
Type=Application
Icon=obsidian
StartupWMClass=obsidian
Categories=Office;Utility;TextEditor;
MimeType=text/markdown;x-scheme-handler/obsidian;
DESK

# Icon
install -Dm644 resources/icon.png \
               %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/obsidian.png

%post
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-desktop-database -q %{_datadir}/applications &>/dev/null || :

%postun
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-desktop-database -q %{_datadir}/applications &>/dev/null || :

%files
%license LICENSE.electron.txt LICENSES.chromium.html
%{_bindir}/obsidian
%dir %{_datadir}/obsidian
%{_datadir}/obsidian/*
%{_datadir}/applications/md.obsidian.Obsidian.desktop
%{_datadir}/icons/hicolor/512x512/apps/obsidian.png

%changelog
* Fri Feb 6 2026 Dhirandar <idhirandar@gmail.com> - 1.11.7-1
- Final working native RPM for Obsidian 1.11.7 (creates .desktop ourselves)
%global debug_package %{nil}
