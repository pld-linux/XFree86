Summary:        XFree86 Window System servers and basic programs
Summary(de):    Xfree86 Window-System-Server und grundlegende Programme
Summary(fr):    Serveurs du système XFree86 et programmes de base
Summary(pl):    XFree86 Window System wraz z podstawowymi programami
Summary(tr):    XFree86 Pencereleme Sistemi sunucularý ve temel programlar
Name:           XFree86
Version:        3.3.3.1
Release:        5
Copyright:      MIT
Group:          X11/XFree86
Group(pl):      X11/XFree86
Requires:       pam >= 0.66
Requires:       XFree86-modules
Source:         ftp.xfree86.org:/pub/XFree86/3.3.3/source/X333src-1.tgz
Source1:        xdm.pamd
Source2:        xdm.initd
Source3:        xfs.initd
Patch0:         %{name}-3.3.3.1.patch.bz2
Patch1:		XFree86-3.3.3-pld.patch.gz
Patch2:		XFree86-xf86config.patch.gz
Patch3:		XFree86-Xpath.patch.gz
Patch4:		XFree86-3.3.3.1-pam.patch.gz
Patch5:		XFree86-3.3-notiocsltc.patch.gz
Patch6:		XFree86-3.3.3.1-alpha-sockets.patch.gz
Patch7:		XFree86-3.3.3.1-sparc.patch.gz
Patch8:		XFree86-3.3.2-ffb.patch.gz
Patch9:		XFree86-3.3.2.3-ncurses.patch.gz
Patch10:	XFree86-3.3.3.1-glibc.patch.gz
Patch11:	XFree86-3.3.2.3-jay.patch.gz
Patch12:	XFree86-3.3.3.1-alpha-at.patch.gz
Patch13:	XFree86-3.3.3.1-czskkbd.patch.gz
Patch14:	XFree86-3.3-iso88592xlclocale.patch.gz
Patch15:	XFree86-3.3.3-joy.patch.gz
Patch16:	XFree86-3.3.3-arm.patch.gz
Patch17:	XFree86-3.3.3-ru_SU.patch.gz
Patch18:	XFree86-3.3.3.1-alpha-vga.patch.gz
Patch19:	XFree86-3.3.3.1-xf86fbdev.patch.gz
Patch20:	XFree86-xdm.patch
Patch21:	XFree86-xfsft-1.0.3.patch.gz
Patch22:	XFree86-xfsft-card64.patch.gz
Patch23:	xterm-ptmx-patch
Exclusivearch:  i386 alpha sparc
Buildroot:      /tmp/%{name}-%{version}-root

%ifarch sparc
Obsoletes: X11R6.1
%endif

%description
X Windows is a full featured graphical user interface featuring multiple
windows, multiple clients, and different window styles. It is used on
most Unix platforms, and the clients can also be run under other popular
windowing systems. The X protocol allows applications to be run on either
the local machine or across a network, providing flexibility in client/server
mplementations.

This package contains the basic fonts, programs and documentation for an X
workstation. It does not provide the X server which drives your video
hardware -- those are available in other package.

%decription -l pl
X Window System jest graficznym interfejsem u¿ytkownika, cechuje siê
mo¿liwo¶ci± pracy w wielu oknach, z wieloma klientami i do tego w
ró¿nych wystrojach okien. :) Jest u¿ywany na wiêkszo¶ci platform sytemów
Unix, a klienci mog± byæ uruchamiani tak¿e pod innymi popularnymi 
systemami okienkowymi. Protokó³ X pozwala na uruchamianie aplikacji 
zarówno z lokalnej maszyny jak i poprzez sieæ - daj±c przez to elastyczn± 
implementacjê architektury klient/serwer.

Pakiet ten zawiera podstawowe fonty, programy oraz dokumentacje dla
stacji X. Nie zawiera X serwera który jest po¶rednikiem z Twoj± kart± 
graficzn± -- jest on w innym pakiecie.

%package modules
Summary:     XFree86 modules
Group:       X11/XFree86
Group(pl):   X11/XFree86
Summary(pl): Wspólne modu³y dla wszystkich serwerów graficznych.

%description -l de modules
%description -l fr modules
%description -l tr modules
%description -l pl modules

%package libs
Summary:     X11R6 shared libraries
Group:       X11/XFree86
Group(pl):   X11/XFree86
Prereq:      grep 
Summary(de): X11R6 shared Libraries
Summary(pl): Biblioteki dzielone dla X11R6
Summary(fr): Bibliothèques partagées X11R6

%ifarch sparc
Obsoletes: X11R6.1-libs
%endif

%description libs
This package contains the shared libraries most X programs need to run
properly. They are in a separate package to reduce the disk space needed
to run X applications on a machine w/o an X server (over a network).

%package devel
Summary:     X11R6 static libraries, headers and programming man pages
Group:       X11/XFree86
Group(pl):   X11/XFree86
Summary(de): X11R6 statische Libraries, Headers und man pages für Programmierer
Summary(fr): Bibliothèques X11R6 statiques et pages man de programmation
Summary(pl): Biblioteki statyczne, pliki nag³ówkowe dla X11R6
Summary(tr): X11R6 ile geliþtirme için gerekli dosyalar

%ifarch sparc
Obsoletes: X11R6.1-devel
%endif

%description devel
Libraries, header files, and documentation for developing programs that
run as X clients. It includes the base Xlib library as well as the Xt
and Xaw widget sets. For information on programming with these libraries,
PLD recommends the series of books on X Programming produced by
O'Reilly and Associates.

%package	XF86Setup
Group:		X11/XFree86
Group(pl):	X11/XFree86
Summary:	Graphical configuration tool for XFree86
Summary(pl):	Graficzny konfigurator dla XFree86
Requires:	%{name}-VGA16 = %{version}

%description XF86Setup
XF86Setup is a graphical configuration tool for the XFree86 family of
servers. It allows you to configure video settings, keyboard layouts,
mouse type, and other miscellaneous options. It is slow however, and
requires the generic VGA 16 color server be available.

%description -l pl XF86Setup
Graficzny konfigurator dla XFree86

%package S3
Summary:     XFree86 S3 server
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Summary(de): XFree86 S3 Server
Summary(fr): Serveur XFree86 pour S3
Summary(pl): XFree86 serwer dla kart S3
Summary(tr): XFree86 S3 sunucularý

%description S3
X server for cards built around chips from S3, including most #9 cards,
many Diamond Stealth cards, Orchid Farenheits, Mirco Crystal 8S, most STB
cards, and some motherboards with built in graphics accelerators (such
as the IBM ValuePoint line).

%package I128
Summary:     XFree86 #9 Imagine 128 Server
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Summary(de): XFree86 #9 Imagine 128 Server
Summary(fr): Serveur Xfree86 pour #9 Imagine 128
Summary(pl): XFree86 serwer dla kart Number Nine Imagine 128
Summary(tr): XFree86 #9 Imagine 128 sunucusu

%description I128
X server for the #9 Imagine 128 board.

%package S3V
Summary:     XFree86 S3 Virge server
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Summary(de): Xfree86 S3 Virge-Server
Summary(fr): Serveur XFree86 pour S3 Virge
Summary(pl): XFree86 serwer dla kart S3 Virge
Summary(tr): XFree86 S3 Virge sunucusu

%description S3V
X server for cards built around the S3 Virge chipset.

%package Mach64
Summary:     XFree86 Mach64 server
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Summary(de): Xfree86 Mach64-Server
Summary(fr): Serveur Mach64 de XFree86
Summary(pl): XFree86 serwer dla kart Mach64
Summary(tr): XFree86 Mach64 sunucusu

%description Mach64
X server for ATI Mach64 based cards such as the Graphics Xpression, GUP Turbo,
and WinTurbo cards. This server is known to have problems with some Mach64
cards which newer versions of XFree86 (which were only available as BETA
releases at the time of this release) may fix. Look at http://www.xfree86.org
for information on updating this server.

%package Sun
Summary:     XFree86 Sun server (monochrome and 8-bit color SBUS framebuffers)
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Obsoletes:   X11R6.1-Sun
Summary(pl): Serwer XFree86 Sun (dla framebuffera)

%description Sun
To run X Windows programs requires an X server for your specific hardware.
This package includes the X server for Sun computers with monochrome and
8-bit color SBUS framebuffers.

%package SunMono
Summary:     XFree86 Sun server for monochrome SBUS framebuffers only
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Obsoletes:   X11R6.1-SunMono
Summary(pl): Serwer XFree86 Sun (tylko dla monitorów monochromatycznych)

%description SunMono
To run X Windows programs requires an X server for your specific hardware.
This package includes the X server for Sun computers with monochrome
SBUS framebuffers only.

%package Sun24
Summary:     XFree86 Sun server for all supported SBUS framebuffers
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Obsoletes:   X11R6.1-Sun24
Summary(pl): Serwer XFree86 Sun (dla wszystkich SBUS framebufferów)
 
%description Sun24
To run X Windows programs requires an X server for your specific hardware.
This package includes the X server for Sun computers with all supported
SBUS framebuffers.

%package Xvfb
Summary:     XFree86 Xvfb server
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Summary(pl): Serwer XFree86 Xvfb

%package 3DLabs
Summary:     XFree86 3DLabs server
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Summary(pl): Serwer XFree86 3DLabs

%description 3DLabs
XFree86 3DLabs server

%description -l pl 3DLabs
XFree86 3DLabs server

%description Xvfb
X server which runs in a X window.

%package Xnest
Summary:     XFree86 Xnest server
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Summary(pl): Serwer XFree86 Xnest

%description Xnest
X server which runs in a X window.

%package 8514
Summary:     XFree86 8514 server
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Summary(de): XFree86 8514 Server
Summary(fr): serveur 8514 pour XFree86.
Summary(pl): XFree86 serwer dla kart 8514
Summary(tr): XFree86 8514 sunucusu

%description 8514
X server for older IBM 8514 cards and compatibles from companies such as
ATI.

%package AGX
Summary:     XFree86 AGX server
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Summary(de): XFree86 AGX Server
Summary(fr): serveur AGX pour XFree86.
Summary(pl): XFree86 serwer dla kart AGX
Summary(tr): XFree86 AGX sunucusu

%description AGX
X server for AGX based cards such as the Boca Vortex, Orchid Celsius,
Spider Black Widow, and Hercules Graphite.

%package	FBDev
Summary:	XFree68/86 FBDev server
Summary(pl):	XFree86/86 FBDev server
Group:		X11/XFree86/Servers
Group(pl):	X11/XFree86/Serwery

%description FBDev
X server for the generic frame buffer device used on the Amiga, Atari
and Macintosh/m68k machines.  Support for Intel and Alpha architectures
is now included in the Linux 2.2 kernel as well.

%description -l pl FBDev
X serwer wspieraj±cy frame buffera dla Amigi, Atari i Macintosha /m68k.
Wsparcie dla platform Intel i Alpha jest w j±drze systemu.

%package Mach32
Summary:     XFree86 Mach32 server
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Summary(de): Xfree86 Mach32-Server
Summary(fr): Serveur XFree86 pour Mach32
Summary(pl): XFree86 serwer dla kart Mach32
Summary(tr): XFree86 Mach32 sunucusu

%description Mach32
X server for cards built around ATI's Mach32 chip, including the ATI
Graphics Ultra Pro and Ultra Plus.

%package Mach8
Summary:     XFree86 Mach8 server
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Summary(de): XFree86 Mach8 Server
Summary(fr): Serveur Mach8 pour XFree86
Summary(pl): XFree86 serwer dla kart Mach8
Summary(tr): XFree86 Mach8 sunucusu

%description Mach8
X server for cards built around ATI's Mach8 chip, including the ATI
8514 Ultra and Graphics Ultra.

%package Mono
Summary:     XFree86 Mono server
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Summary(de): Xfree86 Mono-Server
Summary(fr): Serveur Monochrome de XFree86
Summary(pl): XFree86 serwer dla kart Monochromatycznych
Summary(tr): XFree86 Mono sunucusu

%description Mono
Generic monochrome (2 color) server for VGA cards, which works on nearly
all VGA style boards with limited resolutions.

%package P9000
Summary:     XFree86 P9000 server
Group:       X11/XFree86/Servers
Summary(pl): XFree86 serwer dla kart P9000
Summary(de): XFree86 P9000 Server
Summary(fr): Serveur XFree86 pour P9000
Summary(tr): XFree86 P9000 sunucusu

%description P9000
X server for cards built around the Weitek P9000 chips such as most
Diamond Viper cards and the Orchid P9000 card.

%package SVGA
Summary:     XFree86 SVGA server
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Summary(de): XFree86 SVGA-Server
Summary(fr): Serveur XFree86 pour SVGA
Summary(pl): XFree86 serwer dla kart SVGA
Summary(tr): XFree86 SVGA sunucusu

%description SVGA
X server for most simple framebuffer SVGA devices, including cards built
from ET4000 chips, Cirrus Logic chips, Chips and Technologies laptop chips,
Trident 8900 and 9000 chips. It works for Diamond Speedstar, Orchid
Kelvins, STB Nitros and Horizons, Genoa 8500VL, most Actix boards,
the Spider VLB Plus. It also works for many other chips and cards, so try
this server if you are having problems.

%package VGA16
Summary:     XFree86 VGA16 server
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Summary(de): XFree86 VGA16-Server
Summary(fr): Serveur XFree86 pour VGA16
Summary(pl): XFree86 serwer dla kart CGA16
Summary(tr): XFree86 VGA16 sunucusu

%description VGA16
Generic 16 color server for VGA boards. This works on nearly all VGA style
graphics boards, but only in low resolution with few colors.

%package W32
Summary:     XFree86 W32 server
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Summary(de): XFree86 W32 Server
Summary(fr): Serveur XFree86 pour W32
Summary(pl): XFree86 serwer dla kart W32
Summary(tr): XFree86 W32 sunucusu

%description W32
X server for cards built around the ET4000/W32 chips, including the
Genoa 8900 Phantom 32i, Hercules Dynamite cards, LeadTek WinFast S200,
Sigma Concorde, STB LightSpeed, TechWorks Thunderbolt, and ViewTop PCI.

%package TGA
Summary:     XFree86 TGA server
Group:       X11/XFree86/Servers
Group(pl):   X11/XFree86/Serwery
Summary(pl): XFree86 serwer dla kart TGA

%description TGA
Eight bit X server for Digital TGA boards based on the DC21040 chips. These
adapters are very popular in Alpha workstations and are included with Alpha
UDB (Multia) machines.

%package -n xdm
Summary:     XDM
Group:       X11/XFree86
Group(pl):   X11/XFree86
Obsoletes:   gdm
Obsoletes:   kdm
Requires:    %{name} = %{version}
Summary(pl): XDM

%description -n xdm

%package -n xfs
Summary:     XFS
Group:       X11/XFree86
Group(pl):   X11/XFree86
Obsoletes:   xfsft
Summary(pl): XFS

%description -n xfs

%package -n xauth
Summary:     XAuth
Group:       X11/XFree86
Group(pl):   X11/XFree86
Summary(pl): XAuth

%description -n xauth

%description -l de W32
Genoa 8900 Phantom 32I, Hercules Dynamite, LeaTek WinFast S200, 
Sigma Concorde, STB LightSpeed, TechWorks Thunderbolt und ViewTop PCI.

%description -l de devel
Libraries, Header-Dateien und Dokumentation zum Entwickeln von Programmen,
die als X-Clients laufen. Enthält die Xlib-Library und die Widget-Sätze Xt
und Xaw. Information zum Programmieren mit diesen Libraries finden Sie 
in der Buchreihe zur X-Programmierung von O'Reilly and Associates.

%description -l de Mono
Generischer monochromer (Schwarzweiß-) Server für VGA-Karten, der 
praktisch mit allen VGA-ähnlichen Karten mit beschränkter Auflösung
funktioniert.

%description -l de 8514
X-Server für ältere IBM 8514- und kompatible Karten, z.B. von ATI.

%description -l de P9000
X-Server für Karten auf Basis des Weitek P9000-Chip, wie die meisten 
Diamond Viper und Orchid P9000-Karten.

%description -l de AGX
X-Server für Karten auf AGX-Basis wie etwa Boca Vortex, Orchid Celsius, 
Spider Black Widow und Hercules Graphite.

%description -l de VGA16
Generischer 16-Farben-Server für VGA-Karten. Funktioniert auf fast allen VGA-
Grafikkarten, allerdings nur bei geringer Auflösung und wenigen Farben.

%description -l de S3
X-Server für Steckkarten mit dem S3-Chipsatz (inkl. den meisten #9-Karten),
Karten wie Diamond Stealth, Orchid Farenheit und Mirco Crystal 8S, den meisten STB-Karten
sowie einigen Motherboards mit integrierten Grafikbeschleunigern (z.B. 
die Reihe IBM ValuePoint).

%description -l de Mach32
X-Server für Karten auf der Basis des ATI Mach32-Chip, einschließlich 
ATI Graphics Ultra Pro und Ultra Plus.

%description -l de libs
Dieses Paket enthält die zur gemeinsamen Nutzung vorgesehenen Libraries,
die die meisten X-Programme für den einwandfreien Betrieb benötigen. Sie
wurden in einem separaten Paket untergebracht, um den
Festplattenspeicherplatz auf Computern zu reduzieren, die ohne einen X-
Server (über ein Netz) arbeiten.

%description -l de SVGA
X-Server für die elementarsten Framebuffer-SVGA-Geräte, einschließlich 
Karten, die aus ET4000-Chips, Cirrus Logic-Chips, Chips and Technologies 
Laptop-Chips sowie Trident 8900 und 9000 Chips gebaut sind. Funktioniert 
mit Diamond Speedstar, Orchid Kelvins, STB Nitros und Horizons, 
Genoa 8500VL, den meisten Actix-Karten sowie Spider VLB Plus und außerdem 
mit vielen anderen Chips und Karten. Es lohnt sich, diesen Server 
auszuprobieren, wenn Sie Probleme haben.

%description -l de S3V
X-Server für Grafikkarten mit dem S3 Virge-Chipsatz.

%description -l de Mach64
X-Server für ATI Mach64-Karten wie Graphics Xpression, GUP Turbo,
und WinTurbo. Dieser Server verursacht gelegentlich Probleme mit Mach64-Karten,
die aber von einer neueren Version von XFree86 (der als Beta-Version verfügbar ist)
gelöst werden könnten. Unter
http://www.xfree86.org finden Sie Informationen zum Aktualisieren dieses Servers.

%description -l de Mach8
X-Server für Karten auf der Basis des ATI Mach8-Chips, einschließlich
des ATI 8514 Ultra und des Graphics Ultra.

%description -l de I128
X-Server für die Steckkarte #9 Imagine 128

%description -l de -n xdm
%description -l de -n xauth

%description -l de -n xfs

%description -l de
X-Windows ist eine voll funktionsfähige grafische Benutzeroberfläche 
mit mehreren Fenstern, mehreren Clients und verschiedenen Arten von 
Fenstern. Es kommt auf den meisten Unix-Plattformen zum Einsatz. Die 
Clients lassen sich auch mit Hilfe anderer Fenstersysteme anzeigen. 
Das X-Protokoll gestattet die Ausführung der Applikationen direkt auf 
lokalen Rechnern oder über ein Netz und bietet große Flexibilität bei 
Client-Server-Implementierungen.

%description -l fr W32
Serveur X pour les cartes basée sur les chips ET4000/W32, dontla Genoa 8900 Phantom 32i, les cartes Hercules Dynamite, la LeadTek WinFast
S200, la Sigma Concorde, la STB LightSpeed, la TechWorks Thunderbolt,
et la ViewTop PCI.

%description -l fr devel
Bibliothéques, fichiers d'en-tête, et documentation pour développer des
programmes s'exécutant en clients X. Cela comprend la Bibliothéque Xlib
de base aussi bien que les ensembles de widgets Xt et Xaw. Pour des
informations sur la programmation avec ces Bibliothéques, Red Hat 
recommande la série d'ouvrages sur la programmation  X editée par
O'Reilly and Associates.

%description -l fr Mono
Serveur générique monochrome (2 couleurs) pour les cartes VGA, fonctionne avec
pratiquement toutes les cartes VGA ayant des résolutions limitées.

%description -l fr 8514
Serveur X pour les vieilles cartes IBM 8514 et compatibles comme lesATI.

%description -l fr P9000
Serveur X pour les cartes construites autour des circuits P9000 de
Weitek, comme la plupart des cartes Diamond Viper et l'Orchid P9000.

%description -l fr AGX
Serveur X pour les cartes à base d'AGX comme la Boca Vortex, l'Orchid


%description -l fr VGA16
Serveur 16 couleurs générique pour cartes VGA. Fonctionne avec presque
toutes les cartes VGA, mais seulement en faible résolution avec peu de couleurs.

%description -l fr S3
Serveur X pour les cartes construites autour des circuits S3, dont la
plupart des cartes #9, de nombreuses Diamond Stealth, Orchid Farenheits,
Mirco Crystal 8S, la plupart des cartes STB et certaines cartes mères
intégrant des accélérateurs graphiques (comme la gamme ValuePoint d'IBM).

%description -l fr Mach32
Serveur X pour les cartes utilisant le circuit ATI Mach32, dont les
cartes ATI Graphics Ultra Pro et Ultra Plus.

%description -l fr libs
Ce paquetage contient les bibliothèques partagées nécessaires à de nombreux
programmes X. Elles se trouvent dans un paquetage séparé afin de réduire
l'espace disque nécessaire à l'exécution des applications X sur une machine
sans serveur X (en réseau).

%description -l fr SVGA
Serveur X pour les circuits SVGA les plus simples, dont les cartes construites
avec les circuits ET4000, Cirrus Logic, Chips and Technologies laptop,
Trident 8900 et 9000. Fonctionne pour les cartes Diamond Speedstar, Orchid
Kelvins, STB Nitros et Horizons, Genoa 8500VL, la plupart des Actix
et la Spider VLB Plus. Fonctionne aussi pour de nombreux autres circuits
et cartes. Essayez ce serveur si vous avez des problèmes.

%description -l fr S3V
Serveur X pour les cartes construites autour du circuit S3 Virge

%description -l fr Mach64
Serveur X pour les cartes basées sur l'ATI Mach64, comme les cartes GUP Turbo,
Graphics Xpression et WinTurbo. Ce serveur est connu pour avoir des problèmes
avec certaines cartes Mach64 que les versions plus récentes d'XFree86 corrigent
(elles ne sont encore qu'en version BETA au moment de cette distribution).
Consultez http://www.xfree86.org pour les informations de mise à jour du serveur.

%description -l fr Mach8
Serveur X pour les cartes basées sur les chips ATI Mach8, dont les cartes
ATI 8514 Ultra et Graphics Ultra.

%description -l fr I128
Serveur X pour les cartes #9 Imagine 128.

%description -l fr -n xdm

%description -l fr -n xfs

%description -l fr -n xauth

%description -l tr W32
Genoa 8900 Phantom 32i, Hercules Dynamite kartlarý, LeadTek WinFast S200,
Sigma Concorde, STB LightSpeed, TechWorks Thunderbolt, ve ViewTop PCI
gibi kartlarýn kullandýðý ET4000/W32 tabanlý kartlar için X sunucusu.

%description -l tr devel
X istemcisi olarak çalýþacak programlar geliþtirmek için gereken statik
kitaplýklar, baþlýk dosyalarý ve belgeler. Xlib kitaplýðýnýn yanýsýra Xt ve
Xaw arayüz kitaplýklarýný da içerir.

%description -l tr Mono
Mono (2 renk) VGA kartlarý için genel X sunucusu. Kýsýtlý bir çözünürlük
altýnda birçok VGA kart ile çalýþýr.

%description -l tr 8514
Eski IBM 8514 ve uyumlu kartlar (ATI gibi) için sunucu.

%description -l tr P9000
Diamond Viper ve Orchid P9000 gibi Weitek P9000 tabanlý kartlar için X
sunucusu.

%description -l tr AGX
Boca Vortex, Orchid Celsius, Spider Black Widow ve Hercules Graphite gibi AGX
tabanlý kartlar için X sunucusu.

%description -l tr VGA16
VGA kartlarý için genel 16 renk sunucusu. Çoðu VGA tipi kart ile düþük renk
ve çözünürlükte çalýþýr.

%description -l tr S3
S3 tabanlý ekran kartlarý için sunucular. Çoðu #9, Diamond Stealth, Orchid
Fahrenheit, Mirco Crystal 8S, çoðu STB ve bazý anakarta tümleþik grafik
hýzlandýrýcýlar bu gruba girer. S3 Virge sunucusu ayrý bir pakette yer alýr.

%description -l tr Mach32
ATI Mach32 tabanlý ATI Graphics Ultra Pro ve Ultra Plus kartlarý için X
sunucusu.

%description -l tr libs
Bu paket X programlarýnýn düzgün çalýþabilmeleri için gereken kitaplýklarý
içerir. Bunlar, X programlarýný (sunucu olsun olmasýn) çalýþtýrmak için
gerekli disk alanýný azaltmak için ayrý bir paket olarak sunulmuþtur.

%description -l tr SVGA
ET4000, Cirrus Logic, Chips and Technologies dizüstü, Trident 8900 ve 9000
gibi basit 'framebuffer' SVGA kullananan kartlar için X sunucusu. Ayný
zamanda Diamond Speedstar, Orchid Kelvins, STB Nitros / Horizons, Genoa
8500VL, çoðu Actix kartlarý, Spider VLB Plus gibi kartlar ve birçok diðer
kart ile de çalýþýr. Herhangi bir sorun yaþarsanýz bu sunucuyu deneyin.

%description -l tr S3V
XFree86 S3 Virge sunucusu

%description -l tr Mach64
ATI Mach64 tabanlý kartlar için X sunucusu. Graphics Xpression, GUP Turbo ve
WinTurbo gibi kartlarý destekler. Bazý Mach64 kartlarýn yeni XFree86 ile
sorun yaþadýklarý bilinmektedir. Bu sorunla ilgili son bilgilere ulaþmak için
lütfen http://www.xfree86.org adresine bakýn.

%description -l tr Mach8
ATI 8514 Ultra ve Graphics Ultra gibi ATI Mach8 tabanlý kartlar için X
sunucusu.

%description -l tr I128
#9 Imagine kartý için X sunucusu.

%description -l tr -n xdm
%description -l tr -n xfs
%description -l tr -n xauth

%description -l tr
X Window sistemi, çoklu pencere, çoklu istemci ve çeþitli pencere stilleriyle
geniþ özelliklere sahip bir Grafik Kullanýcý Arabirimidir. Çoðu UNIX sisteminde
çalýþtýðý gibi istemcileri de birçok pencereleme sistemiyle çalýþabilir. X
protokolu kullanan uygulamalarýn yerel makina veya bilgisayar aðý üzerinden
çalýþtýrýlabilmesi esnek bir istemci/sunucu ortamý saðlar. Bu paket bir X
istasyonu için gerekli olan temel yazýtiplerini, programlarý ve belgeleri
sunar. Ekran kartýnýzý sürmek için gerekli olan X sunucusu bu pakete dahil
deðildir.

%description -l pl libs
Pakiet zawieraj±cy podstawowe biblioteki dla programów kozystaj±cych
z systemu X-Window. Wydzielony w celu oszczednosci miejsca, nie
wp³ywa na mo¿liwo¶ci pracy aplikacji X-Windows poprzez np. sieæ.
Nie potrzebny dla komputerów nie posiadaj±cych X-serwerów.

%description -l pl devel

%description -l pl S3

%description -l pl I128

%description -l pl S3V

%description -l pl Mach64

%description -l pl Sun

%description -l pl SunMono

%description -l pl Sun24

%description -l pl Xvfb

%description -l pl Xnest

%description -l pl 8514

%description -l pl AGX

%description -l pl Mach32

%description -l pl Mach8

%description -l pl Mono

%description -l pl P9000

%description -l pl SVGA

%description -l pl VGA16

%description -l pl W32

%description -l pl TGA

%description -l pl -n xdm
%description -l pl -n xfs
%description -l pl -n xauth

%prep
%setup -q -c
%patch0  -p1
%patch1  -p1
%patch2  -p1
%patch3  -p1
%patch4  -p1
%patch5  -p1
%patch6  -p1
%patch7  -p1
%patch8  -p1
%patch9  -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p0
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
(cd xc; patch -p1 $RPM_SOURCE_DIR/xterm-ptmx.patch)

%build
# Clean up to save a *lot* of disk space
find . -name "*.orig" -print | xargs rm -f
find . -size 0 -print | xargs rm -f

make -C xc \
	    "BOOTSTRAPCFLAGS=$RPM_OPT_FLAGS" \
	    "CDEBUGFLAGS=" "CCOPTIONS=$RPM_OPT_FLAGS" \
	    "CXXDEBUGFLAGS=" "CXXOPTIONS=$RPM_OPT_FLAGS" \
	    World

%install
install -d $RPM_BUILD_ROOT/usr/{include,X11R6/{bin,lib/X11,man/{man1,man3,man5}}}
install -d $RPM_BUILD_ROOT/etc/{pam.d,rc.d/{init.d,rc3.d,rc5.d}}
install -d $RPM_BUILD_ROOT/usr/include

make -C xc  "DESTDIR=$RPM_BUILD_ROOT" \
	    "INSTBINFLAGS=-m 755 -s" \
	    "INSTPGMFLAGS=-m 755 -s" \
	     install install.man

# setup the default X server
rm -f $RPM_BUILD_ROOT/usr/X11R6/bin/X
ln -s Xwrapper $RPM_BUILD_ROOT/usr/X11R6/bin/X

# libz.a > /dev/piach
rm -f $RPM_BUILD_ROOT/usr/X11R6/lib/libz.a

# Move config stuff to /etc/X11
install -d $RPM_BUILD_ROOT/etc/X11

cp $RPM_BUILD_ROOT/usr/X11R6/lib/X11/XF86Config.eg \
$RPM_BUILD_ROOT/etc/X11/XF86Config

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
install	-d $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts/TrueType
echo 0	>  $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts/TrueType/fonts.dir
echo 0	>  $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts/TrueType/fonts.scale

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/xdm
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/xdm
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/xfs

ln -sf /usr/X11R6/include/X11 $RPM_BUILD_ROOT/usr/include/X11

for n in libX11.so.6.1 libICE.so.6.3 libSM.so.6.0 libXext.so.6.3 libXt.so.6.0 \
	 libXmu.so.6.0 libXaw.so.6.1 libXIE.so.6.0 libXi.so.6.0 \
	 libXtst.so.6.1; do
ln -sf $n $RPM_BUILD_ROOT/usr/X11R6/lib/`echo $n | sed "s/\.so.*/\.so/"`
done

bzip2 -9 $RPM_BUILD_ROOT/usr/X11R6/man/man[135]/*

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config /usr/X11R6/lib/X11/XF86Config.eg
%docdir /usr/X11R6/lib/X11/doc
%doc /usr/X11R6/lib/X11/Cards

%dir /usr/X11R6/lib
%dir /usr/X11R6/lib/X11
%dir /usr/X11R6/lib/X11/xserver

%ifnarch sparc
%dir /usr/X11R6/lib/modules
%endif

%dir /usr/X11R6/bin

%config /etc/X11/twm/system.twmrc
%config /etc/X11/fs/config
%config /etc/X11/xsm/system.xsm
%config /etc/X11/XF86Config
%attr(755,root,root) /etc/X11/xinit/*
%ghost /etc/X11/X

/usr/X11R6/lib/X11/XErrorDB
/usr/X11R6/lib/X11/XKeysymDB
/usr/X11R6/lib/X11/locale
/usr/X11R6/lib/X11/lbxproxy
/usr/X11R6/lib/X11/proxymngr
%attr(-,root,root) %config /usr/X11R6/lib/X11/app-defaults/*

%attr(755,root,root) /usr/X11R6/lib/X11/xinit

%attr(755,root,root) /usr/X11R6/lib/X11/twm
%attr(755,root,root) /usr/X11R6/lib/X11/fs
%attr(755,root,root) /usr/X11R6/lib/X11/xsm

/usr/X11R6/lib/X11/xserver/SecurityPolicy
%attr(-,root,root) /usr/X11R6/lib/X11/XF86Config

%attr(-,root,root) /usr/X11R6/lib/X11/rstart/*

%attr(755,root,root) /usr/X11R6/lib/X11/x11perfcomp/*
/usr/X11R6/lib/X11/*.txt

/usr/X11R6/lib/X11/doc

%dir /usr/X11R6/lib/X11/etc
%attr(-,root,root) /usr/X11R6/lib/X11/etc/*

%attr(4711,root,root) /usr/X11R6/bin/Xwrapper

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

%attr(755,root,root) %config /usr/X11R6/bin/startx

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
%attr(711,root,root) /usr/X11R6/bin/xterm
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

%dir /usr/X11R6/include/X11/bitmaps
/usr/X11R6/include/X11/bitmaps/*

%attr(644,root,man) /usr/X11R6/man/man1/lbxproxy.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/proxymngr.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xfindproxy.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xfwp.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xrx.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/lndir.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/makestrs.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/makeg.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/mkdirhier.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/appres.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/bdftopcf.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/beforelight.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/bitmap.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/bmtoa.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/atobm.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/editres.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/fsinfo.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/fslsfonts.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/fstobdf.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/iceauth.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/mkfontdir.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/showrgb.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/rstart.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/rstartd.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/smproxy.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/twm.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/x11perf.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/x11perfcomp.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xclipboard.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xcutsel.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xclock.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xcmsdb.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xconsole.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/sessreg.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xdpyinfo.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/dga.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xfd.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xhost.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xieperf.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xinit.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/startx.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/setxkbmap.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xkbcomp.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xkbevd.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xkbprint.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xkill.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xlogo.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xlsatoms.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xlsclients.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xlsfonts.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xmag.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xmh.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xmodmap.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xprop.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xrdb.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xrefresh.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xset.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xsetmode.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xsetpointer.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xsetroot.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xsm.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xstdcmap.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xterm.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/resize.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xvidtune.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xwd.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xwininfo.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xwud.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/Xserver.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/XFree86.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/reconfig.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xf86config.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/SuperProbe.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xon.1x.bz2

%files modules
%defattr(-,root,root,755)
/usr/X11R6/lib/X11/xkb
%attr(755,root,root) /usr/X11R6/lib/modules/*

%files -n xdm
%defattr(644,root,root,755)
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/xdm
%attr(750,root,root) %config /etc/rc.d/init.d/xdm
%attr(-,root,root) /etc/X11/xdm/*

%config /usr/X11R6/lib/X11/app-defaults/Chooser

%attr(755,root,root) /usr/X11R6/lib/X11/xdm
%attr(755,root,root) /usr/X11R6/bin/xdm
%attr(755,root,root) /usr/X11R6/bin/sessreg
%attr(644,root, man) /usr/X11R6/man/man1/xdm.1x.bz2

%files -n xfs
%defattr(644,root,root,755)
%attr(700,root,root) %config /etc/rc.d/init.d/xfs
%attr(755,root,root) /usr/X11R6/bin/xfs
%attr(644,root, man) /usr/X11R6/man/man1/xfs.1x.bz2

%files -n xauth
%defattr(644,root,root,755)
%attr(711,root,root) /usr/X11R6/bin/xauth
%attr(644,root, man) /usr/X11R6/man/man1/xauth.1x.bz2

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/lib/*.so.*

%files devel
%defattr(-,root,root,755)

/usr/X11R6/include/X11/*.h

%dir /usr/X11R6/include/X11/ICE
/usr/X11R6/include/X11/ICE/*

%dir /usr/X11R6/include/X11/PEX5
/usr/X11R6/include/X11/PEX5/*

%dir /usr/X11R6/include/X11/PM
/usr/X11R6/include/X11/PM/*

%dir /usr/X11R6/include/X11/SM
/usr/X11R6/include/X11/SM/*

%dir /usr/X11R6/include/X11/Xaw
/usr/X11R6/include/X11/Xaw/*

%dir /usr/X11R6/include/X11/Xmu
/usr/X11R6/include/X11/Xmu/*

%dir /usr/X11R6/include/X11/extensions
/usr/X11R6/include/X11/extensions/*

%dir /usr/X11R6/include/X11/fonts
/usr/X11R6/include/X11/fonts/*

/usr/include/X11

%dir /usr/X11R6/lib/X11/config
/usr/X11R6/lib/X11/config/*

%attr(711,root,root) /usr/X11R6/bin/imake
%attr(711,root,root) /usr/X11R6/bin/makedepend
%attr(755,root,root) /usr/X11R6/bin/xmkmf

%attr(644,root,man) /usr/X11R6/man/man1/imake.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/makedepend.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/xmkmf.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man3/*

/usr/X11R6/lib/*.a

%attr(755,root,root) /usr/X11R6/lib/*.so

%files Xvfb
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/Xvfb
%attr(644,root, man) /usr/X11R6/man/man1/Xvfb.1x.bz2

%files Xnest
%defattr(644,root,root,755)
%attr(711,root,root) /usr/X11R6/bin/Xnest
%attr(644,root, man) /usr/X11R6/man/man1/Xnest.1x.bz2

%ifarch i386 alpha

%files SVGA
%defattr(644,root,root,755)
%attr(711,root,root) /usr/X11R6/bin/XF86_SVGA
%attr(644,root,man) /usr/X11R6/man/man1/XF86_SVGA.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man5/XF86Config.5x.bz2
%endif

%ifarch i386 sparc

%files VGA16
%defattr(644,root,root,755)
%attr(711,root,root) /usr/X11R6/bin/XF86_VGA16
%attr(644,root, man) /usr/X11R6/man/man1/XF86_VGA16.1x.bz2
%attr(644,root, man) /usr/X11R6/man/man5/XF86Config.5x.bz2
%endif

%ifarch i386

%files W32
%defattr(644,root,root,755)
%attr(711,root,root) /usr/X11R6/bin/XF86_W32
%attr(644,root, man) /usr/X11R6/man/man1/XF86_W32.1x.bz2
%attr(644,root, man) /usr/X11R6/man/man1/XF86_Accel.1x.bz2
%attr(644,root, man) /usr/X11R6/man/man5/XF86Config.5x.bz2
%endif

%ifarch i386 alpha

%files Mono
%defattr(644,root,root,755)
%attr(711,root,root) /usr/X11R6/bin/XF86_Mono
%attr(644,root, man) /usr/X11R6/man/man1/XF86_Mono.1x.bz2
%attr(644,root, man) /usr/X11R6/man/man5/XF86Config.5x.bz2
%endif

%ifarch i386 alpha

%files S3
%defattr(644,root,root,755)
%attr(711,root,root) /usr/X11R6/bin/XF86_S3
%attr(644,root, man) /usr/X11R6/man/man1/XF86_S3.1x.bz2
%attr(644,root, man) /usr/X11R6/man/man1/XF86_Accel.1x.bz2
%attr(644,root, man) /usr/X11R6/man/man5/XF86Config.5x.bz2
%endif

%ifarch i386 alpha

%files S3V
%defattr(644,root,root,755)
%attr(711,root,root) /usr/X11R6/bin/XF86_S3V
%attr(644,root, man) /usr/X11R6/man/man1/XF86_S3.1x.bz2
%attr(644,root, man) /usr/X11R6/man/man1/XF86_Accel.1x.bz2
%attr(644,root, man) /usr/X11R6/man/man5/XF86Config.5x.bz2
%endif

%ifarch i386

%files 8514
%defattr(644,root,root,755)
%attr(711,root,root) /usr/X11R6/bin/XF86_8514
%attr(644,root, man) /usr/X11R6/man/man1/XF86_8514.1x.bz2
%attr(644,root, man) /usr/X11R6/man/man1/XF86_Accel.1x.bz2
%attr(644,root, man) /usr/X11R6/man/man5/XF86Config.5x.bz2
%endif

%ifarch i386

%files Mach8
%defattr(644,root,root,755)
%attr(711,root,root) /usr/X11R6/bin/XF86_Mach8
%attr(644,root,man) /usr/X11R6/man/man1/XF86_Mach8.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/XF86_Accel.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man5/XF86Config.5x.bz2
%endif

%ifarch i386

%files Mach32
%defattr(644,root,root,755)
%attr(711,root,root) /usr/X11R6/bin/XF86_Mach32
%attr(644,root, man) /usr/X11R6/man/man1/XF86_Mach32.1x.bz2
%attr(644,root, man) /usr/X11R6/man/man1/XF86_Accel.1x.bz2
%attr(644,root, man) /usr/X11R6/man/man5/XF86Config.5x.bz2
%endif

%files Mach64
%defattr(644, root, root, 755)
%attr(711,root,root) /usr/X11R6/bin/XF86_Mach64
%attr(644,root,man) /usr/X11R6/man/man1/XF86_Mach64.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/XF86_Accel.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man5/XF86Config.5x.bz2

%ifarch i386 alpha

%files P9000
%defattr(644, root, root, 755)
%attr(711,root,root) /usr/X11R6/bin/XF86_P9000
%attr(644,root,man) /usr/X11R6/man/man1/XF86_P9000.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/XF86_Accel.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man5/XF86Config.5x.bz2
%endif

%ifarch i386

%files AGX
%defattr(644, root, root, 755)
%attr(711,root,root) /usr/X11R6/bin/XF86_AGX
%attr(644,root,man) /usr/X11R6/man/man1/XF86_AGX.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/XF86_Accel.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man5/XF86Config.5x.bz2
%endif

%ifarch i386

%files I128
%defattr(644, root, root, 755)
%attr(711,root,root) /usr/X11R6/bin/XF86_I128
%attr(644,root,man) /usr/X11R6/man/man1/XF86_I128.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man1/XF86_Accel.1x.bz2
%attr(644,root,man) /usr/X11R6/man/man5/XF86Config.5x.bz2
%endif

%ifarch alpha

%files TGA
%defattr(644, root, root, 755)
%attr(711,root,root) /usr/X11R6/bin/XF86_TGA
%attr(644,root, man) /usr/X11R6/man/man5/XF86Config.5x.bz2
%endif

%ifarch sparc

%files Sun
%defattr(644,root,root,755)
%attr(711,root,root) /usr/X11R6/bin/Xsun
%attr(-,root,root) /usr/X11R6/lib/X11/xkb
%endif

%ifarch sparc

%files SunMono
%defattr(644, root, root, 755)
%attr(711,root,root) /usr/X11R6/bin/XsunMono
%attr(-,root,root) /usr/X11R6/lib/X11/xkb
%endif

%ifarch sparc

%files Sun24
%defattr(644, root, root, 755)
%attr(711,root,root) /usr/X11R6/bin/Xsun24
%attr(-,root,root) /usr/X11R6/lib/X11/xkb
%endif

%ifarch i386 

%files 3DLabs
%attr(711,root,root) /usr/X11R6/bin/XF86_3DLabs
%endif

%files FBDev
%defattr(644,root,root,755)
%ifarch m68k 
%attr(755,root,root) /usr/X11R6/bin/XF68_FBDev
%attr(644,root, man) /usr/X11R6/man/man1/XF68_FBDev.1x.bz2
%else
%attr(755,root,root) /usr/X11R6/bin/XF86_FBDev
%endif

%files XF86Setup
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/XF86Setup
%attr(755,root,root) /usr/X11R6/bin/xmseconfig
%attr(-,root,root,755) /usr/X11R6/lib/X11/XF86Setup
%attr(644,root, man) /usr/X11R6/man/man1/XF86Setup.1x.bz2
%attr(644,root, man) /usr/X11R6/man/man1/xmseconfig.1x.bz2


%changelog
* Thu Feb 11 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [3.3.3.1-2d]
- next modifications of the spec file,
- fixed xf86config,

  by Maciek Ró¿ycki <macro@ds2.amg.gda.pl>

- added some patches,
- spec still not finished ...

* Thu Dec 17 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- major changes
	    -- Teriblle sorry -- but now it's not it ..;(
- emergency build for PLD Tornado. 

* Tue Dec 08 1998 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- separating binaries,
- building rpm.
