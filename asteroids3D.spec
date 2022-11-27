%define	name	asteroids3D
%define	version	0.5.1
%define release	4
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
%configure --with-gamesdir=%_gamesbindir --with-gamedatadir=%_gamesdatadir/%name
%make

%install
rm -rf $RPM_BUILD_ROOT
make install gamesdir=$RPM_BUILD_ROOT%{_gamesbindir} gamedatadir=$RPM_BUILD_ROOT%{_gamesdatadir}/%name

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=arcade_section
Categories=Game;ArcadeGame;
Name=Asteroids3D
Comment=%{Summary}
EOF

%files
%doc COPYRIGHT README.html 
%{_datadir}/applications/mandriva-%{name}.desktop
%{_gamesdatadir}/%name
%defattr (755,root,root,755)
%{_gamesbindir}/%{name}



