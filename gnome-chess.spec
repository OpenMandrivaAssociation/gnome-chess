%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 0

Name:		gnome-chess
Version:	43.1
Release:	2
Summary:	GNOME Chess game
License:	GPLv2+ and GFDL
Group:		Games/Boards
URL:		https://wiki.gnome.org/Chess
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(x11)
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	vala
BuildRequires:	libxml2-utils
BuildRequires:	pkgconfig(x11)
BuildRequires:  meson
Obsoletes: 	glchess
Requires:	gnuchess
# For fix build issue:  "error: Package `librsvg-2.0' not found in specified Vala API directories or GObject-Introspection GIR directories" (penguin)
BuildRequires:  librsvg-vala-devel
# For help
Requires:	yelp

%description
A chess game which supports several chess engines, with 2D and optionally 3D
support if OpenGL is present.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install


%find_lang %{name} --with-gnome 

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Chess.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Chess.gschema.xml
%{_datadir}/dbus-1/services/org.gnome.Chess.service
#{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/engines.conf
%{_iconsdir}/*/*/apps/org.gnome.Chess*.*
%{_mandir}/man6/%{name}.6*
%{_datadir}/metainfo/org.gnome.Chess.appdata.xml
