Summary:     XFree86 Window System servers and basic programs
Summary(de): Xfree86 Window-System-Server und grundlegende Programme
Summary(fr): Serveurs du système XFree86 et programmes de base
Summary(pl): XFree86 Window System wraz z podstawowymi programami
Summary(tr): XFree86 Pencereleme Sistemi sunucularý ve temel programlar
Name:        XFree86
Version:     3.3.2.3
Release:     20
Copyright:   MIT
Group:       X11/XFree86
Requires:    pam >= 0.59, xbanner
Source0:     ftp://ftp.xfree86.org/pub/XFree86/3.3/X331src-1.tgz
Source1:     ftp://ftp.xfree86.org/pub/XFree86/3.3/X331src-2.tgz
Source2:     ftp://ftp.xfree86.org/pub/XFree86/3.3/X331src-3.tgz
Source3:     ftp://ftp.xfree86.org/pub/XFree86-3.3.2/patches/cfont332.tgz
Source4:     xdm.pamd
Patch0:      XFree86-3.3-rh.patch
Patch1:      XFree86-3.3-xdm.patch
Patch2:      XFree86-3.3.2-fsstnd.patch
Patch3:      XFree86-3.3.2-pam.patch
Patch4:      XFree86-3.3-shlibs.patch
Patch5:      XFree86-3.3-notiocsltc.patch

Patch6:      XFree86-3.3-sparc.patch
Patch7:      XFree86-3.3-creator.patch
Patch8:      XFree86-3.3-sparc-glibc.patch
Patch9:      XFree86-3.3-sparc2.patch
Patch10:     XFree86-3.3-sparc3.patch
Patch11:     XFree86-3.3-sparc4.patch
Patch12:     XFree86-3.3-sparcpci.patch
Patch13:     XFree86-3.3-sparc5.patch
Patch14:     XFree86-3.3-sparcpci2.patch
Patch15:     XFree86-3.3-sparc6.patch
Patch16:     XFree86-3.3-sparcpex.patch

Patch17:     XFree86-3.3-alpha1.patch
Patch18:     XFree86-3.3-alpha2.patch
Patch19:     XFree86-3.3-egcs.patch
Patch20:     XFree86-3.3-mga1.patch

Patch30:     ftp://fpt.xfree86.org/pub/XFree86-3.3.2/patches/3.3.1-3.3.2.diff.gz
Patch31:     3.3.2-patch1
Patch32:     3.3.2-patch2
Patch33:     3.3.2-patch3
Patch34:     XFree86-HasZlib.patch
Exclusivearch: i386 alpha sparc
%ifarch sparc
Obsoletes: X11R6.1
%endif
Buildroot:   /tmp/%{name}-%{version}-root

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
mo¿liwo¶ci± pracy w wielu oknach, z wieloma klientami i do tego w ró¿nych
wystrojach okien. :) Jest u¿ywany na wiêkszo¶ci platform sytemów Unix, a
klienci mog± byæ uruchamiani tak¿e pod innymi popularnymi systemami
okienkowymi. Protokó³ X pozwala na uruchamianie aplikacji zarówno z lokalnej
maszyny jak i poprzez sieæ daj±c przez to elastyczn± implementacjê
architektury klient/serwer.

Pakiet ten zawiera podstawowe fonty, programy oraz dokumentacje dla stacji X. 
Nie zawiera X serwera który jest po¶rednikiem z Twoj± kart± graficzn± - jest
on w innym pakiecie.

%description -l tr
X Window sistemi, çoklu pencere, çoklu istemci ve çeþitli pencere stilleriyle
geniþ özelliklere sahip bir Grafik Kullanýcý Arabirimidir. Çoðu UNIX sisteminde
çalýþtýðý gibi istemcileri de birçok pencereleme sistemiyle çalýþabilir. X
protokolu kullanan uygulamalarýn yerel makina veya bilgisayar aðý üzerinden
çalýþtýrýlabilmesi esnek bir istemci/sunucu ortamý saðlar. Bu paket bir X
istasyonu için gerekli olan temel yazýtiplerini, programlarý ve belgeleri
sunar. Ekran kartýnýzý sürmek için gerekli olan X sunucusu bu pakete dahil
deðildir.

%package 75dpi-fonts
Summary:     X11R6 75dpi fonts - only need on server side
Summary(de): X11RT 76 dpi-Fonts - nur auf Serverseite erforderlich
Summary(fr): Fontes 75 dpi X11R6 - nécessaire uniquement côté serveur
Summary(pl): X11R6 fonty 75dpi - wymagane tylko po stronie serwera
Summary(tr): X11R6 75dpi yazýtipleri - yalnýzca sunucu tarafýnda gerekir
Group:       X11/XFree86/fonts
Prereq:      /usr/X11R6/bin/mkfontdir
%ifarch sparc
Obsoletes: X11R6.1-75dpi-fonts
%endif

%description 75dpi-fonts
The 75dpi fonts used on most Linux systems. Users with high resolution
displays may prefer the 100dpi fonts available in a separate package.

%description -l de 75dpi-fonts
Die 75dpi-Fonts, die auf meisten Linux-Systemen verwendet werden. Für Benutzer
mit einer hochauflösender Darstellung sind die 100dpi-Fonts eines getrennt
erhältlichen Pakets besser geeignet.

%description -l fr 75dpi-fonts
Fontes 75 dpi utilisées sur la plupart des systèmes Linux. Ceux qui ont
des écrans à haute résolution préfèreront les fontes 100 dpi disponibles
dans un autre paquetage.

%description -l pl 75dpi-fonts
Fonty 75dpi u¿ywane na wiêkszo¶ci systemów linuxowych. U¿ytkownicy 
pracuj±cy w wy¿szych rozdzielczo¶ciach mog± u¿yæ fontów 100dpi które s±
dostêpne w innym oddzielnym pakiecie.

%description -l tr 75dpi-fonts
Çoðu Linux sisteminde 75dpi yazýtipi kullanýlýr. Yüksek çözünürlük kullanan
kullanýcýlar 100dpi yazýtiplerini yeðleyebilirler.

%package 100dpi-fonts
Summary:     X11R6 100dpi fonts - only need on server side
Summary(de): X11R6 100dpi-Fonts - nur auf Server-Seite erforderlich
Summary(fr): Fontes 100ppp pour X11R6 - nécessaires seulement coté serveur.
Summary(pl): X11R6 fonty 100dpi - wymagane tylko po stronie serwera
Summary(tr): X11R6 100dpi yazýtipleri - yalnýzca sunucu tarafýnda gereklidir
Group:       X11/XFree86/fonts
Prereq:      /usr/X11R6/bin/mkfontdir
%ifarch sparc
Obsoletes: X11R6.1-100dpi-fonts
%endif

%description 100dpi-fonts
The 100dpi fonts used on most Linux systems. Users with high resolution
displays may prefer the 100dpi fonts available in a separate package.

%description -l de 100dpi-fonts
Die 100dpi-Schriftarten, die auf den meisten Linux-Systemen zum Einsatz
kommen. Anwender mit hochauflösenden Monitoren ziehen unter Umständen
die 100dpi-Schriften vor, die in einem separaten Paket erhältlich sind.

%description -l fr 100dpi-fonts
Les fontes 100dpi sont utilisées par la plupart des systèmes Linux.
Les utilisateurs ayant des hautes résolutions peuvent préférer les 
fontes 100dpi disponibles dans un package séparé.

%description -l pl 100dpi-fonts
Fonty 100dpi u¿ywane na wiêkszo¶ci systemów linuxowych.

%description -l tr 100dpi-fonts
Yüksek çözünürlük kullanan kullanýcýlar 100dpi yazýtiplerini 75dpi olanlara
yeðleyebilirler.

#%package cyrillic-fonts
#Summary:     X11R6 cyrillic fonts - only need on server side
#Summary(de): X11R6 cyrillic-Fonts - nur auf Server-Seite erforderlich
#Summary(fr): Fontes cyrillic pour X11R6 - nécessaires seulement coté serveur.
#Summary(pl): X11R6 fonty 75dpi - wymagane tylko po stronie serwera
#Summary(tr): X11R6 cyrillic yazýtipleri - yalnýzca sunucu tarafýnda gereklidir
#Group:       X11/XFree86/fonts

#%description cyrillic-fonts
#The cyrillic fonts used on most Linux systems. Users with high resolution
#displays may prefer the cyrillic fonts available in a separate package.

#%description -l pl cyrillic-fonts
#Fonty cyrylicy s± u¿ywane na wiêkszo¶ci systemów linuxowych.

#%description -l de cyrillic-fonts
#Die cyrillic-Schriftarten, die auf den meisten Linux-Systemen zum Einsatz
#kommen. Anwender mit hochauflösenden Monitoren ziehen unter Umständen
#die cyrillic-Schriften vor, die in einem separaten Paket erhältlich sind.

#%description -l fr cyrillic-fonts
#Les fontes cyrillic sont utilisées par la plupart des systèmes Linux.
#Les utilisateurs ayant des hautes résolutions peuvent préférer les 
#fontes cyrillic disponibles dans un package séparé.

#%description -l tr cyrillic-fonts
#Yüksek çözünürlük kullanan kullanýcýlar cyrillic yazýtiplerini 75dpi olanlara
#yeðleyebilirler.

%package libs
Summary:     X11R6 shared libraries
Summary(de): X11R6 shared Libraries
Summary(pl): X11R6 biblioteki dzielone (dynamiczne)
Summary(fr): Bibliothèques partagées X11R6
Group:       X11/XFree86
Prereq:      grep, /sbin/ldconfig
%ifarch sparc
Obsoletes: X11R6.1-libs
%endif

%description libs
This package contains the shared libraries most X programs need to run
properly. They are in a separate package to reduce the disk space needed
to run X applications on a machine w/o an X server (over a network).

%description -l de libs
Dieses Paket enthält die zur gemeinsamen Nutzung vorgesehenen Libraries,
die die meisten X-Programme für den einwandfreien Betrieb benötigen. Sie
wurden in einem separaten Paket untergebracht, um den
Festplattenspeicherplatz auf Computern zu reduzieren, die ohne einen X-
Server (über ein Netz) arbeiten.

%description -l fr libs
Ce paquetage contient les bibliothèques partagées nécessaires à de nombreux
programmes X. Elles se trouvent dans un paquetage séparé afin de réduire
l'espace disque nécessaire à l'exécution des applications X sur une machine
sans serveur X (en réseau).

%description -l pl libs
Pakiet zawiera biblioteki dzielone (dynamiczne) wymagane przez wiêkszo¶æ 
programów napisanych pod X'y. Znajduj± siê one w osobnym pakiecie w celu
zaoszczêdzenia miejsca na dysku (X serwer dzia³aj±cy po sieci).

%description -l tr libs
Bu paket X programlarýnýn düzgün çalýþabilmeleri için gereken kitaplýklarý
içerir. Bunlar, X programlarýný (sunucu olsun olmasýn) çalýþtýrmak için
gerekli disk alanýný azaltmak için ayrý bir paket olarak sunulmuþtur.

%package devel
Summary:     X11R6 headers and programming man pages
Summary(de): X11R6 Headers und man pages für Programmierer
Summary(pl): X11R6 Pliki nag³ówkowe oraz strony podrêcznika dla programistów
Group:       X11/XFree86
%ifarch sparc
Obsoletes: X11R6.1-devel
%endif

%description devel
Header files, and documentation for developing programs that
run as X clients. It includes the base Xlib library as well as the Xt
and Xaw widget sets. For information on programming with these libraries,
Red Hat recommends the series of books on X Programming produced by
O'Reilly and Associates.

%description -l de devel
Header-Dateien und Dokumentation zum Entwickeln von Programmen,
die als X-Clients laufen. Enthält die Xlib-Library und die Widget-Sätze Xt
und Xaw. Information zum Programmieren mit diesen Libraries finden Sie 
in der Buchreihe zur X-Programmierung von O'Reilly and Associates.

%description -l pl devel
Pliki nag³ówkowe, dokumentcja dla programistów rozwijaj±cych aplikacje 
klienckie pod X'y. Zawiera podstatwow± bibliotekê Xlib a tak¿e Xt i Xaw.
Wiêcej informacji nt. pisania programów przy u¿yciu tych bibliotek mo¿esz 
znale¼æ w ksi±¿kach wydawnictwa O'Reilly and Associates (X Programming) 
polecanych przez Red Hat'a.

%description -l fr devel
Fichiers d'en-tête, et documentation pour développer des
programmes s'exécutant en clients X. Cela comprend la Bibliothéque Xlib
de base aussi bien que les ensembles de widgets Xt et Xaw. Pour des
informations sur la programmation avec ces Bibliothéques, Red Hat 
recommande la série d'ouvrages sur la programmation  X editée par
O'Reilly and Associates.

%package static
Summary:     X11R6 static libraries
Summary(de): X11R6 statische Libraries
Summary(pl): X11R6 biblioteki statyczne
Summary(fr): Bibliothèques X11R6 statiques
Group:       X11/XFree86

%description static
X11R6 static libraries.

%description -l de static
X11R6 statische Libraries

%description -l pl static
X11R6 biblioteki statyczne.

%description -l fr static
Bibliothèques X11R6 statiques

%package S3
Summary:     XFree86 S3 server
Summary(de): XFree86 S3 Server
Summary(fr): Serveur XFree86 pour S3
Summary(pl): XFree86 serwer dla kart opartych na uk³adzie S3
Summary(tr): XFree86 S3 sunucularý
Group:       X11/XFree86/Servers

%description S3
X server for cards built around chips from S3, including most #9 cards,
many Diamond Stealth cards, Orchid Farenheits, Mirco Crystal 8S, most STB
cards, and some motherboards with built in graphics accelerators (such
as the IBM ValuePoint line).

%description -l de S3
X-Server für Steckkarten mit dem S3-Chipsatz (inkl. den meisten #9-Karten),
Karten wie Diamond Stealth, Orchid Farenheit und Mirco Crystal 8S, den meisten STB-Karten
sowie einigen Motherboards mit integrierten Grafikbeschleunigern (z.B. 
die Reihe IBM ValuePoint).

%description -l fr S3
Serveur X pour les cartes construites autour des circuits S3, dont la
plupart des cartes #9, de nombreuses Diamond Stealth, Orchid Farenheits,
Mirco Crystal 8S, la plupart des cartes STB et certaines cartes mères
intégrant des accélérateurs graphiques (comme la gamme ValuePoint d'IBM).

%description -l pl S3
X serwer dla kart opartych na uk³adzie S3 - s± ta m.in. #9, wiele kart 
Diamond Stealth, Orchid Farenheits, Mirco Crystal 8S, wiêkszo¶c kart STB
a tak¿e niektóre p³yty g³ówne z wbudowanymi akcelatorami graficznymi 
(jak np. ValuePoint IBM'a).

%description -l tr S3
S3 tabanlý ekran kartlarý için sunucular. Çoðu #9, Diamond Stealth, Orchid
Fahrenheit, Mirco Crystal 8S, çoðu STB ve bazý anakarta tümleþik grafik
hýzlandýrýcýlar bu gruba girer. S3 Virge sunucusu ayrý bir pakette yer alýr.

%package I128
Summary:     XFree86 #9 Imagine 128 Server
Summary(de): XFree86 #9 Imagine 128 Server
Summary(fr): Serveur Xfree86 pour #9 Imagine 128
Summary(pl): XFree86 serwer dla kart #9 Imagine 128
Summary(tr): XFree86 #9 Imagine 128 sunucusu
Group:       X11/XFree86/Servers

%description I128
X server for the #9 Imagine 128 board.

%description I128
X serwer dla kart the #9 Imagine 128.

%description -l de I128
X-Server für die Steckkarte #9 Imagine 128

%description -l fr I128
Serveur X pour les cartes #9 Imagine 128.

%description -l tr I128
#9 Imagine kartý için X sunucusu.

%package S3V
Summary:     XFree86 S3 Virge server
Summary(de): Xfree86 S3 Virge-Server
Summary(fr): Serveur XFree86 pour S3 Virge
Summary(pl): XFree86 serwer dla kart S3 Virge
Summary(tr): XFree86 S3 Virge sunucusu
Group:       X11/XFree86/Servers

%description S3V
X server for cards built around the S3 Virge chipset.

%description -l de S3V
X-Server für Grafikkarten mit dem S3 Virge-Chipsatz.

%description -l pl S3V
X serwer dla kart opartych na S3 Virge'u.

%description -l fr S3V
Serveur X pour les cartes construites autour du circuit S3 Virge

%description -l tr S3V
XFree86 S3 Virge sunucusu

%package Mach64
Summary:     XFree86 Mach64 server
Summary(de): Xfree86 Mach64-Server
Summary(fr): Serveur Mach64 de XFree86
Summary(pl): XFree86 serwer dla kart Mach64
Summary(tr): XFree86 Mach64 sunucusu
Group:       X11/XFree86/Servers

%description Mach64
X server for ATI Mach64 based cards such as the Graphics Xpression, GUP Turbo,
and WinTurbo cards. This server is known to have problems with some Mach64
cards which newer versions of XFree86 (which were only available as BETA
releases at the time of this release) may fix. Look at http://www.xfree86.org
for information on updating this server.

%description -l de Mach64
X-Server für ATI Mach64-Karten wie Graphics Xpression, GUP Turbo,
und WinTurbo. Dieser Server verursacht gelegentlich Probleme mit Mach64-Karten,
die aber von einer neueren Version von XFree86 (der als Beta-Version verfügbar ist)
gelöst werden könnten. Unter
http://www.xfree86.org finden Sie Informationen zum Aktualisieren dieses Servers.

%description -l fr Mach64
Serveur X pour les cartes basées sur l'ATI Mach64, comme les cartes GUP Turbo,
Graphics Xpression et WinTurbo. Ce serveur est connu pour avoir des problèmes
avec certaines cartes Mach64 que les versions plus récentes d'XFree86 corrigent
(elles ne sont encore qu'en version BETA au moment de cette distribution).
Consultez http://www.xfree86.org pour les informations de mise à jour du serveur.

%description -l pl Mach64
X serwer dla kart opartych na uk³adzie ATI Mach64 jak np. Graphics Xpression,
GUP Turbo, a tak¿e WinTurbo. Serwer jest znany z problemów z niektórymi 
kartami Mach64, które jednak mog± byæ ju¿ poprawione w nowszej wersji 
XFree86 (osi±galna wy³±cznie jako wersja BETA). Spójrz na stronê 
http://www.xfree86.org gdzie znajdziesz informacje nt. nowszych wersji 
XFree86.

%description -l tr Mach64
ATI Mach64 tabanlý kartlar için X sunucusu. Graphics Xpression, GUP Turbo ve
WinTurbo gibi kartlarý destekler. Bazý Mach64 kartlarýn yeni XFree86 ile
sorun yaþadýklarý bilinmektedir. Bu sorunla ilgili son bilgilere ulaþmak için
lütfen http://www.xfree86.org adresine bakýn.

%package Sun
Summary:     XFree86 Sun server for monochrome and 8-bit color SBUS framebuffers
Summary(pl): XFree86 Sun serwer do monochromatycznych kart i 8-bitowych kolorowych framebufferów SBUS
Group:       X11/XFree86/Servers
Obsoletes:   X11R6.1-Sun

%description Sun
To run X Windows programs requires an X server for your specific hardware.
This package includes the X server for Sun computers with monochrome and
8-bit color SBUS framebuffers.

%description -l pl Sun
Aby uruchomiæ X Window System potrzebujesz X serwera dostosowanego do Twojego
sprzêtu. Ten pakiet zawiera X serwer dla komputerów firmy Sun z 
monochromatycznymi lub te¿ 8-bitowymi kolorowymi framebufferami SBUS.

%package SunMono
Summary:     XFree86 Sun server for monochrome SBUS framebuffers only
Summary(pl): XFree86 Sun serwer wy³±cznie do monochromatycznych framebufferów SBUS
Group:       X11/XFree86/Servers
Obsoletes:   X11R6.1-SunMono

%description SunMono
To run X Windows programs requires an X server for your specific hardware.
This package includes the X server for Sun computers with monochrome
SBUS framebuffers only.

%description -l pl SunMono
Aby uruchomiæ X Window System potrzebujesz X serwera dostosowanego do Twojego
sprzêtu. Ten pakiet zawiera X serwer dla komputerów firmy Sun z wy³±cznie
monochromatycznymi framebufferami SBUS.

%package Sun24
Summary:     XFree86 Sun server for all supported SBUS framebuffers
Summary(pl): XFree86 serwer Sun'owski dla wszystkich wspieranych framebufferów SBUS
Group:       X11/XFree86/Servers
Obsoletes:   X11R6.1-Sun24

%description Sun24
To run X Windows programs requires an X server for your specific hardware.
This package includes the X server for Sun computers with all supported
SBUS framebuffers.

%description -l pl Sun24
Aby uruchomiæ X Window System potrzebujesz X serwera dostosowanego do Twojego
sprzêtu. Ten pakiet zawiera X serwer dla komputerów firmy Sun dla wszystkich 
wspieranych framebufferów SBUS.

%package Xvfb
Summary:    XFree86 Xvfb server
Summary(pl): Xfree86 serwer Xvfb
Group:      X11/XFree86/Servers

%description Xvfb
X server which runs in a X window.

%description -l pl Xvfb
X serwer uruchamiany w okienku pod innym X serwerem.

%package Xnest
Summary:     XFree86 Xnest server
Summary(pl): XFree86 serwer Xnest
Group:       X11/XFree86/Servers

%description Xnest
X server which runs in a X window.

%description -l pl Xnest
X serwer uruchamiany w okienku pod innym X serwerem.

%package 8514
Summary:     XFree86 8514 server
Summary(de): XFree86 8514 Server
Summary(fr): serveur 8514 pour XFree86.
Summary(pl): XFree86 serwer dla kart 8514
Summary(tr): XFree86 8514 sunucusu
Group:       X11/XFree86/Servers

%description 8514
X server for older IBM 8514 cards and compatibles from companies such as
ATI.

%description -l de 8514
X-Server für ältere IBM 8514- und kompatible Karten, z.B. von ATI.

%description -l fr 8514
Serveur X pour les vieilles cartes IBM 8514 et compatibles comme lesATI.

%description -l pl 8514
X serwer dla starszych kart IBM 8514 oraz kompatybilnych robionych przez inne 
firmy takie jak np. ATI.

%description -l tr 8514
Eski IBM 8514 ve uyumlu kartlar (ATI gibi) için sunucu.

%package AGX
Summary:     XFree86 AGX server
Summary(de): XFree86 AGX Server
Summary(fr): serveur AGX pour XFree86.
Summary(pl): XFree86 serwer dla kart AGX.
Summary(tr): XFree86 AGX sunucusu
Group:       X11/XFree86/Servers

%description AGX
X server for AGX based cards such as the Boca Vortex, Orchid Celsius,
Spider Black Widow, and Hercules Graphite.

%description -l de AGX
X-Server für Karten auf AGX-Basis wie etwa Boca Vortex, Orchid Celsius, 
Spider Black Widow und Hercules Graphite.

%description -l fr AGX
Serveur X pour les cartes à base d'AGX comme la Boca Vortex, l'Orchid

%description -l pl AGX
X serwer dla kart bazuj±cych na AGX takich jak Boca Vortex, Orchid Celsius,
Spider Black Window oraz Hercules Graphite.

%description -l tr AGX
Boca Vortex, Orchid Celsius, Spider Black Widow ve Hercules Graphite gibi AGX
tabanlý kartlar için X sunucusu.

%package Mach32
Summary:     XFree86 Mach32 server
Summary(de): Xfree86 Mach32-Server
Summary(fr): Serveur XFree86 pour Mach32
Summary(pl): XFree86 serwer dla kart Mach32
Summary(tr): XFree86 Mach32 sunucusu
Group:       X11/XFree86/Servers

%description Mach32
X server for cards built around ATI's Mach32 chip, including the ATI
Graphics Ultra Pro and Ultra Plus.

%description -l de Mach32
X-Server für Karten auf der Basis des ATI Mach32-Chip, einschließlich 
ATI Graphics Ultra Pro und Ultra Plus.

%description -l fr Mach32
Serveur X pour les cartes utilisant le circuit ATI Mach32, dont les
cartes ATI Graphics Ultra Pro et Ultra Plus.

%description -l pl Mach32
X serwer dla kart zbudowanych na uk³adzie ATI Mach32 w³±czaj±c w to ATI
Graphics Ultra Pro oraz Ultra Plus

%description -l tr Mach32
ATI Mach32 tabanlý ATI Graphics Ultra Pro ve Ultra Plus kartlarý için X
sunucusu.

%package Mach8
Summary:     XFree86 Mach8 server
Summary(de): XFree86 Mach8 Server
Summary(fr): Serveur Mach8 pour XFree86
Summary(pl): XFree86 serwer dla kart Mach8
Summary(tr): XFree86 Mach8 sunucusu
Group:       X11/XFree86/Servers

%description Mach8
X server for cards built around ATI's Mach8 chip, including the ATI
8514 Ultra and Graphics Ultra.

%description -l de Mach8
X-Server für Karten auf der Basis des ATI Mach8-Chips, einschließlich
des ATI 8514 Ultra und des Graphics Ultra.

%description -l fr Mach8
Serveur X pour les cartes basées sur les chips ATI Mach8, dont les cartes
ATI 8514 Ultra et Graphics Ultra.

%description -l pl Mach8
X serwer dla kart opartych na uk³adzie ATI Mach8, w³±czaj±c w to ATI 8514 
Ultra oraz graphics Ultra.

%description -l tr Mach8
ATI 8514 Ultra ve Graphics Ultra gibi ATI Mach8 tabanlý kartlar için X
sunucusu.

%package Mono
Summary:     XFree86 Mono server
Summary(de): Xfree86 Mono-Server
Summary(fr): Serveur Monochrome de XFree86
Summary(pl): XFree86 Monochromatyczny serwer
Summary(tr): XFree86 Mono sunucusu
Group:       X11/XFree86/Servers

%description Mono
Generic monochrome (2 color) server for VGA cards, which works on nearly
all VGA style boards with limited resolutions.

%description -l de Mono
Generischer monochromer (Schwarzweiß-) Server für VGA-Karten, der 
praktisch mit allen VGA-ähnlichen Karten mit beschränkter Auflösung
funktioniert.

%description -l fr Mono
Serveur générique monochrome (2 couleurs) pour les cartes VGA, fonctionne avec
pratiquement toutes les cartes VGA ayant des résolutions limitées.

%description -l pl Mono
Dwu kolorowy (monochromatyczny) serwer dla kart VGA, pracuje na wszystkich 
typu VGA w ograniczonej rozdzielczo¶ci.

%description -l tr Mono
Mono (2 renk) VGA kartlarý için genel X sunucusu. Kýsýtlý bir çözünürlük
altýnda birçok VGA kart ile çalýþýr.

%package P9000
Summary:     XFree86 P9000 server
Summary(de): XFree86 P9000 Server
Summary(fr): Serveur XFree86 pour P9000
Summary(pl): XFree86 serwer dla kart P9000
Summary(tr): XFree86 P9000 sunucusu
Group:       X11/XFree86/Servers

%description P9000
X server for cards built around the Weitek P9000 chips such as most
Diamond Viper cards and the Orchid P9000 card.

%description -l de P9000
X-Server für Karten auf Basis des Weitek P9000-Chip, wie die meisten 
Diamond Viper und Orchid P9000-Karten.

%description -l fr P9000
Serveur X pour les cartes construites autour des circuits P9000 de
Weitek, comme la plupart des cartes Diamond Viper et l'Orchid P9000.

%description -l pl P9000
X serwer dla kart zbudowanych na uk³adzie Weitek P9000 czyli w wiêkszo¶ci 
karty Diamond Viper oraz Orchid P9000.

%description -l tr P9000
Diamond Viper ve Orchid P9000 gibi Weitek P9000 tabanlý kartlar için X
sunucusu.

%package SVGA
Summary:     XFree86 SVGA server
Summary(de): XFree86 SVGA-Server
Summary(fr): Serveur XFree86 pour SVGA
Summary(pl): XFree86 serwer dla kart SVGA
Summary(tr): XFree86 SVGA sunucusu
Group:       X11/XFree86/Servers

%description SVGA
X server for most simple framebuffer SVGA devices, including cards built
from ET4000 chips, Cirrus Logic chips, Chips and Technologies laptop chips,
Trident 8900 and 9000 chips. It works for Diamond Speedstar, Orchid
Kelvins, STB Nitros and Horizons, Genoa 8500VL, most Actix boards,
the Spider VLB Plus. It also works for many other chips and cards, so try
this server if you are having problems.

%description -l de SVGA
X-Server für die elementarsten Framebuffer-SVGA-Geräte, einschließlich 
Karten, die aus ET4000-Chips, Cirrus Logic-Chips, Chips and Technologies 
Laptop-Chips sowie Trident 8900 und 9000 Chips gebaut sind. Funktioniert 
mit Diamond Speedstar, Orchid Kelvins, STB Nitros und Horizons, 
Genoa 8500VL, den meisten Actix-Karten sowie Spider VLB Plus und außerdem 
mit vielen anderen Chips und Karten. Es lohnt sich, diesen Server 
auszuprobieren, wenn Sie Probleme haben.

%description -l fr SVGA
Serveur X pour les circuits SVGA les plus simples, dont les cartes construites
avec les circuits ET4000, Cirrus Logic, Chips and Technologies laptop,
Trident 8900 et 9000. Fonctionne pour les cartes Diamond Speedstar, Orchid
Kelvins, STB Nitros et Horizons, Genoa 8500VL, la plupart des Actix
et la Spider VLB Plus. Fonctionne aussi pour de nombreux autres circuits
et cartes. Essayez ce serveur si vous avez des problèmes.

%description -l pl SVGA
X serwer dla wiêkszo¶ci prostych kart SVGA, w³±czaj±c karty zbudowane na 
uk³adach ET4000, Cirrus Logic, Trident 8900 i 9000, oraz uk³ady wystêpuj±ce 
w laptopach. Dzia³a tak¿e z kartami Diamnod Speedstar, Orchid Kelvins,
STB Nitros i Horizons, Genoa 8500VL, wiêkszo¶æ Actix, Spider VLB Plus. 
Dzia³a równie¿ na wielu innych kartach opartych na innych uk³adach wiêc
spróbuj ten serwer je¶li masz jakie¶ problemy.

%description -l tr SVGA
ET4000, Cirrus Logic, Chips and Technologies dizüstü, Trident 8900 ve 9000
gibi basit 'framebuffer' SVGA kullananan kartlar için X sunucusu. Ayný
zamanda Diamond Speedstar, Orchid Kelvins, STB Nitros / Horizons, Genoa
8500VL, çoðu Actix kartlarý, Spider VLB Plus gibi kartlar ve birçok diðer
kart ile de çalýþýr. Herhangi bir sorun yaþarsanýz bu sunucuyu deneyin.

%package VGA16
Summary:     XFree86 VGA16 server
Summary(de): XFree86 VGA16-Server
Summary(fr): Serveur XFree86 pour VGA16
Summary(pl): XFree86 serwer dla kart VGA16
Summary(tr): XFree86 VGA16 sunucusu
Group:       X11/XFree86/Servers

%description VGA16
Generic 16 color server for VGA boards. This works on nearly all VGA style
graphics boards, but only in low resolution with few colors.

%description -l de VGA16
Generischer 16-Farben-Server für VGA-Karten. Funktioniert auf fast allen VGA-
Grafikkarten, allerdings nur bei geringer Auflösung und wenigen Farben.

%description -l fr VGA16
Serveur 16 couleurs générique pour cartes VGA. Fonctionne avec presque
toutes les cartes VGA, mais seulement en faible résolution avec peu de couleurs.

%description -l pl VGA16
Podstawowy serwer dla 16 kolorowego trybu pracy kart VGA. Dzia³a ze 
wszystkimi kartami VGA ale jedynie w niskiej rozdzielczo¶ci i ma³ej ilo¶ci 
kolorów.

%description -l tr VGA16
VGA kartlarý için genel 16 renk sunucusu. Çoðu VGA tipi kart ile düþük renk
ve çözünürlükte çalýþýr.

%package W32
Summary:     XFree86 W32 server
Summary(de): XFree86 W32 Server
Summary(fr): Serveur XFree86 pour W32
Summary(pl): XFree86 serwer dla kart W32
Summary(tr): XFree86 W32 sunucusu
Group:       X11/XFree86/Servers

%description W32
X server for cards built around the ET4000/W32 chips, including the
Genoa 8900 Phantom 32i, Hercules Dynamite cards, LeadTek WinFast S200,
Sigma Concorde, STB LightSpeed, TechWorks Thunderbolt, and ViewTop PCI.

%description -l de W32
Genoa 8900 Phantom 32I, Hercules Dynamite, LeaTek WinFast S200, 
Sigma Concorde, STB LightSpeed, TechWorks Thunderbolt und ViewTop PCI.

%description -l fr W32
Serveur X pour les cartes basée sur les chips ET4000/W32, dontla Genoa 8900 Phantom 32i, les cartes Hercules Dynamite, la LeadTek WinFast
S200, la Sigma Concorde, la STB LightSpeed, la TechWorks Thunderbolt,
et la ViewTop PCI.

%description -l pl W32
X serwer dla kart zbudowanych na uk³adzie ET4000/W32, w³±czaj±c w to karty 
Genoa 8900 Phantom 32i, Hercules Dynamite, LeadTek WinFast S200, 
Sigma Concorde, STB LightSpeed, TechWorks Thunderbolt oraz karty ViewTop (PCI).

%description -l tr W32
Genoa 8900 Phantom 32i, Hercules Dynamite kartlarý, LeadTek WinFast S200,
Sigma Concorde, STB LightSpeed, TechWorks Thunderbolt, ve ViewTop PCI
gibi kartlarýn kullandýðý ET4000/W32 tabanlý kartlar için X sunucusu.

%package TGA
Summary:     XFree86 TGA server
Summary(pl): XFree86 serwer dla kart TGA
Group:       X11/XFree86/Servers

%description TGA
Eight bit X server for Digital TGA boards based on the DC21040 chips. These
adapters are very popular in Alpha workstations and are included with Alpha
UDB (Multia) machines.

%description -l pl TGA
256-cio kolorowy X serwer dla kart Digital TGA zbudowanych na uk³adzie 
DC21040. S± to bardzo popularne karty wystêpuj±ce w stacjach roboczych Alpha 
w tym Alpha UDB (Multia).

#%package XF86Setup
#Group:       X11/XFree86
#Summary:     Graphical configuration tool for XFree86
#Summary(pl): Graficzne narzêdzie do konfiguracji XFree86
#Requires:    XFree86-VGA16 = %{version}

#%description XF86Setup
#XF86Setup is a graphical configuration tool for the XFree86 family of
#servers. It allows you to configure video settings, keyboard layouts,
#mouse type, and other miscellaneous options. It is slow however, and
#requires the generic VGA 16 color server be available.

#%description -l pl XF86Setup
#XF86Setup jest graficznym narzêdziem do konfiguracji XFree86. Pozwala na 
#skonfigurowanie karty graficznej, klawiatury, myszki itp. Znany jest z tego 
#¿e jest do¶¶ wolny, wymaga tak¿e zainstalowanego serwera VGA 16.

%prep
%setup -q -c -a 1 -a 2 -a 3
%patch30 -p0 -b .orig

# Clean up to save a *lot* of disk space
find . -name "*.orig" -print | xargs rm -f
find . -size 0 -print | xargs rm -f

%patch0 -p1 -b .rh
%patch1 -p1 -b .rhxdm
%patch2 -p1 -b .fsstnd
%patch3 -p1 -b .nopam
%patch4 -p0 -b .shlibs
%patch5 -p1 -b .tiocsltc

%patch31 -p0 -b .pat1
%patch32 -p0 -b .pat2
%patch33 -p0 -b .pat3

%ifarch sparc
%patch6 -p1 -b .sparc
%patch7 -p1 -b .ffb
%patch8 -p1 -b .glibc
%patch9 -p1 -b .sparc2
%patch10 -p1 -b .sparc3
%patch11 -p1 -b .sparc4
%patch12 -p1 -b .sparcpci
%patch13 -p1 -b .sparc5
%patch14 -p1 -b .sparcpci2
%patch15 -p1 -b .sparc6
%patch16 -p1 -b .sparcpex
%endif

%patch17 -p0 -b .alpha1
%patch18 -p0 -b .alpha2
%patch19 -p0 -b .egcs
%patch20 -p0 -b .mga1

%patch34 -p1 -b .HasZlib

%build
(cd xc; \
make World	CDEBUGFLAGS="$RPM_OPT_FLAGS" \
		CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
		LOCAL_LDFLAGS=-s )

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/{pam.d,X11},usr/{include,bin,lib}}
install ${RPM_SOURCE_DIR}/xdm.pamd $RPM_BUILD_ROOT/etc/pam.d/xdm

ln -s ../X11R6/include/X11 $RPM_BUILD_ROOT/usr/include/X11

(cd xc; make install install.man DESTDIR=$RPM_BUILD_ROOT)

# setup the default X server
rm -f $RPM_BUILD_ROOT/usr/X11R6/bin/X
ln -s Xwrapper $RPM_BUILD_ROOT/usr/X11R6/bin/X

ln -sf ../../../../etc/X11/XF86Config $RPM_BUILD_ROOT/usr/X11R6/lib/X11/XF86Config

for i in xdm twm fs xsm; do
    cp -ar $RPM_BUILD_ROOT/usr/X11R6/lib/X11/$i $RPM_BUILD_ROOT/etc/X11
    rm -rf $RPM_BUILD_ROOT/usr/X11R6/lib/X11/$i
    ln -sf ../../../../etc/X11/$i $RPM_BUILD_ROOT/usr/X11R6/lib/X11/$i
done

# we get xinit from a separate package
rm -rf $RPM_BUILD_ROOT/usr/X11R6/lib/X11/xinit
ln -sf ../../../../etc/X11/xinit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/xinit

# Fix up symlinks
rm -f $RPM_BUILD_ROOT/usr/{bin/X11,include/X11,lib/X11}
ln -sf ../X11R6/bin $RPM_BUILD_ROOT/usr/bin/X11
ln -sf ../X11R6/include/X11 $RPM_BUILD_ROOT/usr/include/X11
ln -sf ../X11R6/lib/X11 $RPM_BUILD_ROOT/usr/lib/X11

(set +x; strip $RPM_BUILD_ROOT/usr/X11R6/{bin/*,lib/lib*.so.*.*})

for n in libX11.so.6.1 libICE.so.6.3 libSM.so.6.0 libXext.so.6.3 libXt.so.6.0 \
	 libXmu.so.6.0 libXaw.so.6.1 libXIE.so.6.0 libXi.so.6.0 \
	 libXtst.so.6.1; do
	ln -sf $n $RPM_BUILD_ROOT/usr/X11R6/lib/`echo $n | sed "s/\.so.*/\.so/"`
done

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*so.*.*

%post libs
grep "^/usr/X11R6/lib$" $RPM_BUILD_ROOT/etc/ld.so.conf >/dev/null 2>&1
[ $? -ne 0 ] && echo "/usr/X11R6/lib" >> $RPM_BUILD_ROOT/etc/ld.so.conf
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

%post 75dpi-fonts
mkfontdir /usr/X11R6/lib/X11/fonts/75dpi

%postun 75dpi-fonts
mkfontdir /usr/X11R6/lib/X11/fonts/75dpi

%post 100dpi-fonts
mkfontdir /usr/X11R6/lib/X11/fonts/100dpi

%postun 100dpi-fonts
mkfontdir /usr/X11R6/lib/X11/fonts/100dpi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%config %doc /usr/X11R6/lib/X11/XF86Config.eg
%docdir /usr/X11R6/lib/X11/doc
%doc /usr/X11R6/lib/X11/Cards

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
/usr/X11R6/lib/modules
/usr/X11R6/lib/X11/xkb
%endif

%config /etc/pam.d/xdm
%config /etc/X11/twm/system.twmrc
%config /etc/X11/fs/config
%config /etc/X11/xsm/system.xsm
%config /etc/X11/xdm/xdm-config
%config /etc/X11/xdm/chooser
%config /etc/X11/xdm/Xsetup_0
%config /etc/X11/xdm/Xsession
%config /etc/X11/xdm/Xservers
%config /etc/X11/xdm/Xresources
%config /etc/X11/xdm/Xaccess
%config /etc/X11/xdm/TakeConsole
%config /etc/X11/xdm/GiveConsole

/usr/X11R6/lib/X11/XErrorDB
/usr/X11R6/lib/X11/XKeysymDB
/usr/X11R6/lib/X11/locale
/usr/X11R6/lib/X11/lbxproxy
/usr/X11R6/lib/X11/proxymngr
%config /usr/X11R6/lib/X11/app-defaults/*

/usr/X11R6/lib/X11/xinit
/usr/X11R6/lib/X11/xdm
/usr/X11R6/lib/X11/twm
/usr/X11R6/lib/X11/fs
/usr/X11R6/lib/X11/xsm

/usr/X11R6/lib/X11/xserver/SecurityPolicy
/usr/X11R6/lib/X11/XF86Config
/usr/X11R6/lib/X11/rstart/rstartd.real
%config /usr/X11R6/lib/X11/rstart/config
/usr/X11R6/lib/X11/rstart/commands/x11r6/@List
/usr/X11R6/lib/X11/rstart/commands/x11r6/LoadMonitor
/usr/X11R6/lib/X11/rstart/commands/x11r6/Terminal
/usr/X11R6/lib/X11/rstart/commands/@List
/usr/X11R6/lib/X11/rstart/commands/ListContexts
/usr/X11R6/lib/X11/rstart/commands/ListGenericCommands
/usr/X11R6/lib/X11/rstart/contexts/@List
/usr/X11R6/lib/X11/rstart/contexts/default
/usr/X11R6/lib/X11/rstart/contexts/x11r6
/usr/X11R6/lib/X11/x11perfcomp
/usr/X11R6/lib/X11/doc
/usr/X11R6/lib/X11/etc/sun.termcap
/usr/X11R6/lib/X11/etc/sun.terminfo
/usr/X11R6/lib/X11/etc/xterm.termcap
/usr/X11R6/lib/X11/etc/xterm.terminfo
/usr/X11R6/lib/X11/etc/et4000clock.c
/usr/X11R6/lib/X11/etc/xmodmap.std
/usr/X11R6/lib/X11/etc/postinst.sh
/usr/X11R6/lib/X11/etc/preinst.sh
%attr(711, root, root) /usr/X11R6/bin/Xwrapper
%attr(755, root, root) /usr/X11R6/bin/X
%attr(755, root, root) /usr/X11R6/bin/Xprt
%attr(755, root, root) /usr/X11R6/bin/lbxproxy
#%attr(755, root, root) /usr/X11R6/bin/oclock
%attr(755, root, root) /usr/X11R6/bin/proxymngr
%attr(755, root, root) /usr/X11R6/bin/rstartd
%attr(755, root, root) /usr/X11R6/bin/xfindproxy
%attr(755, root, root) /usr/X11R6/bin/xfwp
%attr(755, root, root) /usr/X11R6/bin/xrx
%attr(755, root, root) /usr/X11R6/bin/lndir
%attr(755, root, root) /usr/X11R6/bin/mkdirhier
%attr(755, root, root) /usr/X11R6/bin/gccmakedep
%attr(755, root, root) /usr/X11R6/bin/mergelib
%attr(755, root, root) /usr/X11R6/bin/makeg
%attr(755, root, root) /usr/X11R6/bin/appres
%attr(755, root, root) /usr/X11R6/bin/bdftopcf
%attr(755, root, root) /usr/X11R6/bin/beforelight
%attr(755, root, root) /usr/X11R6/bin/bitmap
%attr(755, root, root) /usr/X11R6/bin/bmtoa
%attr(755, root, root) /usr/X11R6/bin/atobm
%attr(755, root, root) /usr/X11R6/bin/editres
%attr(755, root, root) /usr/X11R6/bin/fsinfo
%attr(755, root, root) /usr/X11R6/bin/fslsfonts
%attr(755, root, root) /usr/X11R6/bin/fstobdf
%attr(755, root, root) /usr/X11R6/bin/iceauth
%attr(755, root, root) /usr/X11R6/bin/mkfontdir
%attr(755, root, root) /usr/X11R6/bin/showrgb
%attr(755, root, root) /usr/X11R6/bin/rstart
%attr(755, root, root) /usr/X11R6/bin/smproxy
%attr(755, root, root) /usr/X11R6/bin/twm
%attr(755, root, root) /usr/X11R6/bin/x11perf
%attr(755, root, root) /usr/X11R6/bin/x11perfcomp
%attr(755, root, root) /usr/X11R6/bin/Xmark
%attr(755, root, root) /usr/X11R6/bin/xauth
%attr(755, root, root) /usr/X11R6/bin/xclipboard
%attr(755, root, root) /usr/X11R6/bin/xcutsel
%attr(755, root, root) /usr/X11R6/bin/xclock
%attr(755, root, root) /usr/X11R6/bin/xcmsdb
%attr(755, root, root) /usr/X11R6/bin/xconsole
%attr(755, root, root) /usr/X11R6/bin/xdm
%attr(755, root, root) /usr/X11R6/bin/sessreg
%attr(755, root, root) /usr/X11R6/bin/xdpyinfo
%attr(755, root, root) /usr/X11R6/bin/dga
%attr(755, root, root) /usr/X11R6/bin/xfd
%attr(755, root, root) /usr/X11R6/bin/xfs
%attr(755, root, root) /usr/X11R6/bin/xhost
%attr(755, root, root) /usr/X11R6/bin/xieperf
%attr(755, root, root) /usr/X11R6/bin/xinit
%config %attr(755, root, root) /usr/X11R6/bin/startx
%attr(755, root, root) /usr/X11R6/bin/setxkbmap
%attr(755, root, root) /usr/X11R6/bin/xkbcomp
%attr(755, root, root) /usr/X11R6/bin/xkbevd
%attr(755, root, root) /usr/X11R6/bin/xkbprint
%attr(755, root, root) /usr/X11R6/bin/xkbvleds
%attr(755, root, root) /usr/X11R6/bin/xkbwatch
%attr(755, root, root) /usr/X11R6/bin/xkbbell
%attr(755, root, root) /usr/X11R6/bin/xkill
%attr(755, root, root) /usr/X11R6/bin/xlogo
%attr(755, root, root) /usr/X11R6/bin/xlsatoms
%attr(755, root, root) /usr/X11R6/bin/xlsclients
%attr(755, root, root) /usr/X11R6/bin/xlsfonts
%attr(755, root, root) /usr/X11R6/bin/xmag
%attr(755, root, root) /usr/X11R6/bin/xmh
%attr(755, root, root) /usr/X11R6/bin/xmodmap
%attr(755, root, root) /usr/X11R6/bin/xprop
%attr(755, root, root) /usr/X11R6/bin/xrdb
%attr(755, root, root) /usr/X11R6/bin/xset
%attr(755, root, root) /usr/X11R6/bin/xrefresh
%attr(755, root, root) /usr/X11R6/bin/xsetmode
%attr(755, root, root) /usr/X11R6/bin/xsetpointer
%attr(755, root, root) /usr/X11R6/bin/xsetroot
%attr(755, root, root) /usr/X11R6/bin/xsm
%attr(755, root, root) /usr/X11R6/bin/xstdcmap
%attr(4755, root, root) /usr/X11R6/bin/xterm
%attr(755, root, root) /usr/X11R6/bin/resize
%attr(755, root, root) /usr/X11R6/bin/xvidtune
%attr(755, root, root) /usr/X11R6/bin/xwd
%attr(755, root, root) /usr/X11R6/bin/xwininfo
%attr(755, root, root) /usr/X11R6/bin/xwud
%attr(755, root, root) /usr/X11R6/bin/reconfig
%attr(755, root, root) /usr/X11R6/bin/xf86config
%attr(755, root, root) /usr/X11R6/bin/scanpci
%attr(755, root, root) /usr/X11R6/bin/SuperProbe
%attr(755, root, root) /usr/X11R6/bin/xon
/usr/X11R6/include/X11/bitmaps

%attr(644, root,  man) /usr/X11R6/man/man1/lbxproxy.1x
#%attr(644, root,  man) /usr/X11R6/man/man1/oclock.1x
%attr(644, root,  man) /usr/X11R6/man/man1/proxymngr.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xfindproxy.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xfwp.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xrx.1x
%attr(644, root,  man) /usr/X11R6/man/man1/lndir.1x
%attr(644, root,  man) /usr/X11R6/man/man1/makestrs.1x
%attr(644, root,  man) /usr/X11R6/man/man1/makeg.1x
%attr(644, root,  man) /usr/X11R6/man/man1/mkdirhier.1x
%attr(644, root,  man) /usr/X11R6/man/man1/appres.1x
%attr(644, root,  man) /usr/X11R6/man/man1/bdftopcf.1x
%attr(644, root,  man) /usr/X11R6/man/man1/beforelight.1x
%attr(644, root,  man) /usr/X11R6/man/man1/bitmap.1x
%attr(644, root,  man) /usr/X11R6/man/man1/bmtoa.1x
%attr(644, root,  man) /usr/X11R6/man/man1/atobm.1x
%attr(644, root,  man) /usr/X11R6/man/man1/editres.1x
%attr(644, root,  man) /usr/X11R6/man/man1/fsinfo.1x
%attr(644, root,  man) /usr/X11R6/man/man1/fslsfonts.1x
%attr(644, root,  man) /usr/X11R6/man/man1/fstobdf.1x
%attr(644, root,  man) /usr/X11R6/man/man1/iceauth.1x
%attr(644, root,  man) /usr/X11R6/man/man1/mkfontdir.1x
%attr(644, root,  man) /usr/X11R6/man/man1/showrgb.1x
%attr(644, root,  man) /usr/X11R6/man/man1/rstart.1x
%attr(644, root,  man) /usr/X11R6/man/man1/rstartd.1x
%attr(644, root,  man) /usr/X11R6/man/man1/smproxy.1x
%attr(644, root,  man) /usr/X11R6/man/man1/twm.1x
%attr(644, root,  man) /usr/X11R6/man/man1/x11perf.1x
%attr(644, root,  man) /usr/X11R6/man/man1/x11perfcomp.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xauth.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xclipboard.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xcutsel.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xclock.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xcmsdb.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xconsole.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xdm.1x
%attr(644, root,  man) /usr/X11R6/man/man1/sessreg.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xdpyinfo.1x
%attr(644, root,  man) /usr/X11R6/man/man1/dga.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xfd.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xfs.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xhost.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xieperf.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xinit.1x
%attr(644, root,  man) /usr/X11R6/man/man1/startx.1x
%attr(644, root,  man) /usr/X11R6/man/man1/setxkbmap.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xkbcomp.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xkbevd.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xkbprint.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xkill.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xlogo.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xlsatoms.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xlsclients.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xlsfonts.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xmag.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xmh.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xmodmap.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xprop.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xrdb.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xrefresh.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xset.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xsetmode.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xsetpointer.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xsetroot.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xsm.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xstdcmap.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xterm.1x
%attr(644, root,  man) /usr/X11R6/man/man1/resize.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xvidtune.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xwd.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xwininfo.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xwud.1x
%attr(644, root,  man) /usr/X11R6/man/man1/Xserver.1x
%attr(644, root,  man) /usr/X11R6/man/man1/XFree86.1x
%attr(644, root,  man) /usr/X11R6/man/man1/reconfig.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xf86config.1x
%attr(644, root,  man) /usr/X11R6/man/man1/SuperProbe.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xon.1x

/usr/X11R6/lib/X11/fonts/Speedo
/usr/X11R6/lib/X11/fonts/Type1
%dir /usr/X11R6/lib/X11/fonts/misc
%attr(644, root, root) /usr/X11R6/lib/X11/fonts/misc/*pcf.gz
%attr(644, root, root) %verify(not md5 size mtime) /usr/X11R6/lib/X11/fonts/misc/fonts.*

%config /usr/X11R6/lib/X11/rgb.txt

%ifnarch alpha
/usr/X11R6/lib/X11/fonts/PEX
%endif

%files libs
%attr(755, root, root) /usr/X11R6/lib/lib*.so.*.*
%attr(  -, root, root) /usr/lib/X11

%files devel
%defattr(644, root, root, 755)
/usr/X11R6/include
/usr/include/X11
%dir /usr/X11R6/man/man3
%attr(644, root,  man) /usr/X11R6/man/man3/*

/usr/X11R6/lib/X11/config
%attr(755, root, root) /usr/X11R6/bin/imake
%attr(755, root, root) /usr/X11R6/bin/makedepend
%attr(755, root, root) /usr/X11R6/bin/xmkmf

%attr(644, root,  man) /usr/X11R6/man/man1/imake.1x
%attr(644, root,  man) /usr/X11R6/man/man1/makedepend.1x
%attr(644, root,  man) /usr/X11R6/man/man1/xmkmf.1x

/usr/X11R6/lib/lib*.so

%files static
%attr(644, root, root) /usr/X11R6/lib/lib*.a

%files Xvfb
%attr(755, root, root) /usr/X11R6/bin/Xvfb
%attr(644, root,  man) /usr/X11R6/man/man1/Xvfb.1x

%files Xnest
%attr(755, root, root) /usr/X11R6/bin/Xnest
%attr(644, root,  man) /usr/X11R6/man/man1/Xnest.1x

%ifarch i386 alpha

%files SVGA
%attr(755, root, root) /usr/X11R6/bin/XF86_SVGA
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_SVGA.1x
%attr(644, root,  man) /usr/X11R6/man/man5/XF86Config.5x

%endif

%ifarch i386 sparc

%files VGA16
%attr(755, root, root) /usr/X11R6/bin/XF86_VGA16
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_VGA16.1x
%attr(644, root,  man) /usr/X11R6/man/man5/XF86Config.5x

%endif

%ifarch i386

%files W32
%attr(755, root, root) /usr/X11R6/bin/XF86_W32
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_W32.1x
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_Accel.1x
%attr(644, root,  man) /usr/X11R6/man/man5/XF86Config.5x
%endif

%ifarch i386 alpha

%files Mono
%attr(755, root, root) /usr/X11R6/bin/XF86_Mono
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_Mono.1x
%attr(644, root,  man) /usr/X11R6/man/man5/XF86Config.5x
%endif

%ifarch i386 alpha

%files S3
%attr(755, root, root) /usr/X11R6/bin/XF86_S3
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_S3.1x
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_Accel.1x
%attr(644, root,  man) /usr/X11R6/man/man5/XF86Config.5x
%endif

%ifarch i386 alpha

%files S3V
%attr(755, root, root) /usr/X11R6/bin/XF86_S3V
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_S3.1x
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_Accel.1x
%attr(644, root,  man) /usr/X11R6/man/man5/XF86Config.5x
%endif

%ifarch i386

%files 8514
%attr(755, root, root) /usr/X11R6/bin/XF86_8514
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_8514.1x
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_Accel.1x
%attr(644, root,  man) /usr/X11R6/man/man5/XF86Config.5x
%endif

%ifarch i386

%files Mach8
%attr(755, root, root) /usr/X11R6/bin/XF86_Mach8
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_Mach8.1x
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_Accel.1x
%attr(644, root,  man) /usr/X11R6/man/man5/XF86Config.5x
%endif

%ifarch i386

%files Mach32
%attr(755, root, root) /usr/X11R6/bin/XF86_Mach32
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_Mach32.1x
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_Accel.1x
%attr(644, root,  man) /usr/X11R6/man/man5/XF86Config.5x
%endif

%files Mach64
%attr(755, root, root) /usr/X11R6/bin/XF86_Mach64
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_Mach64.1x
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_Accel.1x
%attr(644, root,  man) /usr/X11R6/man/man5/XF86Config.5x

%ifarch i386 alpha

%files P9000
%attr(755, root, root) /usr/X11R6/bin/XF86_P9000
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_P9000.1x
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_Accel.1x
%attr(644, root,  man) /usr/X11R6/man/man5/XF86Config.5x
%endif

%ifarch i386

%files AGX
%attr(755, root, root) /usr/X11R6/bin/XF86_AGX
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_AGX.1x
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_Accel.1x
%attr(644, root,  man) /usr/X11R6/man/man5/XF86Config.5x
%endif

%ifarch i386

%files I128
%attr(755, root, root) /usr/X11R6/bin/XF86_I128
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_I128.1x
%attr(644, root,  man) /usr/X11R6/man/man1/XF86_Accel.1x
%attr(644, root,  man) /usr/X11R6/man/man5/XF86Config.5x
%endif

%ifarch alpha

%files TGA
%attr(755, root, root) /usr/X11R6/bin/XF86_TGA
%attr(644, root,  man) /usr/X11R6/man/man5/XF86Config.5x

%endif

%ifarch sparc

%files Sun
%attr(755, root, root) /usr/X11R6/bin/Xsun
%endif

%ifarch sparc

%files SunMono
%attr(755, root, root) /usr/X11R6/bin/XsunMono

%endif

%ifarch sparc

%files Sun24
%attr(755, root, root) /usr/X11R6/bin/Xsun24

%endif

%files 75dpi-fonts
%defattr(644, root, root, 755)
%dir /usr/X11R6/lib/X11/fonts/75dpi
/usr/X11R6/lib/X11/fonts/75dpi/*pcf.gz
%verify(not md5 size mtime) /usr/X11R6/lib/X11/fonts/75dpi/fonts.*

%files 100dpi-fonts
%defattr(644, root, root, 755)
%dir /usr/X11R6/lib/X11/fonts/100dpi
/usr/X11R6/lib/X11/fonts/100dpi/*pcf.gz
%verify(not md5 size mtime) /usr/X11R6/lib/X11/fonts/100dpi/fonts.*

#%files cyrillic-fonts
#%defattr(644, root, root, 755)
#%dir /usr/X11R6/lib/X11/fonts/cyrillic
#/usr/X11R6/lib/X11/fonts/cyrillic/*pcf.gz
#%verify(not md5 size mtime) /usr/X11R6/lib/X11/fonts/cyrillic/fonts.*

#%files XF86Setup
#%attr(755, root, root) /usr/X11R6/bin/XF86Setup
#%attr(755, root, root) /usr/X11R6/bin/xmseconfig
#/usr/X11R6/lib/X11/XF86Setup
#%attr(644, root,  man) /usr/X11R6/man/man1/XF86Setup.1x
#%attr(644, root,  man) /usr/X11R6/man/man1/xmseconfig.1x

%changelog
* Mon Aug 16 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.3.2-20]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added static subpackage,
- changed dependencies to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added using $RPM_OPT_FLAGS during compile,
- added stripping shared libraries,
- /usr/X11R6/lib/modules on i386 and alpha architectures moved to main
  package,
- added pl translation (Andrzej Nakonieczny <dzemik@tuniv.szczecin.pl>),
- all builded against system libz (XFree86-HasZlib.patch),
- added cyrylic-fonts subpacckage with koi-8 fonts,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Thu Jun 04 1998 Prospector System <bugs@redhat.com>
- translations modified for fr

* Thu Jun 04 1998 Prospector System <bugs@redhat.com>
- translations modified for fr

* Tue Jun 02 1998 Erik Troan <ewt@redhat.com>
- added more security fixes

* Tue May 19 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr

* Wed May 13 1998 Jeff Johnson <jbj@redhat.com>
- Merge in sparc changes.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue May 05 1998 Jakub Jelinek <jj@ultra.linux.cz>
- Fix colormaps on SBUS cards, add /dev/fb to the list
  of checked devices even for XSunMono

* Mon May 04 1998 Erik Troan <ewt@redhat.com>
- included security fix which fixes a large number of problems

* Wed Apr 22 1998 Jakub Jelinek <jj@ultra.linux.cz>
- Fix fb mapping on non-accelerated SBUS cards
- Further PCI SPARC changes (from ecd).

* Tue Apr 14 1998 Jakub Jelinek <jj@ultra.linux.cz>
- Merge in PCI SPARC support (written by Eddie C. Dost).

* Tue Apr 07 1998 Jakub Jelinek <jj@ultra.linux.cz>
- Unmap all fb mappings before closing fb in SBUS servers,
  otherwise new kernels don't call fb_close and bad things
  happen.

* Mon Mar 30 1998 Erik Troan <ewt@redhat.com>
- swhiched to using the Xwrapper from XFree86 rather then a separate package

* Sat Mar 21 1998 Jakub Jelinek <jj@ultra.linux.cz>
- built sparc version against glibc

* Sat Mar 21 1998 Michal Rehacek <majkl@iname.com>
- Accelerated support for Creator/Creator3D

* Tue Mar 03 1998 Erik Troan <ewt@redhat.com>
- updated to XFree86 3.3.2

* Fri Jan 16 1998 Erik Troan <ewt@redhat.com>
- turned off setuid bit for X servers
- require xserver-wrapper (which replaces /usr/X11R6/bin/X)

* Wed Nov 05 1997 Erik Troan <ewt@redhat.com>
- removed XF86Setup
- updated file list to include some missing files

* Tue Nov 04 1997 Michael K. Johnson <johnsonm@redhat.com>
- New PAM conversation function conventions

* Mon Sep 29 1997 Erik Troan <ewt@redhat.com>
- built against tcl/tk 8.0

* Wed Sep 03 1997 Erik Troan <ewt@redhat.com>
- set libc version to 6 (which turns on thread support as well)
- used wildcards more liberally in file lists

* Tue Sep 02 1997 Erik Troan <ewt@redhat.com>
- added notiocsltc patch
- added /usr/X11R6/lib/X11/xserver/SecurityPolicy

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- updated to XFree86 3.3.1

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- add shlibs patch, we links shared libraries against -lc

* Thu Jun 12 1997 Erik Troan <ewt@redhat.com>
- Increased release number to 10 for glibc version

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- Updated to XFree86 3.3

* Thu Mar 20 1997 Erik Troan <ewt@redhat.com>
- Changed xdm to use xbanner
- Changed xdm paths to point to /var/run, /var/log, /etc/X11/xdm instead
  of all pointing to /usr/X11R6/lib/X11/xdm

* Thu Mar 06 1997 Erik Troan <ewt@redhat.com>
- Modified to use pam.d.
