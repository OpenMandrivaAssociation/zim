%define name	zim
%define version	0.48
%define release	%mkrel 2

Summary:	A desktop wiki and outliner
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		http://www.zim-wiki.org/downloads/%{name}-%version.tar.gz
License:	GPLv2
Group:		Editors
Url:		http://www.zim-wiki.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel
BuildRequires:	python-gobject
Requires:	python
Requires:	pygtk2.0
Requires:	python-gobject
Requires:	python-simplejson
Suggests:	pyxdg
Suggests:	xdg-utils
BuildArch:	noarch

%description
Zim is a WYSIWYG text editor written in Gtk2-Perl which aims to bring
the concept of a wiki to your desktop. Every page is saved as a text
file with wiki markup. Pages can contain links to other pages, and are
saved automatically. Creating a new page is as easy as linking to a
non-existing page. Pages are ordered in a hierarchical structure that
gives it the look and feel of an outliner. This tool is intended to
keep track of TODO lists or to serve as a personal scratch book.

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf %{buildroot}
python setup.py install --skip-xdg-cmd --root=%{buildroot}

#install icons
install -D -m 0644 data/zim.png %{buildroot}%{_icons64dir}/zim.png
install -D -m 0644 data/zim.png %{buildroot}%{_iconsdir}/hicolor/64x64/mimetypes/application-x-zim-notebook.png
install -D -m 0644 data/zim.png %{buildroot}%{_iconsdir}/hicolor/64x64/mimetypes/gnome-mime-application-x-zim-notebook.png

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README.txt CHANGELOG.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{python_sitelib}/*
%{_mandir}/man1/%{name}*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/mime/*
%{_iconsdir}/hicolor/*/*/*
