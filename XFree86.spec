Summary:	XFree86 Window System servers and basic programs
Summary(de):	Xfree86 Window-System-Server und grundlegende Programme
Summary(fr):	Serveurs du système XFree86 et programmes de base
Summary(pl):	XFree86 Window System wraz z podstawowymi programami
Summary(tr):	XFree86 Pencereleme Sistemi sunucularý ve temel programlar
Name:		XFree86
Version:	4.0.2
Release:	5
License:	MIT
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Source0:	ftp://ftp.xfree86.org/pub/XFree86/4.0/source/X402src-1.tgz
Source1:	ftp://download.sourceforge.net/pub/sourceforge/mesa3d/MesaLib-3.4.tar.bz2
Source2:	ftp://ftp.pld.org.pl/software/xinit/xdm-xinitrc-0.2.tar.bz2
Source3:	xdm.pamd
Source4:	xdm.init
Source5:	xfs.init
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
Patch0:		%{name}-PLD.patch
Patch1:		%{name}-HasZlib.patch
Patch2:		%{name}-DisableDebug.patch
Patch3:		%{name}-Xwrapper.patch
Patch4:		%{name}-xfs.patch
Patch5:		%{name}-xfs-fix.patch
Patch6:		%{name}-xfs-logger.patch
Patch7:		%{name}-xterm-utempter.patch
Patch8:		%{name}-app_defaults_dir.patch
Patch9:		%{name}-startx_xauth.patch
Patch10:	%{name}-v4l.patch
Patch11:	%{name}-broken-includes.patch
Patch12:	%{name}-alpha-pcibus-lemming.patch
Patch13:	%{name}-fhs.patch
Patch14:	%{name}-xdmsecurity.patch
Patch15:	%{name}-xman.patch
Patch16:	%{name}-HasXdmAuth.patch
Patch17:	%{name}-xdm-fixes.patch
Patch18:	%{name}-imake-kernel-version.patch
Patch19:	%{name}-no-kernel-modules.patch
Patch20:	%{name}-cirrus.patch
Patch21:	%{name}-locale.alias.patch
Patch22:	%{name}-parallelmake.patch
Patch23:	%{name}-portuguese.patch
Patch24:	%{name}-XF86CardDrivers-cfg.patch
Patch25:	%{name}-pic.patch
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
BuildRequires:	utempter-devel
BuildRequires:	tcl-devel
BuildRequires:	pam-devel
%ifarch %{ix86}
BuildRequires:	Glide2x_SDK
BuildRequires:	Glide_V3-DRI-devel >= 3.10-7
%endif
Requires:	xauth
Prereq:		Xfree86-libs
Obsoletes:	xpm-progs
Exclusivearch:	%{ix86} alpha sparc m68k armv4l noarch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch sparc sparc64
Obsoletes:	X11R6.1
%endif

%define		_fontdir	/usr/share/fonts
%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man
%define		_appnkldir	%{_datadir}/applnk

%description
If you want to install the X Window System (TM) on your machine,
you'll need to install XFree86.

The X Window System provides the base technology for developing
graphical user interfaces. Simply stated, X draws the elements of the
GUI on the user's screen and builds methods for sending user
interactions back to the application. X also supports remote
application deployment--running an application on another computer
while viewing the input/output on your machine. X is a powerful
environment which supports many different applications, such as games,
programming tools, graphics programs, text editors, etc. XFree86 is
the version of X which runs on Linux, as well as other platforms.

This package contains the basic fonts, programs and documentation for
an X workstation. However, this package doesn't provide the program
which you will need to drive your video hardware. To control your
video card, you'll need the particular X server package which
corresponds to your computer's video card.

%description -l de
X-Windows ist eine voll funktionsfähige grafische Benutzeroberfläche
mit mehreren Fenstern, mehreren Clients und verschiedenen Arten von
Fenstern. Es kommt auf den meisten Unix-Plattformen zum Einsatz. Die
Clients lassen sich auch mit Hilfe anderer Fenstersysteme anzeigen.
Das X-Protokoll gestattet die Ausführung der Applikationen direkt auf
lokalen Rechnern oder über ein Netz und bietet große Flexibilität bei
Client-Server-Implementierungen.

%description -l pl
X Window System jest graficznym interfejsem u¿ytkownika, cechuje siê
mo¿liwo¶ci± pracy w wielu oknach, z wieloma klientami i do tego w
ró¿nych wystrojach okien. :) Jest u¿ywany na wiêkszo¶ci platform
sytemów Unix, a klienci mog± byæ uruchamiani tak¿e pod innymi
popularnymi systemami okienkowymi. Protokó³ X pozwala na uruchamianie
aplikacji zarówno z lokalnej maszyny jak i poprzez sieæ - daj±c przez
to elastyczn± implementacjê architektury klient/serwer.

Pakiet ten nie zawiera X serwera który jest po¶rednikiem z Twoj± kart±
graficzn± (jest on w innym pakiecie).

%description -l tr
X Window sistemi, çoklu pencere, çoklu istemci ve çeþitli pencere
stilleriyle geniþ özelliklere sahip bir Grafik Kullanýcý Arabirimidir.
Çoðu UNIX sisteminde çalýþtýðý gibi istemcileri de birçok pencereleme
sistemiyle çalýþabilir. X protokolu kullanan uygulamalarýn yerel
makina veya bilgisayar aðý üzerinden çalýþtýrýlabilmesi esnek bir
istemci/sunucu ortamý saðlar. Bu paket bir X istasyonu için gerekli
olan temel yazýtiplerini, programlarý ve belgeleri sunar. Ekran
kartýnýzý sürmek için gerekli olan X sunucusu bu pakete dahil
deðildir.

%package modules
Summary:	Modules with X servers extensions
Summary(pl):	Wspólne modu³y rozszerzeñ dla wszystkich X serwerów
Group:		X11/XFree86
Group(de):	X11/XFree86
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
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Prereq:		grep
Prereq:		/sbin/ldconfig
Obsoletes:	xpm
Provides:	xpm

%ifarch sparc sparc64
Obsoletes:	X11R6.1-libs
%endif

%description libs
XFree86-libs contains the shared libraries that most X programs need
to run properly. These shared libraries are in a separate package in
order to reduce the disk space needed to run X applications on a
machine without an X server (i.e, over a network).

%description -l de libs
Dieses Paket enthält die zur gemeinsamen Nutzung vorgesehenen
Libraries, die die meisten X-Programme für den einwandfreien Betrieb
benötigen. Sie wurden in einem separaten Paket untergebracht, um den
Festplattenspeicherplatz auf Computern zu reduzieren, die ohne einen
X- Server (über ein Netz) arbeiten.

%description -l fr libs
Ce paquetage contient les bibliothèques partagées nécessaires à de
nombreux programmes X. Elles se trouvent dans un paquetage séparé afin
de réduire l'espace disque nécessaire à l'exécution des applications X
sur une machine sans serveur X (en réseau).

%description -l pl libs
Pakiet zawieraj±cy podstawowe biblioteki dla programów kozystaj±cych z
systemu X Window. Wydzielony w celu oszczednosci miejsca, nie wp³ywa
na mo¿liwo¶ci pracy aplikacji X Window poprzez np. sieæ. Nie potrzebny
dla komputerów nie posiadaj±cych X serwerów.

%description -l tr libs
Bu paket X programlarýnýn düzgün çalýþabilmeleri için gereken
kitaplýklarý içerir. Bunlar, X programlarýný (sunucu olsun olmasýn)
çalýþtýrmak için gerekli disk alanýný azaltmak için ayrý bir paket
olarak sunulmuþtur.

%package devel
Summary:	X11R6 headers and programming man pages
Summary(de):	X11R6 Headers und man pages für Programmierer
Summary(fr):	Pages man de programmation
Summary(pl):	Pliki nag³ówkowe dla X11R6
Summary(tr):	X11R6 ile geliþtirme için gerekli dosyalar
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name}-libs = %{version}
Obsoletes:	xpm-devel
%ifarch sparc sparc64
Obsoletes:	X11R6.1-devel
%endif

%description devel
Libraries, header files, and documentation for developing programs
that run as X clients. It includes the base Xlib library as well as
the Xt and Xaw widget sets. For information on programming with these
libraries, PLD recommends the series of books on X Programming
produced by O'Reilly and Associates.

%description -l de devel
Libraries, Header-Dateien und Dokumentation zum Entwickeln von
Programmen, die als X-Clients laufen. Enthält die Xlib-Library und die
Widget-Sätze Xt und Xaw. Information zum Programmieren mit diesen
Libraries finden Sie in der Buchreihe zur X-Programmierung von
O'Reilly and Associates.

%description -l fr devel
Bibliothéques, fichiers d'en-tête, et documentation pour développer
des programmes s'exécutant en clients X. Cela comprend la Bibliothéque
Xlib de base aussi bien que les ensembles de widgets Xt et Xaw. Pour
des informations sur la programmation avec ces Bibliothéques, Red Hat
recommande la série d'ouvrages sur la programmation X editée par
O'Reilly and Associates.

%description -l pl devel
Pliki nag³ówkowe, dokumentcja dla programistów rozwijaj±cych aplikacje
klienckie pod X'y. Zawiera podstatwow± bibliotekê Xlib a tak¿e Xt i
Xaw. Wiêcej informacji nt. pisania programów przy u¿yciu tych
bibliotek mo¿esz znale¼æ w ksi±¿kach wydawnictwa O'Reilly and
Associates (X Programming) polecanych przez Red Hat'a.

%description -l tr devel
X istemcisi olarak çalýþacak programlar geliþtirmek için gereken
statik kitaplýklar, baþlýk dosyalarý ve belgeler. Xlib kitaplýðýnýn
yanýsýra Xt ve Xaw arayüz kitaplýklarýný da içerir.

%package static
Summary:	X11R6 static libraries
Summary(pl):	Biblioteki sytatyczne do X11R6
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name}-devel = %{version}
%ifarch sparc sparc64
Obsoletes:	X11R6.1-devel
%endif
Obsoletes:	xpm-static
#Obsoletes:	Mesa-static

%description static
X11R6 static libraries.

%description -l pl static
Biblioteki sytatyczne do X11R6.

%package OpenGL-core
Summary:	OpenGL support for X11R6
Summary(pl):	Wsparciem OpenGL dla systemu X11R6
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name}-libs = %{version}
Obsoletes:	Mesa

%description OpenGL-core
OpenGL support for X11R6 system.

%description -l pl OpenGL-core
Wsparcie OpenGL dla systemu X11R6

%package OpenGL-libs
Summary:	OpenGL libraries for X11R6
Summary(pl):	Biblioteki OpenGL dla systemu X11R6
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name}-libs = %{version}
Requires:	%{name}-OpenGL-core
Provides:	OpenGL
Obsoletes:	%{name}-OpenGL
Obsoletes:	Mesa

%description OpenGL-libs
OpenGL libraries for X11R6 system.

%description -l pl OpenGL-libs
Biblioteki OpenGL dla systemu X11R6

%package OpenGL-devel
Summary:	OpenGL for X11R6 development
Summary(pl):	Pliki nag³ówkowe dla OpenGL dla systemu X11R6
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name}-OpenGL-libs = %{version}
Provides:	OpenGL-devel
Obsoletes:	Mesa-devel glxMesa-devel

%description OpenGL-devel
Headert and man pages for OpenGL for X11R6.

%description -l pl OpenGL-devel
Pliki nag³ówkowe dla OpenGL dla systemu X11R6.

%package OpenGL-static
Summary:	X11R6 static libraries with OpenGL
Summary(pl):	Biblioteki sytatyczne do X11R6 ze wsparciem dla OpenGL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name}-OpenGL-devel = %{version}
Provides:	OpenGL-static
Obsoletes:	Mesa-static

%description OpenGL-static
X11R6 static libraries with OpenGL.

%description -l pl OpenGL-static
Biblioteki sytatyczne zawieraj±ce wsparcie dla OpenGL do X11R6.

%package setup
Summary:	Graphical configuration tool for XFree86
Summary(pl):	Graficzny konfigurator dla XFree86
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-Xserver = %{version}
Obsoletes:	XFree86-xf86cfg

%description setup
Setup containst a configuration tool for the XFree86 family of
servers. It allows you to configure video settings, keyboard layouts,
mouse type, and other miscellaneous options. It is slow however, and
requires the generic VGA 16 color server be available.

%description -l pl setup
Pakiet setup zawiera narzêdzia do konfiguracji Xfree86.

%package Xvfb
Summary:	XFree86 Xvfb server
Summary(pl):	Serwer XFree86 Xvfb
Group:		X11/XFree86/Servers
Group(de):	X11/XFree86/Server
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description Xvfb
Xvfb (X Virtual Frame Buffer) is an X Windows System server that is
capable of running on machines with no display hardware and no
physical input devices. Xvfb emulates a dumb framebuffer using virtual
memory. Xvfb doesn't open any devices, but behaves otherwise as an X
display. Xvfb is normally used for testing servers. Using Xvfb, the
mfb or cfb code for any depth can be exercised without using real
hardware that supports the desired depths. Xvfb has also been used to
test X clients against unusual depths and screen configurations, to do
batch processing with Xvfb as a background rendering engine, to do
load testing, to help with porting an X server to a new platform, and
to provide an unobtrusive way of running applications which really
don't need an X server but insist on having one.

If you need to test your X server or your X clients, you may want to
install Xvfb for that purpose.

%package Xnest
Summary:	XFree86 Xnest server
Summary(pl):	Serwer XFree86 Xnest
Group:		X11/XFree86/Servers
Group(de):	X11/XFree86/Server
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description Xnest
Xnest is an X Window System server which runs in an X window. Xnest is
a 'nested' window server, actually a client of the real X server,
which manages windows and graphics requests for Xnest, while Xnest
manages the windows and graphics requests for its own clients.

You will need to install Xnest if you require an X server which will
run as a client of your real X server (perhaps for testing purposes).

%package Xprt
Summary:	X print server
Summary(pl):	X print server
Group:		X11/XFree86/Servers
Group(de):	X11/XFree86/Server
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
Group(de):	X11/XFree86/Server
Group(pl):	X11/XFree86/Serwery
Requires:	pam
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts >= 4.0
Obsoletes:	%{name}-VGA16 %{name}-SVGA %{name}-Mono
Obsoletes:	XFree86-S3 XFree86-S3V XFree86-I128
Obsoletes:	XFree86-Mach8 XFree86-Mach32 XFree86-Mach64
Obsoletes:	XFree86-8514 XFree86-AGX XFree86-3DLabs
Obsoletes:	XFree86-P9000 XFree86-W32
Obsoletes:	XFree86-ATI XFree86-Alliance XFree86-ChipsTechnologies
Obsoletes:	XFree86-Cirrus XFree86-Cyrix XFree86-FBDev
Obsoletes:	XFree86-i740 XFree86-i810 XFree86-mga
Obsoletes:	XFree86-NeoMagic XFree86-NVidia
Obsoletes:	XFree86-Rage128 XFree86-Rendition
Obsoletes:	XFree86-S3V XFree86-SiS XFree86-3dfx
Obsoletes:	XFree86-Trident XFree86-Tseng XFree86-VGA16
Obsoletes:	XFree86-TGA XFree86-FBDev
Obsoletes:	XFree86-Sun XFree86-Sun24 XFree86-SunMono
Obsoletes:	XFree86-XF86Setup, Xconfigurator

%description Xserver
X server for most simple framebuffer SVGA devices, including cards
built from ET4000 chips, Cirrus Logic chips, Chips and Technologies
laptop chips, Trident 8900 and 9000 chips. It works for Diamond
Speedstar, Orchid Kelvins, STB Nitros and Horizons, Genoa 8500VL, most
Actix boards, the Spider VLB Plus. It also works for many other chips
and cards, so try this server if you are having problems.

%description -l de Xserver
X-Server für die elementarsten Framebuffer-SVGA-Geräte, einschließlich
Karten, die aus ET4000-Chips, Cirrus Logic-Chips, Chips and
Technologies Laptop-Chips sowie Trident 8900 und 9000 Chips gebaut
sind. Funktioniert mit Diamond Speedstar, Orchid Kelvins, STB Nitros
und Horizons, Genoa 8500VL, den meisten Actix-Karten sowie Spider VLB
Plus und außerdem mit vielen anderen Chips und Karten. Es lohnt sich,
diesen Server auszuprobieren, wenn Sie Probleme haben.

%description -l fr Xserver
Serveur X pour les circuits SVGA les plus simples, dont les cartes
construites avec les circuits ET4000, Cirrus Logic, Chips and
Technologies laptop, Trident 8900 et 9000. Fonctionne pour les cartes
Diamond Speedstar, Orchid Kelvins, STB Nitros et Horizons, Genoa
8500VL, la plupart des Actix et la Spider VLB Plus. Fonctionne aussi
pour de nombreux autres circuits et cartes. Essayez ce serveur si vous
avez des problèmes.

%description -l pl Xserver
X serwer dla wiêkszo¶ci prostych kart SVGA, w³±czaj±c karty zbudowane
na uk³adach ET4000, Cirrus Logic, Trident 8900 i 9000, oraz uk³ady
wystêpuj±ce w laptopach. Dzia³a tak¿e z kartami Diamnod Speedstar,
Orchid Kelvins, STB Nitros i Horizons, Genoa 8500VL, wiêkszo¶æ Actix,
Spider VLB Plus. Dzia³a równie¿ na wielu innych kartach opartych na
innych uk³adach wiêc spróbuj tego serwera je¶li masz jakie¶ problemy.

%description -l tr Xserver
ET4000, Cirrus Logic, Chips and Technologies dizüstü, Trident 8900 ve
9000 gibi basit 'framebuffer' SVGA kullananan kartlar için X sunucusu.
Ayný zamanda Diamond Speedstar, Orchid Kelvins, STB Nitros / Horizons,
Genoa 8500VL, çoðu Actix kartlarý, Spider VLB Plus gibi kartlar ve
birçok diðer kart ile de çalýþýr. Herhangi bir sorun yaþarsanýz bu
sunucuyu deneyin.

%package driver-apm
Summary:	Alliance Promotion video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-apm
Alliance Promotion driver for XFree86 4.0+.

%package driver-ark
Summary:	Ark Logic video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-ark
Ark Logic driver for XFree86 4.0+.

%package driver-ati
Summary:	ATI video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-ati
ATI video driver.

%package driver-chips
Summary:	Chips and Technologies video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-chips
Chips and Technologies video driver.

%package driver-cirrus
Summary:	Cirrus Logic video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-cirrus
Cirrus Logic video driver.

%package driver-cyrix
Summary:	Cyrix video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-cyrix
Cyrix video driver.

%package driver-fbdev
Summary:	Video driver for framebuffer device
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-fbdev
Video driver for framebuffer device.

%package driver-ffb
Summary:	Video driver for DRI sparc framebuffer device
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-ffb
Video driver for DRI sparc framebuffer device.

%package driver-glide
Summary:	Voodoo 1 and Voodoo 2 video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-glide
Voodoo 1 and Voodoo 2 video driver.

%package driver-glint
Summary:	GLINT/Permedia video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	OpenGL

%description driver-glint
GLINT/Permedia video driver.

%package driver-i128
Summary:	Number 9 I128 video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-i128
Number 9 I128 video driver.

%package driver-i740
Summary:	Intel i740 video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-i740
Intel i740 video driver.

%package driver-i810
Summary:	Intel i810 video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	OpenGL

%description driver-i810
Intel i810 video driver.

%package driver-mga
Summary:	Matrox video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	OpenGL

%description driver-mga
Matrox video driver.

%package driver-neomagic
Summary:	NeoMagic video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-neomagic
NeoMagic video driver.

%package driver-nv
Summary:	NVIDIA video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-nv
NVIDIA video driver.

%package driver-r128
Summary:	ATI Rage 128 video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	OpenGL

%description driver-r128
ATI Rage 128 video driver.

%package driver-radeon
Summary:	ATI Radeon video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-radeon
ATI Radeon video driver.

%package driver-rendition
Summary:	Rendition video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-rendition
Rendition video driver.

%package driver-s3virge
Summary:	S3 ViRGE video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-s3virge
S3 ViRGE video driver.

%package driver-savage
Summary:	S3 Savage video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-savage
S3 Savage video driver.

%package driver-siliconmotion
Summary:	Silicon Motion video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-siliconmotion
Silicon Motion video driver.

%package driver-sis
Summary:	SiS video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-sis
SiS video driver.

%package driver-sunbw2
Summary:	sunbw2 - Sun BW2 video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-sunbw2
sunbw2 - Sun BW2 video driver.

%package driver-suncg14
Summary:	suncg14 - Sun CG14 video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-suncg14
suncg14 - Sun CG14 video driver.

%package driver-suncg3
Summary:	suncg3 - Sun CG3 video cards driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-suncg3
suncg3 - Sun CG3 video cards driver.

%package driver-suncg6
Summary:	suncg6 - Sun GX and Turbo GX video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-suncg6
suncg6 - Sun GX and Turbo GX video driver.

%package driver-sunffb
Summary:	sunffb - Sun Creator, Creator 3D and Elite 3D video cards driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-sunffb
sunffb - Sun Creator, Creator 3D and Elite 3D video cards driver.

%package driver-sunleo
Summary:	sunleo - Sun Leo (ZX) video cards driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-sunleo
sunleo - Sun Leo (ZX) video cards driver.

%package driver-suntcx
Summary:	suntcx - Sun TCX video cards driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-suntcx
suntcx - Sun TCX video cards driver.

%package driver-tdfx
Summary:	3Dfx video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	OpenGL

%description driver-tdfx
3Dfx video driver.

%package driver-tga
Summary:	TGA video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-tga
TGA video driver.

%package driver-trident
Summary:	Trident video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-trident
Trident video driver.

%package driver-tseng
Summary:	Tseng Labs video driver
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-tseng
Tseng Labs video driver.

%package DPS
Summary:	Display PostScript
Summary(pl):	Display PostScript
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Obsoletes:	dgs

%description DPS
X-Windows Display PostScript is device-independent imaging model for
displaying information on a screen.

%description -l pl DPS
X-Windows Display PostScript, to niezale¿ny od urz±dzenia model
wy¶wietlania informacji na ekranie.

%package DPS-devel
Summary:	Display PostScript
Summary(pl):	Display PostScript
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-DPS = %{version}
Obsoletes:	dgs-devel

%description DPS-devel
Header files for develop X-Windows Display Postscript.

%description -l pl DPS-devel
Pliki nag³ówkowe do biblioteki do X-Windows Display PostScript.

%package DPS-static
Summary:	Display PostScript
Summary(pl):	Display PostScript
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-DPS-devel = %{version}
Obsoletes:	dgs-static

%description DPS-static
X-Windows Display PostScript static libraries.

%description -l pl DPS-static
Statyczne biblioteko do X-Windows Display PostScript.

%package -n sessreg
Summary:	sessreg - manage utmp/wtmp entries for non-init clients
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-libs = %{version}

%description -n sessreg
Sessreg is a simple program for managing utmp/wtmp entries for xdm
sessions.

System V has a better interface to /var/run/utmp than BSD; it
dynamically allocates entries in the file, instead of writing them at
fixed positions indexed by position in /etc/ttys.

%package -n xdm
Summary:	xdm - X Display Manager with support for XDMCP, host chooser
Summary(pl):	XDM
Group:		X11/XFree86
Group(de):	X11/XFree86
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
Xdm manages a collection of X displays, which may be on the local host
or remote servers. The design of xdm was guided by the needs of X
terminals as well as the X Consortium standard XDMCP, the X Display
Manager Control Protocol.

%package -n twm
Summary:	Tab Window Manager for the X Window System
Summary(pl):	Twm - podstawowy zarz±dca okien dla X Window System
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia

%description -n twm
Twm is a window manager for the X Window System. It provides
titlebars, shaped windows, several forms of icon management,
user-defined macro functions, click-to-type and pointerdriven keyboard
focus, and user-specified key and pointer button bindings.

%package -n xfs
Summary:	Font server for XFree86
Summary(pl):	Serwer fontów do XFree86
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-libs = %{version}
Prereq:		chkconfig
Obsoletes:	xfsft XFree86-xfs

%description -n xfs
This is a font server for XFree86. You can serve fonts to other X
servers remotely with this package, and the remote system will be able
to use all fonts installed on the font server, even if they are not
installed on the remote computer.

%package -n xauth
Summary:	xauth - X authority file utility
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-libs = %{version}

%description -n xauth
The xauth program is used to edit and display the authorization
information used in connecting to the X server. This program is
usually used to extract authorization records from one machine and
merge them in on another (as is the case when using remote logins or
granting access to other users).

%package tools
Summary:	Various tools for XFree86
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name} = %{version}
Obsoletes:	X11R6-contrib

%description tools
Various tools for X, including listres, xbiff, xedit, xeyes, xcalc,
xload and xman, among others.

If you're using X, you should install XFree86-tools. You will also
need to install the XFree86 package, the XFree86 package which
corresponds to your video card, one of the XFree86 fonts packages, the
Xconfigurator package and the XFree86-libs package.

Finally, if you are going to develop applications that run as X
clients, you will also need to install XFree86-devel.

This package contains all applications that used to be in
X11R6-contrib in older releases.

#--- %prep ---------------------------

%prep
%setup -q -c -a1 -a2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0
# Not ready yet
#%patch6 -p0
%patch7 -p1
%patch8 -p1
%patch9 -p0
%patch10 -p1
%patch11 -p1
%patch12 -p0
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p0
%patch21 -p0
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
rm -f xc/config/cf/host.def

#--- %build --------------------------

%build
%{__make} -S -C xc World DEFAULT_OS_CPU_FROB=%{_target_cpu} \
	"BOOTSTRAPCFLAGS=%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}" \
	"CCOPTIONS=%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}" \
	"CXXOPTIONS=%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}" \
	"CXXDEBUGFLAGS=" "CDEBUGFLAGS="

cd Mesa*

%configure \
	--enable-static \
	--enable-shared \
	--with-ggi="no" \
	--with-svga="no" \
	--disable-ggi-fbdev \
	--disable-ggi-genkgi \
%ifarch %{ix86} \
	--enable-x86 \
  %ifarch i586 i686 \
	--enable-mmx \
	--enable-3dnow \
  %else \
    %ifarch k6 \
	--enable-mmx \
	--enable-3dnow" \
    %else \
	--disable-mmx \
	--disable-3dnow \
    %endif \
  %endif \
%else \
	--disable-x86 \
	--disable-mmx \
	--disable-3dnow
%endif

%{__make} -C src-glu
	
#--- %install ------------------------

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{sysconfig,X11,pam.d,rc.d/init.d,security/console.apps} \
	$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/pl \
	$RPM_BUILD_ROOT/var/lib/xkb \
	$RPM_BUILD_ROOT/usr/include \
	$RPM_BUILD_ROOT/usr/bin \
	$RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties \
	$RPM_BUILD_ROOT{%{_appnkldir}/Utilities,%{_datadir}/pixmaps}

%{__make} -C xc	"DESTDIR=$RPM_BUILD_ROOT" \
		"DOCDIR=/usr/share/doc/%{name}-%{version}" \
		"INSTBINFLAGS=-m 755" \
		"INSTPGMFLAGS=-m 755" \
		"RAWCPP=/lib/cpp" \
		install install.man

%{__make} -C Mesa*/src-glu install \
	DESTDIR=$RPM_BUILD_ROOT

install Mesa*/include/GL/glu.h $RPM_BUILD_ROOT%{_includedir}/GL/

# setting default X
rm -f $RPM_BUILD_ROOT%{_bindir}/X
ln -sf XFree86 $RPM_BUILD_ROOT%{_bindir}/X

# setting ghost X in /etc/X11 -- xf86config will fix this ...
ln -s ../..%{_bindir}/XFree86 $RPM_BUILD_ROOT/etc/X11/X

# add X11 links in /usr/bin and /usr/include
ln -s ../X11R6/include/X11 $RPM_BUILD_ROOT/usr/include/X11
ln -s ../X11R6/bin $RPM_BUILD_ROOT/usr/bin/X11

# fix libGL*.so links
rm -f $RPM_BUILD_ROOT%{_libdir}/libGL*.so
ln -sf libGL.so.1 $RPM_BUILD_ROOT%{_libdir}/libGL.so
ln -sf libGLU.so.1 $RPM_BUILD_ROOT%{_libdir}/libGLU.so

# set up PLD xdm config
rm -f $RPM_BUILD_ROOT/etc/X11/xdm/{*Console,Xaccess,Xsession,Xsetup*}
install xdm-xinitrc-*/pixmaps/* $RPM_BUILD_ROOT/etc/X11/xdm/pixmaps/
install xdm-xinitrc-*/{*Console,Xaccess,Xsession,Xsetup*} $RPM_BUILD_ROOT/etc/X11/xdm/

install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/xdm
install %{SOURCE7} $RPM_BUILD_ROOT/etc/pam.d/xserver
install %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/xdm
install %{SOURCE5} $RPM_BUILD_ROOT/etc/rc.d/init.d/xfs
install %{SOURCE6} $RPM_BUILD_ROOT/etc/X11/fs/config
install %{SOURCE8} $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/pl/XTerm

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

# do not duplicate xkbcomp program
rm -f $RPM_BUILD_ROOT%{_libdir}/X11/xkb/xkbcomp
ln -sf %{_bindir}/xkbcomp $RPM_BUILD_ROOT/etc/X11/xkb/xkbcomp

ln -sf ../../../share/doc/%{name}-%{version} \
	$RPM_BUILD_ROOT%{_libdir}/X11/doc

rm -f $RPM_BUILD_ROOT%{_libdir}/X11/config/host.def

:> $RPM_BUILD_ROOT%{_libdir}/X11/config/host.def
:> $RPM_BUILD_ROOT/etc/X11/XF86Config

rm -rf $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/html

%ifnarch sparc sparc64
gzip -9nf $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/*

# don't gzip README.* files, they are needed by XF86Setup
gunzip $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/README.*

%endif

#--- %post{un}, %preun, %verifyscript, %trigge ----------

%triggerpostun modules -- XFree86-modules < 4.0.2
if [ -d /usr/X11R6/lib/X11/xkb ]; then
	rm -rf /usr/X11R6/lib/X11/xkb
	ln -sf ../../../../etc/X11/xkb /usr/X11R6/lib/X11/xkb
fi

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

%post   DPS -p /sbin/ldconfig
%postun DPS -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

#--- %files --------------------------

%files
%defattr(644,root,root,755)
%ifnarch sparc sparc64
%doc %{_docdir}/%{name}-%{version}/*
%doc %{_libdir}/X11/doc
%endif

%dir %{_prefix}
%dir %{_libdir}
%dir %{_libdir}/X11
%dir %{_bindir}

%{_libdir}/X11/XErrorDB
%{_libdir}/X11/XftConfig
%{_libdir}/X11/XKeysymDB
%{_libdir}/X11/locale

%dir %{_libdir}/X11/app-defaults
%{_libdir}/X11/app-defaults/XCalc
%{_libdir}/X11/app-defaults/XCalc-color
%{_libdir}/X11/app-defaults/XClipboard
%{_libdir}/X11/app-defaults/XClock
%{_libdir}/X11/app-defaults/XLoad
%{_libdir}/X11/app-defaults/XLogo
%{_libdir}/X11/app-defaults/XLogo-color
%{_libdir}/X11/app-defaults/XSm
%{_libdir}/X11/app-defaults/XTerm
%{_libdir}/X11/app-defaults/XTerm-color
%ifnarch sparc sparc64
%{_libdir}/X11/app-defaults/XF86Cfg
%endif

%attr(755,root,root) %{_libdir}/X11/lbxproxy
%attr(755,root,root) %{_libdir}/X11/proxymngr
%attr(755,root,root) %{_libdir}/X11/rstart
%attr(755,root,root) %{_libdir}/X11/xserver
%attr(755,root,root) %{_libdir}/X11/fonts
%attr(755,root,root) %{_libdir}/X11/xinit
%attr(755,root,root) %{_libdir}/X11/xsm

%dir /etc/X11/lbxproxy
%dir /etc/X11/proxymngr
%dir /etc/X11/rstart
%dir /etc/X11/rstart/commands
%dir /etc/X11/rstart/commands/x11r6
%dir /etc/X11/rstart/contexts
%dir /etc/X11/xserver
%dir /etc/X11/xsm
%dir /etc/X11/xinit

/etc/X11/lbxproxy/*
/etc/X11/proxymngr/*
%attr(-,root,root) /etc/X11/rstart/config
%attr(-,root,root) /etc/X11/rstart/rstartd.real
%attr(-,root,root) /etc/X11/rstart/commands/x
%attr(-,root,root) /etc/X11/rstart/commands/x11
%attr(-,root,root) /etc/X11/rstart/commands/*List*
%attr(-,root,root) /etc/X11/rstart/commands/x11r6/*
%attr(-,root,root) /etc/X11/rstart/contexts/*
/etc/X11/xserver/SecurityPolicy
/etc/X11/xsm/*

%lang(pl) %{_libdir}/X11/app-defaults/pl

%dir %{_libdir}/X11/x11perfcomp
%attr(755,root,root) %{_libdir}/X11/x11perfcomp/*
%{_libdir}/X11/*.txt

%attr(755,root,root) %{_bindir}/Xmark
%attr(755,root,root) %{_bindir}/appres
%attr(755,root,root) %{_bindir}/atobm
%attr(755,root,root) %{_bindir}/bdftopcf
%attr(755,root,root) %{_bindir}/bitmap
%attr(755,root,root) %{_bindir}/bmtoa
%attr(755,root,root) %{_bindir}/cxpm
%attr(755,root,root) %{_bindir}/dga
%attr(755,root,root) %{_bindir}/editres
%attr(755,root,root) %{_bindir}/iceauth
%attr(755,root,root) %{_bindir}/lbxproxy
%attr(755,root,root) %{_bindir}/lndir
%attr(755,root,root) %{_bindir}/makeg
%attr(755,root,root) %{_bindir}/makestrs
%attr(755,root,root) %{_bindir}/mergelib
%attr(755,root,root) %{_bindir}/mkdirhier
%attr(755,root,root) %{_bindir}/mkfontdir
%attr(755,root,root) %{_bindir}/proxymngr
%attr(755,root,root) %{_bindir}/resize
%attr(755,root,root) %{_bindir}/revpath
%attr(755,root,root) %{_bindir}/rstart
%attr(755,root,root) %{_bindir}/rstartd
%attr(755,root,root) %{_bindir}/setxkbmap
%attr(755,root,root) %{_bindir}/showrgb
%attr(755,root,root) %{_bindir}/smproxy
%attr(755,root,root) %{_bindir}/startx
%attr(755,root,root) %{_bindir}/sxpm
%attr(755,root,root) %{_bindir}/xcmsdb
%attr(755,root,root) %{_bindir}/xconsole
%attr(755,root,root) %{_bindir}/xcutsel
%attr(755,root,root) %{_bindir}/xdpyinfo
%attr(755,root,root) %{_bindir}/xfindproxy
%attr(755,root,root) %{_bindir}/xfwp
%attr(755,root,root) %{_bindir}/xgamma
%attr(755,root,root) %{_bindir}/xhost
%attr(755,root,root) %{_bindir}/xinit
%attr(755,root,root) %{_bindir}/xkbbell
%attr(755,root,root) %{_bindir}/xkbcomp
%attr(755,root,root) %{_bindir}/xkbevd
%attr(755,root,root) %{_bindir}/xkbprint
%attr(755,root,root) %{_bindir}/xkbvleds
%attr(755,root,root) %{_bindir}/xkbwatch
%attr(755,root,root) %{_bindir}/xlsatoms
%attr(755,root,root) %{_bindir}/xlsclients
%attr(755,root,root) %{_bindir}/xlsfonts
%attr(755,root,root) %{_bindir}/xmodmap
%attr(755,root,root) %{_bindir}/xon
%attr(755,root,root) %{_bindir}/xprop
%attr(755,root,root) %{_bindir}/xrdb
%attr(755,root,root) %{_bindir}/xrefresh
%attr(755,root,root) %{_bindir}/xset
%attr(755,root,root) %{_bindir}/xsetmode
%attr(755,root,root) %{_bindir}/xsetpointer
%attr(755,root,root) %{_bindir}/xsetroot
%attr(755,root,root) %{_bindir}/xsm
%attr(755,root,root) %{_bindir}/xstdcmap
%attr(755,root,root) %{_bindir}/xterm
%attr(755,root,root) %{_bindir}/xvidtune
%attr(755,root,root) %{_bindir}/xvinfo
%attr(755,root,root) %{_bindir}/xwd
%attr(755,root,root) %{_bindir}/xwud

%{_includedir}/X11/bitmaps
%{_includedir}/X11/pixmaps

%{_appnkldir}/Utilities/*.desktop
%{_appnkldir}/*.desktop
%{_datadir}/pixmaps/*

%{_mandir}/man1/Xmark.1*
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
%{_mandir}/man1/xcutsel.1*
%{_mandir}/man1/xcmsdb.1*
%{_mandir}/man1/xconsole.1*
%{_mandir}/man1/xdpyinfo.1*
%{_mandir}/man1/dga.1*
%{_mandir}/man1/xhost.1*
%{_mandir}/man1/xinit.1*
%{_mandir}/man1/startx.1*
%{_mandir}/man1/setxkbmap.1*
%{_mandir}/man1/xkbcomp.1*
%{_mandir}/man1/xkbevd.1*
%{_mandir}/man1/xkbprint.1*
%{_mandir}/man1/xlsatoms.1*
%{_mandir}/man1/xlsclients.1*
%{_mandir}/man1/xlsfonts.1*
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
%{_mandir}/man1/xvinfo.1*
%{_mandir}/man1/xwd.1*
%{_mandir}/man1/xwud.1*
%{_mandir}/man1/xon.1*
%{_mandir}/man1/revpath.1*
%{_mandir}/man1/xgamma.1*
%{_mandir}/man1/cxpm.1*
%{_mandir}/man1/sxpm.1*
%ifnarch alpha
%{_mandir}/man1/libxrx.1*
%endif
%{_mandir}/man7/*

/usr/bin/X11

%files modules
%defattr(-,root,root,755)
%{_libdir}/X11/xkb
/etc/X11/xkb
/var/lib/xkb
%dir %{_libdir}/modules
%ifnarch alpha
%dir %{_libdir}/modules/dri
%endif
%dir %{_libdir}/modules/drivers
%ifnarch sparc sparc64
%{_libdir}/modules/*.uc
%endif
%attr(755,root,root) %{_libdir}/modules/*.a
%attr(755,root,root) %{_libdir}/modules/codeconv
%attr(755,root,root) %{_libdir}/modules/drivers/linux
%ifnarch sparc sparc64
%attr(755,root,root) %{_libdir}/modules/drivers/vga_drv.o
%attr(755,root,root) %{_libdir}/modules/drivers/vesa_drv.o
%endif
%dir %{_libdir}/modules/extensions
%attr(755,root,root) %{_libdir}/modules/extensions/libdbe.a
%attr(755,root,root) %{_libdir}/modules/extensions/libdri.a
%attr(755,root,root) %{_libdir}/modules/extensions/libextmod.a
%attr(755,root,root) %{_libdir}/modules/extensions/libpex5.a
%attr(755,root,root) %{_libdir}/modules/extensions/librecord.a
%attr(755,root,root) %{_libdir}/modules/extensions/libxie.a
%attr(755,root,root) %{_libdir}/modules/fonts
%attr(755,root,root) %{_libdir}/modules/input
%attr(755,root,root) %{_libdir}/modules/linux
%{_mandir}/man4/citron*
%{_mandir}/man4/dynapro*
%{_mandir}/man4/keyboard*
%{_mandir}/man4/microtouch*
%{_mandir}/man4/mouse*
%{_mandir}/man4/v4l*
%ifnarch sparc sparc64
%{_mandir}/man4/vga*
%{_mandir}/man4/vesa*
%endif
%{_mandir}/man4/void*
%{_mandir}/man4/wacom*
%{_mandir}/man4/elographics*
%{_mandir}/man4/mutouch*

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
/var/lib/xdm

%{_libdir}/X11/app-defaults/Chooser

%attr(755,root,root) %{_libdir}/X11/xdm
%attr(755,root,root) %{_bindir}/xdm
%attr(755,root,root) %{_bindir}/chooser
%ifarch alpha
%attr(755,root,root) %{_libdir}/libXdmGreet.so*
%endif
%{_mandir}/man1/xdm.1*

%dir /etc/X11/xdm
%attr(755,root,root) %config /etc/X11/xdm/GiveConsole
%attr(755,root,root) %config /etc/X11/xdm/TakeConsole
%attr(755,root,root) %config /etc/X11/xdm/Xsession
%attr(755,root,root) %config /etc/X11/xdm/Xsetup_0
%attr(755,root,root) %config /etc/X11/xdm/Xwilling
%config /etc/X11/xdm/Xaccess
%config /etc/X11/xdm/Xresources
%config /etc/X11/xdm/Xservers
%config /etc/X11/xdm/xdm-config
/etc/X11/xdm/pixmaps

%files -n twm
%defattr(644,root,root,755)
%{_datadir}/gnome/wm-properties/twm.desktop
%attr(755,root,root) %{_bindir}/twm
%dir /etc/X11/twm
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
%attr(755,root,root) %{_libdir}/libX*.so.*.*
%attr(755,root,root) %{_libdir}/libI*.so.*.*
%attr(755,root,root) %{_libdir}/libP*.so.*.*
%attr(755,root,root) %{_libdir}/libS*.so.*.*
%ifnarch alpha
%attr(755,root,root) %{_libdir}/libx*.so.*.*
%endif

%files OpenGL-core
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGL.so.*.*
%ifnarch sparc sparc64
%attr(755,root,root) %{_libdir}/modules/extensions/libglx.a
%attr(755,root,root) %{_libdir}/modules/extensions/libGLcore.a
%endif

%files OpenGL-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glxinfo
%attr(755,root,root) %{_libdir}/libGLU.so.*.*
%ifnarch alpha
%attr(755,root,root) %{_libdir}/libOSMesa.so.*.*
%endif
%{_mandir}/man1/glxinfo.1*

%files OpenGL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLU.la
%attr(755,root,root) %{_libdir}/libGL*.so
%attr(755,root,root) %{_libdir}/libGLw.a
%ifnarch alpha
%attr(755,root,root) %{_libdir}/libOSMesa*.so
%endif
%dir %{_includedir}/GL
%attr(644,root,root) %{_includedir}/GL/*
%{_mandir}/man3/glX*

%files OpenGL-static
%defattr(644,root,root,755)
%{_libdir}/libGL.a
%{_libdir}/libGLU.a

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gccmakedep
%attr(755,root,root) %{_libdir}/libX*.so
%attr(755,root,root) %{_libdir}/libI*.so
%attr(755,root,root) %{_libdir}/libP*.so
%attr(755,root,root) %{_libdir}/libS*.so
%ifnarch alpha
%attr(755,root,root) %{_libdir}/libx*.so
%endif
%{_libdir}/libFS.a
%{_libdir}/libXau.a
%{_libdir}/libXdmcp.a
%{_libdir}/libXfontcache.a
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
%{_libdir}/libXinerama.a

%dir %{_includedir}/X11
%{_includedir}/X11/*.h
%{_includedir}/X11/ICE
%{_includedir}/X11/PEX5
%{_includedir}/X11/PM
%{_includedir}/X11/SM
%{_includedir}/X11/Xaw
%{_includedir}/X11/Xft
%{_includedir}/X11/Xmu
%{_includedir}/X11/extensions
%{_includedir}/X11/fonts
%{_includedir}/xf86*.h
%{_libdir}/X11/config

%attr(755,root,root) %{_bindir}/imake
%attr(755,root,root) %{_bindir}/makedepend
%attr(755,root,root) %{_bindir}/xmkmf

%{_mandir}/man1/imake.1*
%{_mandir}/man1/makedepend.1*
%{_mandir}/man1/xmkmf.1*
%{_mandir}/man3/[A-Z]*

/usr/include/X11

%files static
%defattr(644,root,root,755)
%{_libdir}/libICE.a
%{_libdir}/libPEX5.a
%{_libdir}/libSM.a
%{_libdir}/libX11.a
%{_libdir}/libXIE.a
%{_libdir}/libXaw.a
%{_libdir}/libXft.a
%{_libdir}/libXext.a
%{_libdir}/libXfont.a
%{_libdir}/libXi.a
%{_libdir}/libXmu.a
%{_libdir}/libXp.a
%{_libdir}/libXpm.a
%{_libdir}/libXrender.a
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

%{_libdir}/X11/Cards

%config(noreplace) %verify(not md5 mtime size) /etc/X11/XF86Config
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/xserver
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.xserver
%config(missingok) /etc/security/console.apps/xserver

%ifnarch sparc sparc64

%files driver-apm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/apm_drv.o
%{_mandir}/man4/apm*

%endif
%ifnarch sparc sparc64

%files driver-ark
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/ark_drv.o

%endif

%files driver-ati
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/ati*_drv.o
#%{_mandir}/man4/ati*

%ifnarch sparc sparc64

%files driver-chips
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/chips_drv.o
%{_mandir}/man4/chips*

%endif
%ifnarch sparc sparc64

%files driver-cirrus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/cirrus_*.o
%{_mandir}/man4/cirrus*

%endif
%ifnarch sparc sparc64

%files driver-cyrix
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/cyrix_drv.o
%{_mandir}/man4/cyrix*

%endif

%files driver-fbdev
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/fbdev_drv.o
%{_mandir}/man4/fbdev*
%ifnarch sparc sparc64

%files driver-glide
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/glide_drv.o
%{_mandir}/man4/glide*

%endif

%files driver-glint
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/glint_drv.o
%ifnarch sparc sparc64
%attr(755,root,root) %{_libdir}/modules/dri/gamma_dri.so
%endif
%{_mandir}/man4/glint*

%ifnarch sparc sparc64

%files driver-i128
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/i128_drv.o
%{_mandir}/man4/i128*

%endif
%ifnarch sparc sparc64

%files driver-i740
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/i740_drv.o
%{_mandir}/man4/i740*

%endif
%ifnarch sparc sparc64

%files driver-i810
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/i810_drv.o
%attr(755,root,root) %{_libdir}/modules/dri/i810_dri.so
%{_mandir}/man4/i810*

%endif
%ifnarch sparc sparc64

%files driver-mga
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/mga_drv.o
%attr(755,root,root) %{_libdir}/modules/dri/mga_dri.so
%{_mandir}/man4/mga*

%endif
%ifnarch sparc sparc64

%files driver-neomagic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/neomagic_drv.o
%{_mandir}/man4/neomagic*

%endif
%ifnarch sparc sparc64

%files driver-nv
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/nv_drv.o
%{_mandir}/man4/nv*

%endif
%ifnarch sparc sparc64

%files driver-r128
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/r128_drv.o
%ifnarch sparc sparc64
%attr(755,root,root) %{_libdir}/modules/dri/r128_dri.so
%endif
%{_mandir}/man4/r128*

%endif

%files driver-radeon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/radeon_drv.o

%ifnarch sparc sparc64

%files driver-rendition
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/rendition_drv.o
%{_mandir}/man4/rendition*

%endif
%ifnarch sparc sparc64

%files driver-s3virge
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/s3virge_drv.o
%{_mandir}/man4/s3virge*

%endif
%ifnarch sparc sparc64

%files driver-savage
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/savage_drv.o
%{_mandir}/man4/savage*

%endif
%ifnarch sparc sparc64

%files driver-siliconmotion
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/siliconmotion_drv.o
%{_mandir}/man4/siliconmotion*

%endif
%ifnarch sparc sparc64

%files driver-sis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/sis_drv.o
%attr(755,root,root) %{_libdir}/modules/dri/sis_dri.so
%{_mandir}/man4/sis*

%endif
%ifarch sparc sparc64

%files driver-sunbw2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/sunbw2_drv.o
%{_mandir}/man4/sunbw2*

%endif
%ifarch sparc sparc64

%files driver-suncg14
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/suncg14_drv.o
%{_mandir}/man4/suncg14*

%endif
%ifarch sparc sparc64

%files driver-suncg3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/suncg3_drv.o
%{_mandir}/man4/suncg3*

%endif
%ifarch sparc sparc64

%files driver-suncg6
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/suncg6_drv.o
%{_mandir}/man4/suncg6*

%endif
%ifarch sparc sparc64

%files driver-sunffb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/sunffb_drv.o
%attr(755,root,root) %{_libdir}/modules/dri/ffb_dri.so
%{_mandir}/man4/sunffb*

%endif
%ifarch sparc sparc64

%files driver-sunleo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/sunleo_drv.o
%{_mandir}/man4/sunleo*

%endif
%ifarch sparc sparc64

%files driver-suntcx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/suntcx_drv.o
%{_mandir}/man4/suntcx*

%endif
%ifnarch sparc sparc64

%files driver-tdfx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/tdfx_drv.o
%attr(755,root,root) %{_libdir}/modules/dri/tdfx_dri.so
%{_mandir}/man4/tdfx*

%endif
%ifnarch sparc sparc64

%files driver-tga
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/tga_drv.o

%endif
%ifnarch sparc sparc64

%files driver-trident
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/trident_drv.o
%{_mandir}/man4/trident*

%endif
%ifnarch sparc sparc64

%files driver-tseng
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/tseng_drv.o
%{_mandir}/man4/tseng*

%endif

%files DPS
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/makepsres
%attr(755,root,root) %{_bindir}/pswrap
%attr(755,root,root) %{_libdir}/libdps.so.*.*
%attr(755,root,root) %{_libdir}/libdpstk.so.*.*
%attr(755,root,root) %{_libdir}/libpsres.so.*.*
%{_mandir}/man1/makepsres*
%{_mandir}/man1/pswrap*

%files DPS-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdps.so
%attr(755,root,root) %{_libdir}/libdpstk.so
%attr(755,root,root) %{_libdir}/libpsres.so
%{_includedir}/DPS

%files DPS-static
%defattr(644,root,root,755)
%{_libdir}/libdps.a
%{_libdir}/libdpstk.a
%{_libdir}/libpsres.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/beforelight
%attr(755,root,root) %{_bindir}/ico
%attr(755,root,root) %{_bindir}/listres
%attr(755,root,root) %{_bindir}/showfont
%attr(755,root,root) %{_bindir}/viewres
%attr(755,root,root) %{_bindir}/x11perf
%attr(755,root,root) %{_bindir}/x11perfcomp
%attr(755,root,root) %{_bindir}/xbiff
%attr(755,root,root) %{_bindir}/xcalc
%attr(755,root,root) %{_bindir}/xclipboard
%attr(755,root,root) %{_bindir}/xclock
%attr(755,root,root) %{_bindir}/xditview
%attr(755,root,root) %{_bindir}/xedit
%attr(755,root,root) %{_bindir}/xev
%attr(755,root,root) %{_bindir}/xeyes
%attr(755,root,root) %{_bindir}/xfd
%attr(755,root,root) %{_bindir}/xfontsel
%attr(755,root,root) %{_bindir}/xgc
%attr(755,root,root) %{_bindir}/xieperf
%attr(755,root,root) %{_bindir}/xload
%attr(755,root,root) %{_bindir}/xmag
%attr(755,root,root) %{_bindir}/xman
%attr(755,root,root) %{_bindir}/xmessage
%attr(755,root,root) %{_bindir}/xwininfo
%attr(755,root,root) %{_bindir}/oclock
%attr(755,root,root) %{_bindir}/xlogo
%attr(755,root,root) %{_bindir}/xkill
%attr(755,root,root) %{_bindir}/rman
%{_libdir}/X11/xman.help
%{_mandir}/man1/beforelight.1*
%{_mandir}/man1/ico.1*
%{_mandir}/man1/listres.1*
%{_mandir}/man1/showfont.1*
%{_mandir}/man1/viewres.1*
%{_mandir}/man1/x11perf.1*
%{_mandir}/man1/x11perfcomp.1*
%{_mandir}/man1/xbiff.1*
%{_mandir}/man1/xcalc.1*
%{_mandir}/man1/xclipboard.1*
%{_mandir}/man1/xclock.1*
%{_mandir}/man1/xditview.1*
%{_mandir}/man1/xedit.1*
%{_mandir}/man1/xev.1*
%{_mandir}/man1/xeyes.1*
%{_mandir}/man1/xfd.1*
%{_mandir}/man1/xfontsel.1*
%{_mandir}/man1/xgc.1*
%{_mandir}/man1/xieperf.1*
%{_mandir}/man1/xload.1*
%{_mandir}/man1/xmag.1*
%{_mandir}/man1/xman.1*
%{_mandir}/man1/xmessage.1*
%{_mandir}/man1/xwininfo.1*
%{_mandir}/man1/xkill.1*
%{_mandir}/man1/xlogo.1*
%{_mandir}/man1/oclock.1*
%{_mandir}/man1/rman.1*
%{_libdir}/X11/app-defaults/Beforelight
%{_libdir}/X11/app-defaults/Bitmap
%{_libdir}/X11/app-defaults/Bitmap-color
%{_libdir}/X11/app-defaults/Clock-color
%{_libdir}/X11/app-defaults/Editres
%{_libdir}/X11/app-defaults/Editres-color
%{_libdir}/X11/app-defaults/Viewres
%{_libdir}/X11/app-defaults/Xvidtune
%{_libdir}/X11/app-defaults/XConsole
%{_libdir}/X11/app-defaults/Xedit
%{_libdir}/X11/app-defaults/Xedit-color
%{_libdir}/X11/app-defaults/Xfd
%{_libdir}/X11/app-defaults/Xgc
%{_libdir}/X11/app-defaults/Xmag
%{_libdir}/X11/app-defaults/Xman
%{_libdir}/X11/app-defaults/Xmessage
%{_libdir}/X11/app-defaults/XFontSel
%{_libdir}/X11/app-defaults/Xditview
%{_libdir}/X11/app-defaults/Xditview-chrtr

%files setup
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/SuperProbe
%attr(755,root,root) %{_bindir}/pcitweak
%attr(755,root,root) %{_bindir}/scanpci
%attr(755,root,root) %{_bindir}/xf86cfg
%attr(755,root,root) %{_bindir}/xf86config
%{_mandir}/man1/SuperProbe.1*
%{_mandir}/man1/scanpci.1*
%{_mandir}/man1/pcitweak.1*
%{_mandir}/man1/xf86cfg.1*
%{_mandir}/man1/xf86config.1*
