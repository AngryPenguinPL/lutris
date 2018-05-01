Name:           lutris
Version:        0.4.14
Release:        %mkrel 1
Summary:        Install and play any video game easily
Group:          Games/Other
License:        GPLv3+
URL:            http://lutris.net
Source0:        http://lutris.net/releases/%{name}_%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3egg(setuptools)
BuildRequires:  python-gobject3
BuildRequires:  python-gi
BuildRequires:  python-pyxdg

Requires:       python-dbus
Requires:       python-evdev
Requires:       python-gobject3
Requires:       python-pyxdg
Requires:       python-yaml
Requires:       xrandr
Recommends:     python-pyinotify

%description
Lutris is a gaming platform for GNU/Linux. Its goal is to make
gaming on Linux as easy as possible by taking care of installing
and setting up the game for the user. The only thing you have to
do is play the game. It aims to support every game that is playable
on Linux.

%prep
%setup -q -n %{name}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/polkit-1/actions/*
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{name}/
