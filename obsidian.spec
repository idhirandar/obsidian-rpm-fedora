Name:           obsidian
Version:        1.10.3
Release:        1%{?dist}
Summary:        A powerful knowledge base on top of local Markdown files

License:        Obsidian EULA
URL:            https://obsidian.md
Source0:        Obsidian-%{version}.tar.gz

BuildArch:      x86_64
AutoReqProv:    no

Requires:       hicolor-icon-theme
Requires:       gtk3

%description
Obsidian is a powerful and extensible knowledge base that works on top of
a local folder of plain text Markdown files.

%prep
%setup -q -n obsidian-%{version}

%build
# pre-built Electron app → nothing to compile

%install
install -dm 755 %{buildroot}%{_bindir}
install -dm 755 %{buildroot}%{_datadir}/obsidian
install -dm 755 %{buildroot}%{_datadir}/applications
install -dm 755 %{buildroot}%{_datadir}/icons/hicolor/512x512/apps

# copy the whole app
cp -a * %{buildroot}%{_datadir}/obsidian/

# binary symlink
ln -s %{_datadir}/obsidian/obsidian %{buildroot}%{_bindir}/obsidian

# desktop file
cat > %{buildroot}%{_datadir}/applications/md.obsidian.Obsidian.desktop <<'DESKTOP'
[Desktop Entry]
Name=Obsidian
Comment=Knowledge base that works on local Markdown files
Exec=obsidian %U
Terminal=false
Type=Application
Icon=obsidian
StartupWMClass=obsidian
Categories=Office;Utility;TextEditor;
MimeType=text/markdown;x-scheme-handler/obsidian;
DESKTOP

# icon
install -Dm 644 resources/icon.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/obsidian.png

%files
%{_bindir}/obsidian
%{_datadir}/obsidian/
%{_datadir}/applications/md.obsidian.Obsidian.desktop
%{_datadir}/icons/hicolor/512x512/apps/obsidian.png

%changelog
* Mon Nov 24 2025 You <you@example.com> - 1.10.3-1
- Initial build that actually works
%global debug_package %{nil}
