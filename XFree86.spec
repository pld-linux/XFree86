
%define         _sver %(echo %{version} | tr -d .)

Summary:	XFree86 Window System servers and basic programs
Summary(de):	Xfree86 Window-System-Server und grundlegende Programme
Summary(es):	Programas básicos y servidores para el sistema de ventanas XFree86
Summary(fr):	Serveurs du système XFree86 et programmes de base
Summary(pl):	XFree86 Window System wraz z podstawowymi programami
Summary(tr):	XFree86 Pencereleme Sistemi sunucularý ve temel programlar
Summary(pt_BR):	Programas básicos e servidores para o sistema de janelas XFree86
Name:		XFree86
Version:	4.2.0
Release:	0.8
License:	MIT
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(es):	X11/XFree86
Group(fr):	X11/XFree86
Group(pl):	X11/XFree86
Group(pt_BR):	X11/XFree86
Group(tr):	X11/XFree86
Source0:	ftp://ftp.xfree86.org/pub/XFree86/%{version}/source/X%{_sver}src-1.tgz
Source1:	ftp://ftp.pld.org.pl/software/xinit/xdm-xinitrc-0.2.tar.bz2
Source2:	xdm.pamd
Source3:	xserver.pamd
Source4:	xdm.init
Source5:	xfs.init
Source6:	xfs.config
Source7:	XTerm.ad-pl
Source8:	xdm.sysconfig
Source9:	xfs.sysconfig
Source10:	twm.desktop
Source11:	xclipboard.desktop
Source12:	xconsole.desktop
Source13:	xterm.desktop
Source14:	xlogo64.png
Source15:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-Xman-pages.tar.bz2
Patch0:		%{name}-PLD.patch
Patch1:		%{name}-HasZlib.patch
Patch2:		%{name}-DisableDebug.patch
Patch3:		%{name}-Xwrapper.patch
Patch4:		%{name}-xfs.patch
Patch5:		%{name}-xfs-fix.patch
Patch6:		%{name}-xfs-logger.patch
Patch7:		%{name}-xterm-utempter.patch
Patch8:		%{name}-app_defaults_dir.patch
Patch9:		%{name}-v4l.patch
Patch10:	%{name}-broken-includes.patch
Patch11:	%{name}-alpha-pcibus-lemming.patch
Patch12:	%{name}-fhs.patch
Patch13:	%{name}-xdmsecurity.patch
Patch14:	%{name}-xman.patch
Patch15:	%{name}-HasXdmAuth.patch
Patch16:	%{name}-xdm-fixes.patch
Patch17:	%{name}-imake-kernel-version.patch
Patch18:	%{name}-no-kernel-modules.patch
Patch19:	%{name}-parallelmake.patch
Patch20:	%{name}-pic.patch
Patch21:	%{name}-r128-busmstr2.patch
Patch22:	%{name}-neomagic_swcursor.patch
Patch23:	%{name}-mga-busmstr.patch
Patch24:	%{name}-agpgart-load.patch
Patch25:	%{name}-mkfontdir-chmod_644.patch
Patch26:	%{name}-HasFreetype2.patch
Patch27:	%{name}-config-s3.patch
Patch28:	%{name}-sparc_pci_domains.patch
Patch29:	%{name}-s3virge_mx_console_corruption_fix.patch
Patch30:	%{name}-dri_directory_mode_fix.patch
Patch31:	%{name}-alpha_GLX_align_fix.patch
Patch32:	%{name}-XftConfig_in_correct_place.patch
Patch33:        %{name}-compaq-alpha-megapatch.patch
Patch34:	%{name}-PEX+XIE.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	gcc-c++
BuildRequires:	ncurses-devel
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRequires:	tcl-devel
BuildRequires:	utempter-devel
BuildRequires:	zlib-devel
%ifarch %{ix86} alpha
BuildRequires:	Glide3-DRI-devel
%endif
# Required by xc/programs/Xserver/hw/xfree86/drivers/glide/glide_driver.c
%ifarch %{ix86}
BuildRequires:	Glide2x_SDK
%endif
Requires:	xauth
Requires:	%{name}-common
Requires(post):	fileutils
ExclusiveArch:	%{ix86} alpha sparc m68k armv4l noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	xpm-progs
Obsoletes:	xterm

%ifarch sparc sparc64
Obsoletes:	X11R6.1
%endif

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_wmpropsdir	%{_datadir}/wm-properties

# avoid Mesa dependency in XFree86-OpenGL-libs
# Glide3 (libglide3.so.3) can be provided by Glide_V3-DRI or Glide_V5-DRI
%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libOSMesa.so.3.3   libglide3.so.3

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
X-Window ist eine voll funktionsfähige grafische Benutzeroberfläche
mit mehreren Fenstern, mehreren Clients und verschiedenen Arten von
Fenstern. Es kommt auf den meisten Unix-Plattformen zum Einsatz. Die
Clients lassen sich auch mit Hilfe anderer Fenstersysteme anzeigen.
Das X-Protokoll gestattet die Ausführung der Applikationen direkt auf
lokalen Rechnern oder über ein Netz und bietet große Flexibilität bei
Client-Server-Implementierungen.

%description -l es
X Window es una interface gráfica completa con múltiples ventanas,
múltiples clientes y diferentes estilos de ventanas. Se usa en la
mayoría de las plataformas Unix, y los clientes también pueden
ejecutar en otros sistemas de ventanas populares. El protocolo X
permite que las aplicaciones puedan ejecutarse tanto en la máquina
local como a través de la red, y proveer flexibilidad en
implementaciones cliente/servidor. Este paquete contiene las fuentes
básicas, programas y documentación para una estación de trabajo X. No
ofrece un servidor X que acceda tu hardware de vídeo -- estos son
puestos a disposición en otro paquete.

%description -l pl
X Window System jest graficznym interfejsem u¿ytkownika; cechuje siê
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

%description -l pt_BR
X Window é uma interface gráfica completa com múltiplas janelas,
múltiplos clientes e diferentes estilos de janelas. É usado na maioria
das plataformas Unix, e clientes também podem rodar em outros sistemas
de janelas populares. O protocolo X permite que aplicações possam
rodar tanto na máquina local como através da rede, provendo
flexibilidade em implementações cliente/servidor.

Este pacote contém as fontes básicas, programas e documentação para
uma estação de trabalho X. Ele não fornece um servidor X que acessa
seu hardware de vídeo -- estes são disponibilizados em outro pacote.

%package common
Summary:	XFree86 files required both on server and client side
Summary(pl):	Pliki XFree86 wymagane zarówno po stronie serwera jak i klienta
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86

%description common
XFree86 files required both on server and client side.

%description common -l pl
Pliki XFree86 wymagane zarówno po stronie serwera jak i klienta.

%package DPS
Summary:	Display PostScript
Summary(pl):	Display PostScript
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Provides:	DPS
Obsoletes:	dgs

%description DPS
X-Window Display PostScript is device-independent imaging model for
displaying information on a screen.

%description DPS -l pl
X-Window Display PostScript to niezale¿ny od urz±dzenia model
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
Header files for develop X-Window Display Postscript.

%description DPS-devel -l pl
Pliki nag³ówkowe biblioteki X-Window Display PostScript.

%package DPS-static
Summary:	Display PostScript
Summary(pl):	Display PostScript
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-DPS-devel = %{version}
Obsoletes:	dgs-static

%description DPS-static
X-Window Display PostScript static libraries.

%description DPS-static -l pl
Statyczne biblioteki X-Window Display PostScript.

%package PEX
Summary:	PEX extension library
Summary(pl):	Biblioteka rozszerzenia PEX
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-libs = %{version}

%description PEX
PEX extension library. Since XFree86 4.2.0 it's no longer included by
default.

%description PEX -l pl
Biblioteka rozszerzenia PEX. Od wersji XFree86 4.2.0 nie jest ju¿
do³±czane domy¶lnie.

%package PEX-devel
Summary:	PEX extension headers
Summary(pl):	Pliki nag³ówkowe rozszerzenia PEX
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-PEX = %{version}

%description PEX-devel
PEX extension headers.

%description PEX-devel -l pl
Pliki nag³ówkowe rozszerzenia PEX.

%package PEX-static
Summary:	PEX extension static library
Summary(pl):	Statyczna biblioteka rozszerzenia PEX
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-PEX-devel = %{version}

%description PEX-static
PEX extension static library.

%description PEX-static -l pl
Statyczna biblioteka rozszerzenia PEX.

%package XIE
Summary:	XIE extension library
Summary(pl):	Biblioteka rozszerzenia XIE
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-libs = %{version}

%description XIE
XIE (X Image Extension) extension library. Since XFree86 4.2.0 it's no
longer included by default.

%description XIE -l pl
Biblioteka rozszerzenia XIE (X Image Extension). Od wersji XFree86
4.2.0 nie jest ju¿ do³±czane domy¶lnie

%package XIE-devel
Summary:	XIE extension headers
Summary(pl):	Pliki nag³ówkowe rozszerzenia XIE
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-XIE = %{version}

%description XIE-devel
XIE extension headers.

%description XIE-devel -l pl
Pliki nag³ówkowe rozszerzenia XIE.

%package XIE-static
Summary:	XIE extension static library
Summary(pl):	Statyczna biblioteka rozszerzenia XIE
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-XIE-devel = %{version}

%description XIE-static
XIE extension static library.

%description XIE-static -l pl
Statyczna biblioteka rozszerzenia XIE.

%package OpenGL-core
Summary:	OpenGL support for X11R6
Summary(pl):	Wsparcie OpenGL dla systemu X11R6
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-libs = %{version}

%description OpenGL-core
OpenGL support for X11R6 system.

%description OpenGL-core -l pl
Wsparcie OpenGL dla systemu X11R6.

%package OpenGL-devel
Summary:	OpenGL for X11R6 development
Summary(pl):	Pliki nag³ówkowe OpenGL dla systemu X11R6
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-OpenGL-libs = %{version}
Requires:	%{name}-devel
Provides:	OpenGL-devel
Obsoletes:	Mesa-devel
Obsoletes:	glxMesa-devel
Obsoletes:	XFree86-OpenGL-doc

%description OpenGL-devel
Headers and man pages for OpenGL for X11R6.

%description OpenGL-devel -l pl
Pliki nag³ówkowe i manuale do OpenGL dla systemu X11R6.

%package OpenGL-libs
Summary:	OpenGL libraries for X11R6
Summary(pl):	Biblioteki OpenGL dla systemu X11R6
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-libs = %{version}
Requires:	%{name}-OpenGL-core
Provides:	OpenGL
Obsoletes:	%{name}-OpenGL
Obsoletes:	Mesa

%description OpenGL-libs
OpenGL libraries for X11R6 system.

%description OpenGL-libs -l pl
Biblioteki OpenGL dla systemu X11R6.

%package OpenGL-static
Summary:	X11R6 static libraries with OpenGL
Summary(pl):	Biblioteki statyczne do X11R6 ze wsparciem dla OpenGL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-OpenGL-devel = %{version}
Provides:	OpenGL-static
Obsoletes:	Mesa-static

%description OpenGL-static
X11R6 static libraries with OpenGL.

%description OpenGL-static -l pl
Biblioteki statyczne zawieraj±ce wsparcie dla OpenGL do X11R6.

%package Xnest
Summary:	XFree86 Xnest server
Summary(pl):	Serwer XFree86 Xnest
Group:		X11/XFree86/Servers
Group(de):	X11/XFree86/Server
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-common /usr/X11R6/lib/X11/rgb.txt
Requires:	XFree86-fonts-base

%description Xnest
Xnest is an X Window System server which runs in an X window. Xnest is
a 'nested' window server, actually a client of the real X server,
which manages windows and graphics requests for Xnest, while Xnest
manages the windows and graphics requests for its own clients.

You will need to install Xnest if you require an X server which will
run as a client of your real X server (perhaps for testing purposes).

%description Xnest -l pl
Xnest jest X serwerem uruchamianym w okienku innego X serwera. Xnest
zachowuje siê jak X klient w stosunku do prawdziwego X serwera, a jak
X serwer dla w³asnych klientów.

%package Xprt
Summary:	X print server
Summary(pl):	X serwer z rozszerzeniem Xprint
Group:		X11/XFree86/Servers
Group(de):	X11/XFree86/Server
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-common /usr/X11R6/lib/X11/rgb.txt
Requires:	XFree86-fonts-base

%description Xprt
Xprt provides an X server with the print extension and special DDX
implementation.

%description Xprt -l pl
Xprt jest X serwerem z rozszerzeniem Xprint.

%package Xserver
Summary:	XFree86 X display server
Summary(de):	XFree86 Server
Summary(fr):	Serveur XFree86
Summary(pl):	Serwer XFree86
Summary(tr):	XFree86 sunucusu
Group:		X11/XFree86/Servers
Group(de):	X11/XFree86/Server
Group(pl):	X11/XFree86/Serwery
Requires:	pam
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-common /usr/X11R6/lib/X11/rgb.txt
Requires:	XFree86-fonts-base
Obsoletes:	XFree86-VGA16 XFree86-SVGA XFree86-Mono
# obsoleted by many drivers: suncg3,suncg6,suncg14,sunffb,sunleo,suntcx
Obsoletes:	XFree86-Sun XFree86-Sun24
# still not supported in 4.2.0:
#Obsoletes:	XFree86-Mach8 XFree86-8514 XFree86-AGX XFree86-P9000
# (and many drivers from XF86_SVGA server... and some from others)
Obsoletes:	XFree86-XF86Setup Xconfigurator

%description Xserver
Generally used X server which uses display hardware. It requires
proper driver for your display hardware - package itself contains only
drivers for VGA and VESA-compliant cards (without acceleration). Other
drivers can be found in XFree86-driver-* packages.

%description Xserver -l de
X-Server für die elementarsten Framebuffer-SVGA-Geräte, einschließlich
Karten, die aus ET4000-Chips, Cirrus Logic-Chips, Chips and
Technologies Laptop-Chips sowie Trident 8900 und 9000 Chips gebaut
sind. Funktioniert mit Diamond Speedstar, Orchid Kelvins, STB Nitros
und Horizons, Genoa 8500VL, den meisten Actix-Karten sowie Spider VLB
Plus und außerdem mit vielen anderen Chips und Karten. Es lohnt sich,
diesen Server auszuprobieren, wenn Sie Probleme haben.

%description Xserver -l fr
Serveur X pour les circuits SVGA les plus simples, dont les cartes
construites avec les circuits ET4000, Cirrus Logic, Chips and
Technologies laptop, Trident 8900 et 9000. Fonctionne pour les cartes
Diamond Speedstar, Orchid Kelvins, STB Nitros et Horizons, Genoa
8500VL, la plupart des Actix et la Spider VLB Plus. Fonctionne aussi
pour de nombreux autres circuits et cartes. Essayez ce serveur si vous
avez des problèmes.

%description Xserver -l pl
Jest to podstawowy Xserwer wy¶wietlaj±cy obraz na karcie graficznej.
Do dzia³ania wymaga odpowiedniego sterownika - sam pakiet zawiera
tylko odpowiedni dla kart VGA oraz SVGA zgodnych z VESA (bez
akceleracji). Inne sterowniki mo¿na znale¼æ w pakietach
XFree86-driver-*.

%description Xserver -l tr
ET4000, Cirrus Logic, Chips and Technologies dizüstü, Trident 8900 ve
9000 gibi basit 'framebuffer' SVGA kullananan kartlar için X sunucusu.
Ayný zamanda Diamond Speedstar, Orchid Kelvins, STB Nitros / Horizons,
Genoa 8500VL, çoðu Actix kartlarý, Spider VLB Plus gibi kartlar ve
birçok diðer kart ile de çalýþýr. Herhangi bir sorun yaþarsanýz bu
sunucuyu deneyin.

%package Xvfb
Summary:	XFree86 Xvfb server
Summary(pl):	Serwer XFree86 Xvfb
Group:		X11/XFree86/Servers
Group(de):	X11/XFree86/Server
Group(pl):	X11/XFree86/Serwery
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-common /usr/X11R6/lib/X11/rgb.txt
Requires:	XFree86-fonts-base

%description Xvfb
Xvfb (X Virtual Frame Buffer) is an X Window System server that is
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

%description Xvfb -l pl
Xvfb (X Virtual Frame Buffer) jest X serwerem, który mo¿na uruchamiaæ
na maszynach bez urz±dzeñ wy¶wietlaj±cych ani fizycznych urz±dzeñ
wej¶ciowych. Xvfb emuluje prosty framebuffer w pamiêci. Zwykle jest
u¿ywany do testowania X serwerów, mo¿e te¿ byæ u¿ywany do testowania X
klientów w rzadko u¿ywanych konfiguracjach ekranu. Mo¿na te¿ u¿yæ Xvfb
do uruchomienia aplikacji, które w rzeczywisto¶ci nie wymagaj± X
serwera, ale odmawiaj± uruchomienia bez niego.

%package devel
Summary:	X11R6 headers and programming man pages
Summary(de):	X11R6 Headers und man pages für Programmierer
Summary(fr):	Pages man de programmation
Summary(pl):	Pliki nag³ówkowe X11R6
Summary(tr):	X11R6 ile geliþtirme için gerekli dosyalar
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-libs = %{version}
Obsoletes:	xpm-devel
Provides:	xpm-devel
%ifarch sparc sparc64
Obsoletes:	X11R6.1-devel
%endif

%description devel
Libraries, header files, and documentation for developing programs
that run as X clients. It includes the base Xlib library as well as
the Xt and Xaw widget sets. For information on programming with these
libraries, PLD recommends the series of books on X Programming
produced by O'Reilly and Associates.

%description devel -l de
Libraries, Header-Dateien und Dokumentation zum Entwickeln von
Programmen, die als X-Clients laufen. Enthält die Xlib-Library und die
Widget-Sätze Xt und Xaw. Information zum Programmieren mit diesen
Libraries finden Sie in der Buchreihe zur X-Programmierung von
O'Reilly and Associates.

%description devel -l fr
Bibliothéques, fichiers d'en-tête, et documentation pour développer
des programmes s'exécutant en clients X. Cela comprend la Bibliothéque
Xlib de base aussi bien que les ensembles de widgets Xt et Xaw. Pour
des informations sur la programmation avec ces Bibliothéques, Red Hat
recommande la série d'ouvrages sur la programmation X editée par
O'Reilly and Associates.

%description devel -l pl
Pliki nag³ówkowe, dokumentcja dla programistów rozwijaj±cych aplikacje
klienckie pod X Window. Zawiera podstawow± bibliotekê Xlib a tak¿e Xt
i Xaw. Wiêcej informacji nt. pisania programów przy u¿yciu tych
bibliotek mo¿esz znale¼æ w ksi±¿kach wydawnictwa O'Reilly and
Associates (X Programming) polecanych przez Red Hata.

%description devel -l tr
X istemcisi olarak çalýþacak programlar geliþtirmek için gereken
statik kitaplýklar, baþlýk dosyalarý ve belgeler. Xlib kitaplýðýnýn
yanýsýra Xt ve Xaw arayüz kitaplýklarýný da içerir.

%package driver-apm
Summary:	Alliance Promotion video driver
Summary(pl):	Sterownik do kart Alliance Promotion
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-Alliance

%description driver-apm
Alliance Promotion driver.

%description driver-apm -l pl
Sterownik do kart Alliance Promotion.

%package driver-ark
Summary:	Ark Logic video driver
Summary(pl):	Sterownik do kart Ark Logic
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-ark
Ark Logic driver.

%description driver-ark -l pl
Sterownik do kart Ark Logic.

%package driver-ati
Summary:	ATI video driver
Summary(pl):	Sterownik do kart ATI
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-ATI XFree86-Mach32 XFree86-Mach64

%description driver-ati
ATI video driver.

%description driver-ati -l pl
Sterownik do kart ATI.

%package driver-chips
Summary:	Chips and Technologies video driver
Summary(pl):	Sterownik do kart na uk³adach Chips and Technologies
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-ChipsTechnologies

%description driver-chips
Chips and Technologies video driver.

%description driver-chips -l pl
Sterownik do kart na uk³adach Chips and Technologies.

%package driver-cirrus
Summary:	Cirrus Logic video driver
Summary(pl):	Sterownik do kart Cirrus Logic
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-Cirrus

%description driver-cirrus
Cirrus Logic video driver.

%description driver-cirrus -l pl
Sterownik do kart Cirrus Logic.

%package driver-cyrix
Summary:	Cyrix video driver
Summary(pl):	Sterownik do grafiki na uk³adzie Cyrix MediaGX
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-Cyrix

%description driver-cyrix
Cyrix video driver.

%description driver-cyrix -l pl
Sterownik do grafiki na uk³adzie Cyrix MediaGX.

%package driver-fbdev
Summary:	Video driver for framebuffer device
Summary(pl):	Sterownik korzystaj±cy z framebuffera
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-FBDev

%description driver-fbdev
Non-accelerated video driver for framebuffer device.

%description driver-fbdev -l pl
Nieakcelerowany sterownik korzystaj±cy z framebuffera.

%package driver-ffb
Summary:	Video driver for DRI sparc framebuffer device
Summary(pl):	Sterownik do framebuffera DRI na sparc
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-ffb
Video driver for DRI sparc framebuffer device.

%description driver-ffb -l pl
Sterownik do framebuffera DRI na sparc.

%package driver-glide
Summary:	3Dfx Voodoo1 and Voodoo2 video driver
Summary(pl):	Sterownik do kart 3Dfx Voodoo1 i Voodoo2
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-glide
Voodoo1 and Voodoo2 video driver.

%description driver-glide -l pl
Sterownik do kart Voodoo1 i Voodoo2 firmy 3Dfx.

%package driver-glint
Summary:	GLINT/Permedia video driver
Summary(pl):	Sterownik do kart GLINT i Permedia
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	OpenGL
Obsoletes:	XFree86-3DLabs

%description driver-glint
GLINT/Permedia video driver.

%description driver-glint -l pl
Sterownik do kart GLINT i Permedia.

%package driver-i128
Summary:	Number 9 I128 video driver
Summary(pl):	Sterownik do kart Number 9 I128
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-I128

%description driver-i128
Number 9 I128 video driver.

%description driver-i128 -l pl
Sterownik do kart Number 9 I128.

%package driver-i740
Summary:	Intel i740 video driver
Summary(pl):	Sterownik do kart na uk³adzie Intel i740
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-i740

%description driver-i740
Intel i740 video driver.

%description driver-i740 -l pl
Sterownik do kart na uk³adzie Intel i740.

%package driver-i810
Summary:	Intel i810/i815 video driver
Summary(pl):	Sterownik do grafiki na uk³adach Intel i810 i i815
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	OpenGL
Obsoletes:	XFree86-i810

%description driver-i810
Intel i810/i815 video driver.

%description driver-i810 -l pl
Sterownik do grafiki na uk³adach Intel i810 i i815.

%package driver-mga
Summary:	Matrox video driver
Summary(pl):	Sterownik do kart Matrox
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	OpenGL
Obsoletes:	XFree86-mga

%description driver-mga
Matrox video driver.

%description driver-mga -l pl
Sterownik do kart Matrox.

%package driver-neomagic
Summary:	NeoMagic video driver
Summary(pl):	Sterownik do kart NeoMagic
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-NeoMagic

%description driver-neomagic
NeoMagic video driver.

%description driver-neomagic -l pl
Sterownik do kart NeoMagic.

%package driver-nv
Summary:	nVidia video driver
Summary(pl):	Sterownik do kart na uk³adach firmy nVidia
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-NVidia

%description driver-nv
nVidia video driver. Supports Riva128, RivaTNT, GeForce.

%description driver-nv -l pl
Sterownik do kart na uk³adach firmy nVidia: Riva128, RivaTNT, GeForce.

%package driver-r128
Summary:	ATI Rage 128 video driver
Summary(pl):	Sterownik do kart ATI Rage 128
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	OpenGL
Obsoletes:	XFree86-Rage128

%description driver-r128
ATI Rage 128 video driver.

%description driver-r128 -l pl
Sterownik do kart ATI Rage 128.

%package driver-radeon
Summary:	ATI Radeon video driver
Summary(pl):	Sterownik do kart ATI Radeon
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	OpenGL

%description driver-radeon
ATI Radeon video driver.

%description driver-radeon -l pl
Sterownik do kart ATI Radeon.

%package driver-rendition
Summary:	Rendition video driver
Summary(pl):	Sterownik do kart Rendition
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-Rendition

%description driver-rendition
Rendition/Micron video driver.

%description driver-rendition -l pl
Sterownik do kart Verite firmowanych przez Rendition/Micron.

%package driver-s3virge
Summary:	S3 ViRGE/Trio3D video driver
Summary(pl):	Sterownik do kart na uk³adach S3 ViRGE i Trio3D
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-S3V

%description driver-s3virge
S3 ViRGE/Trio3D video driver.

%description driver-s3virge -l pl
Sterownik do kart na uk³adach S3 ViRGE i Trio3D.

%package driver-s3
Summary:	S3 Trio video driver
Summary(pl):	Sterownik do kart na uk³adach S3 Trio
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-S3

%description driver-s3
S3 Trio video driver.

%description driver-s3 -l pl
Sterownik do kart na uk³adach S3 Trio.

%package driver-savage
Summary:	S3 Savage video driver
Summary(pl):	Sterownik do kart na uk³adach S3 Savage
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-savage
S3 Savage video driver.

%description driver-savage -l pl
Sterownik do kart na uk³adach S3 Savage.

%package driver-siliconmotion
Summary:	Silicon Motion video driver
Summary(pl):	Sterownik do kart na uk³adach Silicon Motion
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-siliconmotion
Silicon Motion video driver.

%description driver-siliconmotion -l pl
Sterownik do kart na uk³adach Lynx firmy Silicon Motion.

%package driver-sis
Summary:	SiS video driver
Summary(pl):	Sterownik do kart na uk³adach SiS
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-SiS

%description driver-sis
SiS video driver.

%description driver-sis -l pl
Sterownik do kart na uk³adach SiS.

%package driver-sunbw2
Summary:	sunbw2 - Sun BW2 video driver
Summary(pl):	Sterownik do monochromatycznego framebuffera BW2 na Sunie
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-SunMono

%description driver-sunbw2
sunbw2 - Sun BW2 video driver.

%description driver-sunbw2 -l pl
Sterownik do monochromatycznego framebuffera BW2 na Sunie.

%package driver-suncg14
Summary:	suncg14 - Sun CG14 video driver
Summary(pl):	Sterownik do kolorowego framebuffera CG14 na Sunie
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-suncg14
suncg14 - Sun CG14 video driver.

%description driver-suncg14 -l pl
Sterownik do kolorowego framebuffera CG14 na Sunie.

%package driver-suncg3
Summary:	suncg3 - Sun CG3 video cards driver
Summary(pl):	Sterownik do kolorowego framebuffera CG3 na Sunie
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-suncg3
suncg3 - Sun CG3 video cards driver.

%description driver-suncg3 -l pl
Sterownik do kolorowego framebuffera CG3 na Sunie.

%package driver-suncg6
Summary:	suncg6 - Sun GX and Turbo GX video driver
Summary(pl):	Sterownik do grafiki GX i Turbo GX na Sunie
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-suncg6
suncg6 - Sun GX and Turbo GX video driver.

%description driver-suncg6 -l pl
Sterownik do grafiki GX i Turbo GX na Sunie.

%package driver-sunffb
Summary:	sunffb - Sun Creator, Creator 3D and Elite 3D video cards driver
Summary(pl):	Sterownik do kart Sun Creator, Creator 3D, Elite 3D
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-sunffb
sunffb - Sun Creator, Creator 3D and Elite 3D video cards driver.

%description driver-sunffb -l pl
Sterownik do kart Sun Creator, Creator 3D, Elite 3D.

%package driver-sunleo
Summary:	sunleo - Sun Leo (ZX) video cards driver
Summary(pl):	Sterownik do kart Sun Leo (ZX)
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-sunleo
sunleo - Sun Leo (ZX) video cards driver.

%description driver-sunleo -l pl
Sterownik do kart Sun Leo (ZX).

%package driver-suntcx
Summary:	suntcx - Sun TCX video cards driver
Summary(pl):	Sterownik do kart Sun TCX
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-suntcx
suntcx - Sun TCX video cards driver.

%description driver-suntcx -l pl
Sterownik do kart Sun TCX.

%package driver-tdfx
Summary:	3Dfx video driver
Summary(pl):	Sterownik do kart 3Dfx
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	OpenGL
Requires:	Glide3-DRI
Obsoletes:	XFree86-3dfx

%description driver-tdfx
3Dfx video driver. Supports Voodoo Banshee, Voodoo3, Voodoo4, Voodoo5.
For Banshee or Voodoo3, DRI driver requires Glide_V3-DRI package, for
Voodoo4 or Voodoo5 it requires Glide_V5-DRI package.

%description driver-tdfx -l pl
Sterownik do kart 3Dfx: Voodoo Banshee, Voodoo3, Voodoo4, Voodoo5.
Sterownik DRI wymaga pakietu Glide_V3-DRI do kart Banshee lub Voodoo3,
a Glide_V5-DRI do kart Voodoo4 lub Voodoo5.

%package driver-tga
Summary:	TGA video driver
Summary(pl):	Sterownik do kart TGA
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-TGA

%description driver-tga
TGA video driver.

%description driver-tga -l pl
Sterownik do kart TGA.

%package driver-trident
Summary:	Trident video driver
Summary(pl):	Sterownik do kart Trident
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-Trident

%description driver-trident
Trident video driver.

%description driver-trident -l pl
Sterownik do kart Trident.

%package driver-tseng
Summary:	Tseng Labs video driver
Summary(pl):	Sterownik do kart Tseng Labs
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-Tseng XFree86-W32

%description driver-tseng
Tseng Labs video driver.

%description driver-tseng -l pl
Sterownik do kart firmy Tseng Labs.

%package driver-vmware
Summary:	VMWare SVGA video driver
Summary(pl):	Sterownik do emulowanych kart SVGA pod VMware
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-vmware
VMware SVGA video driver.

%description driver-vmware -l pl
Sterownik do emulowanych kart SVGA pod VMware.

%package libs
Summary:	X11R6 shared libraries
Summary(de):	X11R6 shared Libraries
Summary(es):	Bibliotecas compartidas X11R6
Summary(pl):	Biblioteki dzielone dla X11R6
Summary(fr):	Bibliothèques partagées X11R6
Summary(pt_BR):	Bibliotecas compartilhadas X11R6
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(es):	X11/XFree86
Group(fr):	X11/XFree86
Group(pl):	X11/XFree86
Group(pt_BR):	X11/XFree86
PreReq:		/sbin/ldconfig
PreReq:		grep
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

If you are installing the X Window System on your machine, you will
need to install XFree86-libs. You will also need to install the
XFree86 package, XFree86-Xserver, one of the XFree86-driver-*,
XFree86-fonts, XFree86-fonts-ISO8859-1, optionally some of the other
fonts (choose 75dpi or 100dpi depending upon your monitor's
resolution), the XFree86-setup and the XFree86-tools. And, finally, if
you are going to be developing applications that run as X clients, you
will also need to install XFree86-devel.

%description libs -l de
Dieses Paket enthält die zur gemeinsamen Nutzung vorgesehenen
Libraries, die die meisten X-Programme für den einwandfreien Betrieb
benötigen. Sie wurden in einem separaten Paket untergebracht, um den
Festplattenspeicherplatz auf Computern zu reduzieren, die ohne einen
X- Server (über ein Netz) arbeiten.

%description libs -l es
Este paquete contiene bibliotecas compartidas que la mayoría de los
programas X necesitan para ejecutarse correctamente. Están en un
paquete a parte, para reducir el espacio en disco necesario para
ejecutar aplicaciones X en una máquina sin un servidor X (a través de
la red).

%description libs -l fr
Ce paquetage contient les bibliothèques partagées nécessaires à de
nombreux programmes X. Elles se trouvent dans un paquetage séparé afin
de réduire l'espace disque nécessaire à l'exécution des applications X
sur une machine sans serveur X (en réseau).

%description libs -l pl
Pakiet zawieraj±cy podstawowe biblioteki potrzebne wiêkszo¶ci
programów korzystaj±cych z systemu X Window. Wydzielony w celu
oszczêdno¶ci miejsca potrzebnego do uruchamiania aplikacji X Window na
komputerach bez X serwera (np. przez sieæ).

%description libs -l tr
Bu paket X programlarýnýn düzgün çalýþabilmeleri için gereken
kitaplýklarý içerir. Bunlar, X programlarýný (sunucu olsun olmasýn)
çalýþtýrmak için gerekli disk alanýný azaltmak için ayrý bir paket
olarak sunulmuþtur.

%description libs -l pt_BR
Este pacote contém bibliotecas compartilhadas que a maioria dos
programas X precisam para rodar corretamente. Eles estão em um pacote
separado para reduzir o espaço em disco necessário para rodar
aplicações X em uma máquina sem um servidor X (através da rede).

%package modules
Summary:	Modules with X servers extensions
Summary(pl):	Wspólne dla wszystkich X serwerów modu³y rozszerzeñ
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(es):	X11/XFree86
Group(fr):	X11/XFree86
Group(pl):	X11/XFree86
Group(pt_BR):	X11/XFree86

%description modules
Modules with X servers extensions.

%description modules -l pl
Wspólne dla wszystkich X serwerów modu³y rozszerzeñ.

%package module-PEX
Summary:	PEX extension module
Summary(pl):	Modu³ rozszerzenia PEX
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}

%description module-PEX
PEX extension module for X server. Since XFree86 4.2.0 it's no longer
included by default.

%description module-PEX -l pl
Modu³ rozszerzenia PEX dla X serwera. Od wersji XFree86 4.2.0 nie jest
ju¿ do³±czane domy¶lnie.

%package module-XIE
Summary:	XIE extension module
Summary(pl):	Modu³ rozszerzenia XIE
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-modules = %{version}

%description module-XIE
XIE (X Image Extension) extension module for X server. Since XFree86
4.2.0 it's no longer included by default.

%description module-XIE -l pl
Modu³ rozszerzenia XIE (X Image Extension) dla X serwera. Od wersji
XFree86 4.2.0 nie jest ju¿ do³±czane domy¶lnie.

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

%description setup -l pl
Pakiet setup zawiera narzêdzia do konfiguracji XFree86. Pozwala na
skonfigurowanie ustawieñ obrazu, klawiatury, typu myszki i innych
ró¿nych rzeczy. Jednak¿e jest wolny i wymaga dostêpno¶ci serwera do
standardowej 16-kolorowej VGA.

%package static
Summary:	X11R6 static libraries
Summary(pl):	Biblioteki statyczne X11R6
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}
%ifarch sparc sparc64
Obsoletes:	X11R6.1-devel
%endif
Obsoletes:	xpm-static
#Obsoletes:	Mesa-static

%description static
X11R6 static libraries.

%description static -l pl
Biblioteki statyczne X11R6.

%package tools
Summary:	Various tools for XFree86
Summary(pl):	Ró¿ne narzêdzia dla XFree86
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name} >= %{version}
Requires:	XFree86-libs = %{version}
Obsoletes:	X11R6-contrib

%description tools
Various tools for X, including listres, xbiff, xedit, xeyes, xcalc,
xload and xman, among others.

If you're using X, you should install XFree86-tools. You will also
need to install the XFree86 package, the XFree86 package which
corresponds to your video card, some of the XFree86 fonts packages,
the XFree86-setup package and the XFree86-libs package.

Finally, if you are going to develop applications that run as X
clients, you will also need to install XFree86-devel.

This package contains all applications that used to be in
X11R6-contrib in older releases.

%description tools -l pl
Ró¿ne narzêdzia dla X, w tym listres, xbiff, xedit, xeyes, xcalc,
xload, xman i inne.

Je¶li u¿ywasz Xów powiniene¶ zainstalowaæ XFree86-tools. Bêdziesz
równie¿ musia³ zainstalowaæ pakiet XFree86, pakiet odpowiadaj±cy
Twojej karcie graficznej, jeden z pakietów z fontami, pakiet
Xconfigurator oraz XFree86-libs.

Wreszcie, je¶li zamierzasz tworzyæ aplikacje, które dzia³aj± jako
klienci X, bêdziesz musia³ zainstalowaæ równie¿ XFree86-devel.

Ten pakiet zawiera aplikacje, które by³y w X11R6-contrib w starszych
wersjach X.

%package -n sessreg
Summary:	sessreg - manage utmp/wtmp entries for non-init clients
Summary(pl):	Program do zarz±dzania wpisami w utmp/wtmp
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86

%description -n sessreg
sessreg is a simple program for managing utmp/wtmp entries for xdm
sessions.

System V has a better interface to /var/run/utmp than BSD; it
dynamically allocates entries in the file, instead of writing them at
fixed positions indexed by position in /etc/ttys.

%description -n sessreg -l pl
sessreg jest prostym programem do zarz±dzania wpisami w utmp/wtmp dla
sesji xdm.

System V ma lepszy ni¿ BSD interfejs do /var/run/utmp; dynamicznie
alokuje wpisy w pliku, zamiast zapisywania ich na ustalonych pozycjach
indeksowanych po³o¿eniem w /etc/ttys.

%package -n twm
Summary:	Tab Window Manager for the X Window System
Summary(pl):	Twm - podstawowy zarz±dca okien dla X Window System
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
Requires:	XFree86-libs = %{version}

%description -n twm
Twm is a window manager for the X Window System. It provides
titlebars, shaped windows, several forms of icon management,
user-defined macro functions, click-to-type and pointerdriven keyboard
focus, and user-specified key and pointer button bindings.

%description -n twm -l pl
Twm jest mened¿erem okien dla X Window System. Daje belki tytu³owe,
ramki okien, parê form zarz±dzania ikonami, definiowalne makra,
ustawianie focusu klikniêciem lub po³o¿eniem wska¼nika myszy,
definiowalne przypisania klawiszy i przycisków myszy.

%package -n xauth
Summary:	xauth - X authority file utility
Summary(pl):	xauth - narzêdzie do plików X authority
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

%description -n xauth -l pl
Program xauth s³u¿y do edycji i wy¶wietlania informacji
autoryzacyjnych u¿ywanych przy ³±czeniu z Xserwerem. Ten program
przewa¿nie jest u¿ywany do wyci±gania rekordów autoryzacji z jednej
maszyny i do³±czania ich na innej (w celu umo¿liwienia zdalnego
logowania lub udostêpnienia innym u¿ytkownikom).

%package -n xdm
Summary:	xdm - X Display Manager with support for XDMCP, host chooser
Summary(pl):	XDM - display mened¿er z obs³ug± XDMCP i wybieraniem hostów
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name} = %{version}
Requires:	pam >= 0.71
Requires:	%{name}-libs = %{version}
Requires:	sessreg = %{version}
Requires:	/usr/X11R6/bin/sessreg
Provides:	XDM
PreReq:		chkconfig
Obsoletes:	XFree86-xdm
Obsoletes:	gdm
Obsoletes:	kdm

%description -n xdm
Xdm manages a collection of X displays, which may be on the local host
or remote servers. The design of xdm was guided by the needs of X
terminals as well as the X Consortium standard XDMCP, the X Display
Manager Control Protocol.

%description -n xdm -l pl
Xdm zarz±dza zestawem ekranów X, które mog± byæ lokalne lub na
zdalnych serwerach. Zosta³ zaprojektowany zgodnie z potrzebami X
terminali oraz standardem X Consortium XDMCP.

%package -n xfs
Summary:	Font server for XFree86
Summary(pl):	Serwer fontów dla XFree86
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Requires:	%{name}-libs = %{version}
Requires:	XFree86-fonts-base
PreReq:		chkconfig
PreReq:		/usr/sbin/useradd
PreReq:		/usr/sbin/groupadd
PreReq:		/usr/sbin/userdel
PreReq:		/usr/sbin/groupdel
PreReq:		/usr/bin/getgid
PreReq:		/bin/id
Obsoletes:	xfsft XFree86-xfs

%description -n xfs
This is a font server for XFree86. You can serve fonts to other X
servers remotely with this package, and the remote system will be able
to use all fonts installed on the font server, even if they are not
installed on the remote computer.

%description -n xfs -l pl
Pakiet zawiera serwer fontów dla XFree86. Mo¿e udostêpniaæ fonty dla X
serwerów lokalnych lub zdalnych.

#--- %prep ---------------------------

%prep
%setup -q -c -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0
# not ready yet
#%patch6 -p0
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p0
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
#%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%ifarch sparc sparc64
# needs updating (14 rejects)
#%patch28 -p1
%endif
# don't see what exatly it is doing, is it needed now?
# could someone else look at it (rejects)
#%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%ifarch alpha
%patch33 -p0
%endif
%patch34 -p1

rm -f xc/config/cf/host.def

#--- %build --------------------------

%build
%{__make} -S -C xc World DEFAULT_OS_CPU_FROB=%{_target_cpu} \
	"BOOTSTRAPCFLAGS=%{rpmcflags}" \
	"CCOPTIONS=%{rpmcflags}" \
	"CXXOPTIONS=%{rpmcflags}" \
	"CXXDEBUGFLAGS=" "CDEBUGFLAGS="

#--- %install ------------------------

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{X11,pam.d,rc.d/init.d,security/console.apps,sysconfig} \
	$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/pl \
	$RPM_BUILD_ROOT%{_datadir}/{misc,sounds} \
	$RPM_BUILD_ROOT/usr/{bin,include,lib} \
	$RPM_BUILD_ROOT/var/{log,lib/xkb} \
	$RPM_BUILD_ROOT{%{_applnkdir}/{Utilities,Terminals},%{_pixmapsdir}/mini} \
	$RPM_BUILD_ROOT%{_wmpropsdir}

%{__make} -C xc	"DESTDIR=$RPM_BUILD_ROOT" \
		"DOCDIR=/usr/share/doc/%{name}-%{version}" \
		"INSTBINFLAGS=-m 755" \
		"INSTPGMFLAGS=-m 755" \
		"RAWCPP=/lib/cpp" \
		"BOOTSTRAPCFLAGS=%{rpmcflags}" \
		"CCOPTIONS=%{rpmcflags}" \
		"CXXOPTIONS=%{rpmcflags}" \
		"CXXDEBUGFLAGS=" "CDEBUGFLAGS=" \
		install install.man

# setting default X
rm -f $RPM_BUILD_ROOT%{_bindir}/X
ln -sf XFree86 $RPM_BUILD_ROOT%{_bindir}/X

# setting ghost X in /etc/X11 -- xf86config will fix this ...
ln -sf ../..%{_bindir}/XFree86 $RPM_BUILD_ROOT%{_sysconfdir}/X11/X

# add X11 links in /usr/bin, /usr/lib /usr/include
ln -sf ../X11R6/include/X11 $RPM_BUILD_ROOT/usr/include/X11
ln -sf ../X11R6/lib/X11 $RPM_BUILD_ROOT/usr/lib/X11
ln -sf ../X11R6/bin $RPM_BUILD_ROOT/usr/bin/X11

# fix libGL*.so links
rm -f $RPM_BUILD_ROOT%{_libdir}/libGL*.so
ln -sf libGL.so.1 $RPM_BUILD_ROOT%{_libdir}/libGL.so
ln -sf libGLU.so.1 $RPM_BUILD_ROOT%{_libdir}/libGLU.so

# set up PLD xdm config
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/X11/xdm/{*Console,Xaccess,Xsession,Xsetup*}
install xdm-xinitrc-*/pixmaps/* $RPM_BUILD_ROOT%{_sysconfdir}/X11/xdm/pixmaps/
install xdm-xinitrc-*/{*Console,Xaccess,Xsession,Xsetup*} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xdm/

install %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/xdm
install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/xserver
install %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/xdm
install %{SOURCE5} $RPM_BUILD_ROOT/etc/rc.d/init.d/xfs
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/X11/fs/config
install %{SOURCE7} $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/pl/XTerm

install %{SOURCE8} $RPM_BUILD_ROOT/etc/sysconfig/xdm
install %{SOURCE9} $RPM_BUILD_ROOT/etc/sysconfig/xfs

install %{SOURCE10} $RPM_BUILD_ROOT%{_wmpropsdir}/twm.desktop
install %{SOURCE11} $RPM_BUILD_ROOT%{_applnkdir}/Utilities
install %{SOURCE12} $RPM_BUILD_ROOT%{_applnkdir}/Utilities
install %{SOURCE13} $RPM_BUILD_ROOT%{_applnkdir}/Terminals

install %{SOURCE14} $RPM_BUILD_ROOT%{_datadir}/pixmaps

bzip2 -dc %{SOURCE15} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

> $RPM_BUILD_ROOT/etc/security/console.apps/xserver
> $RPM_BUILD_ROOT/etc/security/blacklist.xserver
> $RPM_BUILD_ROOT/etc/security/blacklist.xdm
> $RPM_BUILD_ROOT/var/log/XFree86.0.log

ln -sf %{_fontsdir} $RPM_BUILD_ROOT%{_libdir}/X11/fonts

# do not duplicate xkbcomp program
rm -f $RPM_BUILD_ROOT%{_libdir}/X11/xkb/xkbcomp
ln -sf %{_bindir}/xkbcomp $RPM_BUILD_ROOT%{_sysconfdir}/X11/xkb/xkbcomp

ln -sf ../../../share/doc/%{name}-%{version} \
	$RPM_BUILD_ROOT%{_libdir}/X11/doc

rm -f $RPM_BUILD_ROOT%{_libdir}/X11/config/host.def

:> $RPM_BUILD_ROOT%{_libdir}/X11/config/host.def
:> $RPM_BUILD_ROOT%{_sysconfdir}/X11/XF86Config

rm -rf $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/html

# directories for applications locales
echo '%defattr(644,root,root,755)' > XFree86-libs.lang
for lang in af az bg bg_BG.cp1251 br ca cs da de el en_GB eo es et eu fi \
	fr ga gl he hr hu is it ja ko lt mi mk nl nn no pl pt pt_BR ro ru sk \
	sl sr sv ta th tr uk wa zh_CN zh_CN.GB2312 zh_TW.Big5 ; do
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/${lang}/LC_MESSAGES
	echo "%lang(${lang}) %{_datadir}/locale/${lang}" >> XFree86-libs.lang
done

%ifnarch sparc sparc64
gzip -9nf $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/*

# don't gzip README.* files, they are needed by XF86Setup
gunzip $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/README.*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

#--- %post{un}, %preun, %verifyscript, %trigge ----------

%post
touch /var/log/XFree86.0.log
chmod 000 /var/log/XFree86.0.log
chown root.root /var/log/XFree86.0.log
chmod 640 /var/log/XFree86.0.log

%post	DPS -p /sbin/ldconfig
%postun	DPS -p /sbin/ldconfig

%post	PEX -p /sbin/ldconfig
%postun	PEX -p /sbin/ldconfig

%post	XIE -p /sbin/ldconfig
%postun	XIE -p /sbin/ldconfig

%post	OpenGL-libs -p /sbin/ldconfig
%postun	OpenGL-libs -p /sbin/ldconfig

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

%triggerpostun modules -- XFree86-modules < 4.0.2
if [ -d /usr/X11R6/lib/X11/xkb ]; then
	rm -rf /usr/X11R6/lib/X11/xkb
	ln -sf ../../../../etc/X11/xkb /usr/X11R6/lib/X11/xkb
fi

%post -n xdm
/sbin/chkconfig --add xdm
if [ -f /var/lock/subsys/xdm ]; then
	/etc/rc.d/init.d/xdm restart >&2
else
	echo "Run \"/etc/rc.d/init.d/xdm start\" to start xdm." >&2
fi

%preun -n xdm
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/xdm ]; then
		/etc/rc.d/init.d/xdm stop >&2
	fi
	/sbin/chkconfig --del xdm
fi

%pre -n xfs
if [ -n "`/usr/bin/getgid xfs`" ]; then
	if [ "`/usr/bin/getgid xfs`" != "56" ]; then
		echo "Warning: group xfs hasn't gid=56. Correct this before installing xfs." 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -g 56 -r -f xfs
fi
if [ -n "`/bin/id -u xfs 2>/dev/null`" ]; then
	if [ "`/bin/id -u xfs`" != "56" ]; then
		echo "Warning: user xfs hasn't uid=56. Corrent this before installing xfs." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 56 -r -d /etc/X11/fs -s /bin/false -c "X Font Server" -g xfs xfs 1>&2
fi

%post -n xfs
/sbin/chkconfig --add xfs
if [ -f /var/lock/subsys/xfs ]; then
	/etc/rc.d/init.d/xfs restart >&2
else
	echo "Run \"/etc/rc.d/init.d/xfs start\" to start font server." >&2
fi

%preun -n xfs
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/xfs ]; then
		/etc/rc.d/init.d/xfs stop >&2
	fi
	/sbin/chkconfig --del xfs
fi

%postun -n xfs
if [ "$1" = "0" ]; then
	/usr/sbin/userdel xfs 2>/dev/null
	/usr/sbin/groupdel xfs 2>/dev/null
fi

#--- %files --------------------------

%files
%defattr(644,root,root,755)
%ifnarch sparc sparc64
%doc %{_docdir}/%{name}-%{version}
%doc %{_libdir}/X11/doc
%endif

%{_sysconfdir}/X11/XftConfig

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

%attr(755,root,root) %{_bindir}/Xmark
%attr(755,root,root) %{_bindir}/appres
%attr(755,root,root) %{_bindir}/atobm
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

%attr(640,root,root) %ghost /var/log/XFree86.0.log

%{_applnkdir}/Utilities/xconsole.desktop
%{_applnkdir}/Terminals/*
%{_libdir}/X11/app-defaults/Xvidtune
%{_pixmapsdir}/x*

%{_mandir}/man1/Xmark.1*
%{_mandir}/man1/appres.1*
%{_mandir}/man1/atobm.1*
%{_mandir}/man1/bdftopcf.1*
%{_mandir}/man1/bitmap.1*
%{_mandir}/man1/bmtoa.1*
%{_mandir}/man1/cxpm.1*
%{_mandir}/man1/dga.1*
%{_mandir}/man1/editres.1*
%{_mandir}/man1/iceauth.1*
%{_mandir}/man1/lbxproxy.1*
%ifnarch alpha
%{_mandir}/man1/libxrx.1*
%endif
%{_mandir}/man1/lndir.1*
%{_mandir}/man1/makestrs.1*
%{_mandir}/man1/makeg.1*
%{_mandir}/man1/mkdirhier.1*
%{_mandir}/man1/mkfontdir.1*
%{_mandir}/man1/proxymngr.1*
%{_mandir}/man1/resize.1*
%{_mandir}/man1/revpath.1*
%{_mandir}/man1/rstart.1*
%{_mandir}/man1/rstartd.1*
%{_mandir}/man1/setxkbmap.1*
%{_mandir}/man1/showrgb.1*
%{_mandir}/man1/smproxy.1*
%{_mandir}/man1/startx.1*
%{_mandir}/man1/sxpm.1*
%{_mandir}/man1/xcmsdb.1*
%{_mandir}/man1/xconsole.1*
%{_mandir}/man1/xcutsel.1*
%{_mandir}/man1/xdpyinfo.1*
%{_mandir}/man1/xfindproxy.1*
%{_mandir}/man1/xfwp.1*
%{_mandir}/man1/xgamma.1*
%{_mandir}/man1/xhost.1*
%{_mandir}/man1/xinit.1*
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
%{_mandir}/man1/xvidtune.1*
%{_mandir}/man1/xvinfo.1*
%{_mandir}/man1/xwd.1*
%{_mandir}/man1/xwud.1*
%{_mandir}/man1/xon.1*
%{_mandir}/man7/*

%lang(it) %{_mandir}/it/man1/startx.1*
%lang(it) %{_mandir}/it/man1/xconsole.1*
%lang(it) %{_mandir}/it/man1/xinit.1*
%lang(it) %{_mandir}/it/man1/xsetpointer.1*

%lang(ko) %{_mandir}/ko/man1/xterm.1*

%lang(pl) %{_mandir}/pl/man1/lbxproxy.1*
%lang(pl) %{_mandir}/pl/man1/startx.1*
%lang(pl) %{_mandir}/pl/man1/xinit.1*
%lang(pl) %{_mandir}/pl/man1/xwd.1*

%files common
%defattr(644,root,root,755)
%{_libdir}/X11/rgb.txt

%files DPS
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/makepsres
%attr(755,root,root) %{_bindir}/pswrap
%attr(755,root,root) %{_bindir}/dpsinfo
%attr(755,root,root) %{_bindir}/dpsexec
%attr(755,root,root) %{_libdir}/libdps.so.*.*
%attr(755,root,root) %{_libdir}/libdpstk.so.*.*
%attr(755,root,root) %{_libdir}/libpsres.so.*.*
%{_mandir}/man1/makepsres*
%{_mandir}/man1/pswrap*
%{_mandir}/man1/dpsexec*
%{_mandir}/man1/dpsinfo*

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

%ifnarch alpha sparc64 ia64
%files PEX
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPEX5.so.*.*
%endif

%files PEX-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPEX5.so
%{_includedir}/X11/PEX5

%files PEX-static
%defattr(644,root,root,755)
%{_libdir}/libPEX5.a

%files XIE
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXIE.so.*.*

%files XIE-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXIE.so
%{_includedir}/X11/extensions/XIE*

%files XIE-static
%defattr(644,root,root,755)
%{_libdir}/libXIE.a

%files OpenGL-core
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGL.so.*.*
%ifnarch sparc sparc64
%attr(755,root,root) %{_libdir}/modules/extensions/libglx.a
%attr(755,root,root) %{_libdir}/modules/extensions/libGLcore.a
%endif

%files OpenGL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGL*.so
%ifnarch alpha
%attr(755,root,root) %{_libdir}/libOSMesa*.so
%endif
%{_libdir}/libGLw.a
%dir %{_includedir}/GL
%attr(644,root,root) %{_includedir}/GL/*
%{_mandir}/man3/gl[A-Z]*
%{_mandir}/man3/glu*
%{_mandir}/man3/GLw*

%files OpenGL-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glxinfo
%attr(755,root,root) %{_libdir}/libGLU.so.*.*
%ifnarch alpha
%attr(755,root,root) %{_libdir}/libOSMesa.so.*.*
%endif
%{_mandir}/man1/glxinfo.1*

%files OpenGL-static
%defattr(644,root,root,755)
%{_libdir}/libGL.a
%{_libdir}/libGLU.a
%ifnarch alpha
%{_libdir}/libOSMesa*.a
%endif

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
%attr(755,root,root) %{_sysconfdir}/X11/X
%attr(755,root,root) %{_bindir}/X
%{_mandir}/man1/XFree86.1*
%{_mandir}/man1/Xserver.1*
%{_mandir}/man5/XF86Config.5*

%{_libdir}/X11/Cards
%{_libdir}/X11/Options

%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/X11/XF86Config
%attr(640,root,root) %config %verify(not md5 size mtime) /etc/pam.d/xserver
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/security/blacklist.xserver
%config(missingok) /etc/security/console.apps/xserver

%files Xvfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xvfb
%{_mandir}/man1/Xvfb.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gccmakedep
%attr(755,root,root) %{_bindir}/bdftopcf
%attr(755,root,root) %{_libdir}/libX[1Ta-t]*.so
%attr(755,root,root) %{_libdir}/libI*.so
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
%{_includedir}/X11/*.h
%{_includedir}/X11/ICE
%{_includedir}/X11/PM
%{_includedir}/X11/SM
%{_includedir}/X11/Xaw
%{_includedir}/X11/Xft
%{_includedir}/X11/Xmu
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/[^X]*.h
%{_includedir}/X11/extensions/X[^I]*.h
%{_includedir}/X11/extensions/XI.h
%{_includedir}/X11/extensions/XI[^E]*.h
%{_includedir}/X11/fonts
%{_includedir}/xf86*.h
%{_libdir}/X11/config

%attr(755,root,root) %{_bindir}/imake
%attr(755,root,root) %{_bindir}/makedepend
%attr(755,root,root) %{_bindir}/xmkmf

%{_mandir}/man1/imake.1*
%{_mandir}/man1/makedepend.1*
%{_mandir}/man1/xmkmf.1*
%{_mandir}/man3/[A-EH-Z]*

%ifnarch sparc sparc64 alpha
%files driver-apm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/apm_drv.o
%{_mandir}/man4/apm*
%endif

%ifnarch sparc sparc64 alpha
%files driver-ark
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/ark_drv.o
%endif

%ifnarch alpha
%files driver-ati
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/ati*_drv.o
#%{_mandir}/man4/ati*
%endif

%ifnarch sparc sparc64 alpha
%files driver-chips
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/chips_drv.o
%{_mandir}/man4/chips*
%endif

%ifnarch sparc sparc64 alpha
%files driver-cirrus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/cirrus_*.o
%{_mandir}/man4/cirrus*
%endif

%ifnarch sparc sparc64 alpha
%files driver-cyrix
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/cyrix_drv.o
%{_mandir}/man4/cyrix*
%endif

%ifnarch alpha
%files driver-fbdev
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/fbdev_drv.o
%{_mandir}/man4/fbdev*
%endif

%ifnarch sparc sparc64 alpha
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

%ifnarch sparc sparc64 alpha
%files driver-i128
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/i128_drv.o
%{_mandir}/man4/i128*
%endif

%ifnarch sparc sparc64 alpha
%files driver-i740
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/i740_drv.o
%{_mandir}/man4/i740*
%endif

%ifnarch sparc sparc64 alpha
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

%ifnarch sparc sparc64 alpha
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
%ifnarch alpha
%attr(755,root,root) %{_libdir}/modules/drivers/r128_drv.o
%endif
%ifnarch sparc sparc64
%attr(755,root,root) %{_libdir}/modules/dri/r128_dri.so
%endif
%ifnarch alpha
%{_mandir}/man4/r128*
%endif
%endif

%files driver-radeon
%defattr(644,root,root,755)
%ifnarch alpha
%attr(755,root,root) %{_libdir}/modules/drivers/radeon_drv.o
%endif
%ifnarch sparc sparc64
%attr(755,root,root) %{_libdir}/modules/dri/radeon_dri.so
%endif

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
%files driver-s3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/s3_drv.o
#%{_mandir}/man4/s3*
%endif

%ifnarch sparc sparc64 alpha
%files driver-savage
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/savage_drv.o
%{_mandir}/man4/savage*
%endif

%ifnarch sparc sparc64 alpha
%files driver-siliconmotion
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/siliconmotion_drv.o
%{_mandir}/man4/siliconmotion*
%endif

%ifnarch sparc sparc64 alpha
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

%ifnarch sparc sparc64 alpha
%files driver-trident
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/trident_drv.o
%{_mandir}/man4/trident*
%endif

%ifnarch sparc sparc64 alpha
%files driver-tseng
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/tseng_drv.o
%{_mandir}/man4/tseng*
%endif

%ifarch %{ix86}
%files driver-vmware
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/vmware_drv.o
%{_mandir}/man4/vmware*
%endif

%files libs -f XFree86-libs.lang
%defattr(644,root,root,755)
%dir %{_libdir}
%dir %{_libdir}/X11
%{_libdir}/X11/XErrorDB
%{_libdir}/X11/XKeysymDB
%{_libdir}/X11/locale
%dir %{_includedir}
%dir %{_includedir}/X11
%dir %{_bindir}
/usr/bin/X11
/usr/lib/X11
/usr/include/X11
%dir %{_datadir}/locale
%dir %{_datadir}/misc
%dir %{_datadir}/sounds
%dir %{_pixmapsdir}
%dir %{_pixmapsdir}/mini
%dir %{_wmpropsdir}
%attr(755,root,root) %{_libdir}/libX[1Ta-t]*.so.*.*
%attr(755,root,root) %{_libdir}/libI*.so.*.*
%attr(755,root,root) %{_libdir}/libS*.so.*.*
%ifnarch alpha
%attr(755,root,root) %{_libdir}/libx*.so.*.*
%endif

%files modules
%defattr(644,root,root,755)
%{_libdir}/X11/xkb
%{_sysconfdir}/X11/xkb
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
%ifnarch alpha
%attr(755,root,root) %{_libdir}/modules/drivers/vesa_drv.o
%endif
%endif
%dir %{_libdir}/modules/extensions
%attr(755,root,root) %{_libdir}/modules/extensions/libdbe.a
%attr(755,root,root) %{_libdir}/modules/extensions/libdri.a
%attr(755,root,root) %{_libdir}/modules/extensions/libextmod.a
%attr(755,root,root) %{_libdir}/modules/extensions/librecord.a
%attr(755,root,root) %{_libdir}/modules/extensions/libxtrap.a
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
%ifnarch alpha
%{_mandir}/man4/vesa*
%endif
%endif
%{_mandir}/man4/void*
%{_mandir}/man4/wacom*
%{_mandir}/man4/elographics*
%{_mandir}/man4/mutouch*

%ifnarch alpha sparc64 ia64
%files module-PEX
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/extensions/libpex5.a
%endif

%files module-XIE
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/extensions/libxie.a

%files setup
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcitweak
%attr(755,root,root) %{_bindir}/scanpci
%attr(755,root,root) %{_bindir}/xf86cfg
%attr(755,root,root) %{_bindir}/xf86config
%{_mandir}/man1/scanpci.1*
%{_mandir}/man1/pcitweak.1*
%{_mandir}/man1/xf86cfg.1*
%{_mandir}/man1/xf86config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libICE.a
%{_libdir}/libSM.a
%{_libdir}/libX11.a
%{_libdir}/libXaw.a
%{_libdir}/libXft.a
%{_libdir}/libXext.a
%{_libdir}/libXfont.a
%{_libdir}/libXi.a
%{_libdir}/libXmu.a
%{_libdir}/libXmuu.a
%{_libdir}/libXp.a
%{_libdir}/libXpm.a
%{_libdir}/libXrender.a
%{_libdir}/libXt.a
%{_libdir}/libXtst.a

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
%attr(755,root,root) %{_bindir}/xload
%attr(755,root,root) %{_bindir}/xmag
%attr(755,root,root) %{_bindir}/xman
%attr(755,root,root) %{_bindir}/xmessage
%attr(755,root,root) %{_bindir}/xmh
%attr(755,root,root) %{_bindir}/xwininfo
%attr(755,root,root) %{_bindir}/oclock
%attr(755,root,root) %{_bindir}/xlogo
%attr(755,root,root) %{_bindir}/xkill
%attr(755,root,root) %{_bindir}/rman
%attr(755,root,root) %{_bindir}/xtrap*
%attr(755,root,root) %{_bindir}/texteroids
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
%{_mandir}/man1/xload.1*
%{_mandir}/man1/xmag.1*
%{_mandir}/man1/xman.1*
%{_mandir}/man1/xmessage.1*
%{_mandir}/man1/xmh.1*
%{_mandir}/man1/xwininfo.1*
%{_mandir}/man1/xkill.1*
%{_mandir}/man1/xlogo.1*
%{_mandir}/man1/oclock.1*
%{_mandir}/man1/rman.1*
%{_mandir}/man1/xtrap.1*
%{_mandir}/man1/texteroids.1*

%lang(it) %{_mandir}/it/man1/xload.1*

%lang(pl) %{_mandir}/pl/man1/rman.1*

%{_libdir}/X11/app-defaults/Beforelight
%{_libdir}/X11/app-defaults/Bitmap
%{_libdir}/X11/app-defaults/Bitmap-color
%{_libdir}/X11/app-defaults/Clock-color
%{_libdir}/X11/app-defaults/Editres
%{_libdir}/X11/app-defaults/Editres-color
%{_libdir}/X11/app-defaults/Viewres
%{_libdir}/X11/app-defaults/XConsole
%{_libdir}/X11/app-defaults/Xedit
%{_libdir}/X11/app-defaults/Xedit-color
%{_libdir}/X11/app-defaults/Xfd
%{_libdir}/X11/app-defaults/Xgc
%{_libdir}/X11/app-defaults/Xmag
%{_libdir}/X11/app-defaults/Xman
%{_libdir}/X11/app-defaults/Xmessage
%{_libdir}/X11/app-defaults/Xmh
%{_libdir}/X11/app-defaults/XFontSel
%{_libdir}/X11/app-defaults/Xditview
%{_libdir}/X11/app-defaults/Xditview-chrtr

%{_applnkdir}/Utilities/xclipboard.desktop

%files -n sessreg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sessreg
%{_mandir}/man1/sessreg.1*

%files -n twm
%defattr(644,root,root,755)
%{_wmpropsdir}/twm.desktop
%attr(755,root,root) %{_bindir}/twm
%dir %{_sysconfdir}/X11/twm
%config %{_sysconfdir}/X11/twm/system.twmrc
%attr(755,root,root) %{_libdir}/X11/twm
%{_mandir}/man1/twm.1*

%files -n xauth
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xauth
%{_mandir}/man1/xauth.1*

%files -n xdm
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/pam.d/xdm
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/security/blacklist.xdm
%attr(754,root,root) /etc/rc.d/init.d/xdm
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/xdm
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
/etc/X11/xdm/authdir

%files -n xfs
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/xfs
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/xfs
%dir %{_sysconfdir}/X11/fs
%attr(755,root,root) %{_libdir}/X11/fs
%config(noreplace) %{_sysconfdir}/X11/fs/config
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/X11/XftConfig

%attr(755,root,root) %{_bindir}/xfs
%attr(755,root,root) %{_bindir}/fslsfonts
%attr(755,root,root) %{_bindir}/fstobdf
%attr(755,root,root) %{_bindir}/mkcfm
%attr(755,root,root) %{_bindir}/xfsinfo
%attr(755,root,root) %{_bindir}/xftcache

%{_mandir}/man1/xfs.1*
%{_mandir}/man1/fslsfonts.1*
%{_mandir}/man1/fstobdf.1*
%{_mandir}/man1/mkcfm.1*
%{_mandir}/man1/xfsinfo.1*
%{_mandir}/man1/xftcache.1*
