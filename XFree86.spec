Summary:	XFree86 Window System servers and basic programs
Summary(de):	Xfree86 Window-System-Server und grundlegende Programme
Summary(fr):	Serveurs du syst�me XFree86 et programmes de base
Summary(pl):	XFree86 Window System wraz z podstawowymi programami
Summary(tr):	XFree86 Pencereleme Sistemi sunucular� ve temel programlar
Name: 		XFree86
Version:	3.3.3.1
Release:	54
Copyright:	MIT
Group:		X11/XFree86
Group(pl):	X11/XFree86
Source0:	ftp://ftp.xfree86.org/pub/XFree86/3.3.3/source/X333src-1.tgz
Source1:	xdm.pamd
Source2:	xdm.initd
Source3:	xfs.initd
Source4:	xfs.config
Source5:	xserver.pamd
Source6:	XTerm.ad-pl
Patch0:		ftp://ftp.xfree86.org/pub/XFree86/3.3.3/fixes/3.3.3-3.3.3.1.diff.gz
Patch1:		XFree86-rh.patch
Patch2:		XFree86-rhxdm.patch
Patch3:		XFree86-fsstnd.patch
Patch4:		XFree86-nopam.patch
Patch5:		XFree86-pamconsole.patch
Patch6:		XFree86-alpha-sockets.patch
# sparc patches from ultrapenguin
Patch7:		XFree86-sparc.patch
Patch8:		XFree86-ffb.patch.gz
# enable FBDev device on alpha / intel
Patch9:		XFree86-fbdev.patch
# fix xinput problems with threads / GTK+ -- Owen Taylor's fix
Patch10:	XFree86-xinput.patch
# more sun patches from ultrapenguin
Patch11:	XFree86-suncards.patch
Patch12:	XFree86-sparc2.patch
Patch13:	XFree86-creator2.patch.gz
Patch14:	XFree86-newcreator.patch
Patch15:	XFree86-sparc3.patch.gz
# the following was causing problems with RagePRO based ATI
# chipsets, but this has been fixed
Patch16:	XFree86-mach64.patch.gz
Patch17:	XFree86-creator4.patch.gz
Patch18:	XFree86-jay.patch
Patch19:	XFree86-86setup.patch
Patch20:	XFree86-czskkbd.patch
Patch21:	XFree86-is_keyboard.patch
# use glibc 2.1 routines for utmp, doesn't require xterm to be setuid
Patch22:	XFree86-nosuidxterm.patch
Patch23:	XFree86-joy.patch
Patch24:	XFree86-arm.patch
Patch25:	XFree86-xfsft.patch
Patch26:	XFree86-ru_SU.patch
Patch27:	XFree86-startx_xauth.patch
Patch28:	XFree86-xfsredhat.patch
Patch29:	XFree86-mgafix.patch
# the following patch is incomplete..broken..and thus commented out.
Patch30:	XFree86-alphadga.patch
# work by VMWare, inc. to provide hardware accelerated DGA "XFree86 3.4"
Patch31:	XFree86-dga1.1.patch
# Patch from Ian Reid Remmler <ian@marmoset.resnet.tamu.edu> to fix mouse
# movement with Kensington ExpertMouse / ThinkingMouse
Patch32:	XFree86-thinkingmouse.patch
# fix keymap error for dvorak keyboards
Patch33:	XFree86-dvorak.patch
# Fix dainbramage where the X server chmods whatever .X11-unix points to
Patch34:	XFree86-tmpdir.patch
# link xterm with libncurses instead libtermcap
Patch35:	XFree86-ncurses.patch
# Compile X serwers againsty system installed libz.so
Patch36:	XFree86-HasZlib.patch
# Man dir in /usr/X11R6/man or %{_mandir}
Patch37:	XFree86-fhs.patch
Patch38:	XFree86-voodoo-Rush.patch
Patch39:	XFree86-voodoo-Banshee.patch
Patch40:	XFree86-NVIDIA.patch
Patch41:	XFree86-xf86config-3dfx.patch
Patch42:	XFree86-G200dga.patch
Patch43:	XFree86-ffbcrash.patch
Patch44:	XFree86-fixiso8859-2.patch
Patch45:	XFree86-ru_sparc.patch
Patch46:	XFree86-xinitrace.patch
Patch47:	XFree86-xterm-color.patch
Patch48:	XFree86-xdm+pam_env.patch
Patch49:	XFree86-XF86Config-path.patch
Patch50:	XFree86-XF86Setup-fonts.patch
Patch51:	XFree86-IPv6.patch

BuildPrereq:	ncurses-devel
BuildPrereq:	zlib-devel
BuildPrereq:	utempter-devel
BuildPrereq:	tcl-devel
Requires:	pam
Requires:	xauth
Exclusivearch:	i386 i486 i586 i686 alpha sparc m68k armv4l
Buildroot:	/tmp/%{name}-%{version}-root/

%ifarch sparc
Obsoletes: X11R6.1
%endif

%define	_fontdir	/usr/share/fonts

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

In addition to installing this package, you will need to install the XFree86
package which corresponds to your video card, the X11R6-contrib package, the
Xconfigurator package and the XFree86-libs package. You may also need to
install one of the XFree86 fonts packages.

And finally, if you are going to develop applications that run as X clients,
you will also need to install XFree86-devel.

%description -l de
X-Windows ist eine voll funktionsf�hige grafische Benutzeroberfl�che mit
mehreren Fenstern, mehreren Clients und verschiedenen Arten von Fenstern. Es
kommt auf den meisten Unix-Plattformen zum Einsatz. Die Clients lassen sich
auch mit Hilfe anderer Fenstersysteme anzeigen. Das X-Protokoll gestattet
die Ausf�hrung der Applikationen direkt auf lokalen Rechnern oder �ber ein
Netz und bietet gro�e Flexibilit�t bei Client-Server-Implementierungen.

%decription -l pl

X Window System jest graficznym interfejsem u�ytkownika, cechuje si�
mo�liwo�ci� pracy w wielu oknach, z wieloma klientami i do tego w r�nych
wystrojach okien. :) Jest u�ywany na wi�kszo�ci platform sytem�w Unix, a
klienci mog� by� uruchamiani tak�e pod innymi popularnymi systemami
okienkowymi. Protok� X pozwala na uruchamianie aplikacji zar�wno z lokalnej
maszyny jak i poprzez sie� - daj�c przez to elastyczn� implementacj�
architektury klient/serwer.

Pakiet ten nie zawiera X serwera kt�ry jest po�rednikiem z Twoj� kart�
graficzn� (jest on w innym pakiecie).

%description -l tr
X Window sistemi, �oklu pencere, �oklu istemci ve �e�itli pencere
stilleriyle geni� �zelliklere sahip bir Grafik Kullan�c� Arabirimidir. �o�u
UNIX sisteminde �al��t��� gibi istemcileri de bir�ok pencereleme sistemiyle
�al��abilir. X protokolu kullanan uygulamalar�n yerel makina veya bilgisayar
a�� �zerinden �al��t�r�labilmesi esnek bir istemci/sunucu ortam� sa�lar. Bu
paket bir X istasyonu i�in gerekli olan temel yaz�tiplerini, programlar� ve
belgeleri sunar. Ekran kart�n�z� s�rmek i�in gerekli olan X sunucusu bu
pakete dahil de�ildir.

%package modules
Summary:	Modules with X servers extensions
Summary(pl):	Wsp�lne modu�y rozszerze� dla wszystkich X serwer�w
Group:		X11/XFree86
Group(pl):	X11/XFree86

%description modules
Modules with X servers extensions.

%description -l pl modules
Wsp�lne modu�y rozszerze� dla wszystkich X serwer�w.

%package libs
Summary:	X11R6 shared libraries
Summary(de):	X11R6 shared Libraries
Summary(pl):	Biblioteki dzielone dla X11R6
Summary(fr):	Biblioth�ques partag�es X11R6
Group:		X11/XFree86
Group(pl):	X11/XFree86
Prereq:		grep
Prereq:		/sbin/ldconfig

%ifarch sparc
Obsoletes: X11R6.1-libs
%endif

%description libs
XFree86-libs contains the shared libraries that most X programs need to run
properly. These shared libraries are in a separate package in order to
reduce the disk space needed to run X applications on a machine without an X
server (i.e, over a network).

If you are installing the X Window System on your machine, you will need to
install XFree86-libs. You will also need to install the XFree86 package, the
XFree86-75dpi-fonts package or the XFree86-100dpi-fonts package (depending
upon your monitor's resolution), the Xconfigurator package and the
X11R6-contrib package. And, finally, if you are going to be developing
applications that run as X clients, you will also need to install
XFree86-devel.

%description -l de libs
Dieses Paket enth�lt die zur gemeinsamen Nutzung vorgesehenen Libraries, die
die meisten X-Programme f�r den einwandfreien Betrieb ben�tigen. Sie wurden
in einem separaten Paket untergebracht, um den Festplattenspeicherplatz auf
Computern zu reduzieren, die ohne einen X- Server (�ber ein Netz) arbeiten.

%description -l fr libs
Ce paquetage contient les biblioth�ques partag�es n�cessaires � de nombreux
programmes X. Elles se trouvent dans un paquetage s�par� afin de r�duire
l'espace disque n�cessaire � l'ex�cution des applications X sur une machine
sans serveur X (en r�seau).

%description -l pl libs
Pakiet zawieraj�cy podstawowe biblioteki dla program�w kozystaj�cych z
systemu X Window. Wydzielony w celu oszczednosci miejsca, nie wp�ywa na
mo�liwo�ci pracy aplikacji X Windows poprzez np. sie�. Nie potrzebny dla
komputer�w nie posiadaj�cych X serwer�w.

%description -l tr libs
Bu paket X programlar�n�n d�zg�n �al��abilmeleri i�in gereken kitapl�klar�
i�erir. Bunlar, X programlar�n� (sunucu olsun olmas�n) �al��t�rmak i�in
gerekli disk alan�n� azaltmak i�in ayr� bir paket olarak sunulmu�tur.

%package devel
Summary:	X11R6 headers and programming man pages
Summary(de):	X11R6 Headers und man pages f�r Programmierer
Summary(fr):	Pages man de programmation
Summary(pl):	Pliki nag��wkowe dla X11R6
Summary(tr):	X11R6 ile geli�tirme i�in gerekli dosyalar
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
die als X-Clients laufen. Enth�lt die Xlib-Library und die Widget-S�tze Xt
und Xaw. Information zum Programmieren mit diesen Libraries finden Sie in
der Buchreihe zur X-Programmierung von O'Reilly and Associates.

%description -l fr devel
Biblioth�ques, fichiers d'en-t�te, et documentation pour d�velopper des
programmes s'ex�cutant en clients X. Cela comprend la Biblioth�que Xlib de
base aussi bien que les ensembles de widgets Xt et Xaw. Pour des
informations sur la programmation avec ces Biblioth�ques, Red Hat recommande
la s�rie d'ouvrages sur la programmation X edit�e par O'Reilly and
Associates.

%description -l pl devel
Pliki nag��wkowe, dokumentcja dla programist�w rozwijaj�cych aplikacje
klienckie pod X'y. Zawiera podstatwow� bibliotek� Xlib a tak�e Xt i Xaw.
Wi�cej informacji nt. pisania program�w przy u�yciu tych bibliotek mo�esz
znale�� w ksi��kach wydawnictwa O'Reilly and Associates (X Programming)
polecanych przez Red Hat'a.

%description -l tr devel
X istemcisi olarak �al��acak programlar geli�tirmek i�in gereken statik
kitapl�klar, ba�l�k dosyalar� ve belgeler. Xlib kitapl���n�n yan�s�ra Xt ve
Xaw aray�z kitapl�klar�n� da i�erir.

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

%package	XF86Setup
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
Graficzny konfigurator dla XFree86

%package S3
Summary:	XFree86 S3 server
Summary(de):	XFree86 S3 Server
Summary(fr):	Serveur XFree86 pour S3
Summary(pl):	XFree86 serwer dla kart S3
Summary(tr):	XFree86 S3 sunucular�
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

%description S3
XFree86-S3 is the X server for video cards based on S3 chips, including most
#9 cards, many Diamond Stealth cards, Orchid Farenheits, Mirco Crystal 8S,
most STB cards, and some motherboards with built-in graphics accelerators
(such as the IBM ValuePoint line). Note that if you have an S3 ViRGE based
video card, you'll need XFree86-S3V instead of XFree86-S3.

If you are installing the X Window System and you have a video card based on
an S3 chip, you should install XFree86-S3. You will also need to install
the XFree86 package, one or more XFree86 fonts packages, the X11R6-contrib
package, the Xconfigurator package and the XFree86-libs package. And,
finally, if you are going to develop applications that run as X clients, you
will also need to install XFree86-devel.

%description -l de S3
X-Server f�r Steckkarten mit dem S3-Chipsatz (inkl. den meisten #9-Karten),
Karten wie Diamond Stealth, Orchid Farenheit und Mirco Crystal 8S, den
meisten STB-Karten sowie einigen Motherboards mit integrierten
Grafikbeschleunigern (z.B. die Reihe IBM ValuePoint).

%description -l fr S3
Serveur X pour les cartes construites autour des circuits S3, dont la
plupart des cartes #9, de nombreuses Diamond Stealth, Orchid Farenheits,
Mirco Crystal 8S, la plupart des cartes STB et certaines cartes m�res
int�grant des acc�l�rateurs graphiques (comme la gamme ValuePoint d'IBM).

%description -l pl S3
X serwer dla kart opartych na uk�adzie S3 - s� ta m.in. #9, wiele kart
Diamond Stealth, Orchid Farenheits, Mirco Crystal 8S, wi�kszo�c kart STB a
tak�e niekt�re p�yty g��wne z wbudowanymi akcelatorami graficznymi (jak np.
ValuePoint IBM'a).

%description -l tr S3
S3 tabanl� ekran kartlar� i�in sunucular. �o�u #9, Diamond Stealth, Orchid
Fahrenheit, Mirco Crystal 8S, �o�u STB ve baz� anakarta t�mle�ik grafik
h�zland�r�c�lar bu gruba girer. S3 Virge sunucusu ayr� bir pakette yer al�r.

%package I128
Summary:	XFree86 #9 Imagine 128 Server
Summary(de):	XFree86 #9 Imagine 128 Server
Summary(fr):	Serveur Xfree86 pour #9 Imagine 128
Summary(pl):	XFree86 serwer dla kart Number Nine Imagine 128
Summary(tr):	XFree86 #9 Imagine 128 sunucusu
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

%description I128
X server for the #9 Imagine 128 board.

%description -l de I128
X-Server f�r die Steckkarte #9 Imagine 128

%description -l fr I128
Serveur X pour les cartes #9 Imagine 128.

%description -l pl I128
X serwer do kart #9 Imagine 128.

%description -l tr I128
#9 Imagine kart� i�in X sunucusu.

%package S3V
Summary:	XFree86 S3 Virge server
Summary(de):	Xfree86 S3 Virge-Server
Summary(fr):	Serveur XFree86 pour S3 Virge
Summary(pl):	XFree86 serwer dla kart S3 Virge
Summary(tr):	XFree86 S3 Virge sunucusu
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

%description S3V
XFree86-S3V is the X server for video cards based on the S3 ViRGE chipset.

If you are installing the X Window System and you have a video card based on
an S3 ViRGE chip, you should install XFree86-S3V. You will also need to
install the XFree86 package, one or more of the XFree86 fonts packages, the
X11R6-contrib package, the Xconfigurator package and the XFree86-libs
package. And, finally, if you are going to develop applications that run as
X clients, you will also need to install XFree86-devel.

%description -l de S3V
X-Server f�r Grafikkarten mit dem S3 Virge-Chipsatz.

%description -l fr S3V
Serveur X pour les cartes construites autour du circuit S3 Virge.

%description -l pl S3V
X serwer dla kart opartych na S3 Virge.

%description -l tr S3V
XFree86 S3 Virge sunucusu

%package Mach64
Summary:	XFree86 Mach64 server
Summary(de):	Xfree86 Mach64-Server
Summary(fr):	Serveur Mach64 de XFree86
Summary(pl):	XFree86 serwer dla kart Mach64
Summary(tr):	XFree86 Mach64 sunucusu
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

%description Mach64
XFree86-Mach64 is the server package for cards based on ATI's Mach64 chip,
such as the Graphics Xpression, GUP Turbo, and WinTurbo cards. Note that
this server is known to have problems with some Mach64 cards. Check
http://www.xfree86.org for current information on updating this server.

If you are installing the X Window System and the video card in your system
is based on the Mach64 chip, you need to install XFree86-Mach64. You will
also need to install the XFree86 package, one or more of the XFree86 fonts
packages, the X11R6-contrib package, the Xconfigurator package and the
XFree86-libs package. And, finally, if you are going to be developing
applications that run as X clients, you will also need to install
XFree86-devel.

%description -l de Mach64
X-Server f�r ATI Mach64-Karten wie Graphics Xpression, GUP Turbo, und
WinTurbo. Dieser Server verursacht gelegentlich Probleme mit Mach64-Karten,
die aber von einer neueren Version von XFree86 (der als Beta-Version
verf�gbar ist) gel�st werden k�nnten. Unter http://www.xfree86.org finden
Sie Informationen zum Aktualisieren dieses Servers.

%description -l fr Mach64
Serveur X pour les cartes bas�es sur l'ATI Mach64, comme les cartes GUP
Turbo, Graphics Xpression et WinTurbo. Ce serveur est connu pour avoir des
probl�mes avec certaines cartes Mach64 que les versions plus r�centes
d'XFree86 corrigent (elles ne sont encore qu'en version BETA au moment de
cette distribution). Consultez http://www.xfree86.org pour les informations
de mise � jour du serveur.

%description -l pl Mach64
X serwer dla kart opartych na uk�adzie ATI Mach64 jak np. Graphics
Xpression, GUP Turbo, a tak�e WinTurbo. Serwer jest znany z problem�w z
niekt�rymi kartami Mach64, kt�re jednak mog� by� ju� poprawione w nowszej
wersji XFree86 (osi�galna wy��cznie jako wersja BETA). Sp�jrz na stron�
http://www.xfree86.org/ gdzie znajdziesz informacje nt. nowszych wersji
XFree86.

%description -l tr Mach64
ATI Mach64 tabanl� kartlar i�in X sunucusu. Graphics Xpression, GUP Turbo ve
WinTurbo gibi kartlar� destekler. Baz� Mach64 kartlar�n yeni XFree86 ile
sorun ya�ad�klar� bilinmektedir. Bu sorunla ilgili son bilgilere ula�mak
i�in l�tfen http://www.xfree86.org adresine bak�n.

%package Sun
Summary:	XFree86 Sun server (monochrome and 8-bit color SBUS framebuffers)
Summary(pl):	Serwer XFree86 Sun (dla framebuffera)
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Obsoletes:	X11R6.1-Sun

%description Sun
To run X Windows programs requires an X server for your specific hardware.
This package includes the X server for Sun computers with monochrome and
8-bit color SBUS framebuffers.

%description -l pl Sun
Aby uruchomi� X Window System potrzebujesz X serwera dostosowanego do
Twojego sprz�tu. Ten pakiet zawiera X serwer dla komputer�w firmy Sun z
monochromatycznymi lub te� 8-bitowymi kolorowymi framebufferami SBUS.

%package SunMono
Summary:	XFree86 Sun server for monochrome SBUS framebuffers only
Summary(pl):	Serwer XFree86 Sun (tylko dla monitor�w monochromatycznych)
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Obsoletes:	X11R6.1-SunMono

%description SunMono
To run X Windows programs requires an X server for your specific hardware.
This package includes the X server for Sun computers with monochrome
SBUS framebuffers only.

%description -l pl SunMono
Aby uruchomi� X Window System potrzebujesz X serwera dostosowanego do
Twojego sprz�tu. Ten pakiet zawiera X serwer dla komputer�w firmy Sun z
wy��cznie monochromatycznymi framebufferami SBUS.

%package Sun24
Summary:	XFree86 Sun server for all supported SBUS framebuffers
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Obsoletes:	X11R6.1-Sun24
Summary(pl):	Serwer XFree86 Sun (dla wszystkich SBUS framebuffer�w)

%description Sun24
To run X Windows programs requires an X server for your specific hardware.
This package includes the X server for Sun computers with all supported
SBUS framebuffers.

%description -l pl Sun24
Aby uruchomi� X Window System potrzebujesz X serwera dostosowanego do
Twojego sprz�tu. Ten pakiet zawiera X serwer dla komputer�w firmy Sun dla
wszystkich wspieranych framebuffer�w SBUS.

%package Xvfb
Summary:	XFree86 Xvfb server
Summary(pl):	Serwer XFree86 Xvfb
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

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

%description -l pl Xvfb

%package 3DLabs
Summary:	XFree86 3DLabs server
Summary(pl):	Serwer XFree86 3DLabs
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

%description 3DLabs
X server for cards built around 3D Labs GLINT and Permedia chipsets,
including GLINT 500TX with IBM RGB526 RAMDAC, GLINT MX with IBM RGB526 and
IBM RGB640 RAMDAC, Permedia with IBM RGB526 RAMDAC and the Permedia 2
(classic, 2a, 2v).

%description -l pl 3DLabs
XFree86 3DLabs server.

%package Xnest
Summary:	XFree86 Xnest server
Summary(pl):	Serwer XFree86 Xnest
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

%description Xnest
Xnest is an X Window System server which runs in an X window. Xnest is a
'nested' window server, actually a client of the real X server, which
manages windows and graphics requests for Xnest, while Xnest manages the
windows and graphics requests for its own clients.

You will need to install Xnest if you require an X server which will run as
a client of your real X server (perhaps for testing purposes).

%description -l pl Xnest

%package Xptr
Summary:	X print server
Summary(pl):	X print server
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

%description Xptr
Xprt provides an X server with the print extension and special DDX
implementation.

%description -l pl Xptr

%package 8514
Summary:	XFree86 8514 server
Summary(de):	XFree86 8514 Server
Summary(fr):	serveur 8514 pour XFree86.
Summary(pl):	XFree86 serwer dla kart 8514
Summary(tr):	XFree86 8514 sunucusu
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

%description 8514
X server for older IBM 8514 cards and compatibles from companies such as
ATI.

%description -l de 8514
If you are installing the X Window System and the video card in your system
is an older IBM 8514 or a compatible from a company such as ATI, you should
install XFree86-8514.

To install the X Window System, you will need to install the XFree86
package, one or more of the XFree86 fonts packages, the X11R6-contrib
package, the Xconfigurator package and the XFree86-libs package.

If you are going to develop applications that run as X clients, you will
also need to install the XFree86-devel package.

%description -l fr 8514
Serveur X pour les vieilles cartes IBM 8514 et compatibles comme lesATI.

%description -l pl 8514
X serwer dla starszych kart IBM 8514 oraz kompatybilnych robionych przez
inne firmy takie jak np. ATI.

%description -l tr 8514
Eski IBM 8514 ve uyumlu kartlar (ATI gibi) i�in sunucu.

%package AGX
Summary:	XFree86 AGX server
Summary(de):	XFree86 AGX Server
Summary(fr):	serveur AGX pour XFree86.
Summary(pl):	XFree86 serwer dla kart AGX
Summary(tr):	XFree86 AGX sunucusu
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

%description AGX
This is the X server for AGX-based cards, such as the Boca Vortex, Orchid
Celsius, Spider Black Widow and Hercules Graphite.

If you are installing the X Window System and the video card in your system
is an AGX, you'll need to install XFree86-AGX. To install the X Window
System, you will need to install the XFree86 package, one or more of the
XFree86 fonts packages, the X11R6-contrib package, the Xconfigurator package
and the XFree86-libs package.

Finally, if you are going to develop applications that run as X clients, you
will also need to install the XFree86-devel package.

%description -l de AGX
X-Server f�r Karten auf AGX-Basis wie etwa Boca Vortex, Orchid Celsius,
Spider Black Widow und Hercules Graphite.

%description -l fr AGX
Serveur X pour les cartes � base d'AGX comme la Boca Vortex, l'Orchid

%description -l pl AGX

%description -l tr AGX
Boca Vortex, Orchid Celsius, Spider Black Widow ve Hercules Graphite gibi AGX
tabanl� kartlar i�in X sunucusu.

%package FBDev
Summary:	XFree68/86 FBDev server
Summary(pl):	XFree86/86 FBDev server
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

%description FBDev
X server for the generic frame buffer device used on the Amiga, Atari
and Macintosh/m68k machines. Support for Intel and Alpha architectures
is now included in the Linux 2.2 kernel as well.

%description -l pl FBDev
X serwer wspieraj�cy frame buffera dla Amigi, Atari i Macintosha /m68k.
Wsparcie dla platform Intel i Alpha jest w j�drze systemu.

%package Mach32
Summary:	XFree86 Mach32 server
Summary(de):	Xfree86 Mach32-Server
Summary(fr):	Serveur XFree86 pour Mach32
Summary(pl):	XFree86 serwer dla kart Mach32
Summary(tr):	XFree86 Mach32 sunucusu
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

%description Mach32
XFree86-Mach32 is the X server package for video cards built around ATI's
Mach32 chip, including the ATI Graphics Ultra Pro and Ultra Plus.

If you are installing the X Window System and the video card in your system
is based on the Mach32 chip, you need to install XFree86-Mach32. You will
also need to install the XFree86 package, one or more of the XFree86 fonts
packages, the X11R6-contrib package, the Xconfigurator package and the
XFree86-libs package. And, finally, if you are going to develop applications
that run as X clients, you will also need to install XFree86-devel.

%description -l de Mach32
X-Server f�r Karten auf der Basis des ATI Mach32-Chip, einschlie�lich
ATI Graphics Ultra Pro und Ultra Plus.

%description -l fr Mach32
Serveur X pour les cartes utilisant le circuit ATI Mach32, dont les
cartes ATI Graphics Ultra Pro et Ultra Plus.

%description -l pl Mach32
X serwer dla kart zbudowanych na uk�adzie ATI Mach32 w��czaj�c w to ATI
Graphics Ultra Pro oraz Ultra Plus.

%description -l tr Mach32
ATI Mach32 tabanl� ATI Graphics Ultra Pro ve Ultra Plus kartlar� i�in X
sunucusu.

%package Mach8
Summary:	XFree86 Mach8 server
Summary(de):	XFree86 Mach8 Server
Summary(fr):	Serveur Mach8 pour XFree86
Summary(pl):	XFree86 serwer dla kart Mach8
Summary(tr):	XFree86 Mach8 sunucusu
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

%description Mach8
XFree86-Mach 8 is the X server for video cards built around ATI's Mach8
chip, including the ATI 8514 Ultra and Graphics Ultra.

If you are installing the X Window System and the video card in your system
is based on the Mach8 chip, you need to install XFree86-Mach8. You will also
need to install the XFree86 package, one or more of the XFree86 fonts
packages, the X11R6-contrib package, the Xconfigurator package and the
XFree86-libs package. And, finally, if you are going to be developing
applications that run as X clients, you will also need to install
XFree86-devel.

%description -l de Mach8
X-Server f�r Karten auf der Basis des ATI Mach8-Chips, einschlie�lich
des ATI 8514 Ultra und des Graphics Ultra.

%description -l fr Mach8
Serveur X pour les cartes bas�es sur les chips ATI Mach8, dont les cartes
ATI 8514 Ultra et Graphics Ultra.

%description -l pl Mach8
X serwer dla kart opartych na uk�adzie ATI Mach8, w��czaj�c w to ATI 8514
Ultra oraz graphics Ultra.

%description -l tr Mach8
ATI 8514 Ultra ve Graphics Ultra gibi ATI Mach8 tabanl� kartlar i�in X
sunucusu.

%package Mono
Summary:	XFree86 Mono server
Summary(de):	Xfree86 Mono-Server
Summary(fr):	Serveur Monochrome de XFree86
Summary(pl):	XFree86 serwer dla kart Monochromatycznych
Summary(tr):	XFree86 Mono sunucusu
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

%description Mono
XFree86-Mono is a generic monochrome (2 color) server for VGA cards.
XFree86-Mono will work for nearly all VGA compatible cards, but will only
support a monochrome display.

If you are installing the X Window System and your VGA card is not currently
supported, you should install and try either XFree86-Mono or XFree86-VGA16,
depending upon the capabilities of your display. You will also need to
install the XFree86 package, one or more of the XFree86 fonts packages, the
X11R6-contrib package, the Xconfigurator package and the XFree86-libs
package. And, finally, if you are going to develop applications that run as
X clients, you will also need to install XFree86-devel.

%description -l de Mono
Generischer monochromer (Schwarzwei�-) Server f�r VGA-Karten, der
praktisch mit allen VGA-�hnlichen Karten mit beschr�nkter Aufl�sung
funktioniert.

%description -l fr Mono
Serveur g�n�rique monochrome (2 couleurs) pour les cartes VGA, fonctionne avec
pratiquement toutes les cartes VGA ayant des r�solutions limit�es.

%description -l pl Mono
Dwu kolorowy (monochromatyczny) serwer dla kart VGA, pracuje na wszystkich
typu VGA w ograniczonej rozdzielczo�ci.

%description -l tr Mono
Mono (2 renk) VGA kartlar� i�in genel X sunucusu. K�s�tl� bir ��z�n�rl�k
alt�nda bir�ok VGA kart ile �al���r.

%package P9000
Summary:	XFree86 P9000 server
Summary(pl):	XFree86 serwer dla kart P9000
Summary(de):	XFree86 P9000 Server
Summary(fr):	Serveur XFree86 pour P9000
Summary(tr):	XFree86 P9000 sunucusu
Group:		X11/XFree86/Servers
Requires:	%{name}-modules = %{version}-%{release}

%description P9000
XFree86-P9000 is the X server for video cards built around the Weitek P9000
chip, such as most Diamond Viper cards and the Orchid P9000 card.

If you are installing the X Window System and you have a Weitek P9000 based
video card, you should install XFree86-P9000. You will also need to install
the XFree86 package, one or more of the XFree86 fonts packages, the
X11R6-contrib package, the Xconfigurator package and the XFree86-libs
package. And, finally, if you are going to develop applications that run as
X clients, you will also need to install XFree86-devel.

%description -l de P9000
X-Server f�r Karten auf Basis des Weitek P9000-Chip, wie die meisten
Diamond Viper und Orchid P9000-Karten.

%description -l fr P9000
Serveur X pour les cartes construites autour des circuits P9000 de
Weitek, comme la plupart des cartes Diamond Viper et l'Orchid P9000.

%description -l pl P9000
X serwer dla kart zbudowanych na uk�adzie Weitek P9000 czyli w wi�kszo�ci
karty Diamond Viper oraz Orchid P9000.

%description -l tr P9000
Diamond Viper ve Orchid P9000 gibi Weitek P9000 tabanl� kartlar i�in X
sunucusu.

%package SVGA
Summary:	XFree86 SVGA server
Summary(de):	XFree86 SVGA-Server
Summary(fr):	Serveur XFree86 pour SVGA
Summary(pl):	XFree86 serwer dla kart SVGA
Summary(tr):	XFree86 SVGA sunucusu
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

%description SVGA
X server for most simple framebuffer SVGA devices, including cards built
from ET4000 chips, Cirrus Logic chips, Chips and Technologies laptop chips,
Trident 8900 and 9000 chips. It works for Diamond Speedstar, Orchid Kelvins,
STB Nitros and Horizons, Genoa 8500VL, most Actix boards, the Spider VLB
Plus. It also works for many other chips and cards, so try this server if
you are having problems.

%description -l de SVGA
X-Server f�r die elementarsten Framebuffer-SVGA-Ger�te, einschlie�lich
Karten, die aus ET4000-Chips, Cirrus Logic-Chips, Chips and Technologies
Laptop-Chips sowie Trident 8900 und 9000 Chips gebaut sind. Funktioniert mit
Diamond Speedstar, Orchid Kelvins, STB Nitros und Horizons, Genoa 8500VL,
den meisten Actix-Karten sowie Spider VLB Plus und au�erdem mit vielen
anderen Chips und Karten. Es lohnt sich, diesen Server auszuprobieren, wenn
Sie Probleme haben.

%description -l fr SVGA
Serveur X pour les circuits SVGA les plus simples, dont les cartes
construites avec les circuits ET4000, Cirrus Logic, Chips and Technologies
laptop, Trident 8900 et 9000. Fonctionne pour les cartes Diamond Speedstar,
Orchid Kelvins, STB Nitros et Horizons, Genoa 8500VL, la plupart des Actix
et la Spider VLB Plus. Fonctionne aussi pour de nombreux autres circuits et
cartes. Essayez ce serveur si vous avez des probl�mes.

%description -l pl SVGA
X serwer dla wi�kszo�ci prostych kart SVGA, w��czaj�c karty zbudowane na
uk�adach ET4000, Cirrus Logic, Trident 8900 i 9000, oraz uk�ady wyst�puj�ce
w laptopach. Dzia�a tak�e z kartami Diamnod Speedstar, Orchid Kelvins, STB
Nitros i Horizons, Genoa 8500VL, wi�kszo�� Actix, Spider VLB Plus. Dzia�a
r�wnie� na wielu innych kartach opartych na innych uk�adach wi�c spr�buj ten
serwer je�li masz jakie� problemy.

%description -l tr SVGA
ET4000, Cirrus Logic, Chips and Technologies diz�st�, Trident 8900 ve 9000
gibi basit 'framebuffer' SVGA kullananan kartlar i�in X sunucusu. Ayn�
zamanda Diamond Speedstar, Orchid Kelvins, STB Nitros / Horizons, Genoa
8500VL, �o�u Actix kartlar�, Spider VLB Plus gibi kartlar ve bir�ok di�er
kart ile de �al���r. Herhangi bir sorun ya�arsan�z bu sunucuyu deneyin.

%package VGA16
Summary:	XFree86 VGA16 server
Summary(de):	XFree86 VGA16-Server
Summary(fr):	Serveur XFree86 pour VGA16
Summary(pl):	XFree86 serwer dla kart CGA16
Summary(tr):	XFree86 VGA16 sunucusu
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

%description VGA16
XFree86-VGA16 is a generic 16 color server for VGA boards. XFree86-VGA16
will work on nearly all VGA style graphics boards, but will only support a
low resolution, 16 color display.

If you are installing the X Window System and your VGA video card is not
specifically supported by another X server package, you should install
either XFree86-Mono or XFree86-VGA16, depending upon the capabilities of
your display. You will also need to install the XFree86 package, one or more
of the XFree86 fonts packages, the X11R6-contrib package, the Xconfigurator
package and the XFree86-libs package. And, finally, if you are going to be
develop applications that run as X clients, you will also need to install
XFree86-devel.

%description -l de VGA16
Generischer 16-Farben-Server f�r VGA-Karten. Funktioniert auf fast allen VGA-
Grafikkarten, allerdings nur bei geringer Aufl�sung und wenigen Farben.

%description -l fr VGA16
Serveur 16 couleurs g�n�rique pour cartes VGA. Fonctionne avec presque
toutes les cartes VGA, mais seulement en faible r�solution avec peu de couleurs.

%description -l pl VGA16
Podstawowy serwer dla 16 kolorowego trybu pracy kart VGA. Dzia�a ze
wszystkimi kartami VGA ale jedynie w niskiej rozdzielczo�ci i ma�ej ilo�ci
kolor�w.

%description -l tr VGA16
VGA kartlar� i�in genel 16 renk sunucusu. �o�u VGA tipi kart ile d���k renk
ve ��z�n�rl�kte �al���r.

%package W32
Summary:	XFree86 W32 server
Summary(de):	XFree86 W32 Server
Summary(fr):	Serveur XFree86 pour W32
Summary(pl):	XFree86 serwer dla kart W32
Summary(tr):	XFree86 W32 sunucusu
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

%description W32
XFree86-W32 is the X server for cards built around ET4000/W32 chips,
including the Genoa 8900 Phantom 32i, the Hercules Dynamite, the LeadTek
WinFast S200, the Sigma Concorde, the STB LightSpeed, the TechWorks
Thunderbolt, and the ViewTop PCI.

If you are installing the X Window System and your VGA video card is based
on the ET4000/W32 chipset, you should install XFree86-W32. You will also
need to install the XFree86 package, one or more of the XFree86 fonts
packages, the X11R6-contrib package, the Xconfigurator package and the
XFree86-libs package. And, finally, if you are going to develop applications
that run as X clients, you will also need to install XFree86-devel.

%description -l de W32
Genoa 8900 Phantom 32I, Hercules Dynamite, LeaTek WinFast S200,
Sigma Concorde, STB LightSpeed, TechWorks Thunderbolt und ViewTop PCI.

%description -l fr W32
Serveur X pour les cartes bas�e sur les chips ET4000/W32, dontla Genoa 8900
Phantom 32i, les cartes Hercules Dynamite, la LeadTek WinFast S200, la Sigma
Concorde, la STB LightSpeed, la TechWorks Thunderbolt, et la ViewTop PCI.

%description -l pl W32
X serwer dla kart zbudowanych na uk�adzie ET4000/W32, w��czaj�c w to karty
Genoa 8900 Phantom 32i, Hercules Dynamite, LeadTek WinFast S200,
Sigma Concorde, STB LightSpeed, TechWorks Thunderbolt oraz karty ViewTop
(PCI).

%description -l tr W32
Genoa 8900 Phantom 32i, Hercules Dynamite kartlar�, LeadTek WinFast S200,
Sigma Concorde, STB LightSpeed, TechWorks Thunderbolt, ve ViewTop PCI
gibi kartlar�n kulland��� ET4000/W32 tabanl� kartlar i�in X sunucusu.

%package TGA
Summary:	XFree86 TGA server
Summary(pl):	XFree86 serwer dla kart TGA
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}

%description TGA
The XFree86-TGA package contains an 8-bit X server for Digital TGA boards
based on the DC21040 chip. These adapters are very popular in Alpha
workstations and are included with Alpha UDB (Multia) machines.

If you are installing the X Window System and your system uses a Digital TGA
board based on the DC21040 chip, you'll need to install the XFree86-TGA
package.

%description -l pl TGA

%package -n xdm
Summary:	XDM
Summary(pl):	XDM
Group:		X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name} = %{version}
Requires:	pam >= 0.66
Obsoletes:	xdm

%description -n xdm

%description -l pl -n xdm

%package -n xfs
Summary:	Font server for XFree86
Summary(pl):	Serwer font�w do XFree86
Group:		X11/XFree86
Group(pl):	X11/XFree86
Obsoletes:	xfsft XFree86-xfs

%description -n xfs
This is a font server for XFree86. You can serve fonts to other X servers
remotely with this package, and the remote system will be able to use all
fonts installed on the font server, even if they are not installed on the
remote computer.

%description -l pl -n xfs

%package -n xauth
Summary:	XAuth
Group:		X11/XFree86
Group(pl):	X11/XFree86
Summary(pl):	XAuth

%description -n xauth

%description -l pl -n xauth

#--- %prep ---------------------------

%prep
%setup -q -c
%patch0  -p0
%patch1  -p1
%patch2  -p1
%patch3  -p1
%patch4  -p1
%patch5  -p1
# the following patch is in CVS diff format, needs POSIXLY_CORRECT env var.
#export POSIXLY_CORRECT=1
#%patch6 -p1 -b .alpha-sockets
#unset POSIXLY_CORRECT
%patch7  -p1
%patch8  -p1
%patch9  -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
#%patch30 -p1 -b .alphadga
%patch31 -p0
%patch32 -p1
%patch33 -p0
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p0
%patch39 -p0
# the following patch is in CVS diff format, needs POSIXLY_CORRECT env var.
export POSIXLY_CORRECT=1
%patch40 -p0
unset POSIXLY_CORRECT
# XFree make system is realy brain damaged
#%patch41 -p1 -b .3dfx
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1

## Clean up to save a *lot* of disk space
find . -name "*.orig" -print | xargs rm -f
find . -size 0 -print | xargs rm -f

%build
make -C xc World \
	"BOOTSTRAPCFLAGS=$RPM_OPT_FLAGS" \
	"CDEBUGFLAGS=" "CCOPTIONS=$RPM_OPT_FLAGS" \
	"CXXDEBUGFLAGS=" "CXXOPTIONS=$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/lib/X11/pl/app-defaults \
	$RPM_BUILD_ROOT/etc/{X11,pam.d,rc.d/init.d,security/console.apps} \
	$RPM_BUILD_ROOT/var/state/xkb

make -C xc	"DESTDIR=$RPM_BUILD_ROOT" \
		"DOCDIR=/usr/share/doc/%{name}-%{version}" \
		"INSTBINFLAGS=-m 755" \
		"INSTPGMFLAGS=-m 755" \
		install install.man

strip $RPM_BUILD_ROOT/usr/X11R6/bin/* || :
strip --strip-unneeded $RPM_BUILD_ROOT/usr/X11R6/lib/{lib*.so.*.*,modules/*} || :

# setup the default X server
rm -f $RPM_BUILD_ROOT/usr/X11R6/bin/X
ln -s Xwrapper $RPM_BUILD_ROOT/usr/X11R6/bin/X

# Move config stuff to /etc/X11

cp $RPM_BUILD_ROOT/usr/X11R6/lib/X11/XF86Config.eg \
$RPM_BUILD_ROOT/etc/X11/XF86Config
ln -sf ../../../../etc/X11/XF86Config $RPM_BUILD_ROOT/usr/X11R6/lib/X11/XF86Config

# setting default X
rm -f $RPM_BUILD_ROOT/usr/X11R6/bin/X
ln -sf Xwrapper $RPM_BUILD_ROOT/usr/X11R6/bin/X

# setting ghost X in /etc/X11 -- xf86config will fix this ...
ln -s ../../usr/X11R6/bin/Xwrapper $RPM_BUILD_ROOT/etc/X11/X

ln -sf ../../../../etc/X11/XF86Config \
$RPM_BUILD_ROOT/usr/X11R6/lib/X11/XF86Config

for i in xdm twm fs xsm xinit; do
	rm -rf $RPM_BUILD_ROOT/etc/X11/$i
	cp -ar $RPM_BUILD_ROOT/usr/X11R6/lib/X11/$i $RPM_BUILD_ROOT/etc/X11
	rm -rf $RPM_BUILD_ROOT/usr/X11R6/lib/X11/$i
	ln -sf /etc/X11/$i $RPM_BUILD_ROOT/usr/X11R6/lib/X11/$i
done

# make TrueType font dir, touch default .dir and .scale files
install	-d $RPM_BUILD_ROOT%{_fontdir}/TrueType
echo 0 > $RPM_BUILD_ROOT%{_fontdir}/TrueType/fonts.dir
echo 0 > $RPM_BUILD_ROOT%{_fontdir}/TrueType/fonts.scale

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/xdm
install %{SOURCE5} $RPM_BUILD_ROOT/etc/pam.d/xserver
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/xdm
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/xfs
install %{SOURCE4} $RPM_BUILD_ROOT/etc/X11/fs/config
install %{SOURCE6} $RPM_BUILD_ROOT/usr/X11R6/lib/X11/pl/app-defaults/XTerm

touch $RPM_BUILD_ROOT/etc/security/console.apps/xserver
touch $RPM_BUILD_ROOT/etc/security/blacklist.xserver
touch $RPM_BUILD_ROOT/etc/security/blacklist.xdm

#ln -sf ../../usr/X11R6/include/X11 $RPM_BUILD_ROOT%{_includedir}/X11 ##change
ln -sf %{_fontdir} $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts

for n in libX11.so.6.1 libICE.so.6.3 libSM.so.6.0 libXext.so.6.3 libXt.so.6.0 \
	 libXmu.so.6.0 libXaw.so.6.1 libXIE.so.6.0 libXi.so.6.0 \
	 libXtst.so.6.1 libXxf86rush.so.1.0; do
ln -sf $n $RPM_BUILD_ROOT/usr/X11R6/lib/`echo $n | sed "s/\.so.*/\.so/"`
done

# xkb 'compiled' files need to be in /var/state/xkb, so
# /usr is NFS / read-only mountable
mkdir -p $RPM_BUILD_ROOT/var/state/xkb
cp -a $RPM_BUILD_ROOT/usr/X11R6/lib/X11/xkb/compiled/* \
	$RPM_BUILD_ROOT/var/state/xkb
rm -rf $RPM_BUILD_ROOT/usr/X11R6/lib/X11/xkb/compiled
ln -sf ../../../../../var/state/xkb \
	$RPM_BUILD_ROOT/usr/X11R6/lib/X11/xkb/compiled

# do not duplicate xkbcomp program
rm -f $RPM_BUILD_ROOT/usr/X11R6/lib/X11/xkb/xkbcomp
ln -sf ../../../bin/xkbcomp $RPM_BUILD_ROOT/usr/X11R6/lib/X11/xkb/xkbcomp

ln -sf ../../../share/doc/%{name}-%{version} \
	$RPM_BUILD_ROOT/usr/X11R6/lib/X11/doc

# Add 3dfx cards to xf86config database
sed -e s/END// < $RPM_BUILD_ROOT/usr/X11R6/lib/X11/Cards > $RPM_BUILD_ROOT/usr/X11R6/lib/X11/Cards.tmp
/bin/mv $RPM_BUILD_ROOT/usr/X11R6/lib/X11/Cards.tmp $RPM_BUILD_ROOT/usr/X11R6/lib/X11/Cards
cat >> $RPM_BUILD_ROOT/usr/X11R6/lib/X11/Cards <<_EOT_

# 3dfx based cards

NAME 3dfx Banshee
SERVER SVGA
NOCLOCKPROBE

NAME 3dfx Voodoo3 2000
SERVER SVGA
NOCLOCKPROBE

NAME 3dfx Voodoo3 3000
SERVER SVGA
NOCLOCKPROBE

NAME 3dfx Voodoo3 3500
SERVER SVGA
NOCLOCKPROBE

NAME 3dfx Voodoo3 4000
SERVER SVGA
NOCLOCKPROBE

END

_EOT_

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man[135]/* \
	$RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/*

# don't gzip README.* files, they are needed by XF86Setup
gzip -dnf $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/README.*

%post libs
grep "^/usr/X11R6/lib$" /etc/ld.so.conf >/dev/null 2>&1
[ $? -ne 0 ] && echo "/usr/X11R6/lib" >> /etc/ld.so.conf
/sbin/ldconfig

%postun libs
if [ "$1" = "0" ]; then
	grep -v "/usr/X11R6/lib" /etc/ld.so.conf > /etc/ld.so.conf.new
	mv -f /etc/ld.so.conf.new /etc/ld.so.conf
fi
/sbin/ldconfig

%verifyscript libs
echo -n "Looking for /usr/X11R6/lib in /etc/ld.so.conf... "
if ! grep "^/usr/X11R6/lib$" /etc/ld.so.conf > /dev/null; then
	echo "missing"
	echo "/usr/X11R6/lib missing from /etc/ld.so.conf" >&2
else
	echo "found"
fi

%post -n xfs
/sbin/chkconfig --add xfs
if [ -f /var/run/xfs.pid ]; then
        /etc/rc.d/init.d/xfs restart >&2
else
        echo "Run \"/etc/rc.d/init.d/xfs start\" to start font server." >&2
fi
		

%post -n xdm
/sbin/chkconfig --add xdm
if [ -f /var/run/xdm.pid ]; then
        /etc/rc.d/init.d/xdm restart >&2
else
       echo "Run \"/etc/rc.d/init.d/xdm start\" to start xdm." >&2
fi
		
%postun -n xfs
if [ "$1" = "0" ]; then
	/etc/rc.d/init.d/xfs stop >&2
	/sbin/chkconfig --del xfs
fi

%postun -n xdm
if [ "$1" = "0" ]; then
	/etc/rc.d/init.d/xdm stop >&2
	/sbin/chkconfig --del xdm
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%docdir %{_docdir}/%{name}-%{version}
%doc /%{_docdir}/%{name}-%{version}/*
%doc /usr/X11R6/lib/X11/doc

%doc /usr/X11R6/lib/X11/XF86Config.eg
%doc /usr/X11R6/lib/X11/Cards

%ifarch ix86 alpha sparc
%doc /usr/X11R6/lib/X11/Cards
%endif

%dir /usr/X11R6
%dir /usr/X11R6/lib
%dir /usr/X11R6/lib/X11
%dir /usr/X11R6/lib/X11/rstart
%dir /usr/X11R6/lib/X11/rstart/commands
%dir /usr/X11R6/lib/X11/rstart/commands/x11r6
%dir /usr/X11R6/lib/X11/rstart/contexts
%dir /usr/X11R6/lib/X11/etc
%dir /usr/X11R6/lib/X11/fonts
%dir /usr/X11R6/lib/X11/xserver
%dir /usr/X11R6/bin

%ifnarch sparc
%dir /usr/X11R6/lib/modules
%endif

%config(noreplace) %verify(not md5 mtime size) /etc/X11/XF86Config
%config %verify(not md5 mtime size) /etc/pam.d/xserver
%config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.xserver
%config(missingok) /etc/security/console.apps/xserver
%config /etc/X11/twm/system.twmrc
%config /etc/X11/xsm/system.xsm
%ghost /etc/X11/X

/usr/X11R6/lib/X11/XErrorDB
/usr/X11R6/lib/X11/XKeysymDB
/usr/X11R6/lib/X11/locale
/usr/X11R6/lib/X11/lbxproxy
/usr/X11R6/lib/X11/proxymngr
/usr/X11R6/lib/X11/app-defaults

%lang(pl) /usr/X11R6/lib/X11/pl

%attr(755,root,root) /usr/X11R6/lib/X11/xinit

%attr(755,root,root) /usr/X11R6/lib/X11/twm
%attr(755,root,root) /usr/X11R6/lib/X11/fs
%attr(755,root,root) /usr/X11R6/lib/X11/xsm

/usr/X11R6/lib/X11/xserver/SecurityPolicy

%attr(-,root,root) /usr/X11R6/lib/X11/rstart/config
%attr(-,root,root) /usr/X11R6/lib/X11/rstart/rstartd.real
%attr(-,root,root) /usr/X11R6/lib/X11/rstart/commands/x
%attr(-,root,root) /usr/X11R6/lib/X11/rstart/commands/x11
%attr(-,root,root) /usr/X11R6/lib/X11/rstart/commands/*List*
%attr(-,root,root) /usr/X11R6/lib/X11/rstart/commands/x11r6/*
%attr(-,root,root) /usr/X11R6/lib/X11/rstart/contexts/*

%attr(755,root,root) /usr/X11R6/lib/X11/x11perfcomp/*
/usr/X11R6/lib/X11/*.txt

%attr(755,root,root) /usr/X11R6/lib/X11/etc/*

%attr(4755,root,root) /usr/X11R6/bin/Xwrapper

%attr(755,root,root) /usr/X11R6/bin/X
%attr(755,root,root) /usr/X11R6/bin/Xprt
%attr(755,root,root) /usr/X11R6/bin/lbxproxy

%attr(755,root,root) /usr/X11R6/bin/proxymngr
%attr(755,root,root) /usr/X11R6/bin/rstartd
%attr(755,root,root) /usr/X11R6/bin/xfindproxy
%attr(755,root,root) /usr/X11R6/bin/xfwp
%attr(755,root,root) /usr/X11R6/bin/xrx
%attr(755,root,root) /usr/X11R6/bin/lndir
%attr(755,root,root) /usr/X11R6/bin/mkdirhier
%attr(755,root,root) /usr/X11R6/bin/gccmakedep
%attr(755,root,root) /usr/X11R6/bin/mergelib
%attr(755,root,root) /usr/X11R6/bin/makeg
%attr(755,root,root) /usr/X11R6/bin/appres
%attr(755,root,root) /usr/X11R6/bin/bdftopcf
%attr(755,root,root) /usr/X11R6/bin/beforelight
%attr(755,root,root) /usr/X11R6/bin/bitmap
%attr(755,root,root) /usr/X11R6/bin/bmtoa
%attr(755,root,root) /usr/X11R6/bin/atobm
%attr(755,root,root) /usr/X11R6/bin/editres
%attr(755,root,root) /usr/X11R6/bin/fsinfo
%attr(755,root,root) /usr/X11R6/bin/fslsfonts
%attr(755,root,root) /usr/X11R6/bin/fstobdf
%attr(755,root,root) /usr/X11R6/bin/iceauth
%attr(755,root,root) /usr/X11R6/bin/mkfontdir
%attr(755,root,root) /usr/X11R6/bin/showrgb
%attr(755,root,root) /usr/X11R6/bin/rstart
%attr(755,root,root) /usr/X11R6/bin/smproxy
%attr(755,root,root) /usr/X11R6/bin/twm
%attr(755,root,root) /usr/X11R6/bin/x11perf
%attr(755,root,root) /usr/X11R6/bin/x11perfcomp
%attr(755,root,root) /usr/X11R6/bin/Xmark
%attr(755,root,root) /usr/X11R6/bin/xclipboard
%attr(755,root,root) /usr/X11R6/bin/xcutsel
%attr(755,root,root) /usr/X11R6/bin/xclock
%attr(755,root,root) /usr/X11R6/bin/xcmsdb
%attr(755,root,root) /usr/X11R6/bin/xconsole
%attr(755,root,root) /usr/X11R6/bin/xdpyinfo
%attr(755,root,root) /usr/X11R6/bin/dga
%attr(755,root,root) /usr/X11R6/bin/xfd
%attr(755,root,root) /usr/X11R6/bin/xhost
%attr(755,root,root) /usr/X11R6/bin/xieperf
%attr(755,root,root) /usr/X11R6/bin/xinit

%attr(755,root,root) /usr/X11R6/bin/startx

%attr(755,root,root) /usr/X11R6/bin/setxkbmap
%attr(755,root,root) /usr/X11R6/bin/xkbcomp
%attr(755,root,root) /usr/X11R6/bin/xkbevd
%attr(755,root,root) /usr/X11R6/bin/xkbprint
%attr(755,root,root) /usr/X11R6/bin/xkbvleds
%attr(755,root,root) /usr/X11R6/bin/xkbwatch
%attr(755,root,root) /usr/X11R6/bin/xkbbell
%attr(755,root,root) /usr/X11R6/bin/xkill
%attr(755,root,root) /usr/X11R6/bin/xlogo
%attr(755,root,root) /usr/X11R6/bin/xlsatoms
%attr(755,root,root) /usr/X11R6/bin/xlsclients
%attr(755,root,root) /usr/X11R6/bin/xlsfonts
%attr(755,root,root) /usr/X11R6/bin/xmag
%attr(755,root,root) /usr/X11R6/bin/xmh
%attr(755,root,root) /usr/X11R6/bin/xmodmap
%attr(755,root,root) /usr/X11R6/bin/xprop
%attr(755,root,root) /usr/X11R6/bin/xrdb
%attr(755,root,root) /usr/X11R6/bin/xset
%attr(755,root,root) /usr/X11R6/bin/xrefresh
%attr(755,root,root) /usr/X11R6/bin/xsetmode
%attr(755,root,root) /usr/X11R6/bin/xsetpointer
%attr(755,root,root) /usr/X11R6/bin/xsetroot
%attr(755,root,root) /usr/X11R6/bin/xsm
%attr(755,root,root) /usr/X11R6/bin/xstdcmap
%attr(755,root,root) /usr/X11R6/bin/xterm
%attr(755,root,root) /usr/X11R6/bin/resize
%attr(755,root,root) /usr/X11R6/bin/xvidtune
%attr(755,root,root) /usr/X11R6/bin/xwd
%attr(755,root,root) /usr/X11R6/bin/xwininfo
%attr(755,root,root) /usr/X11R6/bin/xwud
%attr(755,root,root) /usr/X11R6/bin/reconfig
%attr(755,root,root) /usr/X11R6/bin/xf86config
%attr(755,root,root) /usr/X11R6/bin/scanpci
%attr(755,root,root) /usr/X11R6/bin/SuperProbe
%attr(755,root,root) /usr/X11R6/bin/xon

/usr/X11R6/include/X11/bitmaps

/usr/X11R6/man/man1/lbxproxy.1*
/usr/X11R6/man/man1/proxymngr.1*
/usr/X11R6/man/man1/xfindproxy.1*
/usr/X11R6/man/man1/xfwp.1*
/usr/X11R6/man/man1/xrx.1*
/usr/X11R6/man/man1/lndir.1*
/usr/X11R6/man/man1/makestrs.1*
/usr/X11R6/man/man1/makeg.1*
/usr/X11R6/man/man1/mkdirhier.1*
/usr/X11R6/man/man1/appres.1*
/usr/X11R6/man/man1/bdftopcf.1*
/usr/X11R6/man/man1/beforelight.1*
/usr/X11R6/man/man1/bitmap.1*
/usr/X11R6/man/man1/bmtoa.1*
/usr/X11R6/man/man1/atobm.1*
/usr/X11R6/man/man1/editres.1*
/usr/X11R6/man/man1/fsinfo.1*
/usr/X11R6/man/man1/fslsfonts.1*
/usr/X11R6/man/man1/fstobdf.1*
/usr/X11R6/man/man1/iceauth.1*
/usr/X11R6/man/man1/mkfontdir.1*
/usr/X11R6/man/man1/showrgb.1*
/usr/X11R6/man/man1/rstart.1*
/usr/X11R6/man/man1/rstartd.1*
/usr/X11R6/man/man1/smproxy.1*
/usr/X11R6/man/man1/twm.1*
/usr/X11R6/man/man1/x11perf.1*
/usr/X11R6/man/man1/x11perfcomp.1*
/usr/X11R6/man/man1/xclipboard.1*
/usr/X11R6/man/man1/xcutsel.1*
/usr/X11R6/man/man1/xclock.1*
/usr/X11R6/man/man1/xcmsdb.1*
/usr/X11R6/man/man1/xconsole.1*
/usr/X11R6/man/man1/sessreg.1*
/usr/X11R6/man/man1/xdpyinfo.1*
/usr/X11R6/man/man1/dga.1*
/usr/X11R6/man/man1/xfd.1*
/usr/X11R6/man/man1/xhost.1*
/usr/X11R6/man/man1/xieperf.1*
/usr/X11R6/man/man1/xinit.1*
/usr/X11R6/man/man1/startx.1*
/usr/X11R6/man/man1/setxkbmap.1*
/usr/X11R6/man/man1/xkbcomp.1*
/usr/X11R6/man/man1/xkbevd.1*
/usr/X11R6/man/man1/xkbprint.1*
/usr/X11R6/man/man1/xkill.1*
/usr/X11R6/man/man1/xlogo.1*
/usr/X11R6/man/man1/xlsatoms.1*
/usr/X11R6/man/man1/xlsclients.1*
/usr/X11R6/man/man1/xlsfonts.1*
/usr/X11R6/man/man1/xmag.1*
/usr/X11R6/man/man1/xmh.1*
/usr/X11R6/man/man1/xmodmap.1*
/usr/X11R6/man/man1/xprop.1*
/usr/X11R6/man/man1/xrdb.1*
/usr/X11R6/man/man1/xrefresh.1*
/usr/X11R6/man/man1/xset.1*
/usr/X11R6/man/man1/xsetmode.1*
/usr/X11R6/man/man1/xsetpointer.1*
/usr/X11R6/man/man1/xsetroot.1*
/usr/X11R6/man/man1/xsm.1*
/usr/X11R6/man/man1/xstdcmap.1*
/usr/X11R6/man/man1/xterm.1*
/usr/X11R6/man/man1/resize.1*
/usr/X11R6/man/man1/xvidtune.1*
/usr/X11R6/man/man1/xwd.1*
/usr/X11R6/man/man1/xwininfo.1*
/usr/X11R6/man/man1/xwud.1*
/usr/X11R6/man/man1/Xserver.1*
/usr/X11R6/man/man1/XFree86.1*
/usr/X11R6/man/man1/reconfig.1*
/usr/X11R6/man/man1/xf86config.1*
/usr/X11R6/man/man1/SuperProbe.1*
/usr/X11R6/man/man1/xon.1*

%ifnarch sparc

%files modules
%defattr(-,root,root,755)
/usr/X11R6/lib/X11/xkb
/var/state/xkb
%attr(755,root,root) /usr/X11R6/lib/modules/*

%endif

%files -n xdm
%defattr(644,root,root,755)
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/xdm
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/security/blacklist.xdm
%attr(754,root,root) /etc/rc.d/init.d/xdm

%config /usr/X11R6/lib/X11/app-defaults/Chooser

%attr(755,root,root) /usr/X11R6/lib/X11/xdm
%attr(755,root,root) /usr/X11R6/bin/xdm
%attr(755,root,root) /usr/X11R6/bin/sessreg
/usr/X11R6/man/man1/xdm.1*

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

%files -n xfs
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/xfs
%dir /etc/X11/fs
%config(noreplace) /etc/X11/fs/config

%attr(755,root,root) /usr/X11R6/bin/xfs
%attr(755,root,root) /usr/X11R6/bin/fsinfo
%attr(755,root,root) /usr/X11R6/bin/fslsfonts
%attr(755,root,root) /usr/X11R6/bin/fstobdf

/usr/X11R6/man/man1/xfs.1*
/usr/X11R6/man/man1/fsinfo.1*
/usr/X11R6/man/man1/fslsfonts.1*
/usr/X11R6/man/man1/fstobdf.1*

%files -n xauth
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/xauth
/usr/X11R6/man/man1/xauth.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*


%files devel
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/lib/lib*.so
/usr/X11R6/lib/libFS.a
/usr/X11R6/lib/libXau.a
/usr/X11R6/lib/libXdmcp.a
/usr/X11R6/lib/libXdpms.a
/usr/X11R6/lib/libXss.a
/usr/X11R6/lib/libXxf86dga.a
/usr/X11R6/lib/libXxf86misc.a
/usr/X11R6/lib/libXxf86vm.a
/usr/X11R6/lib/liboldX.a
/usr/X11R6/lib/libxkbfile.a
/usr/X11R6/lib/libxkbui.a

/usr/X11R6/include/X11/*.h
/usr/X11R6/include/X11/ICE
/usr/X11R6/include/X11/PEX5
/usr/X11R6/include/X11/PM
/usr/X11R6/include/X11/SM
/usr/X11R6/include/X11/Xaw
/usr/X11R6/include/X11/Xmu
/usr/X11R6/include/X11/extensions
/usr/X11R6/include/X11/fonts
/usr/X11R6/lib/X11/config

%attr(755,root,root) /usr/X11R6/bin/imake
%attr(755,root,root) /usr/X11R6/bin/makedepend
%attr(755,root,root) /usr/X11R6/bin/xmkmf

/usr/X11R6/man/man1/imake.1*
/usr/X11R6/man/man1/makedepend.1*
/usr/X11R6/man/man1/xmkmf.1*
/usr/X11R6/man/man3/*

%files static
%defattr(644,root,root,755)
/usr/X11R6/lib/libICE.a
/usr/X11R6/lib/libPEX5.a
/usr/X11R6/lib/libSM.a
/usr/X11R6/lib/libX11.a
/usr/X11R6/lib/libXIE.a
/usr/X11R6/lib/libXaw.a
/usr/X11R6/lib/libXext.a
/usr/X11R6/lib/libXi.a
/usr/X11R6/lib/libXmu.a
/usr/X11R6/lib/libXp.a
/usr/X11R6/lib/libXt.a
/usr/X11R6/lib/libXtst.a
/usr/X11R6/lib/libXxf86rush.a

%files Xvfb
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/Xvfb
/usr/X11R6/man/man1/Xvfb.1*

%files Xnest
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/Xnest
/usr/X11R6/man/man1/Xnest.1*

%ifarch i386 i486 i586 i686 alpha

%files SVGA
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/XF86_SVGA
/usr/X11R6/man/man1/XF86_SVGA.1*
/usr/X11R6/man/man5/XF86Config.5*
%endif

%ifarch i386 i486 i586 i686 sparc

%files VGA16
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/XF86_VGA16
/usr/X11R6/man/man1/XF86_VGA16.1*
/usr/X11R6/man/man5/XF86Config.5*
%endif

%ifarch i386 i486 i586 i686

%files W32
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/XF86_W32
/usr/X11R6/man/man1/XF86_W32.1*
/usr/X11R6/man/man1/XF86_Accel.1*
/usr/X11R6/man/man5/XF86Config.5*
%endif

%ifarch i386 i486 i586 i686 alpha

%files Mono
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/XF86_Mono
/usr/X11R6/man/man1/XF86_Mono.1*
/usr/X11R6/man/man5/XF86Config.5*
%endif

%ifarch i386 i486 i586 i686 alpha

%files S3
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/XF86_S3
/usr/X11R6/man/man1/XF86_S3.1*
/usr/X11R6/man/man1/XF86_Accel.1*
/usr/X11R6/man/man5/XF86Config.5*
%endif

%ifarch i386 i486 i586 i686 alpha

%files S3V
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/XF86_S3V
/usr/X11R6/man/man1/XF86_S3.1*
/usr/X11R6/man/man1/XF86_Accel.1*
/usr/X11R6/man/man5/XF86Config.5*
%endif

%ifarch i386 i486 i586 i686

%files 8514
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/XF86_8514
/usr/X11R6/man/man1/XF86_8514.1*
/usr/X11R6/man/man1/XF86_Accel.1*
/usr/X11R6/man/man5/XF86Config.5*
%endif

%ifarch i386 i486 i586 i686

%files Mach8
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/XF86_Mach8
/usr/X11R6/man/man1/XF86_Mach8.1*
/usr/X11R6/man/man1/XF86_Accel.1*
/usr/X11R6/man/man5/XF86Config.5*
%endif

%ifarch i386 i486 i586 i686

%files Mach32
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/XF86_Mach32
/usr/X11R6/man/man1/XF86_Mach32.1*
/usr/X11R6/man/man1/XF86_Accel.1*
/usr/X11R6/man/man5/XF86Config.5*
%endif

%files Mach64
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/XF86_Mach64
/usr/X11R6/man/man1/XF86_Mach64.1*
/usr/X11R6/man/man1/XF86_Accel.1*
/usr/X11R6/man/man5/XF86Config.5*

%ifarch i386 i486 i586 i686 alpha

%files P9000
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/XF86_P9000
/usr/X11R6/man/man1/XF86_P9000.1*
/usr/X11R6/man/man1/XF86_Accel.1*
/usr/X11R6/man/man5/XF86Config.5*
%endif

%ifarch i386 i486 i586 i686

%files AGX
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/XF86_AGX
/usr/X11R6/man/man1/XF86_AGX.1*
/usr/X11R6/man/man1/XF86_Accel.1*
/usr/X11R6/man/man5/XF86Config.5*
%endif

%ifarch i386 i486 i586 i686

%files I128
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/XF86_I128
/usr/X11R6/man/man1/XF86_I128.1*
/usr/X11R6/man/man1/XF86_Accel.1*
/usr/X11R6/man/man5/XF86Config.5*
%endif

%ifarch alpha

%files TGA
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/XF86_TGA
/usr/X11R6/man/man5/XF86Config.5*
%endif

%ifarch sparc

%files Sun
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/Xsun
%attr(-,root,root) /usr/X11R6/lib/X11/xkb
/var/state/xkb
%endif

%ifarch sparc

%files SunMono
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/XsunMono
%attr(-,root,root) /usr/X11R6/lib/X11/xkb
/var/state/xkb
%endif

%ifarch sparc

%files Sun24
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/Xsun24
%attr(-,root,root) /usr/X11R6/lib/X11/xkb
/var/state/xkb
%endif

%ifarch i386 i486 i586 i686

%files 3DLabs
%attr(755,root,root) /usr/X11R6/bin/XF86_3DLabs
%endif

%files FBDev
%defattr(644,root,root,755)
%ifarch m68k
%attr(755,root,root) /usr/X11R6/bin/XF68_FBDev
/usr/X11R6/man/man1/XF68_FBDev.1*
%else
%attr(755,root,root) /usr/X11R6/bin/XF86_FBDev
%endif

%files XF86Setup
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/XF86Setup
%attr(755,root,root) /usr/X11R6/bin/xmseconfig
/usr/X11R6/lib/X11/XF86Setup
/usr/X11R6/man/man1/XF86Setup.1*
/usr/X11R6/man/man1/xmseconfig.1*
