Summary:	XFree86 Window System servers and basic programs
Summary(de):	Xfree86 Window-System-Server und grundlegende Programme
Summary(es):	Servidores XFree86 y programas de base
Summary(fr):	Serveurs du système XFree86 et programmes de base
Summary(ja):	XFree86 window system ¤Î¥µ¡¼¥Ð¤È´ðËÜÅª¤Ê¥×¥í¥°¥é¥à
Summary(pl):	XFree86 Window System wraz z podstawowymi programami
Summary(tr):	XFree86 Pencereleme Sistemi sunucularý ve temel programlar
Summary(wa):	Sierveus di håynaedje XFree86 eyèt maisses programes
Name:		XFree86
Version:	3.3.6
Release:	21
Copyright:	MIT
Group:		X11/XFree86
Group(pl):	X11/XFree86
Source0:	ftp://ftp.xfree86.org/pub/XFree86/3.3.6/source/X336src-1.tgz
Source1:	ftp://ftp.xfree86.org/pub/XFree86/3.3.6/source/X336src-2.tgz
Source2:	ftp://ftp.dcs.ed.ac.uk/pub/jec/programs/xfsft/xfsft-1.1.6.tar.gz
Source3:	xdm.pamd
Source4:	xdm.init
Source5:	xfs.init
Source6:	xfs.config
Source7:	xserver.pamd
Source8:	XTerm.ad-pl
Source9:	twm.desktop
Source10:	xdm.sysconfig
Source11:	xfs.sysconfig

Patch0:		XFree86-rh.patch
Patch1:		XFree86-rhxdm.patch
Patch2:		XFree86-fsstnd.patch
Patch3:		XFree86-alpha-sockets.patch
# the following was causing problems with RagePRO based ATI
# chipsets, but this has been fixed
# use glibc 2.1 routines for utmp, doesn't require xterm to be setuid
Patch4:		XFree86-nosuidxterm.patch
Patch5:		XFree86-joy.patch
Patch6:		XFree86-ru_SU.patch
Patch7:		XFree86-startx_xauth.patch
Patch8:		XFree86-xfsredhat.patch
# link xterm with libncurses instead libtermcap
Patch9:		XFree86-ncurses.patch
# Compile X serwers againsty system installed libz.so
Patch10:	XFree86-HasZlib.patch
# Man dir in /usr/X11R6/man or %{_mandir}
Patch11:	XFree86-fhs.patch
Patch12:	XFree86-voodoo-Rush.patch
Patch13:	XFree86-xinitrace.patch
Patch14:	XFree86-xterm-color.patch
Patch15:	XFree86-xdm+pam_env.patch
Patch16:	XFree86-XF86Config-path.patch
Patch17:	XFree86-XF86Setup-fonts.patch
Patch18:	XFree86-pam.patch
Patch19:	XFree86-fixiso8859-2.patch
# fix Diamond SpeedStar A50 Xconfigurator setup
Patch20:	XFree86-ssa50.patch
# turn off accel for sis6326 cards
Patch21:	XFree86-sis.patch
Patch22:	XFree86-xfsftfontdir.patch
Patch23:	XFree86-cyrix.patch
Patch24:	ftp://ftp.dcs.ed.ac.uk/pub/jec/programs/xfsft/xfsft-1.1.6-1.1.7.patch
Patch25:	XFree86-3dfxalpha.patch
Patch26:	XFree86-xlib_netscape_fix.patch
Patch27:	XFree86-sparc.patch.bz2
Patch28:	XFree86-enable810.patch
Patch29:	XFree86-5480mem.patch
Patch30:	XFree86-ragemobility.patch
Patch31:	XFree86-xterm_VT100_translations.patch

BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	zlib-devel
BuildRequires:	utempter-devel
BuildRequires:	tcl-devel
BuildRequires:	kernel-headers(agpgart)
Requires:	pam
Requires:	xauth
Requires:	util-linux
Requires:	cpp
Exclusivearch:	%{ix86} alpha sparc m68k armv4l
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch sparc
Obsoletes:	X11R6.1
%endif

%define		_fontdir	/usr/share/fonts
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
If you want to install the X Window System (TM) on your machine,
you'll need to install XFree86. The X Window System provides the base
technology for developing graphical user interfaces. Simply stated, X
draws the elements of the GUI on the user's screen and builds methods
for sending user interactions back to the application. X also supports
remote application deployment--running an application on another
computer while viewing the input/output on your machine. X is a
powerful environment which supports many different applications, such
as games, programming tools, graphics programs, text editors, etc.
XFree86 is the version of X which runs on Linux, as well as other
platforms. This package contains the basic fonts, programs and
documentation for an X workstation. However, this package doesn't
provide the program which you will need to drive your video hardware.
To control your video card, you'll need the particular X server
package which corresponds to your computer's video card.

%description -l de
X-Windows ist eine voll funktionsfähige grafische Benutzeroberfläche
mit mehreren Fenstern, mehreren Clients und verschiedenen Arten von
Fenstern. Es kommt auf den meisten Unix-Plattformen zum Einsatz. Die
Clients lassen sich auch mit Hilfe anderer Fenstersysteme anzeigen.
Das X-Protokoll gestattet die Ausführung der Applikationen direkt auf
lokalen Rechnern oder über ein Netz und bietet große Flexibilität bei
Client-Server-Implementierungen.

%description -l fr
XFree86 est nécessaire pour installer le système X Window. Ce dernier
est l'interface graphique standarde sous Unix. X Window fournit les
primitives graphiques pour dessiner les éléments du GUI (Graphical
User Interface : Interface Utilisateur Graphique) ainsi que le
protocole X permettant aux applicatifs d'utiliser un serveur X distant
(exécution à distance d'une application graphique s'affichant sur
l'écran local). X Window est un environnement puissant supportant
différentes applications (jeux, outils de programmation, programmes
graphiques, éditeurs de texte, ...). XFree86 est la version libre du
système X Window pour Linux ainsi que pour d'autres systèmes Unix
libres (FreeBSD, NetBSD, OpenBSD, Hurd, ...) Ce package comprend les
polices de base, les programmes et la documention pour l'usage en tant
que station de travail. Ce package ne contient PAS le pilote graphique
(le serveur X) nécessaire pour utiliser votre carte vidéo. Pour celà,
il faudra installer un serveur X correspondant à votre carte. En plus
du serveur X correspondant, il sera nécessaire d'installer les
packages X11R6-contrib, Xconfigurator, XFree86-libs, ainsi
qu'éventuellement un package de polices.

%decription -l pl
X Window System jest graficznym interfejsem u¿ytkownika, cechuje siê
mo¿liwo¶ci± pracy w wielu oknach, z wieloma klientami i do tego w ró¿nych
wystrojach okien.:) Jest u¿ywany na wiêkszo¶ci platform sytemów Unix, a
klienci mog± byæ uruchamiani tak¿e pod innymi popularnymi systemami
okienkowymi. Protokó³ X pozwala na uruchamianie aplikacji zarówno z lokalnej
maszyny jak i poprzez sieæ - daj±c przez to elastyczn± implementacjê
architektury klient/serwer.

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
Group(pl):	X11/XFree86

%description modules
Modules with X servers extensions.

%description -l pl modules
Wspólne modu³y rozszerzeñ dla wszystkich X serwerów.

%package libs
Summary:	X Window System shared libraries
Summary(de):	X11R6 shared Libraries
Summary(es):	Bibliotecas dinámicas de funciones X11R6
Summary(ja):	X11R6 ¶¦Í­¥é¥¤¥Ö¥é¥ê (Xaw È´¤­)
Summary(pl):	Biblioteki wspó³dzielone X Window System
Summary(fr):	Bibliothèques partagées X11R6
Summary(wa):	Pårteyes lîvreyes di foncsions di X11R6
Group:		X11/XFree86
Group(pl):	X11/XFree86
Prereq:		grep
Prereq:		/sbin/ldconfig

%ifarch sparc
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
XFree86-libs contient les bibliothèques dynamiques utilisées par la
plupart des programmes X. Ces bibliothèques sont dans un package
séparé pour diminuer l'espace disque nécessaire pour lancer les
applications X sur une machine sans serveur X (par exemple, sur un
réseau).

%description -l pl libs
Pakiet zawieraj±cy podstawowe biblioteki dla programów kozystaj±cych z
systemu X Window. Wydzielony w celu oszczednosci miejsca, nie wp³ywa
na mo¿liwo¶ci pracy aplikacji X Windows poprzez np. sieæ. Nie
potrzebny dla komputerów nie posiadaj±cych X serwerów.

%description -l tr libs
Bu paket X programlarýnýn düzgün çalýþabilmeleri için gereken
kitaplýklarý içerir. Bunlar, X programlarýný (sunucu olsun olmasýn)
çalýþtýrmak için gerekli disk alanýný azaltmak için ayrý bir paket
olarak sunulmuþtur.

%package devel
Summary:	X11R6 headers and programming man pages
Summary(de):	X11R6 Headers und man pages für Programmierer
Summary(es):	Biblietecas estáticas, archivos de declaraciones y páginas de manual
Summary(fr):	Pages man de programmation
Summary(ja):	X11R6 ¥¹¥¿¥Æ¥£¥Ã¥¯¡¦¥é¥¤¥Ö¥é¥ê¡¢¥Ø¥Ã¥À¡¼¤È´ØÏ¢¤¹¤ë man ¥Ú¡¼¥¸
Summary(pl):	Pliki nag³ówkowe dla X11R6
Summary(tr):	X11R6 ile geliþtirme için gerekli dosyalar
Summary(wa):	Lîvreyes statikes, fitchîs *.h eyèt pådjes di man pol programåcion
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name}-libs = %{version}
%ifarch sparc
Obsoletes:	X11R6.1-devel
%endif

%description devel
XFree86-devel includes the libraries, header files and documentation
you'll need to develop programs which run in X clients. XFree86
includes the base Xlib library as well as the Xt and Xaw widget sets.

%description -l de devel
Libraries, Header-Dateien und Dokumentation zum Entwickeln von
Programmen, die als X-Clients laufen. Enthält die Xlib-Library und die
Widget-Sätze Xt und Xaw. Information zum Programmieren mit diesen
Libraries finden Sie in der Buchreihe zur X-Programmierung von
O'Reilly and Associates.

%description -l fr devel
XFree86-devel comprends les bibliothèques, les fichiers d'en-tête et
la documentation nécessaire pour programmer des clients X Window.
XFree86 comprend les bibliothèque xlib et Xt (intrinsics) ainsi que
les widgets Xaw.

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
Group(pl):	X11/Biblioteki
Requires:	%{name}-devel = %{version}

%ifarch sparc
Obsoletes:	X11R6.1-devel
%endif

%description static
X11R6 static libraries.

%description -l pl static
Biblioteki sytatyczne do X11R6.

%package XF86Setup
Summary:	Graphical configuration tool for XFree86
Summary(de):	GUI-Konfigurationstool für X
Summary(es):	Programa gráfico de configuración de X11
Summary(fr):	Utilitaire de configuration graphique de X11
Summary(pl):	Graficzny konfigurator dla XFree86
Summary(wa):	Usteye grafike po-z apontyî li sistinme X11
Group:		X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-VGA16 = %{version}
Requires:	twm

%description XF86Setup
XF86Setup is a graphical user interface configuration tool for setting
up and configuring XFree86 servers. XF86Setup can configure video
settings, keyboard layouts, mouse types, etc. XF86Setup can't be used
with non-VGA compatible video cards, with fixed-frequency monitors, or
with OS/2.

%description -l fr XF86Setup
XF86Setup est une interface graphique permettant de configurer XFree86
: paramètres vidéo, clavier, type de souri, ... XF86Setup ne peut être
utilisé avec une carte non compatible VGA, ou utilisant des fréquences
vidéos fixes, ou avec OS/2.

%description -l pl XF86Setup
Graficzny konfigurator dla XFree86

%package S3
Summary:	The XFree86 server for video cards based on the S3 chip
Summary(de):	XFree86 S3 Server
Summary(es):	Servidor de XFree86 para tarjetas video S3
Summary(fr):	Serveur XFree86 pour S3
Summary(ja):	XFree86 S3 ¥µ¡¼¥Ð
Summary(pl):	XFree86 serwer dla kart S3
Summary(tr):	XFree86 S3 sunucularý
Summary(wa):	Sierveu di XFree86 po les cåtes videyo avou des chips S3
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description S3
XFree86-S3 is the X server for video cards based on S3 chips,
including most #9 cards, many Diamond Stealth cards, Orchid
Farenheits, Mirco Crystal 8S, most STB cards, and some motherboards
with built-in graphics accelerators (such as the IBM ValuePoint line).
Note that if you have an S3 ViRGE based video card, you'll need
XFree86-S3V instead of XFree86-S3.

%description -l de S3
X-Server für Steckkarten mit dem S3-Chipsatz (inkl. den meisten
#9-Karten), Karten wie Diamond Stealth, Orchid Farenheit und Mirco
Crystal 8S, den meisten STB-Karten sowie einigen Motherboards mit
integrierten Grafikbeschleunigern (z.B. die Reihe IBM ValuePoint).

%description -l fr S3
XFree86-S3 est le serveur X capable de piloter les cartes à base de
puces S3: la majorité des cartes #9, beaucoup de cartes Diamond
Stealth, Orchid Farenheits, Mirco Crystal 8S, la plupart des cartes
STB et certaines cartes mères comprenant un accélérateur graphique
intégré. Note : si votre carte est à base de S3 ViRGE, le serveur
XFree86-S3V doit être installé à la place de XFree86-S3.

%description -l pl S3
X serwer dla kart opartych na uk³adzie S3 - s± ta m.in. #9, wiele kart
Diamond Stealth, Orchid Farenheits, Mirco Crystal 8S, wiêkszo¶c kart
STB a tak¿e niektóre p³yty g³ówne z wbudowanymi akcelatorami
graficznymi (jak np. ValuePoint IBM'a).

%description -l tr S3
S3 tabanlý ekran kartlarý için sunucular. Çoðu #9, Diamond Stealth,
Orchid Fahrenheit, Mirco Crystal 8S, çoðu STB ve bazý anakarta
tümleþik grafik hýzlandýrýcýlar bu gruba girer. S3 Virge sunucusu ayrý
bir pakette yer alýr.

%package I128
Summary:	The XFree86 server for #9 Imagine 128 video cards
Summary(de):	XFree86 #9 Imagine 128 Server
Summary(es):	Servidor Number9 Imagine 128 de XFree86
Summary(ja):	XFree86 #9 Imagine 128 ¥µ¡¼¥Ð
Summary(fr):	Serveur Xfree86 pour #9 Imagine 128
Summary(pl):	XFree86 serwer dla kart Number Nine Imagine 128
Summary(tr):	XFree86 #9 Imagine 128 sunucusu
Summary(wa):	Sierveu Number9 Imagine 128 di XFree86
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description I128
This is the X server for the #9 Imagine 128 and similar video boards.

%description -l de I128
X-Server für die Steckkarte #9 Imagine 128

%description -l fr I128
Il s'agit du serveur X pour cartes #9 Imagine 128.

%description -l pl I128
X serwer do kart #9 Imagine 128.

%description -l tr I128
#9 Imagine kartý için X sunucusu.

%package S3V
Summary:	The XFree86 server for video cards based on the S3 Virge chip
Summary(de):	Xfree86 S3 Virge-Server
Summary(es):	Servidor de XFree86 para tarjetas video a base de S3 Virge
Summary(fr):	Serveur XFree86 pour S3 Virge
Summary(ja):	XFree86 S3 Virge ¥µ¡¼¥Ð
Summary(pl):	XFree86 serwer dla kart S3 Virge
Summary(tr):	XFree86 S3 Virge sunucusu
Summary(wa):	Sierveu di XFree86 po les cåtes videyo avou des S3 Virge
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description S3V
XFree86-S3V is the X server for video cards based on the S3 ViRGE
chipset.


%description -l de S3V
X-Server für Grafikkarten mit dem S3 Virge-Chipsatz.

%description -l fr S3V
Il s'agit du serveur X pour les cartes S3 ViRGE.

%description -l pl S3V
X serwer dla kart opartych na S3 Virge.

%description -l tr S3V
XFree86 S3 Virge sunucusu.

%package Mach64
Summary:	The XFree86 server for Mach64 based video cards
Summary(de):	Xfree86 Mach64-Server
Summary(fr):	Serveur Mach64 de XFree86
Summary(ja):	XFree86 Mach64 ¥µ¡¼¥Ð
Summary(pl):	XFree86 serwer dla kart Mach64
Summary(tr):	XFree86 Mach64 sunucusu
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description Mach64
XFree86-Mach64 is the server package for cards based on ATI's Mach64
chip, such as the Graphics Xpression, GUP Turbo, and WinTurbo cards.
Note that this server is known to have problems with some Mach64
cards.

%description -l de Mach64
X-Server für ATI Mach64-Karten wie Graphics Xpression, GUP Turbo, und
WinTurbo. Dieser Server verursacht gelegentlich Probleme mit
Mach64-Karten, die aber von einer neueren Version von XFree86 (der als
Beta-Version verfügbar ist) gelöst werden könnten.

%description -l fr Mach64
Il s'agit du serveur X pour les cartes ATI Mach64 comme les cartes
Graphics Xpression, GUP Turbo, et WinTurbo. Attention : ce serveur ne
reconnait pas toutes les cartes Mach64.

%description -l pl Mach64
X serwer dla kart opartych na uk³adzie ATI Mach64 jak np. Graphics
Xpression, GUP Turbo, a tak¿e WinTurbo. Serwer jest znany z problemów
z niektórymi kartami Mach64, które jednak mog± byæ ju¿ poprawione w
nowszej wersji XFree86 (osi±galna wy³±cznie jako wersja BETA).

%description -l tr Mach64
ATI Mach64 tabanlý kartlar için X sunucusu. Graphics Xpression, GUP
Turbo ve WinTurbo gibi kartlarý destekler. Bazý Mach64 kartlarýn yeni
XFree86 ile sorun yaþadýklarý bilinmektedir.

%package Sun
Summary:	X server for Suns with monochrome and 8-bit color SBUS framebuffers
Summary(de):	Xfree86 Sun SBUS 8-bit-Server
Summary(es):	Servidor de XFree86 para Suns con framebuffer SBUS 8bit
Summary(fr):	Serveur Sun SBUS 8-bit de XFree86
Summary(pl):	X Serwer mono i 8-bit do Sun-ów z karatami SBUS (framebuffer)
Summary(tr):	XFree86 Sun SBUS 8-bit sunucusu
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-fonts = %{version}
Obsoletes:	X11R6.1-Sun

%description Sun
To run X Windows programs requires an X server for your specific
hardware. This package includes the X server for Sun computers with
monochrome and 8-bit color SBUS framebuffers.

%description -l fr Sun
Il s'agit du serveur X pour les machines Sun supportant le SBUS
framebuffers monochrome et 256 couleurs, comme les CG3 et CGSIX.

%description -l pl Sun
Aby uruchomiæ X Window System potrzebujesz X serwera dostosowanego do
Twojego sprzêtu. Ten pakiet zawiera X serwer dla komputerów firmy Sun
z monochromatycznymi lub te¿ 8-bitowymi kolorowymi framebufferami
SBUS.

%package SunMono
Summary:	X server for Sun computers with monochrome SBUS framebuffers only
Summary(de):	Xfree86 Sun SBUS mono-Server
Summary(es):	Servidor Sun SBUS monocromo de XFree86
Summary(fr):	Serveur Sun SBUS mono de XFree86
Summary(pl):	Serwer XFree86 Sun (tylko dla monitorów monochromatycznych)
Summary(tr):	XFree86 Sun SBUS mono sunucusu
Summary(wa):	Sierveu Sun SBUS è monocrome di XFree86
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-fonts = %{version}
Obsoletes:	X11R6.1-SunMono

%description SunMono
To run X Windows programs requires an X server for your specific
hardware. This package includes the X server for Sun computers with
monochrome SBUS framebuffers only.

%description -l fr SunMono
Il s'agit du serveur X pour les machines Sun utilisant un SBUS
framebuffers monochrome.

%description -l pl SunMono
Aby uruchomiæ X Window System potrzebujesz X serwera dostosowanego do
Twojego sprzêtu. Ten pakiet zawiera X serwer dla komputerów firmy Sun
z wy³±cznie monochromatycznymi framebufferami SBUS.

%package Sun24
Summary:	X server for Suns with all supported SBUS framebuffers
Summary(de):	Xfree86 Sun SBUS-Server
Summary(es):	Servidor de XFree86 para todo tipo de framebuffer SBUS de Sun
Summary(fr):	Serveur Sun SBUS de XFree86
Summary(pl):	Serwer XFree86 Sun (dla wszystkich SBUS framebufferów)
Summary(tr):	XFree86 Sun SBUS sunucusu
Summary(wa):	Sierveu di XFree86 po tots les framebuffers SBUS des Sun
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-fonts = %{version}
Obsoletes:	X11R6.1-Sun24

%description Sun24
The XFree86-Sun24 package contains the X server for Sun computers with
all supported SBUS framebuffers.

%description -l fr Sun24
Il s'agit du serveur X pour les machines Sun supportant le SBUS
framebuffers.

%description -l pl Sun24
Aby uruchomiæ X Window System potrzebujesz X serwera dostosowanego do
Twojego sprzêtu. Ten pakiet zawiera X serwer dla komputerów firmy Sun
dla wszystkich wspieranych framebufferów SBUS.

%package Xvfb
Summary:	A virtual framebuffer X Windows System server for XFree86
Summary(de):	X-Server für virtuelle Framebuffer
Summary(es):	Servidor de XFree86 para framebuffers virtuales
Summary(fr):	Serveur X virtuel
Summary(ja):	XFree86 Xvfb ¥µ¡¼¥Ð
Summary(pl):	Serwer XFree86 Xvfb
Group:		X11/XFree86/Servers
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


%description -l fr Xvfb
Xvfb (X Virtual Frame Buffer) est un serveur X générique exploitant un
frame buffer virtuel pour les machines sans dispositif d'affichage. Il
n'utilise aucun périphérique mais agit comme un affichage X. Il ne
doit être utilisé qu'à des fins de test (nombre de couleurs ou
résolutions "étranges", traitement en tâche de fonds, test de montée
en charge, aide au portage d'un serveur X sur une nouvelle
plate-forme, utilisation d'applications ne nécessitant pas réellement
X mais l'utilisant, ...).

%package 3DLabs
Summary:	XFree86 3DLabs server
Summary(de):	XFree86 3DLabs Server
Summary(es):	Servidor 3DLabs de XFree86
Summary(fr):	Serveur XFree86 pour 3DLabs
Summary(tr):	XFree86 3DLabs sunucusu
Summary(pl):	Serwer XFree86 3DLabs
Summary(wa):	Sierveu 3DLabs di XFree86
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description 3DLabs
X server for cards built around 3D Labs GLINT and Permedia chipsets,
including GLINT 500TX with IBM RGB526 RAMDAC, GLINT MX with IBM RGB526
and IBM RGB640 RAMDAC, Permedia with IBM RGB526 RAMDAC and the
Permedia 2 (classic, 2a, 2v).

%description -l pl 3DLabs
XFree86 3DLabs server.

%package Xnest
Summary:	A nested XFree86 server
Summary(de):	Vernesteter XFree86-Server
Summary(fr):	Sous-serveur X
Summary(pl):	Serwer XFree86 Xnest
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description Xnest
Xnest is an X Window System server which runs in an X window. Xnest is
a 'nested' window server, actually a client of the real X server,
which manages windows and graphics requests for Xnest, while Xnest
manages the windows and graphics requests for its own clients.

%description -l fr Xnest
Il s'agit d'un serveur X tournant par dessus un autre serveur. Seuls
les testeurs devraient l'installer.

%package Xptr
Summary:	X print server
Summary(pl):	X print server
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description Xptr
Xprt provides an X server with the print extension and special DDX
implementation.

%package 8514
Summary:	The XFree86 server program for older IBM 8514 or compatible video cards
Summary(de):	XFree86 8514 Server
Summary(fr):	serveur 8514 pour XFree86.
Summary(ja):	XFree86 8514 ¥µ¡¼¥Ð
Summary(pl):	XFree86 serwer dla kart 8514
Summary(tr):	XFree86 8514 sunucusu
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description 8514
If you are installing the X Window System and the video card in your
system is an older IBM 8514 or a compatible from a company such as
ATI, you should install XFree86-8514.

%description -l fr 8514
Il s'agit du serveur X pour les anciennes cartes IBM 8514 ou
compatibles (comme celles d'ATI).

%description -l pl 8514
X serwer dla starszych kart IBM 8514 oraz kompatybilnych robionych
przez inne firmy takie jak np. ATI.

%description -l tr 8514
Eski IBM 8514 ve uyumlu kartlar (ATI gibi) için sunucu.

%package AGX
Summary:	The XFree86 server for AGX-based video cards
Summary(de):	XFree86 AGX Server
Summary(es):	Servidor de XFree86 para tarjetas AGX
Summary(fr):	serveur AGX pour XFree86.
Summary(ja):	XFree86 AGX ¥µ¡¼¥Ð
Summary(pl):	XFree86 serwer dla kart AGX
Summary(tr):	XFree86 AGX sunucusu
Summary(wa):	Sierveu di XFree86 po les cåtes videyo avou des chips AGX
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description AGX
This is the X server for AGX-based cards, such as the Boca Vortex,
Orchid Celsius, Spider Black Widow and Hercules Graphite.

%description -l de AGX
X-Server für Karten auf AGX-Basis wie etwa Boca Vortex, Orchid
Celsius, Spider Black Widow und Hercules Graphite.

%description -l fr AGX
Il s'agit du serveur X pour les cartes à base d'AGX comme les Boca
Vortex, Orchid Celsius, Spider Black Widow et Hercules Graphite.

%description -l tr AGX
Boca Vortex, Orchid Celsius, Spider Black Widow ve Hercules Graphite
gibi AGX tabanlý kartlar için X sunucusu.

%package FBDev
Summary:	The X server for the generic frame buffer device on some machines
Summary(de):	X-Server für framebuffer-Devices
Summary(es):	Servidor para los framebuffers genéricos de ciertas máquinas
Summary(fr):	Serveur XFree86 pour framebuffer
Summary(pl):	XFree86/86 FBDev server
Summary(wa):	Sierveu po les framebuffers ki chinèt bén tot di sacwantès éndjoles
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description FBDev
X server for the generic frame buffer device used on the Amiga, Atari
and Macintosh/m68k machines. Support for Intel and Alpha architectures
is now included in the Linux 2.2 kernel as well.

%description -l fr FBDev
FBDev est le serveur générique utilisant les frame buffer, utilisé sur
Amiga, Atari et les anciens Macintosh à base de m68k. Le support pour
les machines à base d'Alpha et de ix86 a été inclus dans le noyau 2.2

%description -l pl FBDev
X serwer wspieraj±cy frame buffera dla Amigi, Atari i Macintosha
/m68k. Wsparcie dla platform Intel i Alpha jest w j±drze systemu.

%package Mach32
Summary:	The XFree86 server for Mach32 based video cards
Summary(de):	Xfree86 Mach32-Server
Summary(fr):	Serveur XFree86 pour Mach32
Summary(ja):	XFree86 Mach32 ¥µ¡¼¥Ð
Summary(pl):	XFree86 serwer dla kart Mach32
Summary(tr):	XFree86 Mach32 sunucusu
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description Mach32
XFree86-Mach32 is the X server package for video cards built around
ATI's Mach32 chip, including the ATI Graphics Ultra Pro and Ultra
Plus.

%description -l de Mach32
X-Server für Karten auf der Basis des ATI Mach32-Chip, einschließlich
ATI Graphics Ultra Pro und Ultra Plus.

%description -l fr Mach32
Serveur X pour les cartes utilisant le circuit ATI Mach32, dont les
cartes ATI Graphics Ultra Pro et Ultra Plus.

%description -l pl Mach32
X serwer dla kart zbudowanych na uk³adzie ATI Mach32 w³±czaj±c w to
ATI Graphics Ultra Pro oraz Ultra Plus.

%description -l tr Mach32
ATI Mach32 tabanlý ATI Graphics Ultra Pro ve Ultra Plus kartlarý için
X sunucusu.

%package Mach8
Summary:	The XFree86 server for Mach8 video cards
Summary(de):	XFree86 Mach8 Server
Summary(es):	Servidor Mach8 de XFree86
Summary(fr):	Serveur Mach8 pour XFree86
Summary(ja):	XFree86 Mach8 ¥µ¡¼¥Ð
Summary(pl):	XFree86 serwer dla kart Mach8
Summary(tr):	XFree86 Mach8 sunucusu
Summary(wa):	Sierveu Mach8 di XFree86
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description Mach8
XFree86-Mach 8 is the X server for video cards built around ATI's
Mach8 chip, including the ATI 8514 Ultra and Graphics Ultra.

%description -l de Mach8
X-Server für Karten auf der Basis des ATI Mach8-Chips, einschließlich
des ATI 8514 Ultra und des Graphics Ultra.

%description -l fr Mach8
Serveur X pour les cartes basées sur les chips ATI Mach8, dont les
cartes ATI 8514 Ultra et Graphics Ultra.

%description -l pl Mach8
X serwer dla kart opartych na uk³adzie ATI Mach8, w³±czaj±c w to ATI
8514 Ultra oraz graphics Ultra.

%description -l tr Mach8
ATI 8514 Ultra ve Graphics Ultra gibi ATI Mach8 tabanlý kartlar için X
sunucusu.

%package Mono
Summary:	A generic XFree86 monochrome server for VGA cards
Summary(de):	Xfree86 Mono-Server
Summary(es):	Servidor genérico para tarjetas monocromes o VGA
Summary(fr):	Serveur Monochrome de XFree86
Summary(ja):	XFree86 ¥â¥Î¥¯¥í¡¦¥µ¡¼¥Ð
Summary(pl):	XFree86 serwer dla kart Monochromatycznych
Summary(tr):	XFree86 Mono sunucusu
Summary(wa):	Sierveu ki chine bén tot po cåtes monocrome ou VGA
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description Mono
XFree86-Mono is a generic monochrome (2 color) server for VGA cards.
XFree86-Mono will work for nearly all VGA compatible cards, but will
only support a monochrome display.

%description -l de Mono
Generischer monochromer (Schwarzweiß-) Server für VGA-Karten, der
praktisch mit allen VGA-ähnlichen Karten mit beschränkter Auflösung
funktioniert.

%description -l fr Mono
XFree86-Mono est un serveur générique monochrome (2 couleurs) pour les
cartes VGA. Il fonctionnera avec quasiment toutes les cartes VGA mais
n'affichera qu'en noir et blanc.

%description -l pl Mono
Dwu kolorowy (monochromatyczny) serwer dla kart VGA, pracuje na
wszystkich typu VGA w ograniczonej rozdzielczo¶ci.

%description -l tr Mono
Mono (2 renk) VGA kartlarý için genel X sunucusu. Kýsýtlý bir
çözünürlük altýnda birçok VGA kart ile çalýþýr.

%package P9000
Summary:	The XFree86 server for P9000 cards
Summary(de):	XFree86 P9000 Server
Summary(es):	Servidor XFree86 para tarjetas a base de P9000
Summary(fr):	Serveur XFree86 pour P9000
Summary(ja):	XFree86 P9000 ¥µ¡¼¥Ð
Summary(pl):	XFree86 serwer dla kart P9000
Summary(tr):	XFree86 P9000 sunucusu
Summary(wa):	Sierveu di XFree86 po les cåtes avou des chips P9000
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description P9000
XFree86-P9000 is the X server for video cards built around the Weitek
P9000 chip, such as most Diamond Viper cards and the Orchid P9000
card.

%description -l de P9000
X-Server für Karten auf Basis des Weitek P9000-Chip, wie die meisten
Diamond Viper und Orchid P9000-Karten.

%description -l fr P9000
XFree86-P9000 est le serveur X pour les cartes construites avec une
puce Weitek P9000 comme les cartes Diamond Viper et Orchid P9000.

%description -l pl P9000
X serwer dla kart zbudowanych na uk³adzie Weitek P9000 czyli w
wiêkszo¶ci karty Diamond Viper oraz Orchid P9000.

%description -l tr P9000
Diamond Viper ve Orchid P9000 gibi Weitek P9000 tabanlý kartlar için X
sunucusu.

%package SVGA
Summary:	An XFree86 server for most simple framebuffer SVGA devices
Summary(de):	XFree86 SVGA-Server
Summary(es):	Servidor de XFree86 para tarjetas SVGA simples
Summary(fr):	Serveur XFree86 pour SVGA
Summary(ja):	XFree86 SVGA ¥µ¡¼¥Ð
Summary(pl):	XFree86 serwer dla kart SVGA
Summary(tr):	XFree86 SVGA sunucusu
Summary(wa):	Sierveu di XFree86 po simpes cåtes SVGA
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description SVGA
X server for most simple framebuffer SVGA devices, including cards
built from ET4000 chips, Cirrus Logic chips, Chips and Technologies
laptop chips, Trident 8900 and 9000 chips, and Matrox chips. It works
for Diamond Speedstar, Orchid Kelvins, STB Nitros and Horizons, Genoa
8500VL, most Actix boards, the Spider VLB Plus, etc. It also works for
many other chips and cards, so try this server if you are having
problems.

%description -l de SVGA
X-Server für die elementarsten Framebuffer-SVGA-Geräte, einschließlich
Karten, die aus ET4000-Chips, Cirrus Logic-Chips, Chips and
Technologies Laptop-Chips sowie Trident 8900 und 9000 Chips gebaut
sind. Funktioniert mit Diamond Speedstar, Orchid Kelvins, STB Nitros
und Horizons, Genoa 8500VL, den meisten Actix-Karten sowie Spider VLB
Plus und außerdem mit vielen anderen Chips und Karten. Es lohnt sich,
diesen Server auszuprobieren, wenn Sie Probleme haben.

%description -l fr SVGA
Il s'agit du serveur X pour la plupart des cartes SVGA disposant d'un
framebuffer (c'est-à-dire toutes les cartes compatibles VESA 2, donc
quasiment toutes les cartes construites depuis 1994): cartes à base de
ET4000, Cirrus Logic, Chips and Technologies, Trident 8900 et 9000, et
Matrox. Il fonctionne également avec les cartes Diamond Speedstar,
Orchid Kelvins, STB Nitros et Horizons, Genoa 8500VL, la plupart des
cartes Actix, laSpider VLB Plus, ... Il fonctionne aussi pour de
nombreuses autres cartes, aussi essayez ce pilotes si vous rencontrez
des difficultés.

%description -l pl SVGA
X serwer dla wiêkszo¶ci prostych kart SVGA, w³±czaj±c karty zbudowane
na uk³adach ET4000, Cirrus Logic, Trident 8900 i 9000, oraz uk³ady
wystêpuj±ce w laptopach. Dzia³a tak¿e z kartami Diamnod Speedstar,
Orchid Kelvins, STB Nitros i Horizons, Genoa 8500VL, wiêkszo¶æ Actix,
Spider VLB Plus. Dzia³a równie¿ na wielu innych kartach opartych na
innych uk³adach wiêc spróbuj ten serwer je¶li masz jakie¶ problemy.

%description -l tr SVGA
ET4000, Cirrus Logic, Chips and Technologies dizüstü, Trident 8900 ve
9000 gibi basit 'framebuffer' SVGA kullananan kartlar için X sunucusu.
Ayný zamanda Diamond Speedstar, Orchid Kelvins, STB Nitros / Horizons,
Genoa 8500VL, çoðu Actix kartlarý, Spider VLB Plus gibi kartlar ve
birçok diðer kart ile de çalýþýr. Herhangi bir sorun yaþarsanýz bu
sunucuyu deneyin.

%package VGA16
Summary:	A generic XFree86 server for VGA16 boards
Summary(de):	XFree86 VGA16-Server
Summary(es):	Servidor de XFree86 para tarjetas en modo VGA 16 colores
Summary(fr):	Serveur XFree86 pour VGA16
Summary(ja):	XFree86 VGA16 ¥µ¡¼¥Ð
Summary(pl):	XFree86 serwer dla kart CGA16
Summary(tr):	XFree86 VGA16 sunucusu
Summary(wa):	Sierveu di XFree86 po cåtes è môde VGA è 16 coleurs
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description VGA16
XFree86-VGA16 is a generic 16 color server for VGA boards.
XFree86-VGA16 will work on nearly all VGA style graphics boards, but
will only support a low resolution, 16 color display.

%description -l de VGA16
Generischer 16-Farben-Server für VGA-Karten. Funktioniert auf fast
allen VGA- Grafikkarten, allerdings nur bei geringer Auflösung und
wenigen Farben.

%description -l fr VGA16
XFree86-VGA16 est un serveur générique en 16 couleurs pour les cartes
VGA. XFree86-VGA16 fonctionnera sur quasiment toutes les cartes VGA
mais ne supportera qu'une résolution de 4 bits (16 couleurs).

%description -l pl VGA16
Podstawowy serwer dla 16 kolorowego trybu pracy kart VGA. Dzia³a ze
wszystkimi kartami VGA ale jedynie w niskiej rozdzielczo¶ci i ma³ej
ilo¶ci kolorów.

%description -l tr VGA16
VGA kartlarý için genel 16 renk sunucusu. Çoðu VGA tipi kart ile düþük
renk ve çözünürlükte çalýþýr.

%package W32
Summary:	The XFree86 server for video cards based on ET4000/W32 chips
Summary(de):	XFree86 W32 Server
Summary(es):	Servidor de XFree86 para tarjetas a base de ET4000/W32
Summary(fr):	Serveur XFree86 pour W32
Summary(pl):	XFree86 serwer dla kart W32
Summary(tr):	XFree86 W32 sunucusu
Summary(wa):	Sierveu di XFree86 po cåtes avou des chips ET4000/W32
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description W32
XFree86-W32 is the X server for cards built around ET4000/W32 chips,
including the Genoa 8900 Phantom 32i, the Hercules Dynamite, the
LeadTek WinFast S200, the Sigma Concorde, the STB LightSpeed, the
TechWorks Thunderbolt, and the ViewTop PCI.

%description -l de W32
Genoa 8900 Phantom 32I, Hercules Dynamite, LeaTek WinFast S200, Sigma
Concorde, STB LightSpeed, TechWorks Thunderbolt und ViewTop PCI.

%description -l fr W32
XFree86-W32 est le serveur X pour les cartes construites avec une puce
ET4000/W32 : Genoa 8900 Phantom 32i,Hercules Dynamite, LeadTek WinFast
S200, Sigma Concorde, STB LightSpeed, TechWorksThunderbolt et la
ViewTop PCI.

%description -l pl W32
X serwer dla kart zbudowanych na uk³adzie ET4000/W32, w³±czaj±c w to
karty Genoa 8900 Phantom 32i, Hercules Dynamite, LeadTek WinFast S200,
Sigma Concorde, STB LightSpeed, TechWorks Thunderbolt oraz karty
ViewTop (PCI).

%description -l tr W32
Genoa 8900 Phantom 32i, Hercules Dynamite kartlarý, LeadTek WinFast
S200, Sigma Concorde, STB LightSpeed, TechWorks Thunderbolt, ve
ViewTop PCI gibi kartlarýn kullandýðý ET4000/W32 tabanlý kartlar için
X sunucusu.

%package TGA
Summary:	XFree86 TGA server
Summary(de):	XFree86 Digital TGA (DC21040) Server
Summary(es):	Servidor de XFree86 para tarjetas TGA de Digital (chips DC21040)
Summary(fr):	Serveur XFree86 pour Digital TGA (DC21040)
Summary(pl):	XFree86 serwer dla kart TGA
Summary(tr):	XFree86 Digital TGA (DC21040) sunucusu
Summary(wa):	Sierveu di XFree86 po cåtes TGA di Digital (chips DC21040)
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-fonts = %{version}

%description TGA
The XFree86-TGA package contains an 8-bit X server for Digital TGA
boards based on the DC21040 chip. These adapters are very popular in
Alpha workstations and are included with Alpha UDB (Multia) machines.

%description -l fr TGA
XFree86-TGA est un serveur 8 bits pour les cartes Digital TGA basées
sur la puce DC21040. Ces cartes sont répandues sur les stations Alpha
et sont incluses dans les Alpha UDN (Multia).

%package -n sessreg
Summary:	sessreg - manage utmp/wtmp entries for non-init clients
Group:		X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-libs = %{version}

%description -n sessreg
Sessreg is a simple program for managing utmp/wtmp entries for xdm
sessions.

System V has a better interface to /var/run/utmp than BSD; it
dynamically allocates entries in the file, instead of writing them at
fixed positions indexed by position in /etc/ttys.

%package -n xdm
Summary:	XDM
Summary(pl):	XDM
Group:		X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name} = %{version}
Requires:	pam >= 0.66
Requires:	rc-scripts >= 0.2.0
Requires:	sessreg = %{version}
Requires:	/usr/X11R6/bin/sessreg
Provides:	XDM
Prereq:		chkconfig
Obsoletes:	XFree86-xdm
Obsoletes:	gdm
Obsoletes:	kdm

%description -n xdm
X Display Manager.

%package -n twm
Summary:	Tab Window Manager for the X Window System
Summary(pl):	Twm - podstawowy zarz±dca okien dla X Window System
Group:		X11/Window Managers/Tools
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien/Narzêdzi

%description -n twm
Twm is a window manager for the X Window System. It provides
titlebars, shaped windows, several forms of icon management,
user-defined macro functions, click-to-type and pointerdriven keyboard
focus, and user-specified key and pointer button bindings.

%package -n xfs
Summary:	Font server for XFree86
Summary(de):	Font-Server für XFree86
Summary(es):	Servidor de tipos de letra de XFree86
Summary(fr):	Serveur de polices de XFree86
Summary(pl):	Serwer fontów do XFree86
Summary(wa):	Sierveu de fontes di XFree86
Group:		X11/XFree86
Group(pl):	X11/XFree86
Requires:	rc-scripts >= 0.2.0
Obsoletes:	xfsft XFree86-xfs
Provides:	XFree86-xfs

%description -n xfs
This is a font server for XFree86. You can serve fonts to other X
servers remotely with this package, and the remote system will be able
to use all fonts installed on the font server, even if they are not
installed on the remote computer.

%description -l fr -n xfs
xfs est un serveur de polices pour XFree86, en local ou à distance. Le
système distant peut utiliser ces fontes même s'il ne les possède pas.

%package -n xauth
Summary:	XAuth
Group:		X11/XFree86
Group(pl):	X11/XFree86
Summary(pl):	XAuth

%description -n xauth

%package fonts
Summary:	XFree86 Fonts
Summary(pl):	Fonty dla systemu XFree86
Group:		X11/XFree86
Group(pl):	X11/XFree86
Prereq:		%{_bindir}/mkfontdir

%description fonts
This package contains the basic fonts. This package is required when
you have installed X server.

%description -l pl fonts
Pakiet ten zawiera podstawowe fonty. Pakiet ten jest koniecznie
potrzebny wtedy kiedy masz zainstalowany jakikolwiek X serwer.

%package 75dpi-fonts
Summary:	A set of 75 dpi resolution fonts for the X Window System
Summary(de):	X11RT 76 dpi-Fonts - nur auf Serverseite erforderlich
Summary(es):	Fuentes para X11 a 75 dpi - solo necesarias para el servidor X11
Summary(fr):	Fontes 75 dpi X11R6 - nécessaire uniquement côté serveur
Summary(ja):	X11R6 75dpi ¥Õ¥©¥ó¥È (¥µ¡¼¥ÐÂ¦¤Î¤ß¤ËÉ¬Í×¤Ç¤¹)
Summary(pl):	Fonty o rozdzielczo¶ci 75dpi-niebêdne dla serwera
Summary(tr):	X11R6 75dpi yazýtipleri - yalnýzca sunucu tarafýnda gerekir
Summary(wa):	Fontes po X11 di fintè 75 dpi - ahessåve seulmint pol sierveu X11
Group:		X11/XFree86
Group(pl):	X11/XFree86
Prereq:		%{_bindir}/mkfontdir

%ifarch sparc
Obsoletes:	X11R6.1-75dpi-fonts
%endif

%description 75dpi-fonts
XFree86-75dpi-fonts contains the 75 dpi fonts used on most X Window
Systems. If you're going to use the X Window System, you should
install this package, unless you have a monitor which can support 100
dpi resolution. In that case, you may prefer the 100dpi fonts
available in the XFree86-100dpi-fonts package.

%description -l de 75dpi-fonts
Die 75dpi-Fonts, die auf meisten Linux-Systemen verwendet werden. Für
Benutzer mit einer hochauflösender Darstellung sind die 100dpi-Fonts
eines getrennt erhältlichen Pakets besser geeignet.

%description -l fr 75dpi-fonts
XFree86-75dpi-fonts contient les polices taille 75 dpi utilisées sur
la plupart des systèmes X Window. Si vous vous voulez utiliser X
Window, il est vivement conseillé d'installer ce package à moins que
votre moniteur supporte de grandes résolutions auquel cas vous
préferrez les polices 100dpi contenues dans le package
XFree86-100dpi-fonts.

%description -l pl 75dpi-fonts
Pakiet ten zawiera fonty rastrowe 75dpi. W wypadku wiêkszej
rozdzielczo¶ci zalecane czcionki 100dpi s± dostêpne w osobnym
sk³adzie.

%description -l tr 75dpi-fonts
Çoðu Linux sisteminde 75dpi yazýtipi kullanýlýr. Yüksek çözünürlük
kullanan kullanýcýlar 100dpi yazýtiplerini yeðleyebilirler.

%package 100dpi-fonts
Summary:	X11R6 100dpi fonts - only need on server side
Summary(de):	X11R6 100dpi-Fonts - nur auf Server-Seite erforderlich
Summary(es):	Fuentes para X11 a 100 dpi - solo necesarias para el servidor X11
Summary(fr):	Fontes 100ppp pour X11R6 - nécessaires seulement coté serveur
Summary(ja):	X11R6 100dpi ¥Õ¥©¥ó¥È (¥µ¡¼¥ÐÂ¦¤Î¤ß¤ËÉ¬Í×¤Ç¤¹)
Summary(pl):	Fonty o rozdzielczosci 100dpi-niezbêdne dla serwera.
Summary(tr):	X11R6 100dpi yazýtipleri - yalnýzca sunucu tarafýnda gereklidir
Summary(wa):	Fontes po X11 di fintè 100 dpi - ahessåve seulmint pol sierveu X11
Group:		X11/XFree86
Group(pl):	X11/XFree86
Prereq:		%{_bindir}/mkfontdir

%ifarch sparc
Obsoletes:	X11R6.1-100dpi-fonts
%endif

%description 100dpi-fonts
If you're going to use the X Window System and you have a high
resolution monitor capable of 100 dpi, you should install
XFree86-100dpi-fonts. This package contains a set of 100 dpi fonts
used on most Linux systems.

%description -l de 100dpi-fonts
Die 100dpi-Schriftarten, die auf den meisten Linux-Systemen zum
Einsatz kommen. Anwender mit hochauflösenden Monitoren ziehen unter
Umständen die 100dpi-Schriften vor, die in einem separaten Paket
erhältlich sind.

%description -l fr 100dpi-fonts
Pour utiliser X Window sur des moniteurs haute résolution, ce package
devrait être installé car il apporte des polices haute définition
utilisées sur la plupart des systèmes Linux.

%description -l pl 100dpi-fonts
Pakiet ten zawiera fonty rastrowe 100dpi. Bed± one potrzebne przy
pracy z du¿± rozdzielczo¶ci±.

%description -l tr 100dpi-fonts
Yüksek çözünürlük kullanan kullanýcýlar 100dpi yazýtiplerini 75dpi
olanlara yeðleyebilirler.

%package cyrillic-fonts
Summary:	Cyrillic fonts - only need on server side
Summary(de):	X11R6 Cyrillic-Fonts - nur auf Server-Seite erforderlich
Summary(es):	Fuentes cirílicas para X11 - solo necesarias para el servidor X11
Summary(fr):	Fontes cyrillic pour X11R6 - nécessaires seulement coté serveur
Summary(pl):	Fonty ze znakami cyrylicy
Summary(tr):	X11R6 cyrillic yazytipleri - yalnyzca sunucu tarafynda gereklidir
Summary(wa):	Fontes cirilikes po X11 - ahessåve seulmint pol sierveu X11
Group:		X11/XFree86
Group(pl):	X11/XFree86
Prereq:		%{_bindir}/mkfontdir

%description cyrillic-fonts
The Cyrillic fonts. Those who use a language requiring the Cyrillic
character set should install this package.

%description -l fr cyrillic-fonts
Les fontes cyrilliques. Ceux qui utilisent les caractère cyrilliques
devraient installer ce package.

%description -l pl cyrillic-fonts
Fonty rastrowe czcionkami w cyrylicy.

%prep
%setup -q -c -a1 -a 2
tar x -C xc/lib -f xfsft-1.1.6/libfont.tar
patch -p0 -s -d xc/lib < xfsft-1.1.6/libfont.patch

# these replacement fonts.scale files have extra encodings
install xfsft-1.1.6/fonts.scale.Speedo xc/fonts/scaled/Speedo/fonts.scale
install xfsft-1.1.6/fonts.scale.Type1 xc/fonts/scaled/Type1/fonts.scale

%patch0  -p1
%patch1  -p1
%patch2  -p1
# the following patch is in CVS diff format, needs POSIXLY_CORRECT env var.
#export POSIXLY_CORRECT=1
#%patch3 -p1 -b .alpha-sockets
#unset POSIXLY_CORRECT
%patch4  -p1
%patch5  -p1
%patch6  -p1
%patch7  -p1
%patch8  -p1
%patch9  -p1
%patch10 -p1
%patch11 -p1
%patch12 -p0
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1 -R
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p0
%patch25 -p1
%patch26 -p1
%ifarch sparc sparc64
%patch27 -p1
%endif
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1

## Clean up to save a *lot* of disk space
find . -name "*.orig" -print | xargs rm -f
find . -size 0 -print | xargs rm -f

#--- %build --------------------------

%build
%{__make} -C xc World \
	"BOOTSTRAPCFLAGS=$RPM_OPT_FLAGS -fno-strict-aliasing" \
	"CDEBUGFLAGS=" "CCOPTIONS=$RPM_OPT_FLAGS -fno-strict-aliasing" \
	"CXXDEBUGFLAGS=" "CXXOPTIONS=$RPM_OPT_FLAGS -fno-strict-aliasing"

#--- %install ------------------------

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/X11/pl/app-defaults \
$RPM_BUILD_ROOT%{_sysconfdir}/{X11,pam.d,rc.d/init.d,sysconfig,security/console.apps} \
	$RPM_BUILD_ROOT/var/state/xkb \
	$RPM_BUILD_ROOT/usr/include \
	$RPM_BUILD_ROOT/usr/bin \
	$RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

%{__make} -C xc install install.man \
	"DESTDIR=$RPM_BUILD_ROOT" \
	"INSTBINFLAGS=-m 755" \
	"INSTPGMFLAGS=-m 755"

strip $RPM_BUILD_ROOT%{_bindir}/* || :
strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/{lib*.so.*.*,modules/*} || :

# setup the default X server
rm -f $RPM_BUILD_ROOT%{_bindir}/X
ln -s Xwrapper $RPM_BUILD_ROOT%{_bindir}/X

# Move config stuff to %{_sysconfdir}/X11

cp $RPM_BUILD_ROOT%{_libdir}/X11/XF86Config.eg \
$RPM_BUILD_ROOT%{_sysconfdir}/X11/XF86Config
ln -sf ../../../..%{_sysconfdir}/X11/XF86Config $RPM_BUILD_ROOT%{_libdir}/X11/XF86Config

# setting default X
rm -f $RPM_BUILD_ROOT%{_bindir}/X
ln -sf Xwrapper $RPM_BUILD_ROOT%{_bindir}/X

# setting ghost X in %{_sysconfdir}/X11 -- xf86config will fix this ...
ln -s ../..%{_bindir}/Xwrapper $RPM_BUILD_ROOT%{_sysconfdir}/X11/X

ln -sf ../../../..%{_sysconfdir}/X11/XF86Config \
$RPM_BUILD_ROOT%{_libdir}/X11/XF86Config

for i in xdm twm fs xsm xinit; do
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/X11/$i
	cp -ar $RPM_BUILD_ROOT%{_libdir}/X11/$i $RPM_BUILD_ROOT%{_sysconfdir}/X11
	rm -rf $RPM_BUILD_ROOT%{_libdir}/X11/$i
	ln -sf %{_sysconfdir}/X11/$i $RPM_BUILD_ROOT%{_libdir}/X11/$i
done

# add X11 links in /usr/bin and /usr/include
ln -s ../X11R6/include/X11 $RPM_BUILD_ROOT/usr/include/X11
ln -s ../X11R6/bin $RPM_BUILD_ROOT/usr/bin/X11

# make TrueType font dir, touch default .dir and .scale files
install	-d $RPM_BUILD_ROOT%{_fontdir}/TrueType
echo 0 > $RPM_BUILD_ROOT%{_fontdir}/TrueType/fonts.dir
echo 0 > $RPM_BUILD_ROOT%{_fontdir}/TrueType/fonts.scale

install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/xdm
install %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/xdm
install %{SOURCE5} $RPM_BUILD_ROOT/etc/rc.d/init.d/xfs
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/X11/fs/config
install %{SOURCE7} $RPM_BUILD_ROOT/etc/pam.d/xserver
install %{SOURCE8} $RPM_BUILD_ROOT%{_libdir}/X11/pl/app-defaults/XTerm
install %{SOURCE9} $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties/twm.desktop

install %{SOURCE10} $RPM_BUILD_ROOT/etc/sysconfig/xdm
install %{SOURCE11} $RPM_BUILD_ROOT/etc/sysconfig/xfs

touch $RPM_BUILD_ROOT/etc/security/console.apps/xserver
touch $RPM_BUILD_ROOT/etc/security/blacklist.xserver
touch $RPM_BUILD_ROOT/etc/security/blacklist.xdm

ln -sf %{_fontdir} $RPM_BUILD_ROOT%{_libdir}/X11/fonts

for n in libX11.so.6.1 libICE.so.6.3 libSM.so.6.0 libXext.so.6.3 libXt.so.6.0 \
	libXmu.so.6.0 libXaw.so.6.1 libXIE.so.6.0 libXi.so.6.0 \
	libXtst.so.6.1 libXxf86rush.so.1.0; do
	ln -sf $n $RPM_BUILD_ROOT%{_libdir}/`echo $n | sed "s/\.so.*/\.so/"`
done

# xkb 'compiled' files need to be in /var/state/xkb, so
# /usr is NFS / read-only mountable
install -d $RPM_BUILD_ROOT/var/state/xkb
cp -a $RPM_BUILD_ROOT%{_libdir}/X11/xkb/compiled/* \
	$RPM_BUILD_ROOT/var/state/xkb
rm -rf $RPM_BUILD_ROOT%{_libdir}/X11/xkb/compiled
ln -sf ../../../../../var/state/xkb \
	$RPM_BUILD_ROOT%{_libdir}/X11/xkb/compiled

# do not duplicate xkbcomp program
rm -f $RPM_BUILD_ROOT%{_libdir}/X11/xkb/xkbcomp
ln -sf ../../../bin/xkbcomp $RPM_BUILD_ROOT%{_libdir}/X11/xkb/xkbcomp

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[135]/*

#--- %post{un}, %preun, %verifyscript -

%pre
if [ ! -L /usr/X11R6/lib/X11/fonts ]; then
	mkdir -p /usr/share/fonts
	cp -ar /usr/X11R6/lib/X11/fonts/* /usr/share/fonts
	rm -rf /usr/X11R6/lib/X11/fonts
	ln -sf /usr/share/fonts /usr/X11R6/lib/X11/fonts
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

%post fonts
cd %{_fontdir}/misc
%{_bindir}/mkfontdir
cd %{_fontdir}/Type1
/usr/bin/type1inst -nogs -nolog

%postun fonts
cd %{_fontdir}/misc
umask 022
%{_bindir}/mkfontdir
cd %{_fontdir}/Type1
/usr/bin/type1inst -nogs -nolog

%post 75dpi-fonts
cd %{_fontdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi-fonts
cd %{_fontdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi-fonts
cd %{_fontdir}/100dpi
%{_bindir}/mkfontdir

%postun 100dpi-fonts
cd %{_fontdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post cyrillic-fonts
cd %{_fontdir}/100dpi
%{_bindir}/mkfontdir

%postun cyrillic-fonts
cd %{_fontdir}/100dpi
umask 022
%{_bindir}/mkfontdir

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

%doc %{_libdir}/X11/XF86Config.eg
%doc %{_libdir}/X11/Cards

%ifarch ix86 alpha sparc
%doc %{_libdir}/X11/Cards
%endif

%dir %{_libdir}
%dir %{_libdir}/X11
%dir %{_libdir}/X11/rstart
%dir %{_libdir}/X11/rstart/commands
%dir %{_libdir}/X11/rstart/commands/x11r6
%dir %{_libdir}/X11/rstart/contexts
%dir %{_libdir}/X11/fonts
%dir %{_libdir}/X11/xserver
%dir %{_bindir}

%ifnarch sparc
%dir %{_libdir}/modules
%endif

%config(noreplace) %verify(not md5 mtime size) /etc/X11/XF86Config
%config %verify(not md5 mtime size) /etc/pam.d/xserver
%config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.xserver
%config(missingok) /etc/security/console.apps/xserver
%config /etc/X11/xsm/system.xsm
%ghost /etc/X11/X

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

%attr(755,root,root) %{_libdir}/X11/etc/*

%attr(4755,root,root) %{_bindir}/Xwrapper

%attr(755,root,root) %{_bindir}/X
%attr(755,root,root) %{_bindir}/Xprt
%attr(755,root,root) %{_bindir}/lbxproxy

%attr(755,root,root) %{_bindir}/proxymngr
%attr(755,root,root) %{_bindir}/rstartd
%attr(755,root,root) %{_bindir}/xfindproxy
%attr(755,root,root) %{_bindir}/xfwp
%attr(755,root,root) %{_bindir}/xrx
%attr(755,root,root) %{_bindir}/lndir
%attr(755,root,root) %{_bindir}/mkdirhier
%attr(755,root,root) %{_bindir}/mergelib
%attr(755,root,root) %{_bindir}/makeg
%attr(755,root,root) %{_bindir}/appres
%attr(755,root,root) %{_bindir}/bdftopcf
%attr(755,root,root) %{_bindir}/beforelight
%attr(755,root,root) %{_bindir}/bitmap
%attr(755,root,root) %{_bindir}/bmtoa
%attr(755,root,root) %{_bindir}/atobm
%attr(755,root,root) %{_bindir}/editres
%attr(755,root,root) %{_bindir}/fsinfo
%attr(755,root,root) %{_bindir}/fslsfonts
%attr(755,root,root) %{_bindir}/fstobdf
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
%attr(755,root,root) %{_bindir}/xmh
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
%attr(755,root,root) %{_bindir}/reconfig
%attr(755,root,root) %{_bindir}/xon

%{_includedir}/X11/bitmaps

%{_mandir}/man1/lbxproxy.1*
%{_mandir}/man1/proxymngr.1*
%{_mandir}/man1/xfindproxy.1*
%{_mandir}/man1/xfwp.1*
%{_mandir}/man1/xrx.1*
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
%{_mandir}/man1/fsinfo.1*
%{_mandir}/man1/fslsfonts.1*
%{_mandir}/man1/fstobdf.1*
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
%{_mandir}/man1/sessreg.1*
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
%{_mandir}/man1/xmh.1*
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
%{_mandir}/man1/Xserver.1*
%{_mandir}/man1/XFree86.1*
%{_mandir}/man1/reconfig.1*
%{_mandir}/man1/xon.1*

/usr/bin/X11

%ifnarch sparc

%files modules
%defattr(-,root,root,755)
%{_libdir}/X11/xkb
/var/state/xkb
%dir %{_libdir}/modules
%attr(755,root,root) %{_libdir}/modules/*

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
#/var/state/xdm

%config %{_libdir}/X11/app-defaults/Chooser

%attr(755,root,root) %{_libdir}/X11/xdm
%attr(755,root,root) %{_bindir}/xdm
%{_mandir}/man1/xdm.1*

%dir %{_sysconfdir}/X11/xdm
%config %{_sysconfdir}/X11/xdm/xdm-config
%config %{_sysconfdir}/X11/xdm/chooser
%config %{_sysconfdir}/X11/xdm/Xsetup_0
%config %{_sysconfdir}/X11/xdm/Xsession
%config %{_sysconfdir}/X11/xdm/Xservers
%config %{_sysconfdir}/X11/xdm/Xresources
%config %{_sysconfdir}/X11/xdm/Xaccess
%config %{_sysconfdir}/X11/xdm/TakeConsole
%config %{_sysconfdir}/X11/xdm/GiveConsole

%files -n twm
%defattr(644,root,root,755)
%{_datadir}/gnome/wm-properties/twm.desktop
%attr(755,root,root) %{_bindir}/twm
%config %{_sysconfdir}/X11/twm/system.twmrc
%attr(755,root,root) %{_libdir}/X11/twm
%{_mandir}/man1/twm.1*

%files -n xfs
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/xfs
%dir %{_sysconfdir}/X11/fs
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/X11/fs/config
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/xfs

%attr(755,root,root) %{_bindir}/xfs
%attr(755,root,root) %{_bindir}/fsinfo
%attr(755,root,root) %{_bindir}/fslsfonts
%attr(755,root,root) %{_bindir}/fstobdf
%attr(755,root,root) %{_libdir}/X11/fs

%{_mandir}/man1/xfs.1*
%{_mandir}/man1/fsinfo.1*
%{_mandir}/man1/fslsfonts.1*
%{_mandir}/man1/fstobdf.1*

%files -n xauth
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xauth
%{_mandir}/man1/xauth.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gccmakedep
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/libFS.a
%{_libdir}/libXau.a
%{_libdir}/libXdmcp.a
%{_libdir}/libXdpms.a
%{_libdir}/libXss.a
%{_libdir}/libXxf86dga.a
%{_libdir}/libXxf86misc.a
%{_libdir}/libXxf86vm.a
%{_libdir}/liboldX.a
%{_libdir}/libxkbfile.a
%{_libdir}/libxkbui.a

%{_includedir}/X11/*.h
%{_includedir}/X11/ICE
%{_includedir}/X11/PEX5
%{_includedir}/X11/PM
%{_includedir}/X11/SM
%{_includedir}/X11/Xaw
%{_includedir}/X11/Xmu
%{_includedir}/X11/extensions
%{_includedir}/X11/fonts
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
%{_libdir}/libICE.a
%{_libdir}/libPEX5.a
%{_libdir}/libSM.a
%{_libdir}/libX11.a
%{_libdir}/libXIE.a
%{_libdir}/libXaw.a
%{_libdir}/libXext.a
%{_libdir}/libXi.a  
%{_libdir}/libXmu.a
%{_libdir}/libXp.a
%{_libdir}/libXt.a
%{_libdir}/libXtst.a   
%{_libdir}/libXxf86rush.a

%files Xvfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xvfb
%{_mandir}/man1/Xvfb.1*

%files Xnest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xnest
%{_mandir}/man1/Xnest.1*

%ifarch %{ix86} alpha

%files SVGA
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_SVGA
%{_mandir}/man1/XF86_SVGA.1*
%{_mandir}/man5/XF86Config.5*
%endif

%ifarch %{ix86} sparc

%files VGA16
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_VGA16
%{_mandir}/man1/XF86_VGA16.1*
%{_mandir}/man5/XF86Config.5*
%endif

%ifarch %{ix86}

%files W32
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_W32
%{_mandir}/man1/XF86_W32.1*
%{_mandir}/man1/XF86_Accel.1*
%{_mandir}/man5/XF86Config.5*
%endif

%ifarch %{ix86} alpha

%files Mono
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_Mono
%{_mandir}/man1/XF86_Mono.1*
%{_mandir}/man5/XF86Config.5*
%endif

%ifarch %{ix86} alpha

%files S3
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_S3
%{_mandir}/man1/XF86_S3.1*
%{_mandir}/man1/XF86_Accel.1*
%{_mandir}/man5/XF86Config.5*
%endif

%ifarch %{ix86} alpha

%files S3V
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_S3V
%{_mandir}/man1/XF86_S3.1*
%{_mandir}/man1/XF86_Accel.1*
%{_mandir}/man5/XF86Config.5*
%endif

%ifarch %{ix86}

%files 8514
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_8514
%{_mandir}/man1/XF86_8514.1*
%{_mandir}/man1/XF86_Accel.1*
%{_mandir}/man5/XF86Config.5*
%endif

%ifarch %{ix86}

%files Mach8
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_Mach8
%{_mandir}/man1/XF86_Mach8.1*
%{_mandir}/man1/XF86_Accel.1*
%{_mandir}/man5/XF86Config.5*
%endif

%ifarch %{ix86}

%files Mach32
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_Mach32
%{_mandir}/man1/XF86_Mach32.1*
%{_mandir}/man1/XF86_Accel.1*
%{_mandir}/man5/XF86Config.5*
%endif

%files Mach64
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_Mach64
%{_mandir}/man1/XF86_Mach64.1*
%{_mandir}/man1/XF86_Accel.1*
%{_mandir}/man5/XF86Config.5*

%ifarch %{ix86} alpha

%files P9000
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_P9000
%{_mandir}/man1/XF86_P9000.1*
%{_mandir}/man1/XF86_Accel.1*
%{_mandir}/man5/XF86Config.5*
%endif

%ifarch %{ix86}

%files AGX
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_AGX
%{_mandir}/man1/XF86_AGX.1*
%{_mandir}/man1/XF86_Accel.1*
%{_mandir}/man5/XF86Config.5*
%endif

%ifarch %{ix86}

%files I128
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_I128
%{_mandir}/man1/XF86_I128.1*
%{_mandir}/man1/XF86_Accel.1*
%{_mandir}/man5/XF86Config.5*
%endif

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

%ifarch %{ix86}

%files 3DLabs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_3DLabs
%endif

%files FBDev
%defattr(644,root,root,755)
%ifarch m68k
%attr(755,root,root) %{_bindir}/XF68_FBDev
%{_mandir}/man1/XF68_FBDev.1*
%else
%attr(755,root,root) %{_bindir}/XF86_FBDev
%endif

%files XF86Setup
%defattr(644,root,root,755)
%{_libdir}/X11/doc
%attr(755,root,root) %{_bindir}/XF86Setup
%attr(755,root,root) %{_bindir}/xmseconfig
%attr(755,root,root) %{_bindir}/xf86config
%attr(755,root,root) %{_bindir}/scanpci
%attr(755,root,root) %{_bindir}/SuperProbe
%{_libdir}/X11/XF86Setup
%{_mandir}/man1/XF86Setup.1*
%{_mandir}/man1/xmseconfig.1*
%{_mandir}/man1/xf86config.1*
%{_mandir}/man1/SuperProbe.1*

%files fonts
%defattr(644,root,root,755)
%{_fontdir}/PEX
%{_fontdir}/Speedo
%{_fontdir}/Type1
%dir %{_fontdir}/misc
%{_fontdir}/misc/*gz
%verify(not mtime size md5) %{_fontdir}/misc/fonts.*

%files 75dpi-fonts
%defattr(644,root,root,755)
%dir %{_fontdir}/75dpi
%{_fontdir}/75dpi/*gz
%verify(not mtime size md5) %{_fontdir}/75dpi/fonts.*

%files 100dpi-fonts
%defattr(644,root,root,755)
%dir %{_fontdir}/100dpi
%dir %{_fontdir}/100dpi/*gz
%verify(not mtime size md5) %{_fontdir}/100dpi/fonts.*

%files cyrillic-fonts
%defattr(644,root,root,755)
%{_fontdir}/cyrillic
