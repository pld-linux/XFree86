Summary:	XFree86 Window System servers and basic programs
Summary(de):	Xfree86 Window-System-Server und grundlegende Programme
Summary(fr):	Serveurs du système XFree86 et programmes de base
Summary(pl):	XFree86 Window System wraz z podstawowymi programami
Summary(tr):	XFree86 Pencereleme Sistemi sunucularý ve temel programlar
Name: 		XFree86
Version:	4.0
Release:	0.1
Copyright:	MIT
Group:		X11/XFree86
Group(pl):	X11/XFree86
Source0:	ftp://ftp.xfree86.org/pub/XFree86/4.0/source/X400src-1.tgz
Source3:	xdm.pamd
Source4:	xdm.initd
Source5:	xfs.initd
Source6:	xfs.config
Source7:	xserver.pamd
Source8:	XTerm.ad-pl
Source9:	xdm.sysconfig
Source10:	xfs.sysconfig
Source11:	twm.desktop
Source12:	xclipboard.desktop
Source13:	xconsole.desktop
Source14:	xterm.desktop
Source15:	xlogo64.png
Patch0:		XFree86-4.0-PLD.patch
Patch1:		XFree86-HasZlib.patch
Patch2:		XFree86-DisableDebug.patch
Patch3:		XFree86-3.9.18-Xwrapper.patch
Patch4:		XFree86-3.9.17-PAM.patch
Patch5:		XFree86-4.0-GLU.patch
Patch6:		XFree86-4.0-makedepend.patch

BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
BuildRequires:	utempter-devel
BuildRequires:	tcl-devel
BuildRequires:	pam-devel
Requires:	xauth
Exclusivearch:	%{ix86} alpha sparc m68k armv4l noarch
Buildroot:	/tmp/%{name}-%{version}-root/

%ifarch sparc
Obsoletes: X11R6.1
%endif

%define		_fontdir	/usr/share/fonts
%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man
%define		_appnkldir	%{_datadir}/applnk

%description
If you want to install the X Window System (TM) on your machine, you'll
need to install XFree86.

The X Window System provides the base technology for developing graphical
user interfaces. Simply stated, X draws the elements of the GUI on the
user's screen and builds methods for sending user interactions back to the
application. X also supports remote application deployment--running an
application on another computer while viewing the input/output on your
machine. X is a powerful environment which supports many different
applications, such as games, programming tools, graphics programs, text
editors, etc. XFree86 is the version of X which runs on Linux, as well as
other platforms.

This package contains the basic fonts, programs and documentation for an X
workstation. However, this package doesn't provide the program which you
will need to drive your video hardware. To control your video card, you'll
need the particular X server package which corresponds to your computer's
video card.

%description -l de
X-Windows ist eine voll funktionsfähige grafische Benutzeroberfläche mit
mehreren Fenstern, mehreren Clients und verschiedenen Arten von Fenstern. Es
kommt auf den meisten Unix-Plattformen zum Einsatz. Die Clients lassen sich
auch mit Hilfe anderer Fenstersysteme anzeigen. Das X-Protokoll gestattet
die Ausführung der Applikationen direkt auf lokalen Rechnern oder über ein
Netz und bietet große Flexibilität bei Client-Server-Implementierungen.

%description -l pl
X Window System jest graficznym interfejsem u¿ytkownika, cechuje siê
mo¿liwo¶ci± pracy w wielu oknach, z wieloma klientami i do tego w ró¿nych
wystrojach okien. :) Jest u¿ywany na wiêkszo¶ci platform sytemów Unix, a
klienci mog± byæ uruchamiani tak¿e pod innymi popularnymi systemami
okienkowymi. Protokó³ X pozwala na uruchamianie aplikacji zarówno z lokalnej
maszyny jak i poprzez sieæ - daj±c przez to elastyczn± implementacjê
architektury klient/serwer.

Pakiet ten nie zawiera X serwera który jest po¶rednikiem z Twoj± kart±
graficzn± (jest on w innym pakiecie).

%description -l tr
X Window sistemi, çoklu pencere, çoklu istemci ve çeþitli pencere
stilleriyle geniþ özelliklere sahip bir Grafik Kullanýcý Arabirimidir. Çoðu
UNIX sisteminde çalýþtýðý gibi istemcileri de birçok pencereleme sistemiyle
çalýþabilir. X protokolu kullanan uygulamalarýn yerel makina veya bilgisayar
aðý üzerinden çalýþtýrýlabilmesi esnek bir istemci/sunucu ortamý saðlar. Bu
paket bir X istasyonu için gerekli olan temel yazýtiplerini, programlarý ve
belgeleri sunar. Ekran kartýnýzý sürmek için gerekli olan X sunucusu bu
pakete dahil deðildir.

%package modules
Summary:	Modules with X servers extensions
Summary(pl):	Wspólne modu³y rozszerzeñ dla wszystkich X serwerów
Group:		X11/XFree86
Group(pl):	X11/XFree86

%description modules
Modules with X servers extensions.

%description -l pl modules
Wspólne modu³y rozszerzeñ dla wszystkich X serwerów.

%package libs
Summary:	X11R6 shared libraries
Summary(de):	X11R6 shared Libraries
Summary(pl):	Biblioteki dzielone dla X11R6
Summary(fr):	Bibliothèques partagées X11R6
Group:		X11/XFree86
Group(pl):	X11/XFree86
Prereq:		grep
Prereq:		/sbin/ldconfig
Obsoletes:	Mesa
Obsoletes:	Mesa-devel

%ifarch sparc
Obsoletes: X11R6.1-libs
%endif

%description libs
XFree86-libs contains the shared libraries that most X programs need to run
properly. These shared libraries are in a separate package in order to
reduce the disk space needed to run X applications on a machine without an X
server (i.e, over a network).

%description -l de libs
Dieses Paket enthält die zur gemeinsamen Nutzung vorgesehenen Libraries, die
die meisten X-Programme für den einwandfreien Betrieb benötigen. Sie wurden
in einem separaten Paket untergebracht, um den Festplattenspeicherplatz auf
Computern zu reduzieren, die ohne einen X- Server (über ein Netz) arbeiten.

%description -l fr libs
Ce paquetage contient les bibliothèques partagées nécessaires à de nombreux
programmes X. Elles se trouvent dans un paquetage séparé afin de réduire
l'espace disque nécessaire à l'exécution des applications X sur une machine
sans serveur X (en réseau).

%description -l pl libs
Pakiet zawieraj±cy podstawowe biblioteki dla programów kozystaj±cych z
systemu X Window. Wydzielony w celu oszczednosci miejsca, nie wp³ywa na
mo¿liwo¶ci pracy aplikacji X Window poprzez np. sieæ. Nie potrzebny dla
komputerów nie posiadaj±cych X serwerów.

%description -l tr libs
Bu paket X programlarýnýn düzgün çalýþabilmeleri için gereken kitaplýklarý
içerir. Bunlar, X programlarýný (sunucu olsun olmasýn) çalýþtýrmak için
gerekli disk alanýný azaltmak için ayrý bir paket olarak sunulmuþtur.

%package devel
Summary:	X11R6 headers and programming man pages
Summary(de):	X11R6 Headers und man pages für Programmierer
Summary(fr):	Pages man de programmation
Summary(pl):	Pliki nag³ówkowe dla X11R6
Summary(tr):	X11R6 ile geliþtirme için gerekli dosyalar
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name}-libs = %{version}
%ifarch sparc
Obsoletes:	X11R6.1-devel
%endif

%description devel
Libraries, header files, and documentation for developing programs that run
as X clients. It includes the base Xlib library as well as the Xt and Xaw
widget sets. For information on programming with these libraries, PLD
recommends the series of books on X Programming produced by O'Reilly and
Associates.

%description -l de devel
Libraries, Header-Dateien und Dokumentation zum Entwickeln von Programmen,
die als X-Clients laufen. Enthält die Xlib-Library und die Widget-Sätze Xt
und Xaw. Information zum Programmieren mit diesen Libraries finden Sie in
der Buchreihe zur X-Programmierung von O'Reilly and Associates.

%description -l fr devel
Bibliothéques, fichiers d'en-tête, et documentation pour développer des
programmes s'exécutant en clients X. Cela comprend la Bibliothéque Xlib de
base aussi bien que les ensembles de widgets Xt et Xaw. Pour des
informations sur la programmation avec ces Bibliothéques, Red Hat recommande
la série d'ouvrages sur la programmation X editée par O'Reilly and
Associates.

%description -l pl devel
Pliki nag³ówkowe, dokumentcja dla programistów rozwijaj±cych aplikacje
klienckie pod X'y. Zawiera podstatwow± bibliotekê Xlib a tak¿e Xt i Xaw.
Wiêcej informacji nt. pisania programów przy u¿yciu tych bibliotek mo¿esz
znale¼æ w ksi±¿kach wydawnictwa O'Reilly and Associates (X Programming)
polecanych przez Red Hat'a.

%description -l tr devel
X istemcisi olarak çalýþacak programlar geliþtirmek için gereken statik
kitaplýklar, baþlýk dosyalarý ve belgeler. Xlib kitaplýðýnýn yanýsýra Xt ve
Xaw arayüz kitaplýklarýný da içerir.

%package static
Summary:	X11R6 static libraries
Summary(pl):	Biblioteki sytatyczne do X11R6
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name}-devel = %{version}
%ifarch sparc
Obsoletes:	X11R6.1-devel
%endif
Obsoletes:	Mesa-static

%description static
X11R6 static libraries.

%description -l pl static
Biblioteki sytatyczne do X11R6.

%package XF86Setup
Summary:	Graphical configuration tool for XFree86
Summary(pl):	Graficzny konfigurator dla XFree86
Group:		X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-VGA16 = %{version}

%description XF86Setup
XF86Setup is a graphical configuration tool for the XFree86 family of
servers. It allows you to configure video settings, keyboard layouts, mouse
type, and other miscellaneous options. It is slow however, and requires the
generic VGA 16 color server be available.

%description -l pl XF86Setup
Graficzny konfigurator dla XFree86.

%package Xvfb
Summary:	XFree86 Xvfb server
Summary(pl):	Serwer XFree86 Xvfb
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description Xvfb
Xvfb (X Virtual Frame Buffer) is an X Windows System server that is capable
of running on machines with no display hardware and no physical input
devices. Xvfb emulates a dumb framebuffer using virtual memory. Xvfb doesn't
open any devices, but behaves otherwise as an X display. Xvfb is normally
used for testing servers. Using Xvfb, the mfb or cfb code for any depth can
be exercised without using real hardware that supports the desired depths.
Xvfb has also been used to test X clients against unusual depths and screen
configurations, to do batch processing with Xvfb as a background rendering
engine, to do load testing, to help with porting an X server to a new
platform, and to provide an unobtrusive way of running applications which
really don't need an X server but insist on having one.

If you need to test your X server or your X clients, you may want to install
Xvfb for that purpose.

%package Xnest
Summary:	XFree86 Xnest server
Summary(pl):	Serwer XFree86 Xnest
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description Xnest
Xnest is an X Window System server which runs in an X window. Xnest is a
'nested' window server, actually a client of the real X server, which
manages windows and graphics requests for Xnest, while Xnest manages the
windows and graphics requests for its own clients.

You will need to install Xnest if you require an X server which will run as
a client of your real X server (perhaps for testing purposes).

%package Xprt
Summary:	X print server
Summary(pl):	X print server
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description Xprt
Xprt provides an X server with the print extension and special DDX
implementation.

%package Xserver
Summary:	XFree86 X display server
Summary(de):	XFree86 Server
Summary(fr):	Serveur XFree86
Summary(pl):	XFree86 serwer
Summary(tr):	XFree86 sunucusu
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	pam
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}
Obsoletes:	%{name}-VGA16 %{name}-SVGA %{name}-Mono
Obsoletes:	%{name}-S3 %{name}-S3V %{name}-I128
Obsoletes:	%{name}-Mach8 %{name}-Mach32 %{name}-Mach64
Obsoletes:	%{name}-8514 %{name}-AGX %{name}-3DLabs
Obsoletes:	%{name}-P9000 %{name}-W32

%description Xserver
X server for most simple framebuffer SVGA devices, including cards built
from ET4000 chips, Cirrus Logic chips, Chips and Technologies laptop chips,
Trident 8900 and 9000 chips. It works for Diamond Speedstar, Orchid Kelvins,
STB Nitros and Horizons, Genoa 8500VL, most Actix boards, the Spider VLB
Plus. It also works for many other chips and cards, so try this server if
you are having problems.

%description -l de Xserver
X-Server für die elementarsten Framebuffer-SVGA-Geräte, einschließlich
Karten, die aus ET4000-Chips, Cirrus Logic-Chips, Chips and Technologies
Laptop-Chips sowie Trident 8900 und 9000 Chips gebaut sind. Funktioniert mit
Diamond Speedstar, Orchid Kelvins, STB Nitros und Horizons, Genoa 8500VL,
den meisten Actix-Karten sowie Spider VLB Plus und außerdem mit vielen
anderen Chips und Karten. Es lohnt sich, diesen Server auszuprobieren, wenn
Sie Probleme haben.

%description -l fr Xserver
Serveur X pour les circuits SVGA les plus simples, dont les cartes
construites avec les circuits ET4000, Cirrus Logic, Chips and Technologies
laptop, Trident 8900 et 9000. Fonctionne pour les cartes Diamond Speedstar,
Orchid Kelvins, STB Nitros et Horizons, Genoa 8500VL, la plupart des Actix
et la Spider VLB Plus. Fonctionne aussi pour de nombreux autres circuits et
cartes. Essayez ce serveur si vous avez des problèmes.

%description -l pl Xserver
X serwer dla wiêkszo¶ci prostych kart SVGA, w³±czaj±c karty zbudowane na
uk³adach ET4000, Cirrus Logic, Trident 8900 i 9000, oraz uk³ady wystêpuj±ce
w laptopach. Dzia³a tak¿e z kartami Diamnod Speedstar, Orchid Kelvins, STB
Nitros i Horizons, Genoa 8500VL, wiêkszo¶æ Actix, Spider VLB Plus. Dzia³a
równie¿ na wielu innych kartach opartych na innych uk³adach wiêc spróbuj tego
serwera je¶li masz jakie¶ problemy.

%description -l tr Xserver
ET4000, Cirrus Logic, Chips and Technologies dizüstü, Trident 8900 ve 9000
gibi basit 'framebuffer' SVGA kullananan kartlar için X sunucusu. Ayný
zamanda Diamond Speedstar, Orchid Kelvins, STB Nitros / Horizons, Genoa
8500VL, çoðu Actix kartlarý, Spider VLB Plus gibi kartlar ve birçok diðer
kart ile de çalýþýr. Herhangi bir sorun yaþarsanýz bu sunucuyu deneyin.

%package Sun
Summary:	XFree86 Sun server (monochrome and 8-bit color SBUS framebuffers)
Summary(pl):	Serwer XFree86 Sun (dla framebuffera)
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-fonts = %{version}
Obsoletes:	X11R6.1-Sun

%description Sun
To run X Windows programs requires an X server for your specific hardware.
This package includes the X server for Sun computers with monochrome and
8-bit color SBUS framebuffers.

%description -l pl Sun
Aby uruchomiæ X Window System potrzebujesz X serwera dostosowanego do
Twojego sprzêtu. Ten pakiet zawiera X serwer dla komputerów firmy Sun z
monochromatycznymi lub te¿ 8-bitowymi kolorowymi framebufferami SBUS.

%package SunMono
Summary:	XFree86 Sun server for monochrome SBUS framebuffers only
Summary(pl):	Serwer XFree86 Sun (tylko dla monitorów monochromatycznych)
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-fonts = %{version}
Obsoletes:	X11R6.1-SunMono

%description SunMono
To run X Windows programs requires an X server for your specific hardware.
This package includes the X server for Sun computers with monochrome
SBUS framebuffers only.

%description -l pl SunMono
Aby uruchomiæ X Window System potrzebujesz X serwera dostosowanego do
Twojego sprzêtu. Ten pakiet zawiera X serwer dla komputerów firmy Sun z
wy³±cznie monochromatycznymi framebufferami SBUS.

%package Sun24
Summary:	XFree86 Sun server for all supported SBUS framebuffers
Summary(pl):	Serwer XFree86 Sun (dla wszystkich SBUS framebufferów)
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-fonts = %{version}
Obsoletes:	X11R6.1-Sun24

%description Sun24
To run X Windows programs requires an X server for your specific hardware.
This package includes the X server for Sun computers with all supported
SBUS framebuffers.

%description -l pl Sun24
Aby uruchomiæ X Window System potrzebujesz X serwera dostosowanego do
Twojego sprzêtu. Ten pakiet zawiera X serwer dla komputerów firmy Sun dla
wszystkich wspieranych framebufferów SBUS.

%package TGA
Summary:	XFree86 TGA server
Summary(pl):	XFree86 serwer dla kart TGA
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}
Requires:	%{name}-fonts = %{version}

%description TGA
The XFree86-TGA package contains an 8-bit X server for Digital TGA boards
based on the DC21040 chip. These adapters are very popular in Alpha
workstations and are included with Alpha UDB (Multia) machines.

If you are installing the X Window System and your system uses a Digital TGA
board based on the DC21040 chip, you'll need to install the XFree86-TGA
package.

%package -n sessreg
Summary:	sessreg - manage utmp/wtmp entries for non-init clients
Group:		X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-libs = %{version}

%description -n sessreg
Sessreg is a simple program for managing utmp/wtmp entries for xdm sessions.

System V has a better interface to /var/run/utmp than BSD; it dynamically
allocates entries in the file, instead of writing them at fixed positions
indexed by position in /etc/ttys.

%package -n xdm
Summary:	xdm - X Display Manager with support for XDMCP, host chooser
Summary(pl):	XDM
Group:		X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name} = %{version}
Requires:	pam >= 0.71
Requires:	%{name}-libs = %{version}
Requires:	sessreg = %{version}
Requires:	/usr/X11R6/bin/sessreg
Provides:	XDM
Prereq:		chkconfig
Obsoletes:	XFree86-xdm
Obsoletes:	gdm
Obsoletes:	kdm

%description -n xdm
Xdm manages a collection of X displays, which may be on the local host or
remote servers. The design of xdm was guided by the needs of X terminals as
well as the X Consortium standard XDMCP, the X Display Manager Control
Protocol.

%package -n twm
Summary:	Tab Window Manager for the X Window System
Summary(pl):	Twm - podstawowy zarz±dca okien dla X Window System
Group:		X11/Window Managers/Tools
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien/Narzêdzi

%description -n twm
Twm is a window manager for the X Window System. It provides titlebars,
shaped windows, several forms of icon management, user-defined macro
functions, click-to-type and pointerdriven keyboard focus, and
user-specified key and pointer button bindings.

%package -n xfs
Summary:	Font server for XFree86
Summary(pl):	Serwer fontów do XFree86
Group:		X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-libs = %{version}
Prereq:		chkconfig
Obsoletes:	xfsft XFree86-xfs

%description -n xfs
This is a font server for XFree86. You can serve fonts to other X servers
remotely with this package, and the remote system will be able to use all
fonts installed on the font server, even if they are not installed on the
remote computer.

%package -n xauth
Summary:	xauth - X authority file utility
Group:		X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-libs = %{version}

%description -n xauth
The xauth program is used to edit and display the authorization information
used in connecting to the X server. This program is usually used to extract
authorization records from one machine and merge them in on another (as is
the case when using remote logins or granting access to other users).

#--- %prep ---------------------------

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0
rm -f xc/config/cf/host.def

#--- %build --------------------------

%build
make -C xc World \
	"BOOTSTRAPCFLAGS=$RPM_OPT_FLAGS -fno-strict-aliasing" \
	"CDEBUGFLAGS=" "CCOPTIONS=$RPM_OPT_FLAGS -fno-strict-aliasing" \
	"CXXDEBUGFLAGS=" "CXXOPTIONS=$RPM_OPT_FLAGS -fno-strict-aliasing" \
	"RAWCPP=/lib/cpp"

#--- %install ------------------------

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/X11/pl/app-defaults \
	$RPM_BUILD_ROOT/etc/{sysconfig,X11,pam.d,rc.d/init.d,security/console.apps} \
	$RPM_BUILD_ROOT/var/state/xkb \
	$RPM_BUILD_ROOT/usr/include \
	$RPM_BUILD_ROOT/usr/bin \
	$RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties \
	$RPM_BUILD_ROOT{%{_appnkldir}/Utilities,%{_datadir}/pixmaps} \
	$RPM_BUILD_ROOT/%{_docdir}/%{name}-doc-%{version}

make -C xc	"DESTDIR=$RPM_BUILD_ROOT" \
		"DOCDIR=/usr/share/doc/%{name}-%{version}" \
		"INSTBINFLAGS=-m 755" \
		"INSTPGMFLAGS=-m 755" \
		"RAWCPP=/lib/cpp" \
		install install.man

strip $RPM_BUILD_ROOT%{_bindir}/* || :
strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/{lib*.so.*.*,modules/*.so} || :

# DO NOT STRIP ANYTHING ELSE IN %{_libdir}/modules/ !!!

# Move config stuff to /etc/X11

cp $RPM_BUILD_ROOT%{_libdir}/X11/XF86Config.eg \
	$RPM_BUILD_ROOT/etc/X11/XF86Config
ln -sf ../../../../etc/X11/XF86Config $RPM_BUILD_ROOT%{_libdir}/X11/XF86Config

# setting default X
rm -f $RPM_BUILD_ROOT%{_bindir}/X
ln -sf XFree86 $RPM_BUILD_ROOT%{_bindir}/X

# setting ghost X in /etc/X11 -- xf86config will fix this ...
ln -s ../..%{_bindir}/XFree86 $RPM_BUILD_ROOT/etc/X11/X

# add X11 links in /usr/bin and /usr/include
ln -s ../X11R6/include/X11 $RPM_BUILD_ROOT/usr/include/X11
ln -s ../X11R6/bin $RPM_BUILD_ROOT/usr/bin/X11

install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/xdm
install %{SOURCE7} $RPM_BUILD_ROOT/etc/pam.d/xserver
install %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/xdm
install %{SOURCE5} $RPM_BUILD_ROOT/etc/rc.d/init.d/xfs
install %{SOURCE6} $RPM_BUILD_ROOT/etc/X11/fs/config
install %{SOURCE8} $RPM_BUILD_ROOT%{_libdir}/X11/pl/app-defaults/XTerm

install %{SOURCE9} $RPM_BUILD_ROOT/etc/sysconfig/xdm
install %{SOURCE10} $RPM_BUILD_ROOT/etc/sysconfig/xfs

install %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties/twm.desktop
install %{SOURCE12} $RPM_BUILD_ROOT%{_appnkldir}/Utilities
install %{SOURCE13} $RPM_BUILD_ROOT%{_appnkldir}/Utilities
install %{SOURCE14} $RPM_BUILD_ROOT%{_appnkldir}

install %{SOURCE15} $RPM_BUILD_ROOT%{_datadir}/pixmaps

touch $RPM_BUILD_ROOT/etc/security/console.apps/xserver
touch $RPM_BUILD_ROOT/etc/security/blacklist.xserver
touch $RPM_BUILD_ROOT/etc/security/blacklist.xdm

#ln -sf ../..%{_includedir}/X11 $RPM_BUILD_ROOT%{_includedir}/X11 ##change
ln -sf %{_fontdir} $RPM_BUILD_ROOT%{_libdir}/X11/fonts

# we have libXpm from xpm package
rm -f $RPM_BUILD_ROOT/%{_libdir}/libXpm*

# do not duplicate xkbcomp program
rm -f $RPM_BUILD_ROOT%{_libdir}/X11/xkb/xkbcomp
ln -sf ../../../bin/xkbcomp $RPM_BUILD_ROOT%{_libdir}/X11/xkb/xkbcomp

ln -sf ../../../share/doc/%{name}-%{version} \
	$RPM_BUILD_ROOT%{_libdir}/X11/doc

rm -f $RPM_BUILD_ROOT%{_libdir}/X11/config/host.def
:> $RPM_BUILD_ROOT%{_libdir}/X11/config/host.def

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13457]/* \
	$RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/*

# don't gzip README.* files, they are needed by XF86Setup
gzip -dnf $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/README.*

#--- %post{un}, %preun, %verifyscript -

%post libs
grep "^%{_libdir}$" /etc/ld.so.conf >/dev/null 2>&1
[ $? -ne 0 ] && echo "%{_libdir}" >> /etc/ld.so.conf
/sbin/ldconfig

%postun libs
if [ "$1" = "0" ]; then
	grep -v "%{_libdir}" /etc/ld.so.conf > /etc/ld.so.conf.new
	mv -f /etc/ld.so.conf.new /etc/ld.so.conf
fi
/sbin/ldconfig

%verifyscript libs
echo -n "Looking for %{_libdir} in /etc/ld.so.conf... "
if ! grep "^%{_libdir}$" /etc/ld.so.conf > /dev/null; then
	echo "missing"
	echo "%{_libdir} missing from /etc/ld.so.conf" >&2
else
	echo "found"
fi

%post -n xfs
/sbin/chkconfig --add xfs
if [ -f /var/lock/subsys/xfs ]; then
	/etc/rc.d/init.d/xfs restart >&2
else
	echo "Run \"/etc/rc.d/init.d/xfs start\" to start font server." >&2
fi

%post -n xdm
/sbin/chkconfig --add xdm
if [ -f /var/lock/subsys/xdm ]; then
	/etc/rc.d/init.d/xdm restart >&2
else
	echo "Run \"/etc/rc.d/init.d/xdm start\" to start xdm." >&2
fi
		
%preun -n xfs
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/xfs ]; then
		/etc/rc.d/init.d/xfs stop >&2
	fi
	/sbin/chkconfig --del xfs
fi

%preun -n xdm
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/xdm ]; then
		/etc/rc.d/init.d/xdm stop >&2
	fi
	/sbin/chkconfig --del xdm
fi

%clean
rm -rf $RPM_BUILD_ROOT

#--- %files --------------------------

%files
%defattr(644,root,root,755)
%docdir %{_docdir}/%{name}-%{version}
%doc /%{_docdir}/%{name}-%{version}/*
%doc %{_libdir}/X11/doc

%dir /usr/X11R6
%dir %{_libdir}
%dir %{_libdir}/X11
%dir %{_libdir}/X11/rstart
%dir %{_libdir}/X11/rstart/commands
%dir %{_libdir}/X11/rstart/commands/x11r6
%dir %{_libdir}/X11/rstart/contexts
%dir %{_libdir}/X11/etc
%dir %{_libdir}/X11/fonts
%dir %{_bindir}


%{_libdir}/X11/XErrorDB
%{_libdir}/X11/XKeysymDB
%{_libdir}/X11/locale
%{_libdir}/X11/lbxproxy
%{_libdir}/X11/proxymngr
%{_libdir}/X11/app-defaults

%lang(pl) %{_libdir}/X11/pl

%attr(755,root,root) %{_libdir}/X11/xinit

%attr(755,root,root) %{_libdir}/X11/xsm

%{_libdir}/X11/xserver/SecurityPolicy

%attr(-,root,root) %{_libdir}/X11/rstart/config
%attr(-,root,root) %{_libdir}/X11/rstart/rstartd.real
%attr(-,root,root) %{_libdir}/X11/rstart/commands/x
%attr(-,root,root) %{_libdir}/X11/rstart/commands/x11
%attr(-,root,root) %{_libdir}/X11/rstart/commands/*List*
%attr(-,root,root) %{_libdir}/X11/rstart/commands/x11r6/*
%attr(-,root,root) %{_libdir}/X11/rstart/contexts/*

%attr(755,root,root) %{_libdir}/X11/x11perfcomp/*
%{_libdir}/X11/*.txt

%attr(755,root,root) %{_libdir}/X11/etc/*.sh
%{_libdir}/X11/etc/*.term*
%{_libdir}/X11/etc/xmodmap.std

%attr(755,root,root) %{_bindir}/lbxproxy

%attr(755,root,root) %{_bindir}/proxymngr
%attr(755,root,root) %{_bindir}/rstartd
%attr(755,root,root) %{_bindir}/xfindproxy
%attr(755,root,root) %{_bindir}/xfwp
%attr(755,root,root) %{_bindir}/lndir
%attr(755,root,root) %{_bindir}/mkdirhier
%attr(755,root,root) %{_bindir}/gccmakedep
%attr(755,root,root) %{_bindir}/mergelib
%attr(755,root,root) %{_bindir}/makeg
%attr(755,root,root) %{_bindir}/appres
%attr(755,root,root) %{_bindir}/bdftopcf
%attr(755,root,root) %{_bindir}/beforelight
%attr(755,root,root) %{_bindir}/bitmap
%attr(755,root,root) %{_bindir}/bmtoa
%attr(755,root,root) %{_bindir}/atobm
%attr(755,root,root) %{_bindir}/editres
%attr(755,root,root) %{_bindir}/iceauth
%attr(755,root,root) %{_bindir}/mkfontdir
%attr(755,root,root) %{_bindir}/showrgb
%attr(755,root,root) %{_bindir}/rstart
%attr(755,root,root) %{_bindir}/smproxy
%attr(755,root,root) %{_bindir}/x11perf
%attr(755,root,root) %{_bindir}/x11perfcomp
%attr(755,root,root) %{_bindir}/Xmark
%attr(755,root,root) %{_bindir}/xclipboard
%attr(755,root,root) %{_bindir}/xcutsel
%attr(755,root,root) %{_bindir}/xclock
%attr(755,root,root) %{_bindir}/xcmsdb
%attr(755,root,root) %{_bindir}/xconsole
%attr(755,root,root) %{_bindir}/xdpyinfo
%attr(755,root,root) %{_bindir}/dga
%attr(755,root,root) %{_bindir}/xfd
%attr(755,root,root) %{_bindir}/xhost
%attr(755,root,root) %{_bindir}/xieperf
%attr(755,root,root) %{_bindir}/xinit

%attr(755,root,root) %{_bindir}/startx

%attr(755,root,root) %{_bindir}/setxkbmap
%attr(755,root,root) %{_bindir}/xkbcomp
%attr(755,root,root) %{_bindir}/xkbevd
%attr(755,root,root) %{_bindir}/xkbprint
%attr(755,root,root) %{_bindir}/xkbvleds
%attr(755,root,root) %{_bindir}/xkbwatch
%attr(755,root,root) %{_bindir}/xkbbell
%attr(755,root,root) %{_bindir}/xkill
%attr(755,root,root) %{_bindir}/xlogo
%attr(755,root,root) %{_bindir}/xlsatoms
%attr(755,root,root) %{_bindir}/xlsclients
%attr(755,root,root) %{_bindir}/xlsfonts
%attr(755,root,root) %{_bindir}/xmag
%attr(755,root,root) %{_bindir}/xmodmap
%attr(755,root,root) %{_bindir}/xprop
%attr(755,root,root) %{_bindir}/xrdb
%attr(755,root,root) %{_bindir}/xset
%attr(755,root,root) %{_bindir}/xrefresh
%attr(755,root,root) %{_bindir}/xsetmode
%attr(755,root,root) %{_bindir}/xsetpointer
%attr(755,root,root) %{_bindir}/xsetroot
%attr(755,root,root) %{_bindir}/xsm
%attr(755,root,root) %{_bindir}/xstdcmap
%attr(755,root,root) %{_bindir}/xterm
%attr(755,root,root) %{_bindir}/resize
%attr(755,root,root) %{_bindir}/xvidtune
%attr(755,root,root) %{_bindir}/xwd
%attr(755,root,root) %{_bindir}/xwininfo
%attr(755,root,root) %{_bindir}/xwud
%attr(755,root,root) %{_bindir}/xf86config
%attr(755,root,root) %{_bindir}/scanpci
%attr(755,root,root) %{_bindir}/SuperProbe
%attr(755,root,root) %{_bindir}/xon
%attr(755,root,root) %{_bindir}/makestrs
%attr(755,root,root) %{_bindir}/oclock
%attr(755,root,root) %{_bindir}/pcitweak
%attr(755,root,root) %{_bindir}/revpath
%attr(755,root,root) %{_bindir}/xedit
%attr(755,root,root) %{_bindir}/xgamma

%{_includedir}/X11/bitmaps

%{_appnkldir}/Utilities/*.desktop
%{_appnkldir}/*.desktop
%{_datadir}/pixmaps/*

%{_mandir}/man1/lbxproxy.1*
%{_mandir}/man1/proxymngr.1*
%{_mandir}/man1/xfindproxy.1*
%{_mandir}/man1/xfwp.1*
%{_mandir}/man1/lndir.1*
%{_mandir}/man1/makestrs.1*
%{_mandir}/man1/makeg.1*
%{_mandir}/man1/mkdirhier.1*
%{_mandir}/man1/appres.1*
%{_mandir}/man1/bdftopcf.1*
%{_mandir}/man1/beforelight.1*
%{_mandir}/man1/bitmap.1*
%{_mandir}/man1/bmtoa.1*
%{_mandir}/man1/atobm.1*
%{_mandir}/man1/editres.1*
%{_mandir}/man1/iceauth.1*
%{_mandir}/man1/mkfontdir.1*
%{_mandir}/man1/showrgb.1*
%{_mandir}/man1/rstart.1*
%{_mandir}/man1/rstartd.1*
%{_mandir}/man1/smproxy.1*
%{_mandir}/man1/x11perf.1*
%{_mandir}/man1/x11perfcomp.1*
%{_mandir}/man1/xclipboard.1*
%{_mandir}/man1/xcutsel.1*
%{_mandir}/man1/xclock.1*
%{_mandir}/man1/xcmsdb.1*
%{_mandir}/man1/xconsole.1*
%{_mandir}/man1/xdpyinfo.1*
%{_mandir}/man1/dga.1*
%{_mandir}/man1/xfd.1*
%{_mandir}/man1/xhost.1*
%{_mandir}/man1/xieperf.1*
%{_mandir}/man1/xinit.1*
%{_mandir}/man1/startx.1*
%{_mandir}/man1/setxkbmap.1*
%{_mandir}/man1/xkbcomp.1*
%{_mandir}/man1/xkbevd.1*
%{_mandir}/man1/xkbprint.1*
%{_mandir}/man1/xkill.1*
%{_mandir}/man1/xlogo.1*
%{_mandir}/man1/xlsatoms.1*
%{_mandir}/man1/xlsclients.1*
%{_mandir}/man1/xlsfonts.1*
%{_mandir}/man1/xmag.1*
%{_mandir}/man1/xmodmap.1*
%{_mandir}/man1/xprop.1*
%{_mandir}/man1/xrdb.1*
%{_mandir}/man1/xrefresh.1*
%{_mandir}/man1/xset.1*
%{_mandir}/man1/xsetmode.1*
%{_mandir}/man1/xsetpointer.1*
%{_mandir}/man1/xsetroot.1*
%{_mandir}/man1/xsm.1*
%{_mandir}/man1/xstdcmap.1*
%{_mandir}/man1/xterm.1*
%{_mandir}/man1/resize.1*
%{_mandir}/man1/xvidtune.1*
%{_mandir}/man1/xwd.1*
%{_mandir}/man1/xwininfo.1*
%{_mandir}/man1/xwud.1*
%{_mandir}/man1/xf86config.1*
%{_mandir}/man1/SuperProbe.1*
%{_mandir}/man1/xon.1*
%{_mandir}/man1/libxrx.1*
%{_mandir}/man1/oclock.1*
%{_mandir}/man1/revpath.1*
%{_mandir}/man1/xedit.1*
%{_mandir}/man1/xgamma.1*
%{_mandir}/man7/*

/usr/bin/X11

%ifnarch sparc

%files modules
%defattr(-,root,root,755)
%{_libdir}/X11/xkb
/var/state/xkb
%dir %{_libdir}/modules
%attr(755,root,root) %{_libdir}/modules/*
%{_mandir}/man4/*

%endif

%files -n sessreg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sessreg
%{_mandir}/man1/sessreg.1*

%files -n xdm
%defattr(644,root,root,755)
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/xdm
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/security/blacklist.xdm
%attr(754,root,root) /etc/rc.d/init.d/xdm
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/xdm
/var/state/xdm

%config %{_libdir}/X11/app-defaults/Chooser

%attr(755,root,root) %{_libdir}/X11/xdm
%attr(755,root,root) %{_bindir}/xdm
%{_mandir}/man1/xdm.1*

%dir    /etc/X11/xdm
%config /etc/X11/xdm/xdm-config
%config /etc/X11/xdm/chooser
%config /etc/X11/xdm/Xsetup_0
%config /etc/X11/xdm/Xsession
%config /etc/X11/xdm/Xservers
%config /etc/X11/xdm/Xresources
%config /etc/X11/xdm/Xaccess
%config /etc/X11/xdm/TakeConsole
%config /etc/X11/xdm/GiveConsole

%files -n twm
%defattr(644,root,root,755)
%{_datadir}/gnome/wm-properties/twm.desktop
%attr(755,root,root) %{_bindir}/twm
%config /etc/X11/twm/system.twmrc
%attr(755,root,root) %{_libdir}/X11/twm
%{_mandir}/man1/twm.1*

%files -n xfs
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/xfs
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/xfs
%dir /etc/X11/fs
%attr(755,root,root) %{_libdir}/X11/fs
%config(noreplace) /etc/X11/fs/config

%attr(755,root,root) %{_bindir}/xfs
%attr(755,root,root) %{_bindir}/fsinfo
%attr(755,root,root) %{_bindir}/fslsfonts
%attr(755,root,root) %{_bindir}/fstobdf
%attr(755,root,root) %{_bindir}/mkcfm

%{_mandir}/man1/xfs.1*
%{_mandir}/man1/fsinfo.1*
%{_mandir}/man1/fslsfonts.1*
%{_mandir}/man1/fstobdf.1*
%{_mandir}/man1/mkcfm.1*

%files -n xauth
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xauth
%{_mandir}/man1/xauth.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/libFS.a
%{_libdir}/libXau.a
%{_libdir}/libXdmcp.a
%{_libdir}/libXss.a
%{_libdir}/libXxf86dga.a
%{_libdir}/libXxf86misc.a
%{_libdir}/libXxf86rush.a
%{_libdir}/libXxf86vm.a
%{_libdir}/liboldX.a
%{_libdir}/libxkbfile.a
%{_libdir}/libxkbui.a
%{_libdir}/libXv.a
%{_libdir}/libfntstubs.a
%{_libdir}/libxf86config.a

%{_includedir}/X11/*.h
%{_includedir}/X11/ICE
%{_includedir}/X11/PEX5
%{_includedir}/X11/PM
%{_includedir}/X11/SM
%{_includedir}/X11/Xaw
%{_includedir}/X11/Xmu
%{_includedir}/X11/extensions
%{_includedir}/X11/fonts
%{_includedir}/GL
%{_includedir}/xf86*.h
%{_libdir}/X11/config

%attr(755,root,root) %{_bindir}/imake
%attr(755,root,root) %{_bindir}/makedepend
%attr(755,root,root) %{_bindir}/xmkmf

%{_mandir}/man1/imake.1*
%{_mandir}/man1/makedepend.1*
%{_mandir}/man1/xmkmf.1*
%{_mandir}/man3/*

/usr/include/X11

%files static
%defattr(644,root,root,755)
%{_libdir}/libGL.a
%{_libdir}/libGLU.a
%{_libdir}/libICE.a
%{_libdir}/libPEX5.a
%{_libdir}/libSM.a
%{_libdir}/libX11.a
%{_libdir}/libXIE.a
%{_libdir}/libXaw.a
%{_libdir}/libXext.a
%{_libdir}/libXfont.a
%{_libdir}/libXi.a
%{_libdir}/libXmu.a
%{_libdir}/libXp.a
%{_libdir}/libXt.a
%{_libdir}/libXtst.a

%files Xvfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xvfb
%{_mandir}/man1/Xvfb.1*

%files Xnest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xnest
%{_mandir}/man1/Xnest.1*

%files Xprt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xprt

%files Xserver
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/Xwrapper
%attr(755,root,root) %{_bindir}/XFree86
%attr(755,root,root) /etc/X11/X
%attr(755,root,root) %{_bindir}/X
%{_mandir}/man1/XFree86.1*
%{_mandir}/man1/Xserver.1*
%{_mandir}/man5/XF86Config.5*

%dir %{_libdir}/X11/xserver
%doc %{_libdir}/X11/XF86Config.eg
%doc %{_libdir}/X11/XF86Config.98
%doc %{_libdir}/X11/Cards

%ifarch ix86 alpha sparc
%{_libdir}/X11/Cards
%endif

%config(noreplace) %verify(not md5 mtime size) /etc/X11/XF86Config
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/xserver
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.xserver
%config(missingok) /etc/security/console.apps/xserver

%ifarch alpha

%files TGA
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_TGA
%{_mandir}/man5/XF86Config.5*
%endif

%ifarch sparc

%files Sun
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xsun
%dir %{_libdir}/X11/xkb
%attr(755,root,root) %{_libdir}/X11/xkb/*
/var/state/xkb
%endif

%ifarch sparc

%files SunMono
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XsunMono
%dir %{_libdir}/X11/xkb
%attr(755,root,root) %{_libdir}/X11/xkb/*
/var/state/xkb
%endif

%ifarch sparc

%files Sun24
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xsun24
%dir %{_libdir}/X11/xkb
%attr(755,root,root) %{_libdir}/X11/xkb/*
/var/state/xkb
%endif

#%files XF86Setup
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/XF86Setup
#%attr(755,root,root) %{_bindir}/xmseconfig
#%{_libdir}/X11/XF86Setup
#%{_mandir}/man1/XF86Setup.1*
#%{_mandir}/man1/xmseconfig.1*
