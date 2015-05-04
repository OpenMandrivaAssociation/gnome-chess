%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-chess
Version:	3.16.1
Release:	1
Summary:	GNOME Chess game
License:	GPLv2+ and GFDL
Group:		Games/Boards
URL:		https://wiki.gnome.org/Chess
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(x11)
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	vala-devel >= 0.16.0
BuildRequires:	libxml2-utils
Obsoletes: 	glchess
Requires:	gnuchess
# For help
Requires:	yelp

%description
A chess game which supports several chess engines, with 2D and optionally 3D
support if OpenGL is present.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome --with-help

%files -f %{name}.lang
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.chess.gschema.xml
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/engines.conf
%{_iconsdir}/*/*/apps/%{name}.*
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Sat Feb 21 2015 ovitters <ovitters> 3.14.3-1.mga5
+ Revision: 816238
- new version 3.14.3

* Tue Feb 17 2015 wally <wally> 3.14.2-2.mga5
+ Revision: 815337
- require yelp for showing help

* Mon Dec 22 2014 ovitters <ovitters> 3.14.2-1.mga5
+ Revision: 804793
- new version 3.14.2

* Tue Nov 11 2014 ovitters <ovitters> 3.14.1-1.mga5
+ Revision: 796305
- new version 3.14.1

* Wed Oct 15 2014 umeabot <umeabot> 3.14.0-2.mga5
+ Revision: 743235
- Second Mageia 5 Mass Rebuild

* Mon Sep 22 2014 ovitters <ovitters> 3.14.0-1.mga5
+ Revision: 719184
- new version 3.14.0

* Tue Sep 16 2014 umeabot <umeabot> 3.13.92-2.mga5
+ Revision: 679704
- Mageia 5 Mass Rebuild

* Tue Sep 16 2014 ovitters <ovitters> 3.13.92-1.mga5
+ Revision: 676962
- new version 3.13.92

* Thu Aug 21 2014 ovitters <ovitters> 3.13.90-1.mga5
+ Revision: 666279
- new version 3.13.90

* Wed Jul 23 2014 ovitters <ovitters> 3.13.4-1.mga5
+ Revision: 655745
- new version 3.13.4

* Fri May 30 2014 ovitters <ovitters> 3.13.1-1.mga5
+ Revision: 627982
- new version 3.13.1

* Mon May 12 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622085
- new version 3.12.2

* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 614071
- new version 3.12.1

* Mon Mar 24 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 607932
- new version 3.12.0

* Sun Mar 16 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604237
- new version 3.11.92

* Mon Feb 17 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 593708
- new version 3.11.90

* Wed Feb 05 2014 dams <dams> 3.11.4-1.mga5
+ Revision: 583080
- new version 3.11.4

* Wed Feb 05 2014 dams <dams> 3.11.3-1.mga5
+ Revision: 583007
- new version 3.11.3

  + ovitters <ovitters>
    - new version 3.10.3

* Mon Nov 11 2013 ovitters <ovitters> 3.10.2-1.mga4
+ Revision: 550505
- new version 3.10.2

* Sat Nov 09 2013 ovitters <ovitters> 3.10.1.1-3.mga4
+ Revision: 550158
- fix url

* Tue Oct 22 2013 umeabot <umeabot> 3.10.1.1-2.mga4
+ Revision: 542016
- Mageia 4 Mass Rebuild

* Mon Oct 14 2013 ovitters <ovitters> 3.10.1.1-1.mga4
+ Revision: 496753
- new version 3.10.1.1

* Sat Oct 12 2013 ovitters <ovitters> 3.10.1-1.mga4
+ Revision: 495861
- new version 3.10.1

* Mon Sep 23 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 483888
- new version 3.10.0

* Mon Sep 16 2013 ovitters <ovitters> 3.9.92-1.mga4
+ Revision: 480449
- new version 3.9.92

* Tue Aug 27 2013 ovitters <ovitters> 3.9.90-1.mga4
+ Revision: 472095
- new version 3.9.90

* Tue Jul 30 2013 ovitters <ovitters> 3.9.5-1.mga4
+ Revision: 460831
- new version 3.9.5

* Fri Jul 26 2013 dams <dams> 3.9.4-1.mga4
+ Revision: 458228
- new version 3.9.4

* Wed Jun 26 2013 dams <dams> 3.8.3-1.mga4
+ Revision: 446704
- new version 3.8.3

  + fwang <fwang>
    - cleanup spec

* Sun Jun 09 2013 dams <dams> 3.8.2-1.mga4
+ Revision: 440783
- add 'libxml2-utils' as BR
- imported package gnome-chess

