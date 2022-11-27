
Name:		asteroids3D
Summary:	Summary	A 3D, first-person game of blowing up asteroids
Version:	1.0
Release:	1
License:	GPLv2+
Group:		Games/Arcade
Source:		https://sourceforge.net/projects/a3d/files/asteroids3D-%{version}.tar.xz
URL:		https://sourceforge.net/projects/a3d/	
BuildRequires:	mesa-common-devel

%description
asteroids3D is a 3D, first-person game of blowing up asteroids.
The graphics more accurately reflect the future position of the 
targeted asteroid and provide information about closure rate.

%prep
%setup -q 

%build
%configure --with-gamesdir=%{_bindir} --with-gamedatadir=%{_datadir}/%name
%make_build

%install
%make_install

%files
%{_bindir}/asteroids3D
%{_datadir}/applications/asteroids3D.desktop
%{_datadir}/asteroids3D/
