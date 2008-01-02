%define	name	asteroids3D
%define	version	0.2.2
%define	release	%mkrel 8
%define	Summary	A 3D, first-person game of blowing up asteroids

Name:		%{name}
Summary:	%{Summary}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Arcade

Source:		%name-%version.tar.bz2

URL:		http://www.psc.edu/~smp/a3d/
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	Mesa-common-devel

%description
asteroids3D is a 3D, first-person game of blowing up asteroids.
The graphics more accurately reflect the future position of the 
targeted asteroid and provide information about closure rate.

%prep
%setup -q -n %name
perl -pi -e 's,/usr/X11R6/lib,%{_prefix}/X11R6/%{_lib},' Makefile

%build
%make CC="gcc %optflags -O3"

%install
rm -rf $RPM_BUILD_ROOT
install -m755 %{name} -D %buildroot/%{_gamesbindir}/%{name}

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

%post
%update_menus

%postun
%clean_menus

%clean
rm -fr %buildroot

%files
%defattr (644,root,root,755)
%doc CHANGELOG COPYRIGHT README
%{_datadir}/applications/mandriva-%{name}.desktop
%defattr (755,root,root,755)
%{_gamesbindir}/%{name}

