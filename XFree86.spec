#
# TODO:
# - separate XFS to be standalone - is it possible without duplicated files?
#
# Conditional build:
%bcond_without	glide	# don't build glide driver
%bcond_with	cursors	# build with XcursorTheme-* packages
#
Summary:	XFree86 Window System servers and basic programs
Summary(de):	XFree86 Window-System-Server und grundlegende Programme
Summary(es):	Programas b�sicos y servidores para el sistema de ventanas XFree86
Summary(fr):	Serveurs du syst�me XFree86 et programmes de base
Summary(ja):	XFree86 window system �Υ����Фȴ���Ū�ʥץ����
Summary(ko):	X�� �ʿ��� �⺻���� �۲ð� ���α׷��� ������
Summary(pl):	XFree86 Window System wraz z podstawowymi programami
Summary(tr):	XFree86 Pencereleme Sistemi sunucular� ve temel programlar
Summary(pt_BR):	Programas b�sicos e servidores para o sistema de janelas XFree86
Summary(ru):	������� ������, ��������� � ������������ ��� ������� ������� ��� X
Summary(uk):	����צ ������, �������� �� ���������æ� ��� �����ϧ ����æ� Ц� X
Summary(zh_CN):	XFree86 ����ϵͳ�������ͻ�������
Name:		XFree86
Version:	4.4.0
Release:	10
Epoch:		1
License:	XFree86 1.1
Group:		X11
Source0:	ftp://ftp.xfree86.org/pub/XFree86/4.4.0/source/XFree86-4.4.0-src-1.tgz
# Source0-md5:	97cea3d9e1197dde32ca34e3b6086469
Source1:	ftp://ftp.xfree86.org/pub/XFree86/4.4.0/source/XFree86-4.4.0-src-2.tgz
# Source1-md5:	b9b6c74a03e314569e01d5fd4ff59523
Source2:	ftp://ftp.xfree86.org/pub/XFree86/4.4.0/source/XFree86-4.4.0-src-3.tgz
# Source2-md5:	703404f48d3a15f58389a879d47c769d
Source7:	ftp://ftp.pld-linux.org/software/xinit/xdm-xinitrc-0.2.tar.bz2
# Source7-md5:	0a15b1c374256b5cad7961807baa3896
Source8:	xdm.pamd
Source9:	xserver.pamd
Source10:	xdm.init
Source11:	xfs.init
Source12:	xfs.config
Source13:	XTerm.ad-pl
Source14:	xdm.sysconfig
Source15:	xfs.sysconfig
Source24:	twm.desktop
Source25:	xeyes.desktop
Source26:	xedit.desktop
Source27:	xterm.desktop
Source28:	xclipboard.desktop
Source29:	xclock.desktop
Source30:	oclock.desktop
Source31:	xconsole.desktop
Source34:	xlogo64.png
Source35:	xeyes.png
Source36:	xedit.png
Source37:	xterm.png
Source38:	xclipboard.png
Source39:	xclock.png
Source40:	oclock.png
Source41:	xconsole.png
Source42:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-Xman-pages.tar.bz2
# Source42-md5:	a184106bb83cb27c6963944d9243ac3f
Source44:	%{name}-Xserver-headers
Source45:	%{name}-Xserver-headers-links
Source46:	twm-xsession.desktop
Source47:	xcalc.desktop
Source48:	xload.desktop
Source49:	xmag.desktop
Source50:	xcalc.png
Source51:	xload.png
Source52:	xmag.png
Source53:	http://oss.sgi.com/projects/ogl-sample/ABI/glext.h
# NoSource53-md5: b3e8590b46dbab4341841592147fba26
Source54:	XFree86-xrender.pc
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
Patch26:	%{name}-HasFreetype2.patch
Patch27:	%{name}-config-s3.patch
Patch28:	%{name}-sparc_pci_domains.patch
Patch29:	%{name}-XTerm.ad.patch
Patch30:	%{name}-alpha_GLX_align_fix.patch
Patch32:	%{name}-xman-manpaths.patch
Patch33:	%{name}-clearrts.patch
Patch34:	%{name}-fix-07-s3trio64v2gx+netfinity.patch
Patch35:	%{name}-i740-driver-update-cvs-20020617.patch
Patch36:	%{name}-tdfx-disable-dri-on-16Mb-cards-in-hires.patch
Patch38:	%{name}-tdfx-fix-compiler-warnings.patch
Patch39:	%{name}-tdfx-fix-vtswitch-font-corruption.patch
Patch40:	%{name}-Xfont-Type1-large-DoS.patch
# "strip -g libGLcore.a" leaves empty objects m_debug_*.o, which cause
# warnings during GLcore loading ("m_debug_*.o: no symbols") - shut up them
Patch41:	%{name}-GLcore-strip-a-workaround.patch
Patch42:	%{name}-disable_glide.patch
Patch43:	%{name}-expat.patch
Patch44:	%{name}-pkgconfig.patch
# spencode.o in libspeedo.a is empty - patch like for libGLcore.a
Patch45:	%{name}-spencode-nowarning.patch
# Small (maybe buggy) patch to resolve problems with totem 0.97.0
Patch46:	%{name}-lock.patch
Patch47:	%{name}-sparc-kbd.patch
Patch50:	%{name}-xterm-256colors.patch
Patch52:	%{name}-kernel_headers.patch
Patch53:	%{name}-stdint.patch
Patch54:	%{name}-lnx_kbd.patch
Patch55:	%{name}-elfloader-linux-non-exec-stack.patch
Patch56:	%{name}-exec-shield-GNU-stack.patch
Patch57:	%{name}-libGL-exec-shield-fixes-v2.patch
URL:		http://www.xfree86.org/
BuildRequires:	/usr/bin/perl
# Required by xc/programs/Xserver/hw/xfree86/drivers/glide/glide_driver.c
%ifarch %{ix86} %{x8664} ia64
%{?with_glide:BuildRequires:	Glide2x_SDK}
%endif
BuildRequires:	bison
BuildRequires:	ed
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	pam-devel
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	tcl-devel
BuildRequires:	utempter-devel
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-xauth = %{epoch}:%{version}-%{release}
Requires:	pam >= 0.77.3
Obsoletes:	xpm-progs
Obsoletes:	xterm
%ifarch sparc sparc64
Obsoletes:	X11R6.1
%endif
ExclusiveArch:	%{ix86} %{x8664} alpha armv4l ia64 m68k ppc sparc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_soundsdir	/usr/share/sounds
%define		_themesdir	/usr/share/themes
%define		_wallpapersdir	/usr/share/wallpapers
%define		_wmpropsdir	/usr/share/wm-properties
%define		_xsessdir	/usr/share/xsessions
%define		_wmstylesdir	/etc/sysconfig/wmstyles
%define		_libx11dir	%{_prefix}/lib/X11
%define		_appdefsdir	%{_libx11dir}/app-defaults

# avoid Mesa dependency in XFree86-OpenGL-libs
# Glide3 (libglide3.so.3) can be provided by Glide_V3-DRI or Glide_V5-DRI
%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libOSMesa.so.3.3 libglide3.so.3

# ELF objects with Rendition microcode - disliked by ELF utils
%define		_noautostrip	.*\\.uc
%define		_noautochrpath	.*\\.uc

%description
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
X-Window ist eine voll funktionsf�hige grafische Benutzeroberfl�che
mit mehreren Fenstern, mehreren Clients und verschiedenen Arten von
Fenstern. Es kommt auf den meisten Unix-Plattformen zum Einsatz. Die
Clients lassen sich auch mit Hilfe anderer Fenstersysteme anzeigen.
Das X-Protokoll gestattet die Ausf�hrung der Applikationen direkt auf
lokalen Rechnern oder �ber ein Netz und bietet gro�e Flexibilit�t bei
Client-Server-Implementierungen.

%description -l es
X Window es una interface gr�fica completa con m�ltiples ventanas,
m�ltiples clientes y diferentes estilos de ventanas. Se usa en la
mayor�a de las plataformas Unix, y los clientes tambi�n pueden
ejecutar en otros sistemas de ventanas populares. El protocolo X
permite que las aplicaciones puedan ejecutarse tanto en la m�quina
local como a trav�s de la red, y proveer flexibilidad en
implementaciones cliente/servidor. Este paquete contiene las fuentes
b�sicas, programas y documentaci�n para una estaci�n de trabajo X. No
ofrece un servidor X que acceda tu hardware de v�deo -- estos son
puestos a disposici�n en otro paquete.

%description -l pl
X Window System jest graficznym interfejsem u�ytkownika; cechuje si�
mo�liwo�ci� pracy w wielu oknach, z wieloma klientami i do tego w
r�nych wystrojach okien. :) Jest u�ywany na wi�kszo�ci platform
system�w Unix, a klienci mog� by� uruchamiani tak�e pod innymi
popularnymi systemami okienkowymi. Protok� X pozwala na uruchamianie
aplikacji zar�wno z lokalnej maszyny jak i poprzez sie� - daj�c przez
to elastyczn� implementacj� architektury klient/serwer.

Pakiet ten nie zawiera X serwera kt�ry jest po�rednikiem z Twoj� kart�
graficzn� (jest on w innym pakiecie).

%description -l tr
X Window sistemi, �oklu pencere, �oklu istemci ve �e�itli pencere
stilleriyle geni� �zelliklere sahip bir Grafik Kullan�c� Arabirimidir.
�o�u UNIX sisteminde �al��t��� gibi istemcileri de bir�ok pencereleme
sistemiyle �al��abilir. X protokolu kullanan uygulamalar�n yerel
makina veya bilgisayar a�� �zerinden �al��t�r�labilmesi esnek bir
istemci/sunucu ortam� sa�lar. Bu paket bir X istasyonu i�in gerekli
olan temel yaz�tiplerini, programlar� ve belgeleri sunar. Ekran
kart�n�z� s�rmek i�in gerekli olan X sunucusu bu pakete dahil
de�ildir.

%description -l pt_BR
X Window � uma interface gr�fica completa com m�ltiplas janelas,
m�ltiplos clientes e diferentes estilos de janelas. � usado na maioria
das plataformas Unix, e clientes tamb�m podem rodar em outros sistemas
de janelas populares. O protocolo X permite que aplica��es possam
rodar tanto na m�quina local como atrav�s da rede, provendo
flexibilidade em implementa��es cliente/servidor.

Este pacote cont�m as fontes b�sicas, programas e documenta��o para
uma esta��o de trabalho X. Ele n�o fornece um servidor X que acessa
seu hardware de v�deo -- estes s�o disponibilizados em outro pacote.

%description -l ru
X Window System ������������� ���� ��� ���������� �����������
����������� ������������. �������� ������, X ������ �������� GUI ��
������ ������������ � ����� ������ ��� �������� �������� ������������
���������� ����������. X ����� ������������ ������������� ���������� -
������ �������� �� ��������� ���������� � ������/������� ��
���������������� ������. X - ��� ������ �����, ��������������
��������� ����������, ����� ��� ����, ����������� ��� ������������,
����������� ���������, ��������� ��������� � �.�. XFree86 - ��� ������
X, ���������� �� Linux � ������ ��������.

���� ����� �������� ������� ������, ��������� � ������������ ���
������� ������� X.

������������� ���������� ���������� ������ Xconfigurator, ����������
xfs � ���������� XFree86-libs. �������� �������� ���������� ����� ����
��� ����� ������� ������� XFree86.

�� �, �������, ���� �� ����������� ������������� ����������,
���������� ��� X-�������, ��� ����� ���� ����� ����������
XFree86-devel.

%description -l uk
X Window System ����� ���� ��� �������� ���Ʀ���� ��������Ӧ�
�����������. ����Ԧ�� ������, X ����� �������� GUI �� ����Φ
����������� �� ���դ ������ ��� ������ަ Ħ� ����������� ����������
���������. X ����� Ц�����դ �����Ħ� ���������� ������� - ������
������� �� צ��������� ����'���Ҧ � ������/������� �� ������
�����������. X - �� ������� ����������, ��� Ц�����դ ������ ˦��˦���
Ҧ���� �������, ����� �� ����, ����������� ��� ������ͦ���, ���Ʀ�Φ
��������, ������צ ��������� � �.�. XFree86 - �� ���Ӧ� X, ��� ������
�� Linux �� ����� ��������.

��� ����� ͦ����� ����צ ������, �������� �� ���������æ� ��� �����ϧ
����æ� X.

��������� ����Ȧ��� ���������� ������ Xconfigurator, ���������� xfs ��
¦�̦����� XFree86-libs. ������� ����� ���������� ���������� ���� ���
��˦���� ����Ԧ� ����Ԧ� XFree86.

�� �, �����Ԧ, ���� �� ���������� ���������� �������Φ ��������, ��
�������� �� X-�̦����, ��� ����� ����� ���� ���������� XFree86-devel.

%package common
Summary:	XFree86 files required both on server and client side
Summary(pl):	Pliki XFree86 wymagane zar�wno po stronie serwera jak i klienta
Group:		X11

%description common
XFree86 files required both on server and client side.

%description common -l pl
Pliki XFree86 wymagane zar�wno po stronie serwera jak i klienta.

%package DPS
Summary:	Display PostScript
Summary(pl):	Display PostScript
Group:		X11/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Provides:	DPS
Obsoletes:	dgs

%description DPS
X-Window Display PostScript is device-independent imaging model for
displaying information on a screen.

%description DPS -l pl
X-Window Display PostScript to niezale�ny od urz�dzenia model
wy�wietlania informacji na ekranie.

%package DPS-devel
Summary:	Header files for Display PostScript
Summary(pl):	Pliki nag��wkowe dla Display PostScript
Group:		X11/Development/Libraries
Requires:	%{name}-DPS = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	dgs-devel

%description DPS-devel
Header files for develop X-Window Display Postscript.

%description DPS-devel -l pl
Pliki nag��wkowe biblioteki X-Window Display PostScript.

%package DPS-static
Summary:	Display PostScript static libraries
Summary(pl):	Biblioteki statyczne Display PostScript
Group:		X11/Development/Libraries
Requires:	%{name}-DPS-devel = %{epoch}:%{version}-%{release}
Obsoletes:	dgs-static

%description DPS-static
X-Window Display PostScript static libraries.

%description DPS-static -l pl
Statyczne biblioteki X-Window Display PostScript.

%package OpenGL-core
Summary:	OpenGL support extension modules for Xserver
Summary(pl):	Modu�y rozszerze� X serwera obs�uguj�ce OpenGL
Group:		X11/Xserver
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description OpenGL-core
OpenGL support extension modules for Xserver.

%description OpenGL-core -l pl
Modu�y rozszerze� X serwera obs�uguj�ce OpenGL.

%package OpenGL-libGL
Summary:	OpenGL support for X11R6 - GL library
Summary(pl):	Wsparcie OpenGL dla systemu X11R6 - biblioteka GL
Group:		X11/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-firegl
Obsoletes:	XFree86-driver-nvidia

%description OpenGL-libGL
OpenGL support for X11R6 system - GL library.

%description OpenGL-libGL -l pl
Wsparcie OpenGL dla systemu X11R6 - biblioteka GL.

%package OpenGL-libs
Summary:	OpenGL libraries for X11R6
Summary(pl):	Biblioteki OpenGL dla systemu X11R6
Group:		X11/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Provides:	OpenGL = 1.4
Provides:	OpenGL-GLU = 1.3
Provides:	OpenGL-GLX = 1.4
Obsoletes:	Mesa
Obsoletes:	XFree86-OpenGL

%description OpenGL-libs
OpenGL libraries for X11R6 system.

%description OpenGL-libs -l pl
Biblioteki OpenGL dla systemu X11R6.

%package OpenGL-devel-base
Summary:	OpenGL for X11R6 development (GL and GLX only)
Summary(pl):	Pliki nag��wkowe OpenGL dla systemu X11R6 (tylko GL i GLX)
Group:		X11/Development/Libraries
Requires:	%{name}-OpenGL-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	OpenGL-devel-base
Obsoletes:	XFree86-driver-nvidia-devel

%description OpenGL-devel-base
Base headers (GL and GLX only) for OpenGL for X11R6.

%description OpenGL-devel-base -l pl
Podstawowe pliki nag��wkowe (tylko GL i GLX) OpenGL dla systemu X11R6.

%package OpenGL-devel
Summary:	OpenGL for X11R6 development
Summary(pl):	Pliki nag��wkowe OpenGL dla systemu X11R6
Group:		X11/Development/Libraries
Requires:	%{name}-OpenGL-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	OpenGL-devel-base
Provides:	OpenGL-devel = 1.4
Provides:	OpenGL-GLU-devel = 1.3
Provides:	OpenGL-GLX-devel = 1.4
Obsoletes:	Mesa-devel
Obsoletes:	XFree86-OpenGL-doc
Obsoletes:	glxMesa-devel

%description OpenGL-devel
Headers and man pages for OpenGL for X11R6.

%description OpenGL-devel -l pl
Pliki nag��wkowe i manuale do OpenGL dla systemu X11R6.

%package OpenGL-static
Summary:	X11R6 static libraries with OpenGL
Summary(pl):	Biblioteki statyczne do X11R6 ze wsparciem dla OpenGL
Group:		X11/Development/Libraries
Requires:	%{name}-OpenGL-devel = %{epoch}:%{version}-%{release}
Provides:	OpenGL-static = 1.4
Provides:	OpenGL-GLU-static = 1.3
Obsoletes:	Mesa-static

%description OpenGL-static
X11R6 static libraries with OpenGL.

%description OpenGL-static -l pl
Biblioteki statyczne zawieraj�ce wsparcie dla OpenGL do X11R6.

%package Xnest
Summary:	XFree86 Xnest server
Summary(pl):	Serwer XFree86 Xnest
Summary(ru):	"���������" ������ XFree86
Summary(uk):	"���������" ������ XFree86
Group:		X11/Servers
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	/usr/X11R6/lib/X11/rgb.txt
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
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
zachowuje si� jak X klient w stosunku do prawdziwego X serwera, a jak
X serwer dla w�asnych klient�w.

%description Xnest -l ru
Xnest - ��� ������ X Window System, ������� �������� � ���� X. ��
����� ���� ��� ������ ��������� X-�������, ������� ��������� ������ �
������������ ��������� ��� Xnest � �� �����, ��� Xnest ���������
������ � ������������ ��������� ��� ����� ����������� ��������.

��� ���� ���������� Xnest ���� ��� ����� X-������, ������� ��������
��� ������ ������ ��������� X-������� (������ �����, � ��������
�����).

%description Xnest -l uk
Xnest - �� ������ X Window System, ���� ������ � צ�Φ X. �������� ��
�̦��� ��������� X-�������, ���� ���դ צ����� �� ���Ʀ����� ��������
��� Xnest � ��� ���, �� Xnest ���դ צ����� �� ���Ʀ����� �������� ���
��ϧ� ������� �̦��Ԧ�.

��� ����� ���������� Xnest ���� ��� ���Ҧ��� X-������, ���� ������ ��
�̦��� ������ ��������� X-������� (������ ������, � �������� æ���).

%package Xprt
Summary:	X print server
Summary(pl):	X serwer z rozszerzeniem Xprint
Group:		X11/Servers
PreReq:		xprint-initrc
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	/usr/X11R6/lib/X11/rgb.txt
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
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
Group:		X11/Servers
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	/usr/X11R6/lib/X11/rgb.txt
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Requires:	XFree86-fonts-base
Requires:	pam
Obsoletes:	XFree86-Mono
Obsoletes:	XFree86-SVGA
Obsoletes:	XFree86-VGA16
# obsoleted by many drivers: suncg3,suncg6,suncg14,sunffb,sunleo,suntcx
Obsoletes:	XFree86-Sun
Obsoletes:	XFree86-Sun24
# still not supported in 4.2.0:
#Obsoletes:	XFree86-Mach8 XFree86-8514 XFree86-AGX XFree86-P9000
# (and many drivers from XF86_SVGA server... and some from others)
Obsoletes:	XFree86-XF86Setup
Obsoletes:	Xconfigurator

%description Xserver
Generally used X server which uses display hardware. It requires
proper driver for your display hardware - package itself contains only
drivers for VGA and VESA-compliant cards (without acceleration). Other
drivers can be found in XFree86-driver-* packages.

%description Xserver -l de
X-Server f�r die elementarsten Framebuffer-SVGA-Ger�te, einschlie�lich
Karten, die aus ET4000-Chips, Cirrus Logic-Chips, Chips and
Technologies Laptop-Chips sowie Trident 8900 und 9000 Chips gebaut
sind. Funktioniert mit Diamond Speedstar, Orchid Kelvins, STB Nitros
und Horizons, Genoa 8500VL, den meisten Actix-Karten sowie Spider VLB
Plus und au�erdem mit vielen anderen Chips und Karten. Es lohnt sich,
diesen Server auszuprobieren, wenn Sie Probleme haben.

%description Xserver -l fr
Serveur X pour les circuits SVGA les plus simples, dont les cartes
construites avec les circuits ET4000, Cirrus Logic, Chips and
Technologies laptop, Trident 8900 et 9000. Fonctionne pour les cartes
Diamond Speedstar, Orchid Kelvins, STB Nitros et Horizons, Genoa
8500VL, la plupart des Actix et la Spider VLB Plus. Fonctionne aussi
pour de nombreux autres circuits et cartes. Essayez ce serveur si vous
avez des probl�mes.

%description Xserver -l pl
Jest to podstawowy X serwer wy�wietlaj�cy obraz na karcie graficznej.
Do dzia�ania wymaga odpowiedniego sterownika - sam pakiet zawiera
tylko odpowiedni dla kart VGA oraz SVGA zgodnych z VESA (bez
akceleracji). Inne sterowniki mo�na znale�� w pakietach
XFree86-driver-*.

%description Xserver -l tr
ET4000, Cirrus Logic, Chips and Technologies diz�st�, Trident 8900 ve
9000 gibi basit 'framebuffer' SVGA kullananan kartlar i�in X sunucusu.
Ayn� zamanda Diamond Speedstar, Orchid Kelvins, STB Nitros / Horizons,
Genoa 8500VL, �o�u Actix kartlar�, Spider VLB Plus gibi kartlar ve
bir�ok di�er kart ile de �al���r. Herhangi bir sorun ya�arsan�z bu
sunucuyu deneyin.

%package Xvfb
Summary:	XFree86 Xvfb server
Summary(pl):	Serwer XFree86 Xvfb
Summary(ru):	������ XFree86 ��� ������������ �����������
Summary(uk):	������ XFree86 ��� צ���������� �����������
Group:		X11/Servers
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	/usr/X11R6/lib/X11/rgb.txt
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
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
Xvfb (X Virtual Frame Buffer) jest X serwerem, kt�ry mo�na uruchamia�
na maszynach bez urz�dze� wy�wietlaj�cych ani fizycznych urz�dze�
wej�ciowych. Xvfb emuluje prosty framebuffer w pami�ci. Zwykle jest
u�ywany do testowania X serwer�w, mo�e te� by� u�ywany do testowania X
klient�w w rzadko u�ywanych konfiguracjach ekranu. Mo�na te� u�y� Xvfb
do uruchomienia aplikacji, kt�re w rzeczywisto�ci nie wymagaj� X
serwera, ale odmawiaj� uruchomienia bez niego.

%description Xvfb -l ru
Xvfb (X Virtual Frame Buffer) - ��� X-������, ������� ��������
�������� �� ������� ��� ���������� ���������� � ���������� ���������
�����. Xvfb ��������� ���������� ���������� ��������� �����������
������. Xvfb �� ��������� ������� ���������, ���� ���� ��� ����������
X-������ �� ���� ���������. ������ �� ������������ ��� ��������
��������. ��������� Xvfb, ����� ����������� ��� mfb ��� cfb ��� �����
������� ����� ��� ������������� �������� ����������, ��������������
����� �������. Xvfb ����� ����� ������������ ��� �������� X-�������� �
���������� ��������� ����� � �������������� ������, �����������
�������� ��������� � Xvfb � �������� �������� ���������, ���������
����������� �����, ��� ������ � ������������ X-������� �� �����
��������� � ��� ����������� ������� ����������, ������� ������� ��
����� X-������, �� ������� ���������� �� ���, ���� �� ��� ��������.

���� ��� ���� ����������� ���� X-������� ��� X-�������, �� ������
���������� ��� ���� ���� Xvfb.

%description Xvfb -l uk
Xvfb (X Virtual Frame Buffer) - �� X-������, ������� ��������� ��
������� ��� ��������ϧ ��������� �� צ������ ������ϧ� �����. Xvfb
������ �������Ԧ��� ���������� �������������� צ�������� ���'���. Xvfb
�� צ������� Φ���� ������ϧ�, ������ ���� �� ���������� X-������ �
���Ԧ צ�������. �������� ���� �������������� ��� ����צ��� �����Ҧ�.
�������������� Xvfb, ����� ��������� ��� mfb ��� cfb ��� ����-��ϧ
������� ������� �� ���Ʀ����æ� ������ ��� ������������ ������ϧ
���������, ��� Ц�����դ ��˦ ������. ����� Xvfb ����� ����������� ���
����צ��� X-�̦��Ԧ� � ���������� ��������� ������� �� ���Ʀ����æ���
������, ��������� ������� ������� � Xvfb � ����Ԧ �������� ���������,
��������� ��������Φ �����, ��� �������� � ��������Φ X-������� ��
���� ��������� �� ������� �������, ���� ������� �� ���Ҧ��� X-������,
��� �˦ ����������� �� ����, ��� צ� ��� ���������.

���� ��� ���Ҧ��� ��������� ��ۦ X-������� ��� X-�̦����, �� ������
���������� ��� æ�� æ̦ Xvfb.

%package devel
Summary:	X11R6 headers and programming man pages
Summary(de):	X11R6 Headers und man pages f�r Programmierer
Summary(fr):	Pages man de programmation
Summary(pl):	Pliki nag��wkowe X11R6
Summary(ru):	���������� ������������, ������ � ������������ �� ���������������� X11R6
Summary(tr):	X11R6 ile geli�tirme i�in gerekli dosyalar
Summary(uk):	��̦����� ������ͦ���, ������ �� ���������æ� �� ������������� X11R6
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-imake = %{epoch}:%{version}-%{release}
Requires:	fontconfig-devel >= 1:1.0.0
Provides:	render = 0.8
Provides:	xcursor-devel = 1.0
Provides:	xft-devel = 2.1.0
Provides:	xpm-devel
Provides:	xrender-devel = 0.8.0
%ifarch sparc sparc64
Obsoletes:	X11R6.1-devel
%endif
Obsoletes:	XFree86-render
Obsoletes:	XFree86-xcursor-devel
Obsoletes:	XFree86-xft-devel
Obsoletes:	XFree86-xft2-devel
Obsoletes:	XFree86-xrender-devel
Obsoletes:	Xft-devel
Obsoletes:	render
Obsoletes:	xcursor-devel
Obsoletes:	xft-devel
Obsoletes:	xpm-devel
Obsoletes:	xrender-devel

%description devel
Libraries, header files, and documentation for developing programs
that run as X clients. It includes the base Xlib library as well as
the Xt and Xaw widget sets.

%description devel -l de
Libraries, Header-Dateien und Dokumentation zum Entwickeln von
Programmen, die als X-Clients laufen. Enth�lt die Xlib-Library und die
Widget-S�tze Xt und Xaw.

%description devel -l fr
Biblioth�ques, fichiers d'en-t�te, et documentation pour d�velopper
des programmes s'ex�cutant en clients X. Cela comprend la Biblioth�que
Xlib de base aussi bien que les ensembles de widgets Xt et Xaw.

%description devel -l pl
Pliki nag��wkowe, dokumentcja dla programist�w rozwijaj�cych aplikacje
klienckie pod X Window. Zawiera podstawow� bibliotek� Xlib a tak�e Xt
i Xaw.

%description devel -l ru
XFree86-devel �������� ����������, ������ � ������������, �����������
��� ���������� ��������, ���������� ��� X-�������. XFree86-devel
�������� ������� ���������� Xlib � ������ ���������� Xt � Xaw.

���������� XFree86-devel ���� �� ����������� ������������� ���������,
������� ����� �������� ��� X-�������.

%description devel -l tr
X istemcisi olarak �al��acak programlar geli�tirmek i�in gereken
statik kitapl�klar, ba�l�k dosyalar� ve belgeler. Xlib kitapl���n�n
yan�s�ra Xt ve Xaw aray�z kitapl�klar�n� da i�erir.

%description devel -l uk
XFree86-devel ͦ����� ¦�̦�����, ������ �� ���������æ�, ����Ȧ�Φ
��� �������� �������, �˦ �������� �� X-�̦����. XFree86-devel ͦ�����
������ ¦�̦����� Xlib �� ������ ���ͦ��צ� Xt �� Xaw.

������צ�� XFree86-devel ���� �� ���������� ���������� ��������, �˦
������ ��������� �� X-�̦����.

%package Xserver-devel
Summary:	Header files for XFree86 Xserver drivers/extensions development
Summary(pl):	Pliki nag��wkowe do tworzenia sterownik�w/rozszerze� X serwera XFree86
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description Xserver-devel
Header files for XFree86 Xserver drivers and extensions development.

%description Xserver-devel -l pl
Pliki nag��wkowe do tworzenia sterownik�w i rozszerze� X serwera
XFree86.

%package driver-apm
Summary:	Alliance Promotion video driver
Summary(pl):	Sterownik do kart Alliance Promotion
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Alliance

%description driver-apm
Alliance Promotion driver.

%description driver-apm -l pl
Sterownik do kart Alliance Promotion.

%package driver-ark
Summary:	Ark Logic video driver
Summary(pl):	Sterownik do kart Ark Logic
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description driver-ark
Ark Logic driver.

%description driver-ark -l pl
Sterownik do kart Ark Logic.

%package driver-ati
Summary:	ATI video driver
Summary(pl):	Sterownik do kart ATI
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-ATI
Obsoletes:	XFree86-Mach32
Obsoletes:	XFree86-Mach64

%description driver-ati
ATI video driver.

%description driver-ati -l pl
Sterownik do kart ATI.

%package driver-r128
Summary:	ATI Rage 128 video driver
Summary(pl):	Sterownik do kart ATI Rage 128
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
%ifarch %{ix86} ia64 %{x8664} alpha ppc arm
# for dri
Requires:	%{name}-OpenGL-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-OpenGL-libGL = %{epoch}:%{version}-%{release}
# -libs already required by -OpenGL-libGL
%endif
Obsoletes:	XFree86-Rage128

%description driver-r128
ATI Rage 128 video driver.

%description driver-r128 -l pl
Sterownik do kart ATI Rage 128.

%package driver-radeon
Summary:	ATI Radeon video driver
Summary(pl):	Sterownik do kart ATI Radeon
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Requires:	%{name}-driver-ati = %{epoch}:%{version}-%{release}
%ifarch %{ix86} ia64 %{x8664} alpha ppc arm
# for dri
Requires:	%{name}-OpenGL-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-OpenGL-libGL = %{epoch}:%{version}-%{release}
# -libs already required by -OpenGL-libGL
%endif

%description driver-radeon
ATI Radeon video driver.

%description driver-radeon -l pl
Sterownik do kart ATI Radeon.

%package driver-chips
Summary:	Chips and Technologies video driver
Summary(pl):	Sterownik do kart na uk�adach Chips and Technologies
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-ChipsTechnologies

%description driver-chips
Chips and Technologies video driver.

%description driver-chips -l pl
Sterownik do kart na uk�adach Chips and Technologies.

%package driver-cirrus
Summary:	Cirrus Logic video driver
Summary(pl):	Sterownik do kart Cirrus Logic
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Cirrus

%description driver-cirrus
Cirrus Logic video driver.

%description driver-cirrus -l pl
Sterownik do kart Cirrus Logic.

%package driver-cyrix
Summary:	Cyrix video driver
Summary(pl):	Sterownik do grafiki na uk�adzie Cyrix MediaGX
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Cyrix

%description driver-cyrix
Cyrix video driver.

%description driver-cyrix -l pl
Sterownik do grafiki na uk�adzie Cyrix MediaGX.

%package driver-fbdev
Summary:	Video driver for framebuffer device
Summary(pl):	Sterownik korzystaj�cy z framebuffera
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-FBDev

%description driver-fbdev
Non-accelerated video driver for framebuffer device.

%description driver-fbdev -l pl
Nieakcelerowany sterownik korzystaj�cy z framebuffera.

%package driver-ffb
Summary:	Video driver for DRI sparc framebuffer device
Summary(pl):	Sterownik do framebuffera DRI na sparc
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description driver-ffb
Video driver for DRI sparc framebuffer device.

%description driver-ffb -l pl
Sterownik do framebuffera DRI na sparc.

%package driver-glide
Summary:	3Dfx Voodoo1 and Voodoo2 video driver
Summary(pl):	Sterownik do kart 3Dfx Voodoo1 i Voodoo2
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
# dlopens libglide2x.so
Requires:	Glide_VG

%description driver-glide
Voodoo1 and Voodoo2 video driver.

%description driver-glide -l pl
Sterownik do kart Voodoo1 i Voodoo2 firmy 3Dfx.

%package driver-glint
Summary:	GLINT/Permedia video driver
Summary(pl):	Sterownik do kart GLINT i Permedia
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
%ifarch %{ix86} ia64 %{x8664} alpha ppc arm
# for dri
Requires:	%{name}-OpenGL-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-OpenGL-libGL = %{epoch}:%{version}-%{release}
# -libs already required by -OpenGL-libGL
%endif
Obsoletes:	XFree86-3DLabs

%description driver-glint
GLINT/Permedia video driver.

%description driver-glint -l pl
Sterownik do kart GLINT i Permedia.

%package driver-i128
Summary:	Number 9 I128 video driver
Summary(pl):	Sterownik do kart Number 9 I128
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-I128

%description driver-i128
Number 9 I128 video driver.

%description driver-i128 -l pl
Sterownik do kart Number 9 I128.

%package driver-i740
Summary:	Intel i740 video driver
Summary(pl):	Sterownik do kart na uk�adzie Intel i740
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-i740

%description driver-i740
Intel i740 video driver.

%description driver-i740 -l pl
Sterownik do kart na uk�adzie Intel i740.

%package driver-i810
Summary:	Intel i810/i815/i830 video driver
Summary(pl):	Sterownik do grafiki na uk�adach Intel i810/i815/i830
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
%ifarch %{ix86} ia64
# for dri
Requires:	%{name}-OpenGL-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-OpenGL-libGL = %{epoch}:%{version}-%{release}
# -libs already required by -OpenGL-libGL
%endif
Obsoletes:	XFree86-i810

%description driver-i810
Intel i810/i815/i830 video driver.

%description driver-i810 -l pl
Sterownik do grafiki na uk�adach Intel i810/i815/i830.

%package driver-imstt
Summary:	Integrated Micro Solutions Twin Turbo 128 driver
Summary(pl):	Sterownik do kart Integrated Micro Solutions Twin Turbo 128
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description driver-imstt
Integrated Micro Solutions Twin Turbo 128 driver.

%description driver-imstt -l pl
Sterownik do kart Integrated Micro Solutions Twin Turbo 128.

%package driver-mga
Summary:	Matrox video driver
Summary(pl):	Sterownik do kart Matrox
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
%ifarch %{ix86} ia64 %{x8664} alpha ppc arm
# for dri
Requires:	%{name}-OpenGL-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-OpenGL-libGL = %{epoch}:%{version}-%{release}
# -libs already required by -OpenGL-libGL
%endif
Obsoletes:	XFree86-mga

%description driver-mga
Matrox video driver.

%description driver-mga -l pl
Sterownik do kart Matrox.

%package driver-neomagic
Summary:	NeoMagic video driver
Summary(pl):	Sterownik do kart NeoMagic
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-NeoMagic

%description driver-neomagic
NeoMagic video driver.

%description driver-neomagic -l pl
Sterownik do kart NeoMagic.

%package driver-newport
Summary:	Newport (XL) adapters video driver
Summary(pl):	Sterownik do kart Newport (XL)
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description driver-newport
Newport (XL) adapters video driver (found primarily in SGI Indy and
Indigo2 machines).

%description driver-newport -l pl
Sterownik do kart Newport (XL) (wyst�puj�cych g��wnie w komputerach
SGI Indy i Indigo).

%package driver-nsc
Summary:	National Semiconductors GEODE family video driver
Summary(pl):	Sterownik dla kart na uk�adach z rodziny GEODE firmy National Semiconductors
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description driver-nsc
National Semiconductors GEODE family video driver. Supports GXLV (5530
companion chip), SC1200, SC1400 and GX2 (5535 companion chip).

%description driver-nsc -l pl
Sterownik dla kart na uk�adach z rodziny GEODE firmy National
Semiconductors. Obs�uguje GXLV (uk�ad towarzysz�cy 5530), SC1200,
SC1400 oraz GX2 (uk�ad towarzysz�cy 5535).

%package driver-nv
Summary:	nVidia video driver
Summary(pl):	Sterownik do kart na uk�adach firmy nVidia
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-NVidia

%description driver-nv
nVidia video driver. Supports Riva128, RivaTNT, GeForce.

%description driver-nv -l pl
Sterownik do kart na uk�adach firmy nVidia: Riva128, RivaTNT, GeForce.

%package driver-rendition
Summary:	Rendition video driver
Summary(pl):	Sterownik do kart Rendition
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Rendition

%description driver-rendition
Rendition/Micron video driver.

%description driver-rendition -l pl
Sterownik do kart Verite firmowanych przez Rendition/Micron.

%package driver-s3virge
Summary:	S3 ViRGE/Trio3D video driver
Summary(pl):	Sterownik do kart na uk�adach S3 ViRGE i Trio3D
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-S3V

%description driver-s3virge
S3 ViRGE/Trio3D video driver.

%description driver-s3virge -l pl
Sterownik do kart na uk�adach S3 ViRGE i Trio3D.

%package driver-s3
Summary:	S3 Trio video driver
Summary(pl):	Sterownik do kart na uk�adach S3 Trio
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-S3

%description driver-s3
S3 Trio video driver.

%description driver-s3 -l pl
Sterownik do kart na uk�adach S3 Trio.

%package driver-savage
Summary:	S3 Savage video driver
Summary(pl):	Sterownik do kart na uk�adach S3 Savage
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description driver-savage
S3 Savage video driver.

%description driver-savage -l pl
Sterownik do kart na uk�adach S3 Savage.

%package driver-siliconmotion
Summary:	Silicon Motion video driver
Summary(pl):	Sterownik do kart na uk�adach Silicon Motion
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description driver-siliconmotion
Silicon Motion video driver.

%description driver-siliconmotion -l pl
Sterownik do kart na uk�adach Lynx firmy Silicon Motion.

%package driver-sis
Summary:	SiS video driver
Summary(pl):	Sterownik do kart na uk�adach SiS
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
%ifarch %{ix86} ia64
# for dri
Requires:	%{name}-OpenGL-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-OpenGL-libGL = %{epoch}:%{version}-%{release}
# -libs already required by -OpenGL-libGL
%endif
Obsoletes:	XFree86-SiS

%description driver-sis
SiS video driver.

%description driver-sis -l pl
Sterownik do kart na uk�adach SiS.

%package driver-sunbw2
Summary:	sunbw2 - Sun BW2 video driver
Summary(pl):	Sterownik do monochromatycznego framebuffera BW2 na Sunie
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-SunMono

%description driver-sunbw2
sunbw2 - Sun BW2 video driver.

%description driver-sunbw2 -l pl
Sterownik do monochromatycznego framebuffera BW2 na Sunie.

%package driver-suncg14
Summary:	suncg14 - Sun CG14 video driver
Summary(pl):	Sterownik do kolorowego framebuffera CG14 na Sunie
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description driver-suncg14
suncg14 - Sun CG14 video driver.

%description driver-suncg14 -l pl
Sterownik do kolorowego framebuffera CG14 na Sunie.

%package driver-suncg3
Summary:	suncg3 - Sun CG3 video cards driver
Summary(pl):	Sterownik do kolorowego framebuffera CG3 na Sunie
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description driver-suncg3
suncg3 - Sun CG3 video cards driver.

%description driver-suncg3 -l pl
Sterownik do kolorowego framebuffera CG3 na Sunie.

%package driver-suncg6
Summary:	suncg6 - Sun GX and Turbo GX video driver
Summary(pl):	Sterownik do grafiki GX i Turbo GX na Sunie
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description driver-suncg6
suncg6 - Sun GX and Turbo GX video driver.

%description driver-suncg6 -l pl
Sterownik do grafiki GX i Turbo GX na Sunie.

%package driver-sunffb
Summary:	sunffb - Sun Creator, Creator 3D and Elite 3D video cards driver
Summary(pl):	Sterownik do kart Sun Creator, Creator 3D, Elite 3D
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description driver-sunffb
sunffb - Sun Creator, Creator 3D and Elite 3D video cards driver.

%description driver-sunffb -l pl
Sterownik do kart Sun Creator, Creator 3D, Elite 3D.

%package driver-sunleo
Summary:	sunleo - Sun Leo (ZX) video cards driver
Summary(pl):	Sterownik do kart Sun Leo (ZX)
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description driver-sunleo
sunleo - Sun Leo (ZX) video cards driver.

%description driver-sunleo -l pl
Sterownik do kart Sun Leo (ZX).

%package driver-suntcx
Summary:	suntcx - Sun TCX video cards driver
Summary(pl):	Sterownik do kart Sun TCX
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description driver-suntcx
suntcx - Sun TCX video cards driver.

%description driver-suntcx -l pl
Sterownik do kart Sun TCX.

%package driver-tdfx
Summary:	3Dfx video driver
Summary(pl):	Sterownik do kart 3Dfx
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
%ifarch %{ix86} ia64 alpha arm ppc
# for dri
Requires:	%{name}-OpenGL-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-OpenGL-libGL = %{epoch}:%{version}-%{release}
# -libs already required by -OpenGL-libGL
# dlopens libglide3x.so
Requires:	Glide3-DRI
%endif
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
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-TGA

%description driver-tga
TGA video driver.

%description driver-tga -l pl
Sterownik do kart TGA.

%package driver-trident
Summary:	Trident video driver
Summary(pl):	Sterownik do kart Trident
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Trident

%description driver-trident
Trident video driver.

%description driver-trident -l pl
Sterownik do kart Trident.

%package driver-tseng
Summary:	Tseng Labs video driver
Summary(pl):	Sterownik do kart Tseng Labs
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Tseng
Obsoletes:	XFree86-W32

%description driver-tseng
Tseng Labs video driver.

%description driver-tseng -l pl
Sterownik do kart firmy Tseng Labs.

%package driver-via
Summary:	VIA CLE266 driver
Summary(pl):	Sterownik do kart VIA CLE266
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description driver-via
VIA CLE266 driver.

%description driver-via -l pl
Sterownik do kart VIA CLE266.

%package driver-vmware
Summary:	VMWare SVGA emulated video driver
Summary(pl):	Sterownik do emulacji karty SVGA dost�pnej pod VMware
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description driver-vmware
VMware emulated SVGA video driver. Necessary if you run Linux on
VMware virtual machine.

%description driver-vmware -l pl
Sterownik do emulacji karty SVGA dost�pnej pod VMware. Przydatny,
je�li uruchamiasz Linuksa na wirtualnej maszynie VMware.

%package libs
Summary:	X11R6 shared libraries
Summary(de):	X11R6 shared Libraries
Summary(es):	Bibliotecas compartidas X11R6
Summary(fr):	Biblioth�ques partag�es X11R6
Summary(pl):	Biblioteki dzielone dla X11R6
Summary(pt_BR):	Bibliotecas compartilhadas X11R6
Summary(ru):	����������� ���������� ��� X Window System (X11R6.4)
Summary(uk):	��̦����� �Ц������ ������������ ��� X Window System (X11R6.4)
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	grep
Requires(postun):	fileutils
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	xcursor = 1.0
Provides:	xft = 2.1.0
Provides:	xpm
Provides:	xrender = 0.8.0
%ifarch sparc sparc64
Obsoletes:	X11R6.1-libs
%endif
Obsoletes:	XFree86-xcursor
Obsoletes:	XFree86-xft
Obsoletes:	XFree86-xft2
Obsoletes:	XFree86-xrender
Obsoletes:	Xft
Obsoletes:	xcursor
Obsoletes:	xft
Obsoletes:	xpm
Obsoletes:	xrender

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
Dieses Paket enth�lt die zur gemeinsamen Nutzung vorgesehenen
Libraries, die die meisten X-Programme f�r den einwandfreien Betrieb
ben�tigen. Sie wurden in einem separaten Paket untergebracht, um den
Festplattenspeicherplatz auf Computern zu reduzieren, die ohne einen
X- Server (�ber ein Netz) arbeiten.

%description libs -l es
Este paquete contiene bibliotecas compartidas que la mayor�a de los
programas X necesitan para ejecutarse correctamente. Est�n en un
paquete a parte, para reducir el espacio en disco necesario para
ejecutar aplicaciones X en una m�quina sin un servidor X (a trav�s de
la red).

%description libs -l fr
Ce paquetage contient les biblioth�ques partag�es n�cessaires � de
nombreux programmes X. Elles se trouvent dans un paquetage s�par� afin
de r�duire l'espace disque n�cessaire � l'ex�cution des applications X
sur une machine sans serveur X (en r�seau).

%description libs -l pl
Pakiet zawieraj�cy podstawowe biblioteki potrzebne wi�kszo�ci
program�w korzystaj�cych z systemu X Window. Wydzielony w celu
oszcz�dno�ci miejsca potrzebnego do uruchamiania aplikacji X Window na
komputerach bez X serwera (np. przez sie�).

%description libs -l pt_BR
Este pacote cont�m bibliotecas compartilhadas que a maioria dos
programas X precisam para rodar corretamente. Eles est�o em um pacote
separado para reduzir o espa�o em disco necess�rio para rodar
aplica��es X em uma m�quina sem um servidor X (atrav�s da rede).

%description libs -l tr
Bu paket X programlar�n�n d�zg�n �al��abilmeleri i�in gereken
kitapl�klar� i�erir. Bunlar, X programlar�n� (sunucu olsun olmas�n)
�al��t�rmak i�in gerekli disk alan�n� azaltmak i�in ayr� bir paket
olarak sunulmu�tur.

%description libs -l ru
XFree86-libs �������� ����������� ����������, ������� ���������� ���
������ ����������� �������� ��� X. ��� ���������� �������� � ���������
����� ����� ���������� �������� ������������, ����������� ��� �������
���������� X �� ������� ��� X-������� (��������, �� ����).

���� �� �������������� X Window System �� ����� ������, ��� ����������
���������� XFree86-libs. ����� ���������� ���������� ��������� ������:
XFree86, ���� ��� ��������� ������� ������� XFree86, Xconfigurator,
XFree86-xfs.

���� �� ����������� ������������� ���������, ���������� ��� X-�������,
��� ����� ���� ���������� XFree86-devel.

%description libs -l uk
XFree86-libs ͦ����� ¦�̦����� �Ц������ ������������, ���Ҧ
����Ȧ�Φ ��� ������ ¦�����Ԧ ���������� ������� ��� X. � ¦�̦�����
������Φ � ������� ����� ��� �����ͦ� ��������� ��������, ����Ȧ�����
��� ������� ���������� ������� X �� ������� ��� X-������� (���������,
�� ����֦).

���� �� ������������ X Window System �� ��ۦ� ����Φ, ��� ����Ȧ���
���������� XFree86-libs. ����� ����Ȧ��� ���������� ��˦ ������:
XFree86, ���� ��� ��˦���� ����Ԧ� ����Ԧ� XFree86, Xconfigurator,
XFree86-xfs.

���� �� ���������� ���������� ��������, �˦ �������� �� X-�̦����, ���
����� ����Ȧ��� ���������� XFree86-devel.

%package modules
Summary:	Modules with X servers extensions
Summary(pl):	Wsp�lne dla wszystkich X serwer�w modu�y rozszerze�
Group:		X11/Servers
Obsoletes:	XFree86-module-PEX
Obsoletes:	XFree86-module-XIE

%description modules
Modules with X servers extensions.

%description modules -l pl
Wsp�lne dla wszystkich X serwer�w modu�y rozszerze�.

%package setup
Summary:	Graphical configuration tool for XFree86
Summary(pl):	Graficzny konfigurator dla XFree86
Summary(ru):	������� ��� ������������ XFree86
Summary(uk):	���̦�� ��� ���Ʀ��������� XFree86
Group:		X11
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-xf86cfg

%description setup
Setup containst a configuration tool for the XFree86 family of
servers. It allows you to configure video settings, keyboard layouts,
mouse type, and other miscellaneous options. It is slow however, and
requires the generic VGA 16 color server be available.

%description setup -l pl
Pakiet setup zawiera narz�dzia do konfiguracji XFree86. Pozwala na
skonfigurowanie ustawie� obrazu, klawiatury, typu myszki i innych
r�nych rzeczy. Jednak�e jest wolny i wymaga dost�pno�ci serwera do
standardowej 16-kolorowej VGA.

%description setup -l ru
������� ��� ������������ XFree86.

%description setup -l uk
���̦�� ��� ���Ʀ��������� XFree86.

%package static
Summary:	X11R6 static libraries
Summary(pl):	Biblioteki statyczne X11R6
Summary(ru):	����������� ���������� X11R6
Summary(uk):	������Φ ¦�̦����� X11R6
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	xcursor-static = 1.0
Provides:	xft-static = 2.1.0
Provides:	xpm-static
Provides:	xrender-static = 0.8.0
%ifarch sparc sparc64
Obsoletes:	X11R6.1-devel
%endif
Obsoletes:	XFree86-xcursor-static
Obsoletes:	XFree86-xft-static
Obsoletes:	XFree86-xrender-static
Obsoletes:	Xft-devel
Obsoletes:	xcursor-static
Obsoletes:	xft-static
Obsoletes:	xpm-static
Obsoletes:	xrender-static

%description static
X11R6 static libraries.

%description static -l pl
Biblioteki statyczne X11R6.

%description static -l ru
XFree86-static �������� ����������� ����������, ����������� ���
���������� ��������, ���������� ��� X-�������. ��������� ���������,
������� ����� �������� ��� X-�������.

%description static -l uk
XFree86-static ͦ����� ������Φ ¦�̦�����, ����Ȧ�Φ ��� ��������
�������, �˦ �������� �� X-�̦����.

%package tools
Summary:	Various tools for XFree86
Summary(pl):	R�ne narz�dzia dla XFree86
Summary(ru):	������������� ������� ��� XFree86
Summary(uk):	������Φ�Φ ���̦�� ��� XFree86
Group:		X11
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	man-config
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
R�ne narz�dzia dla X, w tym listres, xbiff, xedit, xeyes, xcalc,
xload, xman i inne.

Je�li u�ywasz X�w powiniene� zainstalowa� XFree86-tools. B�dziesz
r�wnie� musia� zainstalowa� pakiet XFree86, pakiet odpowiadaj�cy
Twojej karcie graficznej, jeden z pakiet�w z fontami, pakiet
Xconfigurator oraz XFree86-libs.

Wreszcie, je�li zamierzasz tworzy� aplikacje, kt�re dzia�aj� jako
klienci X, b�dziesz musia� zainstalowa� r�wnie� XFree86-devel.

Ten pakiet zawiera aplikacje, kt�re by�y w X11R6-contrib w starszych
wersjach X.

%description tools -l ru
������������� ������� ��� X, ������� listres, xbiff, xedit, xeyes,
xcalc, xload, xman � ������.

���� �� �������������� X Window System, ��� ���� ����������
XFree86-tools. ����� ��� ����� ���������� ���������� ����� ������:
XFree86, Xconfigurator, XFree86-xfs � XFree86-libs. ��������, ��� ����
���������� � ������ ������ ������� XFree86.

���� �� ����������� ������������� ���������, ���������� ��� X-�������,
��� ����� ���� ���������� XFree86-devel.

���� ����� �������� ��� ���������, ������� ������ ���������� �
X11R6-contrib.

%description tools -l uk
������Φ�Φ ���̦�� ��� X, ��������� listres, xbiff, xedit, xeyes,
xcalc, xload, xman �� ��ۦ.

���� �� ������������ X Window System, ��� ����Ȧ��� ����������
XFree86-tools. ����� ����� ���������� ��˦ ������: XFree86,
Xconfigurator, XFree86-xfs �� XFree86-libs. �������, ��� �����
���������� � ��ۦ ������ ����Ԧ� XFree86.

���� �� ���������� ���������� ��������, �˦ �������� �� X-�̦����, ���
����� ����Ȧ��� ���������� XFree86-devel.

��� ����� ͦ����� �Ӧ ��������, �˦ ��Φ�� ������� �� X11R6-contrib.

%package -n XcursorTheme-handhelds
Summary:	Cursors Theme "handhelds"
Summary(pl):	Motyw kursor�w "handhelds"
Group:		Themes
Requires:	XFree86-libs
Conflicts:	XFree86 < 4.3.99.901-0.2

%description -n XcursorTheme-handhelds
Cursors theme "handhelds" for X11.

%description -n XcursorTheme-handhelds -l pl
Motyw kursor�w "handhelds" dla X11.

%package -n XcursorTheme-redglass
Summary:	Cursors theme "redglass"
Summary(pl):	Motyw kursor�w "redglass"
Group:		Themes
Requires:	XFree86-libs
Conflicts:	XFree86 < 4.3.99.901-0.2

%description -n XcursorTheme-redglass
Cursors theme "redglass" for X11.

%description -n XcursorTheme-redglass -l pl
Motyw kursor�w "redglass" dla X11.

%package -n XcursorTheme-whiteglass
Summary:	Cursors theme "whiteglass"
Summary(pl):	Motyw kursor�w "whiteglass"
Group:		Themes
Requires:	XFree86-libs
Conflicts:	XFree86 < 4.3.99.901-0.2

%description -n XcursorTheme-whiteglass
Cursors theme "whiteglass" for X11.

%description -n XcursorTheme-whiteglass -l pl
Motyw kursor�w "whiteglass" dla X11.

%package imake
Summary:	C preprocessor interface to the make utility
Summary(pl):	Miedzymordzie do make oparte o preprocesor C
Group:		Development/Building
Provides:	imake = %{epoch}:%{version}-%{release}
Obsoletes:	imake

%description imake
Imake is used to generate Makefiles from a template, a set of cpp
macro functions, and a per-directory input file called an Imakefile.
This allows machine dependencies (such as compiler options, alternate
command names, and special make rules) to be kept separate from the
descriptions of the various items to be built.

%description imake -l pl
Imake jest u�ywany do generowania plik�w Makefile na bazie szablonu,
zbioru makr preprocesora C oraz (dla ka�dego podkatalogu) pliku
wej�ciowego Imakefile. Pozwala to na oddzielenie informacji zale�nych
od �rodowiska kompilacji (takich jak opcje kompilatora, alternatywne
nazwy komend i regu�y specjalne) od opisu r�nych element�w kt�re maj�
by� kompilowane.

%package sessreg
Summary:	sessreg - manage utmp/wtmp entries for non-init clients
Summary(pl):	Program do zarz�dzania wpisami w utmp/wtmp
Group:		X11
Provides:	sessreg = %{epoch}:%{version}-%{release}
Obsoletes:	sessreg

%description sessreg
sessreg is a simple program for managing utmp/wtmp entries for xdm
sessions.

System V has a better interface to /var/run/utmp than BSD; it
dynamically allocates entries in the file, instead of writing them at
fixed positions indexed by position in /etc/ttys.

%description sessreg -l pl
sessreg jest prostym programem do zarz�dzania wpisami w utmp/wtmp dla
sesji xdm.

System V ma lepszy ni� BSD interfejs do /var/run/utmp; dynamicznie
alokuje wpisy w pliku, zamiast zapisywania ich na ustalonych pozycjach
indeksowanych po�o�eniem w /etc/ttys.

%package twm
Summary:	Tab Window Manager for the X Window System
Summary(pl):	Twm - podstawowy zarz�dca okien dla X Window System
Summary(ru):	������� ������� ��������
Summary(uk):	������� צ������ ��������
Group:		X11/Window Managers
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Provides:	twm = %{epoch}:%{version}-%{release}
Obsoletes:	twm

%description twm
Twm is a window manager for the X Window System. It provides
titlebars, shaped windows, several forms of icon management,
user-defined macro functions, click-to-type and pointerdriven keyboard
focus, and user-specified key and pointer button bindings.

%description twm -l pl
Twm jest zarz�dc� okien dla X Window System. Daje belki tytu�owe,
ramki okien, par� form zarz�dzania ikonami, definiowalne makra,
ustawianie focusu klikni�ciem lub po�o�eniem wska�nika myszy,
definiowalne przypisania klawiszy i przycisk�w myszy.

%description twm -l ru
������� ���������� ������� ��������.

%description twm -l uk
������� ���������� צ������ ��������.

%package xauth
Summary:	xauth - X authority file utility
Summary(pl):	xauth - narz�dzie do plik�w X authority
Group:		X11
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Provides:	xauth = %{epoch}:%{version}-%{release}
Obsoletes:	xauth

%description xauth
The xauth program is used to edit and display the authorization
information used in connecting to the X server. This program is
usually used to extract authorization records from one machine and
merge them in on another (as is the case when using remote logins or
granting access to other users).

%description xauth -l pl
Program xauth s�u�y do edycji i wy�wietlania informacji
autoryzacyjnych u�ywanych przy ��czeniu z X serwerem. Ten program
przewa�nie jest u�ywany do wyci�gania rekord�w autoryzacji z jednej
maszyny i do��czania ich na innej (w celu umo�liwienia zdalnego
logowania lub udost�pnienia innym u�ytkownikom).

%package xdm
Summary:	xdm - X Display Manager with support for XDMCP, host chooser
Summary(pl):	XDM - zarz�dca ekran�w z obs�ug� XDMCP i wybieraniem host�w
Summary(ru):	�������� ������� X
Summary(uk):	�������� ������� X
Group:		X11
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	pam >= 0.71
Requires:	%{name}-sessreg = %{epoch}:%{version}-%{release}
Requires:	/usr/X11R6/bin/sessreg
Provides:	XDM
Provides:	xdm = %{epoch}:%{version}-%{release}
Obsoletes:	entrance
Obsoletes:	gdm
Obsoletes:	kdm
Obsoletes:	wdm
Obsoletes:	xdm

%description xdm
Xdm manages a collection of X displays, which may be on the local host
or remote servers. The design of xdm was guided by the needs of X
terminals as well as the X Consortium standard XDMCP, the X Display
Manager Control Protocol.

%description xdm -l pl
Xdm zarz�dza zestawem ekran�w X, kt�re mog� by� lokalne lub na
zdalnych serwerach. Zosta� zaprojektowany zgodnie z potrzebami X
terminali oraz standardem X Consortium XDMCP.

%description xdm -l ru
�������� ������� X.

%description xdm -l uk
�������� ������� X.

%package xfs
Summary:	Font server for XFree86
Summary(pl):	Serwer font�w dla XFree86
Summary(ru):	���������� ��� X Window System
Summary(uk):	���������� ��� X Window System
Group:		X11
PreReq:		rc-scripts
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/useradd
Requires(pre):	/usr/sbin/groupadd
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	XFree86-fonts-base
Provides:	xfs = %{epoch}:%{version}-%{release}
Provides:	group(xfs)
Provides:	user(xfs)
Obsoletes:	xfs
Obsoletes:	xfsft

%description xfs
This is a font server for XFree86. You can serve fonts to other X
servers remotely with this package, and the remote system will be able
to use all fonts installed on the font server, even if they are not
installed on the remote computer.

%description xfs -l pl
Pakiet zawiera serwer font�w dla XFree86. Mo�e udost�pnia� fonty dla X
serwer�w lokalnych lub zdalnych.

%description xfs -l ru
XFree86-xfs �������� ������ ������� ��� XFree86. Xfs ����� �����
������������� ������ ��������� X-��������. ��������� ������� �����
�������� ������������ ��� ������, ������������� �� ������� �������,
���� ���� ��� �� ����������� �� ��������� ����������.

�� ������ ���������� XFree86-xfs ���� �� �������������� X Window
System. ����� ��� �������� ���������� ��������� ������: XFree86,
�����(�) ������� XFree86, ����������� ��� ����� �������, Xconfigurator
� XFree86-libs.

%description xfs -l uk
XFree86-xfs ͦ����� ������ ����Ԧ� ��� XFree86. Xfs ����� ����
�������� ������ צ�������� X-��������. ��������� ������� �����
��������������� �Ӧ ������, �˦ ���������Φ �� �����Ҧ ����Ԧ�, ��צ��
���� ���� �� ���������Φ �� צ��������� ����'���Ҧ.

�� �����Φ ���������� XFree86-xfs ���� �� ������������ X Window
System. ����� ��� ���������� ���������� ������Φ ������: XFree86,
�����(�) ����Ԧ� XFree86, ����Ȧ�Φ ��� ���ϧ �������, Xconfigurator
�� XFree86-libs.

%prep
%setup -qc -a1 -a2 -a7
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p0
%patch6 -p0
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p0
#%patch11 -p0	-- obsoleted???
%patch12 -p1
%patch13 -p1
%patch14 -p0
%patch15 -p1
%patch16 -p0
#%patch17 -p1	-- not ready, is it required?
%patch18 -p1
#%patch19 -p1	-- maybe should be updated to allow using make -j
%patch20 -p0
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch26 -p1
%patch27 -p1
%ifarch sparc sparc64
#%patch28 -p1	-- needs update
%endif
%patch29 -p0
%patch30 -p1
%patch32 -p1
%patch33 -p1
#%patch34 -p1	-- seems not applied (was partially in rc1??? maybe another fix present?)
#%patch35 -p1	-- obsoleted? (but doesn't look to be applied)
%patch36 -p0
#%patch38 -p0	-- causing problems IIRC (but not really needed)
%patch39 -p0
%patch40 -p1
%{!?debug:%patch41 -p1}
%{!?with_glide:%patch42 -p0}
%patch43 -p0
%patch44 -p0
%patch45 -p1
%patch46 -p0
%patch47 -p1
%patch50 -p0
%patch52 -p1
%patch53 -p0
%patch54 -p0
%patch55 -p0
%patch56 -p0
%patch57 -p0

rm -f xc/config/cf/host.def

%build
%{__make} -S -C xc World \
	DEFAULT_OS_CPU_FROB=%{_target_cpu} \
	CC="%{__cc}" \
	BOOTSTRAPCFLAGS="%{rpmcflags}" \
	CCOPTIONS="%{rpmcflags}" \
	CXXOPTIONS="%{rpmcflags}" \
	CXXDEBUGFLAGS="" \
	CDEBUGFLAGS="" \
	ICONDIR="%{_iconsdir}" \
	LINUXDIR="/dev/null"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{pam.d,rc.d/init.d,security/console.apps,sysconfig,xdg} \
	$RPM_BUILD_ROOT%{_sysconfdir}/X11/fs \
	$RPM_BUILD_ROOT%{_appdefsdir}/{cs,da,de,es,fr,hu,it,ja,ko,nl,pl,pt,ru,sk,zh_CN.gb2312,zh_TW.big5} \
	$RPM_BUILD_ROOT%{_datadir}/misc \
	$RPM_BUILD_ROOT%{_sbindir} \
	$RPM_BUILD_ROOT/usr/{bin,include,lib} \
	$RPM_BUILD_ROOT/var/{log,lib/xkb} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_iconsdir},%{_pixmapsdir}/mini} \
	$RPM_BUILD_ROOT{%{_wmpropsdir},%{_soundsdir},%{_themesdir}/{Default,ThinIce,Metal,Industrial,Bluecurve}} \
	$RPM_BUILD_ROOT{%{_xsessdir},%{_wallpapersdir},%{_wmstylesdir}} \
	$RPM_BUILD_ROOT%{_pkgconfigdir}

%{__make} -C xc	install	install.man \
	DESTDIR="$RPM_BUILD_ROOT" \
	DOCDIR="/usr/share/doc/%{name}-%{version}" \
	INSTBINFLAGS="-m 755" \
	INSTPGMFLAGS="-m 755" \
	RAWCPP="/lib/cpp" \
	BOOTSTRAPCFLAGS="%{rpmcflags}" \
	CCOPTIONS="%{rpmcflags}" \
	CXXOPTIONS="%{rpmcflags}" \
	CXXDEBUGFLAGS="" \
	CDEBUGFLAGS="" \
	ICONDIR="%{_iconsdir}" \
	LINUXDIR="/dev/null"

# fix pkgconfig path
if [ "%{_pkgconfigdir}" != "/usr/lib/pkgconfig" ] ; then
	mv $RPM_BUILD_ROOT/usr/lib/pkgconfig/* $RPM_BUILD_ROOT%{_pkgconfigdir}
fi

# setting default X
rm -f $RPM_BUILD_ROOT%{_bindir}/X
ln -sf XFree86 $RPM_BUILD_ROOT%{_bindir}/X

# setting ghost X in /etc/X11 -- xf86config will fix this ...
ln -sf %{_bindir}/XFree86 $RPM_BUILD_ROOT%{_sysconfdir}/X11/X

# add X11 links in /usr/bin, /usr/lib /usr/include
ln -sf %{_includedir}/X11 $RPM_BUILD_ROOT/usr/include/X11
ln -sf %{_libx11dir} $RPM_BUILD_ROOT/usr/lib/X11
ln -sf %{_bindir} $RPM_BUILD_ROOT/usr/bin/X11

# fix libGL*.so links
rm -f $RPM_BUILD_ROOT%{_libdir}/libGL*.so
ln -sf libGL.so.1 $RPM_BUILD_ROOT%{_libdir}/libGL.so
ln -sf libGLU.so.1 $RPM_BUILD_ROOT%{_libdir}/libGLU.so

# according to OpenGL ABI for Linux v1.0
# (http://oss.sgi.com/projects/ogl-sample/ABI/index.html)
# libGL.so.1, libGL.so, libGLU.so.1, libGL.so must be accessible in /usr
# libGL is already linked by XFree86 build, but libGLU not
ln -sf %{_libdir}/libGLU.so.1 $RPM_BUILD_ROOT/usr/%{_lib}/libGLU.so.1
ln -sf %{_libdir}/libGLU.so $RPM_BUILD_ROOT/usr/%{_lib}/libGLU.so

# move instead of symlinking
rm -f $RPM_BUILD_ROOT/usr/include/GL
mv -f $RPM_BUILD_ROOT%{_includedir}/GL $RPM_BUILD_ROOT/usr/include

# get the most current OpenGL extensions
cp -f %{SOURCE53} $RPM_BUILD_ROOT/usr/include/GL/glext.h

# don't include shared version due to Motif issues
rm -f $RPM_BUILD_ROOT%{_libdir}/libGLw.so*

# collect Xserver headers and make symlinks
for f in `cat %{SOURCE44}`; do
	install -D xc/${f} $RPM_BUILD_ROOT%{_includedir}/X11/Xserver/${f}
done
cd $RPM_BUILD_ROOT%{_includedir}/X11/Xserver
sh %{SOURCE45}
cd -

# set up PLD xdm config
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/X11/xdm/{*Console,Xaccess,Xsession,Xsetup*}
install xdm-xinitrc-*/pixmaps/* $RPM_BUILD_ROOT%{_sysconfdir}/X11/xdm/pixmaps
install xdm-xinitrc-*/{*Console,Xaccess,Xsession,Xsetup*} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xdm

install %{SOURCE8} $RPM_BUILD_ROOT/etc/pam.d/xdm
install %{SOURCE9} $RPM_BUILD_ROOT/etc/pam.d/xserver
install %{SOURCE10} $RPM_BUILD_ROOT/etc/rc.d/init.d/xdm
install %{SOURCE11} $RPM_BUILD_ROOT/etc/rc.d/init.d/xfs
install %{SOURCE12} $RPM_BUILD_ROOT%{_sysconfdir}/X11/fs/config
install %{SOURCE13} $RPM_BUILD_ROOT%{_appdefsdir}/pl/XTerm

install %{SOURCE14} $RPM_BUILD_ROOT/etc/sysconfig/xdm
install %{SOURCE15} $RPM_BUILD_ROOT/etc/sysconfig/xfs

install %{SOURCE24} $RPM_BUILD_ROOT%{_wmpropsdir}/twm.desktop
install %{SOURCE25} %{SOURCE26} %{SOURCE27} %{SOURCE28} %{SOURCE29} \
	%{SOURCE30} %{SOURCE31} %{SOURCE47} %{SOURCE48} %{SOURCE49} \
	$RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE34} %{SOURCE35} %{SOURCE36} %{SOURCE37} %{SOURCE38} \
	%{SOURCE39} %{SOURCE40} %{SOURCE41} %{SOURCE50} %{SOURCE51} \
	%{SOURCE52} \
	$RPM_BUILD_ROOT%{_pixmapsdir}

bzip2 -dc %{SOURCE42} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

# install Xrender pkgconfig metadata
install %{SOURCE54} $RPM_BUILD_ROOT%{_pkgconfigdir}/xrender.pc

# twm desktop file for gdm/kdm support
install %{SOURCE46} $RPM_BUILD_ROOT%{_xsessdir}/twm.desktop

:> $RPM_BUILD_ROOT/etc/security/console.apps/xserver
:> $RPM_BUILD_ROOT/etc/security/blacklist.xserver
:> $RPM_BUILD_ROOT/etc/security/blacklist.xdm

ln -sf %{_fontsdir} $RPM_BUILD_ROOT%{_libx11dir}/fonts

# do not duplicate xkbcomp program
rm -f $RPM_BUILD_ROOT%{_libx11dir}/xkb/xkbcomp
ln -sf %{_bindir}/xkbcomp $RPM_BUILD_ROOT%{_sysconfdir}/X11/xkb/xkbcomp

ln -sf /usr/share/doc/%{name}-%{version} $RPM_BUILD_ROOT%{_libx11dir}/doc

rm -f $RPM_BUILD_ROOT%{_libx11dir}/config/host.def

:> $RPM_BUILD_ROOT%{_libx11dir}/config/host.def
:> $RPM_BUILD_ROOT%{_sysconfdir}/X11/XF86Config

rm -rf $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/html

# resolve conflict with man-pages
mv -f $RPM_BUILD_ROOT%{_mandir}/man4/{mouse.4,mouse-x.4}

# help rpm to detect deps
chmod 755 $RPM_BUILD_ROOT%{_libdir}/modules/dri/*.so

%ifnarch sparc sparc64
gzip -9nf $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/*

# don't gzip README.* files, they are needed by XF86Setup
gunzip $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/README.*
%endif

# kill some stuff for cleaner build
# (fontconfig packaged separately, DRM already in kernel)
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/fontconfig.pc \
	$RPM_BUILD_ROOT%{_mandir}/{man3/fontconfig.3x,man1/fc-{cache,list}.1x} \
	$RPM_BUILD_ROOT%{_libdir}/libfontconfig.* \
	$RPM_BUILD_ROOT%{_includedir}/fontconfig \
	$RPM_BUILD_ROOT%{_bindir}/{fc-cache,fc-list} \
	$RPM_BUILD_ROOT/etc/fonts \
	$RPM_BUILD_ROOT%{_prefix}/src

%clean
rm -rf $RPM_BUILD_ROOT

#--- %post{un}, %preun, %verifyscript, %trigge ----------

%post	DPS -p /sbin/ldconfig
%postun DPS -p /sbin/ldconfig

%post	OpenGL-libGL -p /sbin/ldconfig
%postun OpenGL-libGL -p /sbin/ldconfig

%post	OpenGL-libs -p /sbin/ldconfig
%postun OpenGL-libs -p /sbin/ldconfig

%post libs
umask 022
grep -qs "^%{_libdir}$" /etc/ld.so.conf
[ $? -ne 0 ] && echo "%{_libdir}" >> /etc/ld.so.conf
/sbin/ldconfig

%postun libs
if [ "$1" = "0" ]; then
	umask 022
	grep -v "%{_libdir}" /etc/ld.so.conf > /etc/ld.so.conf.new
	mv -f /etc/ld.so.conf.new /etc/ld.so.conf
fi
/sbin/ldconfig

%verifyscript libs
echo -n "Looking for %{_libdir} in /etc/ld.so.conf... "
if ! grep -q "^%{_libdir}$" /etc/ld.so.conf ; then
	echo "missing"
	echo "%{_libdir} missing from /etc/ld.so.conf" >&2
else
	echo "found"
fi

%pre modules
if [ -d /etc/X11/xkb/geometry/hp ]; then
	rm -rf /etc/X11/xkb/geometry/hp
fi

%triggerpostun modules -- XFree86-modules < 4.0.2
if [ -d /usr/X11R6/lib/X11/xkb ]; then
	rm -rf /usr/X11R6/lib/X11/xkb
	ln -sf /etc/X11/xkb /usr/X11R6/lib/X11/xkb
fi

%post xdm
/sbin/chkconfig --add xdm
if [ -f /var/lock/subsys/xdm ]; then
	echo "Run \"/etc/rc.d/init.d/xdm restart\" to restart xdm." >&2
	echo "WARNING: it will terminate all sessions opened from xdm!" >&2
else
	echo "Run \"/etc/rc.d/init.d/xdm start\" to start xdm." >&2
fi

%preun xdm
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/xdm ]; then
		/etc/rc.d/init.d/xdm stop >&2
	fi
	/sbin/chkconfig --del xdm
fi

%pre xfs
%groupadd -P %{name}-xfs -g 56 -r -f xfs
%useradd -P %{name}-xfs -u 56 -r -d /etc/X11/fs -s /bin/false -c "X Font Server" -g xfs xfs

%post xfs
/sbin/chkconfig --add xfs
if [ -f /var/lock/subsys/xfs ]; then
	/etc/rc.d/init.d/xfs restart >&2
else
	echo "Run \"/etc/rc.d/init.d/xfs start\" to start font server." >&2
fi

%preun xfs
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/xfs ]; then
		/etc/rc.d/init.d/xfs stop >&2
	fi
	/sbin/chkconfig --del xfs
fi

%postun xfs
if [ "$1" = "0" ]; then
	%userremove xfs
	%groupremove xfs
fi

#--- %files --------------------------

%files
%defattr(644,root,root,755)
%ifnarch sparc sparc64
%doc %{_docdir}/%{name}-%{version}
%doc %{_libx11dir}/doc
%endif

%{_appdefsdir}/UXTerm
%{_appdefsdir}/XCalc
%{_appdefsdir}/XCalc-color
%{_appdefsdir}/XClipboard
%{_appdefsdir}/XClock
%{_appdefsdir}/XClock-color
%{_appdefsdir}/XLoad
%{_appdefsdir}/XLogo
%{_appdefsdir}/XLogo-color
%{_appdefsdir}/XSm
%{_appdefsdir}/XTerm
%lang(pl) %{_appdefsdir}/pl/XTerm
%{_appdefsdir}/XTerm-color

%attr(755,root,root) %{_libx11dir}/lbxproxy
%attr(755,root,root) %{_libx11dir}/proxymngr
%attr(755,root,root) %{_libx11dir}/rstart
%attr(755,root,root) %{_libx11dir}/fonts
%attr(755,root,root) %{_libx11dir}/xinit
%attr(755,root,root) %{_libx11dir}/xsm

%dir /etc/X11/xinit
%dir /etc/X11/lbxproxy
/etc/X11/lbxproxy/*
%dir /etc/X11/proxymngr
/etc/X11/proxymngr/*
%dir /etc/X11/rstart
/etc/X11/rstart/config
%attr(755,root,root) /etc/X11/rstart/rstartd.real
%dir /etc/X11/rstart/commands
/etc/X11/rstart/commands/x
/etc/X11/rstart/commands/x11
%attr(755,root,root) /etc/X11/rstart/commands/*List*
%dir /etc/X11/rstart/commands/x11r6
%attr(755,root,root) /etc/X11/rstart/commands/x11r6/*
%dir /etc/X11/rstart/contexts
/etc/X11/rstart/contexts/*
%dir /etc/X11/xsm
/etc/X11/xsm/*

%dir %{_libx11dir}/x11perfcomp
%attr(755,root,root) %{_libx11dir}/x11perfcomp/*

%attr(755,root,root) %{_bindir}/Xmark
%attr(755,root,root) %{_bindir}/appres
%attr(755,root,root) %{_bindir}/atobm
%attr(755,root,root) %{_bindir}/bitmap
%attr(755,root,root) %{_bindir}/bmtoa
%attr(755,root,root) %{_bindir}/cxpm
%attr(755,root,root) %{_bindir}/dga
%attr(755,root,root) %{_bindir}/editres
%attr(755,root,root) %{_bindir}/gtf
%attr(755,root,root) %{_bindir}/iceauth
%attr(755,root,root) %{_bindir}/lbxproxy
%attr(755,root,root) %{_bindir}/lndir
%attr(755,root,root) %{_bindir}/luit
%attr(755,root,root) %{_bindir}/makeg
%attr(755,root,root) %{_bindir}/makestrs
%attr(755,root,root) %{_bindir}/mergelib
%attr(755,root,root) %{_bindir}/mkdirhier
%attr(755,root,root) %{_bindir}/mkhtmlindex
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
%attr(755,root,root) %{_bindir}/uxterm
%attr(755,root,root) %{_bindir}/xcmsdb
%attr(755,root,root) %{_bindir}/xconsole
%attr(755,root,root) %{_bindir}/xcursorgen
%attr(755,root,root) %{_bindir}/xcutsel
%attr(755,root,root) %{_bindir}/xdpyinfo
%attr(755,root,root) %{_bindir}/xfindproxy
%attr(755,root,root) %{_bindir}/xfwp
%attr(755,root,root) %{_bindir}/xgamma
%attr(755,root,root) %{_bindir}/xhost
%attr(755,root,root) %{_bindir}/xinit
%attr(755,root,root) %{_bindir}/xkbbell
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
%attr(755,root,root) %{_bindir}/xrandr
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

%{_desktopdir}/xconsole.desktop
%{_desktopdir}/xterm.desktop
%{_pixmapsdir}/xconsole.png
%{_pixmapsdir}/xlogo64.png
%{_pixmapsdir}/xterm.png

%{_appdefsdir}/Xvidtune

%{_mandir}/man1/Xmark.1*
%{_mandir}/man1/appres.1*
%{_mandir}/man1/atobm.1*
%{_mandir}/man1/bitmap.1*
%{_mandir}/man1/bmtoa.1*
%{_mandir}/man1/cxpm.1*
%{_mandir}/man1/dga.1*
%{_mandir}/man1/editres.1*
%{_mandir}/man1/gtf.1*
%{_mandir}/man1/iceauth.1*
%{_mandir}/man1/lbxproxy.1*
%{_mandir}/man1/libxrx.1*
%{_mandir}/man1/lndir.1*
%{_mandir}/man1/luit.1x*
%{_mandir}/man1/makestrs.1*
%{_mandir}/man1/makeg.1*
%{_mandir}/man1/mergelib.1*
%{_mandir}/man1/mkdirhier.1*
%{_mandir}/man1/mkhtmlindex.1*
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
%{_mandir}/man1/xcursorgen.1*
%{_mandir}/man1/xcutsel.1*
%{_mandir}/man1/xdpyinfo.1*
%{_mandir}/man1/xfindproxy.1*
%{_mandir}/man1/xfwp.1*
%{_mandir}/man1/xgamma.1*
%{_mandir}/man1/xhost.1*
%{_mandir}/man1/xinit.1*
%{_mandir}/man1/xkbevd.1*
%{_mandir}/man1/xkbprint.1*
%{_mandir}/man1/xlsatoms.1*
%{_mandir}/man1/xlsclients.1*
%{_mandir}/man1/xlsfonts.1*
%{_mandir}/man1/xmodmap.1*
%{_mandir}/man1/xprop.1*
%{_mandir}/man1/xrandr.1*
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

# to be separated
%attr(755,root,root) %{_bindir}/fonttosfnt
%attr(755,root,root) %{_bindir}/mkfontdir
%attr(755,root,root) %{_bindir}/mkfontscale
%{_mandir}/man1/fonttosfnt.1*
%{_mandir}/man1/mkfontdir.1*
%{_mandir}/man1/mkfontscale.1*

%files common
%defattr(644,root,root,755)
/usr/bin/X11
/usr/lib/X11
%dir %{_bindir}
%dir %{_libdir}
%dir %{_libx11dir}
%{_libx11dir}/rgb.txt

%files DPS
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/makepsres
%attr(755,root,root) %{_bindir}/pswrap
%attr(755,root,root) %{_bindir}/dpsinfo
%attr(755,root,root) %{_bindir}/dpsexec
%attr(755,root,root) %{_libdir}/libdps.so.*.*
%attr(755,root,root) %{_libdir}/libdpstk.so.*.*
%attr(755,root,root) %{_libdir}/libpsres.so.*.*
%{_mandir}/man1/makepsres.1*
%{_mandir}/man1/pswrap.1*
%{_mandir}/man1/dpsexec.1*
%{_mandir}/man1/dpsinfo.1*

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

%files OpenGL-core
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/extensions/libglx.a
%attr(755,root,root) %{_libdir}/modules/extensions/libGLcore.a

%files OpenGL-libGL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGL.so.*.*
%attr(755,root,root) %{_libdir}/libGL.so
# Linux OpenGL ABI compatibility symlinks
%attr(755,root,root) /usr/%{_lib}/libGL.so.1
%attr(755,root,root) /usr/%{_lib}/libGL.so

%files OpenGL-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glxinfo
%attr(755,root,root) %{_bindir}/glxgears
%attr(755,root,root) %{_libdir}/libGLU.so.*.*
# to be fixed: it contains unresolved symbols and would need -lXm
#%attr(755,root,root) %{_libdir}/libGLw.so.*.*
%attr(755,root,root) %{_libdir}/libOSMesa.so.*.*
# Linux OpenGL ABI compatibility symlink
%attr(755,root,root) /usr/%{_lib}/libGLU.so.1
%{_mandir}/man1/glxinfo.1*
%{_mandir}/man1/glxgears.1*

%files OpenGL-devel-base
%defattr(644,root,root,755)
/usr/include/GL/gl.h
/usr/include/GL/glx.h
/usr/include/GL/glext.h
/usr/include/GL/glxtokens.h

%files OpenGL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLU.so
%attr(755,root,root) %{_libdir}/libOSMesa.so
# Linux OpenGL ABI compatibility symlink
%attr(755,root,root) /usr/%{_lib}/libGLU.so
%{_libdir}/libGLw.a
%dir /usr/include/GL
/usr/include/GL/GLwDrawA.h
/usr/include/GL/GLwDrawAP.h
/usr/include/GL/GLwMDrawA.h
/usr/include/GL/GLwMDrawAP.h
/usr/include/GL/glu.h
/usr/include/GL/glxext.h
/usr/include/GL/glxint.h
/usr/include/GL/glxmd.h
/usr/include/GL/glxproto.h
/usr/include/GL/osmesa.h
%{_mandir}/man3/gl[A-Z]*
%{_mandir}/man3/glu*
%{_mandir}/man3/GLw*

%files OpenGL-static
%defattr(644,root,root,755)
%{_libdir}/libGL.a
%{_libdir}/libGLU.a
%{_libdir}/libOSMesa.a

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
%attr(755,root,root) %{_bindir}/getconfig*
%attr(755,root,root) %{_sysconfdir}/X11/X
%attr(755,root,root) %{_bindir}/X
%{_mandir}/man1/XFree86.1*
%{_mandir}/man1/Xserver.1*
%{_mandir}/man1/getconfig.1*
%{_mandir}/man5/XF86Config.5*
%{_mandir}/man5/getconfig.5*

%{_libx11dir}/Cards
%{_libx11dir}/Options
%{_libx11dir}/getconfig

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
%attr(755,root,root) %{_bindir}/bdftopcf
%ifnarch ppc sparc sparc64 sparcv9
%attr(755,root,root) %{_bindir}/ioport
%endif
%attr(755,root,root) %{_bindir}/mmapr
%attr(755,root,root) %{_bindir}/mmapw
%attr(755,root,root) %{_bindir}/xcursor-config
%attr(755,root,root) %{_bindir}/xft-config
%attr(755,root,root) %{_libdir}/libFS.so
%attr(755,root,root) %{_libdir}/libI810XvMC.so
%attr(755,root,root) %{_libdir}/libICE.so
%attr(755,root,root) %{_libdir}/libSM.so
%attr(755,root,root) %{_libdir}/libX11.so
%attr(755,root,root) %{_libdir}/libXRes.so
%attr(755,root,root) %{_libdir}/libXTrap.so
%attr(755,root,root) %{_libdir}/libXaw.so
%attr(755,root,root) %{_libdir}/libXcursor.so
%attr(755,root,root) %{_libdir}/libXext.so
%attr(755,root,root) %{_libdir}/libXfont.so
%attr(755,root,root) %{_libdir}/libXfontcache.so
%attr(755,root,root) %{_libdir}/libXft.so
%attr(755,root,root) %{_libdir}/libXi.so
%attr(755,root,root) %{_libdir}/libXinerama.so
%attr(755,root,root) %{_libdir}/libXmu.so
%attr(755,root,root) %{_libdir}/libXmuu.so
%attr(755,root,root) %{_libdir}/libXp.so
%attr(755,root,root) %{_libdir}/libXpm.so
%attr(755,root,root) %{_libdir}/libXrandr.so
%attr(755,root,root) %{_libdir}/libXrender.so
%attr(755,root,root) %{_libdir}/libXss.so
%attr(755,root,root) %{_libdir}/libXt.so
%attr(755,root,root) %{_libdir}/libXtst.so
%attr(755,root,root) %{_libdir}/libXv.so
%attr(755,root,root) %{_libdir}/libXvMC.so
%attr(755,root,root) %{_libdir}/libXxf86dga.so
%attr(755,root,root) %{_libdir}/libXxf86misc.so
%attr(755,root,root) %{_libdir}/libXxf86rush.so
%attr(755,root,root) %{_libdir}/libXxf86vm.so
%attr(755,root,root) %{_libdir}/libfontenc.so
%attr(755,root,root) %{_libdir}/libxkbfile.so
%attr(755,root,root) %{_libdir}/libxkbui.so
%attr(755,root,root) %{_libdir}/libxrx.so
%{_libdir}/libXau.a
%{_libdir}/libXdmcp.a
%{_libdir}/libfntstubs.a
%{_libdir}/liboldX.a
%{_libdir}/libxf86config.a
%{_includedir}/X11/*.h
%{_includedir}/X11/ICE
%{_includedir}/X11/PM
%{_includedir}/X11/SM
%{_includedir}/X11/Xaw
%{_includedir}/X11/Xcursor
%{_includedir}/X11/Xft
%{_includedir}/X11/Xmu
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/*.h
%{_includedir}/X11/fonts
%{_includedir}/xf86*.h
%{_libx11dir}/config
%{_mandir}/man1/bdftopcf.1*
%{_mandir}/man3/[A-FH-Z]*
%{_pkgconfigdir}/xcursor.pc
%{_pkgconfigdir}/xft.pc
%{_pkgconfigdir}/xrender.pc

%files Xserver-devel
%defattr(644,root,root,755)
%{_includedir}/X11/Xserver

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664}
%files driver-apm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/apm_drv.o
%{_mandir}/man4/apm.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664}
%files driver-ark
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/ark_drv.o
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} mips ppc arm
%files driver-chips
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/chips_drv.o
%{_mandir}/man4/chips.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} alpha
%files driver-cirrus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/cirrus_*.o
%{_mandir}/man4/cirrus.4*
%endif

%ifarch %{ix86} ia64 %{x8664}
%files driver-cyrix
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/cyrix_drv.o
%{_mandir}/man4/cyrix.4*
%endif

%ifarch %{ix86} ia64 %{x8664} sparc sparc64 mips ppc arm superh
%files driver-fbdev
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/fbdev_drv.o
%{_mandir}/man4/fbdev.4*
%endif

%ifarch %{ix86} ia64
%if %{with glide}
%files driver-glide
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/glide_drv.o
%{_mandir}/man4/glide.4*
%endif
%endif

%files driver-glint
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/glint_drv.o
%ifarch %{ix86} ia64 %{x8664} alpha ppc arm
%attr(755,root,root) %{_libdir}/modules/dri/gamma_dri.so
%endif
%{_mandir}/man4/glint.4*

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664}
%files driver-i128
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/i128_drv.o
%{_mandir}/man4/i128.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64
%files driver-i740
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/i740_drv.o
%{_mandir}/man4/i740.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64
%files driver-i810
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/i810_drv.o
# i810_dri alone is built on x86_64 - what for?
%attr(755,root,root) %{_libdir}/modules/dri/i810_dri.so
%attr(755,root,root) %{_libdir}/modules/dri/i830_dri.so
%{_mandir}/man4/i810.4*
%endif

# Devel: %{ix86} sparc sparc64 ppc %{x8664}
%if 0
%files driver-imstt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/imstt_drv.o
%{_mandir}/man4/imstt.4*
%endif

%ifarch %{ix86} ia64 %{x8664} sparc sparc64 mips alpha ppc arm
%files driver-mga
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/mga_drv.o
%ifarch %{ix86} ia64 %{x8664} alpha ppc arm
%attr(755,root,root) %{_libdir}/modules/dri/mga_dri.so
%endif
%{_mandir}/man4/mga.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664}
%files driver-neomagic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/neomagic_drv.o
%{_mandir}/man4/neomagic.4*
%endif

# Devel: %{ix86} sparc sparc64 %{x8664}
%ifarch mips
%files driver-newport
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/newport_drv.o
%{_mandir}/man4/newport.4*
%endif

%ifarch %{ix86}
%files driver-nsc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/nsc_drv.o
%{_mandir}/man4/nsc.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} mips alpha arm ppc
%files driver-nv
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/nv_drv.o
%attr(755,root,root) %{_libdir}/modules/drivers/riva128.o
%{_mandir}/man4/nv.4*
%endif

%files driver-ati
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/ati*_drv.o

%files driver-r128
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/r128*_drv.o
%ifarch %{ix86} ia64 %{x8664} alpha ppc arm
%attr(755,root,root) %{_libdir}/modules/dri/r128_dri.so
%endif
%{_mandir}/man4/r128.4*

%files driver-radeon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/radeon*_drv.o
%ifarch %{ix86} ia64 %{x8664} alpha ppc arm
%attr(755,root,root) %{_libdir}/modules/dri/radeon_dri.so
%attr(755,root,root) %{_libdir}/modules/dri/r200_dri.so
%endif
%{_mandir}/man4/radeon.4*

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} alpha
%files driver-rendition
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/rendition_drv.o
%{_libdir}/modules/*.uc
%{_mandir}/man4/rendition.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} mips alpha ppc arm
%files driver-s3virge
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/s3virge_drv.o
%{_mandir}/man4/s3virge.4*
%endif

%ifarch %{ix86} ia64 %{x8664} mips alpha ppc arm
%files driver-s3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/s3_drv.o
#%%{_mandir}/man4/s3.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} mips alpha ppc arm
%files driver-savage
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/savage_drv.o
%{_mandir}/man4/savage.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} alpha
%files driver-siliconmotion
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/siliconmotion_drv.o
%{_mandir}/man4/siliconmotion.4*
%endif

%ifarch %{ix86} ia64 %{x8664} mips ppc arm
%files driver-sis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/sis_drv.o
%ifarch %{ix86} ia64
%attr(755,root,root) %{_libdir}/modules/dri/sis_dri.so
%endif
%{_mandir}/man4/sis.4*
%endif

%ifarch sparc sparc64
%files driver-sunbw2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/sunbw2_drv.o
%{_mandir}/man4/sunbw2.4*
%endif

%ifarch sparc sparc64
%files driver-suncg14
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/suncg14_drv.o
%{_mandir}/man4/suncg14.4*
%endif

%ifarch sparc sparc64
%files driver-suncg3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/suncg3_drv.o
%{_mandir}/man4/suncg3.4*
%endif

%ifarch sparc sparc64
%files driver-suncg6
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/suncg6_drv.o
%{_mandir}/man4/suncg6.4*
%endif

%ifarch sparc sparc64
%files driver-sunffb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/sunffb_drv.o
# Devel: %{ix86} ia64 (for fun?)
%attr(755,root,root) %{_libdir}/modules/dri/ffb_dri.so
%{_mandir}/man4/sunffb.4*
%endif

%ifarch sparc sparc64
%files driver-sunleo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/sunleo_drv.o
%{_mandir}/man4/sunleo.4*
%endif

%ifarch sparc sparc64
%files driver-suntcx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/suntcx_drv.o
%{_mandir}/man4/suntcx.4*
%endif

%ifarch %{ix86} ia64 %{x8664} sparc sparc64 mips alpha arm ppc
%files driver-tdfx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/tdfx_drv.o
%ifarch %{ix86} ia64 alpha arm ppc
%attr(755,root,root) %{_libdir}/modules/dri/tdfx_dri.so
%endif
%{_mandir}/man4/tdfx.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} alpha
%files driver-tga
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/tga_drv.o
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} mips ppc arm
%files driver-trident
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/trident_drv.o
%{_mandir}/man4/trident.4*
%endif

%ifarch %{ix86} ia64 %{x8664}
%files driver-tseng
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/tseng_drv.o
%{_mandir}/man4/tseng.4*
%endif

%ifarch %{ix86} ia64
%files driver-via
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/via_drv.o
%{_mandir}/man4/via.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64
%files driver-vmware
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/vmware_drv.o
%{_mandir}/man4/vmware.4*
%endif

%files libs
%defattr(644,root,root,755)
%dir /etc/xdg
%dir %{_themesdir}
%dir %{_themesdir}/Default
%dir %{_themesdir}/ThinIce
%dir %{_themesdir}/Metal
%dir %{_themesdir}/Industrial
%dir %{_themesdir}/Bluecurve
%{_libx11dir}/XErrorDB
%{_libx11dir}/XKeysymDB
%dir %{_appdefsdir}
%lang(cs) %dir %{_appdefsdir}/cs
%lang(da) %dir %{_appdefsdir}/da
%lang(de) %dir %{_appdefsdir}/de
%lang(es) %dir %{_appdefsdir}/es
%lang(fr) %dir %{_appdefsdir}/fr
%lang(hu) %dir %{_appdefsdir}/hu
%lang(ko) %dir %{_appdefsdir}/ko
%lang(nl) %dir %{_appdefsdir}/nl
%lang(pl) %dir %{_appdefsdir}/pl
%lang(pt) %dir %{_appdefsdir}/pt
%lang(ru) %dir %{_appdefsdir}/ru
%lang(sk) %dir %{_appdefsdir}/sk
%lang(zh_CN) %dir %{_appdefsdir}/zh_CN.gb2312
%lang(zh_TW) %dir %{_appdefsdir}/zh_TW.big5
%dir %{_libx11dir}/locale
%{_libx11dir}/locale/[!l]*
%{_libx11dir}/locale/locale.*
%dir %{_libx11dir}/locale/%{_lib}
%dir %{_libx11dir}/locale/%{_lib}/common
%attr(755,root,root) %{_libx11dir}/locale/%{_lib}/common/*.so*
%dir %{_includedir}
%dir %{_includedir}/X11
/usr/include/X11
%dir %{_sbindir}
%dir %{_datadir}/misc
%dir %{_iconsdir}
%dir %{_pixmapsdir}
%dir %{_pixmapsdir}/mini
%dir %{_soundsdir}
%dir %{_wallpapersdir}
%dir %{_wmpropsdir}
%dir %{_xsessdir}
%dir %{_wmstylesdir}
%attr(755,root,root) %{_libdir}/libFS.so.*.*
%attr(755,root,root) %{_libdir}/libI810XvMC.so.*.*
%attr(755,root,root) %{_libdir}/libICE.so.*.*
%attr(755,root,root) %{_libdir}/libSM.so.*.*
%attr(755,root,root) %{_libdir}/libX11.so.*.*
%attr(755,root,root) %{_libdir}/libXRes.so.*.*
%attr(755,root,root) %{_libdir}/libXTrap.so.*.*
%attr(755,root,root) %{_libdir}/libXaw.so.*.*
%attr(755,root,root) %{_libdir}/libXcursor.so.*.*
%attr(755,root,root) %{_libdir}/libXext.so.*.*
%attr(755,root,root) %{_libdir}/libXfont.so.*.*
%attr(755,root,root) %{_libdir}/libXfontcache.so.*.*
%attr(755,root,root) %{_libdir}/libXft.so.1.*
%attr(755,root,root) %{_libdir}/libXft.so.2.*
%attr(755,root,root) %{_libdir}/libXi.so.*.*
%attr(755,root,root) %{_libdir}/libXinerama.so.*.*
%attr(755,root,root) %{_libdir}/libXmu.so.*.*
%attr(755,root,root) %{_libdir}/libXmuu.so.*.*
%attr(755,root,root) %{_libdir}/libXp.so.*.*
%attr(755,root,root) %{_libdir}/libXpm.so.*.*
%attr(755,root,root) %{_libdir}/libXrandr.so.*.*
%attr(755,root,root) %{_libdir}/libXrender.so.*.*
%attr(755,root,root) %{_libdir}/libXss.so.*.*
%attr(755,root,root) %{_libdir}/libXt.so.*.*
%attr(755,root,root) %{_libdir}/libXtst.so.*.*
%attr(755,root,root) %{_libdir}/libXv.so.*.*
%attr(755,root,root) %{_libdir}/libXvMC.so.*.*
%attr(755,root,root) %{_libdir}/libXxf86dga.so.*.*
%attr(755,root,root) %{_libdir}/libXxf86misc.so.*.*
%attr(755,root,root) %{_libdir}/libXxf86rush.so.*.*
%attr(755,root,root) %{_libdir}/libXxf86vm.so.*.*
%attr(755,root,root) %{_libdir}/libfontenc.so.*.*
%attr(755,root,root) %{_libdir}/libxkbfile.so.*.*
%attr(755,root,root) %{_libdir}/libxkbui.so.*.*
%attr(755,root,root) %{_libdir}/libxrx.so.*.*

%files modules
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xkbcomp
%{_libx11dir}/xkb
%{_sysconfdir}/X11/xkb
/var/lib/xkb
%dir %{_libdir}/modules
%dir %{_libdir}/modules/dri
%dir %{_libdir}/modules/drivers
%attr(755,root,root) %{_libdir}/modules/*.a
%attr(755,root,root) %{_libdir}/modules/codeconv
%ifnarch %{x8664}
%attr(755,root,root) %{_libdir}/modules/drivers/linux
%endif
%ifarch %{ix86} ia64 %{x8664} sparc sparc64 alpha ppc arm
%attr(755,root,root) %{_libdir}/modules/drivers/vga_drv.o
%endif
%ifarch %{ix86} ia64 %{x8664} sparc sparc64
%attr(755,root,root) %{_libdir}/modules/drivers/vesa_drv.o
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
%attr(755,root,root) %{_libx11dir}/xserver
%dir /etc/X11/xserver
/etc/X11/xserver/SecurityPolicy
#%%{_mandir}/man1/xtr*
%{_mandir}/man1/xkbcomp.1*
%{_mandir}/man4/aiptek.4*
%{_mandir}/man4/citron.4*
%{_mandir}/man4/dmc.4*
%{_mandir}/man4/dynapro.4*
%{_mandir}/man4/elographics.4*
%{_mandir}/man4/fbdevhw.4*
%{_mandir}/man4/fpit.4*
%{_mandir}/man4/js_x.4*
%{_mandir}/man4/kbd.4*
%{_mandir}/man4/keyboard.4*
%{_mandir}/man4/microtouch.4*
%{_mandir}/man4/mouse-x.4*
%{_mandir}/man4/mutouch.4*
%{_mandir}/man4/palmax.4*
%{_mandir}/man4/penmount.4*
%{_mandir}/man4/tek4957.4*
%{_mandir}/man4/ur98.4*
%ifnarch %{x8664}
%{_mandir}/man4/v4l.4*
%endif
%ifarch %{ix86} ia64 %{x8664} sparc sparc64 alpha ppc arm
%{_mandir}/man4/vga.4*
%endif
%ifarch %{ix86} ia64 %{x8664} sparc sparc64
%{_mandir}/man4/vesa.4*
%endif
%{_mandir}/man4/void.4*
%{_mandir}/man4/wacom.4*

%files setup
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcitweak
%attr(755,root,root) %{_bindir}/scanpci
%attr(755,root,root) %{_bindir}/xf86cfg
%attr(755,root,root) %{_bindir}/xf86config
%{_appdefsdir}/XF86Cfg
%{_mandir}/man1/pcitweak.1*
%{_mandir}/man1/scanpci.1*
%{_mandir}/man1/xf86cfg.1*
%{_mandir}/man1/xf86config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libFS.a
%{_libdir}/libI810XvMC.a
%{_libdir}/libICE.a
%{_libdir}/libSM.a
%{_libdir}/libX11.a
%{_libdir}/libXRes.a
%{_libdir}/libXTrap.a
%{_libdir}/libXaw.a
%{_libdir}/libXcursor.a
%{_libdir}/libXext.a
%{_libdir}/libXfont.a
%{_libdir}/libXfontcache.a
%{_libdir}/libXft.a
%{_libdir}/libXi.a
%{_libdir}/libXinerama.a
%{_libdir}/libXmu.a
%{_libdir}/libXmuu.a
%{_libdir}/libXp.a
%{_libdir}/libXpm.a
%{_libdir}/libXrandr.a
%{_libdir}/libXrender.a
%{_libdir}/libXss.a
%{_libdir}/libXt.a
%{_libdir}/libXtst.a
%{_libdir}/libXv.a
%{_libdir}/libXvMC.a
%{_libdir}/libXxf86dga.a
%{_libdir}/libXxf86misc.a
%{_libdir}/libXxf86rush.a
%{_libdir}/libXxf86vm.a
%{_libdir}/libfontenc.a
%{_libdir}/libxkbfile.a
%{_libdir}/libxkbui.a

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
%{_libx11dir}/xedit
%{_libx11dir}/xman.help
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
%{_mandir}/man1/xtr*
%{_mandir}/man1/texteroids.1*

%lang(it) %{_mandir}/it/man1/xload.1*

%lang(pl) %{_mandir}/pl/man1/rman.1*

%{_appdefsdir}/Beforelight
%{_appdefsdir}/Bitmap
%{_appdefsdir}/Bitmap-color
%{_appdefsdir}/Clock-color
%{_appdefsdir}/Editres
%{_appdefsdir}/Editres-color
%{_appdefsdir}/Viewres
%{_appdefsdir}/XConsole
%{_appdefsdir}/Xedit
%{_appdefsdir}/Xedit-color
%{_appdefsdir}/Xfd
%{_appdefsdir}/Xgc
%{_appdefsdir}/Xmag
%{_appdefsdir}/Xman
%{_appdefsdir}/Xmessage
%{_appdefsdir}/Xmessage-color
%{_appdefsdir}/Xmh
%{_appdefsdir}/XFontSel
%{_appdefsdir}/Xditview
%{_appdefsdir}/Xditview-chrtr

%{_desktopdir}/oclock.desktop
%{_desktopdir}/xcalc.desktop
%{_desktopdir}/xclipboard.desktop
%{_desktopdir}/xclock.desktop
%{_desktopdir}/xedit.desktop
%{_desktopdir}/xeyes.desktop
%{_desktopdir}/xload.desktop
%{_desktopdir}/xmag.desktop
%{_pixmapsdir}/oclock.png
%{_pixmapsdir}/xcalc.png
%{_pixmapsdir}/xclipboard.png
%{_pixmapsdir}/xclock.png
%{_pixmapsdir}/xedit.png
%{_pixmapsdir}/xeyes.png
%{_pixmapsdir}/xload.png
%{_pixmapsdir}/xmag.png

%if %{with cursors}
%files -n XcursorTheme-handhelds
%defattr(644,root,root,755)
%{_iconsdir}/handhelds

%files -n XcursorTheme-redglass
%defattr(644,root,root,755)
%{_iconsdir}/redglass

%files -n XcursorTheme-whiteglass
%defattr(644,root,root,755)
%{_iconsdir}/whiteglass
%endif

%files imake
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ccmakedep
%attr(755,root,root) %{_bindir}/cleanlinks
%attr(755,root,root) %{_bindir}/gccmakedep
%attr(755,root,root) %{_bindir}/imake
%attr(755,root,root) %{_bindir}/makedepend
%attr(755,root,root) %{_bindir}/xmkmf

%{_mandir}/man1/imake.1*
%{_mandir}/man1/ccmakedep.1*
%{_mandir}/man1/cleanlinks.1*
%{_mandir}/man1/gccmakedep.1*
%{_mandir}/man1/makedepend.1*
%{_mandir}/man1/xmkmf.1*

%files sessreg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sessreg
%{_mandir}/man1/sessreg.1*

%files twm
%defattr(644,root,root,755)
%{_wmpropsdir}/twm.desktop
%{_xsessdir}/twm.desktop
%attr(755,root,root) %{_bindir}/twm
%dir %{_sysconfdir}/X11/twm
%config %{_sysconfdir}/X11/twm/system.twmrc
%attr(755,root,root) %{_libx11dir}/twm
%{_mandir}/man1/twm.1*

%files xauth
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xauth
%{_mandir}/man1/xauth.1*

%files xdm
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/pam.d/xdm
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/security/blacklist.xdm
%attr(754,root,root) /etc/rc.d/init.d/xdm
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/xdm
/var/lib/xdm

%{_appdefsdir}/Chooser

%attr(755,root,root) %{_libx11dir}/xdm
%attr(755,root,root) %{_bindir}/xdm
%attr(755,root,root) %{_bindir}/chooser
%{_mandir}/man1/xdm.1*

%dir /etc/X11/xdm
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/GiveConsole
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/TakeConsole
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/Xsession
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/Xsetup_0
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/Xwilling
%config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/Xaccess
%config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/Xresources
%config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/Xservers
%config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/xdm-config
/etc/X11/xdm/pixmaps
/etc/X11/xdm/authdir

%files xfs
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/xfs
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/xfs
%dir %{_sysconfdir}/X11/fs
%attr(755,root,root) %{_libx11dir}/fs
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/X11/fs/config

%attr(755,root,root) %{_bindir}/xfs
%attr(755,root,root) %{_bindir}/fslsfonts
%attr(755,root,root) %{_bindir}/fstobdf
%attr(755,root,root) %{_bindir}/mkcfm
%attr(755,root,root) %{_bindir}/xfsinfo

%{_mandir}/man1/xfs.1*
%{_mandir}/man1/fslsfonts.1*
%{_mandir}/man1/fstobdf.1*
%{_mandir}/man1/mkcfm.1*
%{_mandir}/man1/xfsinfo.1*
