Name:           adwaita-highlight-cursor-theme
Version:        40.0
Release:        1%{?dist}
Summary:        Adwaita highlight icon theme

License:        LGPLv3+ or CC-BY-SA
# For the time being.  The changes have not be accepted upstream.
URL:            https://github.com/drepper/adwaita-cursors
Source0:        adwaita-cursors.tar.gz

BuildArch:      noarch

%description
This package contains a variant of the Adwaita cursor theme with added highlighting

%prep
%autosetup -n adwaita-cursors

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons
cp -a Adwaita-highlight $RPM_BUILD_ROOT%{_datadir}/icons

touch $RPM_BUILD_ROOT%{_datadir}/icons/Adwaita-highlight/icon-theme.cache

%transfiletriggerin -- %{_datadir}/icons/Adwaita-highlight
gtk-update-icon-cache --force %{_datadir}/icons/Adwaita-highlight &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/Adwaita-highlight
gtk-update-icon-cache --force %{_datadir}/icons/Adwaita-highlight &>/dev/null || :

%files
%license LICENSE
%dir %{_datadir}/icons/Adwaita-highlight/
%{_datadir}/icons/Adwaita-highlight/cursors/
%ghost %{_datadir}/icons/Adwaita-highlight/icon-theme.cache

%changelog
* Sat May 1 2021 Ulrich Drepper <drepper@redhat.com> - 40.0-1
- First package of the highlight cursor theme
