%add_findprov_lib_path %_libdir/pidgin
%add_findprov_lib_path %_libdir/purple-2
%add_findprov_lib_path %_libdir/finch
%add_findreq_skiplist %perl_vendor_archlib/*

%def_disable perl 1
%def_disable tcl 1
%def_disable tk 1
%def_disable nss 1
%def_disable cyrussasl 1
%def_enable gevolution 1
%def_enable nas 1
%def_disable mono 1
%def_enable consoleui 1
%def_enable dbus 1

Name: pidgin
Version: 2.1.1
Release: alt1

Summary: A GTK+ based multiprotocol instant messaging client
License: GPL
Group: Networking/Instant messaging
Url:  http://pidgin.im/

Packager: Alexey Shabalin <shaba@altlinux.ru>

Source0: %name-%version.tar.bz2
Source1: %name-be.po.bz2

Patch0: pidgin-2.1.0-alt-linking-plugins.patch
Patch1: pidgin-2.1.0-alt-makefile-order.patch
Patch2: pidgin-2.1.0-alt-fixing-pidgin-plugins.patch
Patch3: pidgin-2.1.0-alt-linking-finch-plugins.patch

Provides: gaim = %version
Obsoletes: gaim

Requires: libpurple = %version-%release

BuildRequires: doxygen gcc-c++ GConf gnome-libs-devel graphviz 
BuildRequires: gstreamer-devel imake libgnutls-devel libgpg-error libgtkspell-devel 
BuildRequires: libSM-devel libsqlite3-devel 
#BuildRequires: libstartup-notification-devel libXScrnSaver-devel packages-info-i18n-common 
BuildRequires: libstartup-notification-devel libXScrnSaver-devel
BuildRequires: python-modules-encodings xorg-cf-files libidn-devel 

BuildPreReq: desktop-file-utils

Requires(post,postun): desktop-file-utils
PreReq: GConf

%if_enabled consoleui
BuildRequires:	libncurses-devel libncursesw-devel
%endif

%if_enabled dbus
BuildRequires: libdbus-devel libdbus-glib-devel
%endif

%if_enabled nss
BuildRequires: libnss-devel libnspr-devel
%endif

%if_enabled cyrussasl
BuildRequires: libsasl2-devel 
%endif

%description
Pidgin allows you to talk to anyone using a variety of messaging
protocols including AIM, MSN, Yahoo!, Jabber, Bonjour, Gadu-Gadu,
ICQ, IRC, Novell Groupwise, QQ, Lotus Sametime, SILC, Simple and
Zephyr.  These protocols are implemented using a modular, easy to
use design.  To use a protocol, just add an account using the
account editor.

Pidgin supports many common features of other clients, as well as many
unique features, such as perl scripting, TCL scripting and C plugins.

Pidgin is not affiliated with or endorsed by America Online, Inc.,
Microsoft Corporation, Yahoo! Inc., or ICQ Inc.

%package devel
Summary: Development headers, documentation, and libraries for Pidgin
Group: Development/Other
Requires: %name = %version-%release
Requires: libpurple-devel = %version-%release
Provides: gaim-devel = %version
Obsoletes: gaim-devel

%description devel  
The pidgin-devel package contains the header files, developer
documentation, and libraries required for development of Pidgin scripts
and plugins.

%package -n libpurple
Summary: libpurple library for IM clients like Pidgin and Finch
Group: Networking/Instant messaging

%description -n libpurple
libpurple contains the core IM support for IM clients such as Pidgin
and Finch.

libpurple supports a variety of messaging protocols including AIM, MSN,
Yahoo!, Jabber, Bonjour, Gadu-Gadu, ICQ, IRC, Novell Groupwise, QQ,
Lotus Sametime, SILC, Simple and Zephyr.

%package -n libpurple-devel
Summary: Development headers, documentation, and libraries for libpurple
Group: Development/Other
Requires: libpurple = %version-%release

%description -n libpurple-devel
The libpurple-devel package contains the header files, developer
documentation, and libraries required for development of libpurple based
instant messaging clients or plugins for any libpurple based client.

%if_enabled gevolution
%package -n %name-gevolution
Summary: Gevolution plugin for Pidgin
Group: Networking/Instant messaging
Requires: %name = %version-%release
BuildRequires:	evolution-data-server-devel
Obsoletes: gaim-gevolution
Provides: gaim-gevolution = %version

%description -n %name-gevolution
Gevolution plugin for Pidgin.
%endif

%if_enabled mono
%package -n libpurple-mono
Summary:    Mono .NET plugin support for Pidgin
Group: Networking/Instant messaging
Requires: libpurple = %version-%release
BuildRequires:  mono-devel mono-mcs rpm-build-mono mono-nunit 
BuildRequires:	/proc
Obsoletes: gaim-mono 
Provides: gaim-mono = %version

%description -n libpurple-mono
Mono support for Pidgin.
%endif

%if_enabled perl
%package -n libpurple-perl
Summary: Perl support for Pidgin
Group: Networking/Instant messaging
Requires: libpurple = %version-%release
Requires: perl-base
BuildRequires:  perl-devel perl-XML-Parser 
Obsoletes: gaim-perl
Provides: gaim-perl = %version

%description -n libpurple-perl  
Perl support for Pidgin.
%endif

%if_enabled tcl
%package -n libpurple-tcl
Summary: Tcl/Tk support for Pidgin
Group: Networking/Instant messaging
Requires: libpurple = %version-%release
BuildRequires:	tcl-devel tk-devel
Obsoletes: gaim-tcl 
Provides: gaim-tcl = %version

%description -n libpurple-tcl  
Tcl/Tk support for Pidgin.
%endif

%if_enabled consoleui
%package -n finch
Summary:    A text-based user interface for Pidgin
Group: Networking/Instant messaging
Requires:   libpurple = %version-%release
Provides: gaim-text = %version
Obsoletes: gaim-text

%description -n finch
A text-based user interface for using libpurple.  This can be run from a
standard text console or from a terminal within X Windows.  It
uses ncurses and our homegrown gnt library for drawing windows
and text.

%package -n finch-devel
Summary:    Headers etc. for finch stuffs
Group: Development/Other
Requires: finch = %version-%release
Requires: libpurple-devel = %version-%release
Provides: gaim-text-devel = %version
Obsoletes: gaim-text-devel

%description -n finch-devel
The finch-devel package contains the header files, developer
documentation, and libraries required for development of Finch scripts
and plugins.

%endif

%prep
%setup -q -n %name-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# belarusian translation
bzcat %SOURCE1 > po/be.po
%__subst 's,\(ALL_LINGUAS=\"\),\1be ,' configure

# %%__autoreconf

%__mkdir_p %buildroot/usr/share/dbus-1/services/

%configure	--enable-dot \
		--enable-doxygen \
		%{subst_enable mono} \
		%{subst_enable nas} \
		%{subst_enable perl} \
		%{subst_enable gevolution} \
		%{subst_enable dbus} \
		%{subst_enable tk} \
		%{subst_enable tcl} \
		%{subst_enable nss} \
		%{subst_enable consoleui} \
%if_enabled cyrussasl
		--enable-cyrus-sasl \
%else
		--disable-cyrus-sasl \
%endif
%if_enabled nss
		--with-nss-includes=%_includedir/nss \
		--with-nspr-includes=%_includedir/nspr \
		--with-nspr-libs=%_libdir \
		--with-nss-libs=%_libdir \
%endif
%if_enabled perl
		--with-perl-lib=vendor \
%endif
		--with-dbus-session-dir=%buildroot/usr/share/dbus-1/services/ 

%make_build 

%install

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%make_install install DESTDIR=%buildroot
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

%__mkdir_p %buildroot/%_datadir/applications/


# Menu disabled
#%__mkdir_p %buildroot%_menudir
#%__cat >%buildroot%_menudir/%name <<EOF
#?package(%name): command="%_bindir/%name" needs="X11" \
#icon="%name.xpm" section="/Networking/Instant messaging" \
#title="Gaim" longtitle="A multiprotocol Instant Messenger"
#EOF

%find_lang --with-gnome %name

%post
%gconf2_install purple
%update_menus
%update_desktopdb
%post_ldconfig

%preun
if [ $1 = 0 ]; then
    %gconf2_uninstall purple
fi

%postun
%clean_menus
%clean_desktopdb
%postun_ldconfig

%post -n libpurple -p %post_ldconfig
%post -n finch -p %post_ldconfig


%files -f %name.lang
%doc AUTHORS  COPYING  COPYRIGHT ChangeLog INSTALL NEWS README README.MTN
%doc doc/*.txt
%_bindir/%name
%_libdir/%name
# %%_datadir/dbus-1/services/*.service
%config %_sysconfdir/gconf/schemas/*
%exclude %_libdir/%name/*.la

%_man1dir/%name.*
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name
%_iconsdir/hicolor/??x??/apps/%{name}*.png
%_iconsdir/hicolor/scalable/apps/%{name}*.svg

%if_enabled gevolution
%exclude %_libdir/%name/gevolution.so
%endif

%if_enabled perl
%perl_vendor_archlib/Pidgin.pm
%dir %perl_vendor_autolib/Pidgin
%perl_vendor_autolib/Pidgin/*
%perl_vendor_man3dir/Pidgin*
%endif

%files -n libpurple 
%_libdir/libpurple.so.* 
%_libdir/purple-2
%_datadir/pixmaps/purple
%_datadir/sounds/purple
%exclude %_libdir/purple-2/*.la

%if_enabled tcl
%exclude %_libdir/purple-2/tcl.so
%endif
%if_enabled mono
%exclude %_libdir/purple-2/mono.so
%exclude %_libdir/purple-2/*.dll
%endif
%if_enabled perl
%exclude %_libdir/purple-2/perl.so
%endif

%if_enabled dbus
%_bindir/purple-client-example
%_bindir/purple-remote
%_bindir/purple-send
%_bindir/purple-send-async
%_bindir/purple-url-handler
%_libdir/libpurple-client.so.*
%endif

%if_enabled gevolution
%files -n %name-gevolution
%_libdir/%name/gevolution.so
%endif

%if_enabled mono
%files -n libpurple-mono
%_libdir/purple-2/mono.so
%_libdir/purple-2/*.dll
%endif

%if_enabled perl
%files -n libpurple-perl
%_libdir/purple-2/perl.so
%perl_vendor_archlib/Purple.pm
%dir %perl_vendor_autolib/Purple
%perl_vendor_autolib/Purple/*
%perl_vendor_man3dir/Purple*
%endif

%if_enabled tcl
%files -n libpurple-tcl
%_libdir/purple-2/tcl.so
%endif

%files devel
%_includedir/%name
%_libdir/pkgconfig/%name.pc

%files -n libpurple-devel
%doc ChangeLog.API HACKING PLUGIN_HOWTO
%doc libpurple/purple-notifications-example
%_includedir/libpurple
%_libdir/libpurple.so
%_libdir/libpurple-client.so
%_libdir/pkgconfig/purple.pc
%_datadir/aclocal/purple.m4

%if_enabled consoleui

%files -n finch
%_man1dir/finch.*
%_bindir/finch
%_libdir/libgnt.so.*
%_libdir/gnt
%_libdir/finch
%exclude %_libdir/finch/*.la
%exclude %_libdir/gnt/*.la

%files -n finch-devel
%_includedir/finch
%_includedir/gnt
%_libdir/pkgconfig/gnt.pc
%_libdir/libgnt.so

%endif

%changelog
* Sat Aug 25 2007 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- 2.1.1
- move sounds from pidgin to purple package
- more fine use icons in %%files

* Sat Aug 18 2007 Igor Zubkov <icesik@altlinux.org> 2.1.0-alt2
- NMU:
  + add packager tag
  + remove packages-info-i18n-common from buildrequires
  + fix plugins linking

* Mon Aug 13 2007 Alexey Shabalin <shaba@altlinux.ru> 2.1.0-alt1
- 2.1.0
- mini fix spec in %%files

* Thu Jun 21 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Sat Jun 02 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Thu May 10 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt9
- fix spec

* Mon May 07 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt8
- 2.0.0 release
- rename gaim -> pidgin
- rename libgaim -> libpurple
- rename gaim-test -> finch
- drop all patches

* Sat Mar 31 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt7.beta6
- add PreReq: GConf (#11166)

* Tue Feb 27 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt6.beta6
- fix library path provides
- drop gaim-text (move files to gaim)
- drop gaim-text-devel (move header files to gaim-devel)
- add patches from debian (6,102.103,111)

* Mon Feb 05 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt5.beta6
- 2.0.0beta6
- remove patch for perl

* Mon Dec 25 2006 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt4.beta5
- rebuild with new dbus

* Thu Nov 30 2006 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt3.beta5
- no build plugins: perl, tk/tcl, mono
- disable support libnss/libnspr, cyrus-sasl
- fix spec

* Wed Nov 15 2006 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt2.beta5
-  2.0.0beta5

* Mon Dec 19 2005 Vital Khilko <vk@altlinux.ru> 2.0.0beta1-alt1
- new version

* Thu Dec 08 2005 Vital Khilko <vk@altlinux.ru> 1.5.0-alt2
- #8215

* Fri Aug 12 2005 Vital Khilko <vk@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Mon Jul 11 2005 Vital Khilko <vk@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Tue Jun 21 2005 Vital Khilko <vk@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Mon May 16 2005 Vital Khilko <vk@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Mon Apr 04 2005 Vital Khilko <vk@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Tue Mar 22 2005 Vital Khilko <vk@altlinux.ru> 1.2.0-alt1
- 1.2.0
- gevolution plugin moved to separate package 
- added Perl support

* Wed Mar 02 2005 Vital Khilko <vk@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Tue Feb 22 2005 Vital Khilko <vk@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Tue Feb 01 2005 Vital Khilko <vk@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Thu Jan 20 2005 Vital Khilko <vk@altlinux.ru> 1.1.1-alt1
- 1.1.1
- xosd plugin moved to separate package
- added package independent smileys themes support

* Mon Nov 15 2004 Vital Khilko <vk@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Fri Nov 05 2004 Vital Khilko <vk@altlinux.ru> 1.0.2-alt2
- Rebuilded with libgnutls

* Mon Oct 25 2004 Vital Khilko <vk@altlinux.ru> 1.0.2-alt1
- new version released
- added belarusian translation

* Mon Sep 20 2004 Vital Khilko <vk@altlinux.ru> 1.0.0-alt1
- new version released

* Mon Aug 30 2004 Vital Khilko <vk@altlinux.ru> 0.82.1-alt1
- new version released

* Wed Aug 11 2004 Vital Khilko <vk@altlinux.ru> 0.81-alt1
- new version released
- include osd plugin

* Wed Jul 21 2004 Vital Khilko <vk@altlinux.ru> 0.80-alt2
- enabled evolution plugin

* Mon Jul 19 2004 Vital Khilko <vk@altlinux.ru> 0.80-alt1
- new version released

* Wed Jun 09 2004 Vital Khilko <vk@altlinux.ru> 0.78-alt2
- oscar protocol patch by Slava Astashonak

* Mon May 31 2004 Vital Khilko <vk@altlinux.ru> 0.78-alt1
- new version released

* Sun Apr 25 2004 Vital Khilko <vk@altlinux.ru> 0.77-alt1
- new version released

* Sun Apr 04 2004 Vital Khilko <vk@altlinux.ru> 0.76-alt1
- new version released 

* Tue Mar 16 2004 Vital Khilko <vk@altlinux.ru> 0.75-alt2
- added security patch

* Thu Dec 11 2003 Vital Khilko <vk@altlinux.ru> 0.74-alt1
- new version released
- enabled all features

* Fri Jul 18 2003 Grigory Milev <week@altlinux.ru> 0.65-alt1
- new version released

* Wed Apr 16 2003 Grigory Milev <week@altlinux.ru> 0.61-alt1
- new version released

* Wed Jan 29 2003 Grigory Milev <week@altlinux.ru> 0.59.8-alt2
- added recode plugin

* Wed Jan  8 2003 Grigory Milev <week@altlinux.ru> 0.59.8-alt1
- new version released

* Tue Nov 12 2002 AEN <aen@altlinux.ru> 0.59.1-alt1
- new version (non maintainer build)

* Mon Apr 29 2002 Grigory Milev <week@altlinux.ru> 0.57-alt1
- new version released

* Mon Apr  1 2002 Grigory Milev <week@altlinux.ru> 0.55-alt1
- new version released

* Mon Mar  4 2002 Grigory Milev <week@altlinux.ru> 0.53-alt1
- new version released

* Tue Feb 19 2002 Grigory Milev <week@altlinux.ru> 0.52-alt1
- new version released

* Mon Jan 28 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.51-alt2
- Updated buildrequires.

* Fri Jan 25 2002 Grigory Milev <week@altlinux.ru> 0.51-alt1
- new version released

* Mon Dec 17 2001 Grigory Milev <week@altlinux.ru> 0.50-alt1
- New version released

* Thu Nov 15 2001 Alexander Bokovoy <ab@altlinux.ru> 0.48-alt2
- 0.48
- wmgaim + recode from Grigory Bakunov (black@asplinux.ru)

* Mon Oct 15 2001 Stanislav Ievlev <inger@altlinux.ru> 0.44-alt1
- 0.44

* Wed Jul 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.11.0-alt2
- Rebuilt with new perl.
 
* Mon Jun 25 2001 Stanislav Ievlev <inger@altlinux.ru> 0.11.0-alt1
- 0.11.0 . Rebuilt with perl-5.6.1

* Sat Jan 13 2001 AEN <aen@logic.ru>
- RE  adaptation

* Tue Oct 10 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.10.3-1mdk
- up to 0.10.3

* Tue Sep 26 2000 Daouda Lo <daouda@mandrakesoft.com> 0.9.20-5mdk
- menu title should begin with capital letter.
- ICQ section was replaced by Instant messaging.

* Thu Sep  7 2000 Vincent Saugey <vince@mandrakesoft.com> 0.9.20-4mdk
- Adding small and large icons

* Tue Aug 29 2000 Vincent Saugey <vince@mandrakesoft.com> 0.9.20-3mdk
- Change icon for menu

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.9.20-2mdk
- automatically added BuildRequires

* Mon Jul 17 2000 Vincent Saugey <vince@mandrakesoft.com> 0.9.20-1mdk
- up to 0.9.20

* Fri Jun 23 2000 Vincent Saugey <vince@mandrakesoft.com> 0.9.19-1mdk
- 0.9.19

* Thu Jun  8 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.9.18-1mdk
- 0.9.18
- minor fixes in specfile

* Fri Apr 28 2000 Daouda Lo <daouda@mandrakesoft.com> 0.9.11-3mdk
- add 32*32 icon

* Fri Mar 31 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.9.11-2mdk
- Don't +x the menu entries.

* Fri Mar 31 2000 John Buswell <johnb@mandrakesoft.com> 0.9.11-1mdk
- v0.9.11
- Added menu
- fixed group
- spec-helper

* Wed Nov 03 1999 John Buswell <johnb@mandrakesoft.com>
Build Release

* Tue Nov 02 1999 Lenny Cartier <lenny@mandrakesoft.com>
v0.9.9

* Wed Oct 13 1999 Lenny Cartier <lenny@mandrakesoft.com>
- Specfile adaptations.
