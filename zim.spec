Name:		zim
Version:	0.58
Release:	2
Summary:	A desktop wiki and outliner
Source:		http://www.zim-wiki.org/downloads/%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Editors
Url:		http://www.zim-wiki.org/
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
%setup -q

%install
%__python setup.py install --skip-xdg-cmd --root=%{buildroot}

#install icons
%__install -D -m 0644 data/zim.png %{buildroot}%{_icons64dir}/zim.png
%__install -D -m 0644 data/zim.png %{buildroot}%{_iconsdir}/hicolor/64x64/mimetypes/application-x-zim-notebook.png
%__install -D -m 0644 data/zim.png %{buildroot}%{_iconsdir}/hicolor/64x64/mimetypes/gnome-mime-application-x-zim-notebook.png

%find_lang %{name}

%clean

%files -f %{name}.lang
%doc README.txt CHANGELOG.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{python_sitelib}/*
%{_mandir}/man1/%{name}*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/mime/*
%{_iconsdir}/hicolor/*/*/*
%{_iconsdir}/ubuntu*/*/*/*


%changelog
* Thu Mar 22 2012 Andrey Bondrov <abondrov@mandriva.org> 0.55-1mdv2011.0
+ Revision: 786044
- New version 0.55

* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.50-1
+ Revision: 645496
- update to new version 0.50

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.48-2mdv2011.0
+ Revision: 592373
- rebuild for python 2.7

* Fri Aug 06 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.48-1mdv2011.0
+ Revision: 567190
- update to 0.48
- drop patch0 and use --skip-xdg-cmd instead

* Thu Mar 25 2010 Funda Wang <fwang@mandriva.org> 0.46-1mdv2010.1
+ Revision: 527405
- New version 0.46

* Sat Mar 06 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.44-1mdv2010.1
+ Revision: 515235
- update tp 0.44

* Sat Feb 13 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.43-1mdv2010.1
+ Revision: 505185
- add missing BR
- update to 0.43
- add patch to fix setup.py
- fix license
- clean spec

* Sat Dec 19 2009 Ahmad Samir <ahmadsamir@mandriva.org> 0.28-2mdv2010.1
+ Revision: 480044
- rebuild for perl5.10.1 (bug #56339)

* Sun Jul 19 2009 Funda Wang <fwang@mandriva.org> 0.28-1mdv2010.0
+ Revision: 397456
- new version 0.28

* Mon Aug 25 2008 Funda Wang <fwang@mandriva.org> 0.26-1mdv2009.0
+ Revision: 275621
- New version 0.26

* Wed Aug 06 2008 Olivier Blin <blino@mandriva.org> 0.25-2mdv2009.0
+ Revision: 264208
- rebuild for perl 5.10 (#41070)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Funda Wang <fwang@mandriva.org>
    - add missing BRs

* Sun May 25 2008 Funda Wang <fwang@mandriva.org> 0.25-1mdv2009.0
+ Revision: 211110
- update to new version 0.25
- fix URL

* Wed Apr 23 2008 Funda Wang <fwang@mandriva.org> 0.24-1mdv2009.0
+ Revision: 196730
- New version 0.24

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 22 2007 Funda Wang <fwang@mandriva.org> 0.23-1mdv2008.1
+ Revision: 111173
- New version 0.23

* Fri Oct 12 2007 Jérôme Soyer <saispo@mandriva.org> 0.22-1mdv2008.1
+ Revision: 97304
- New release 0.22

* Sun Aug 19 2007 Funda Wang <fwang@mandriva.org> 0.20-1mdv2008.0
+ Revision: 67025
- New version 0.20

* Thu Apr 19 2007 Olivier Blin <blino@mandriva.org> 0.19-1mdv2008.0
+ Revision: 14988
- 0.19


* Sun Feb 18 2007 Jérôme Soyer <saispo@mandriva.org> 0.17-1mdv2007.0
+ Revision: 122457
- New release 0.17

* Thu Aug 24 2006 Olivier Blin <oblin@mandriva.com> 0.16-2mdv2007.0
+ Revision: 57640
- fix typo in summary
- Import zim

* Sun Jul 30 2006 Olivier Blin <blino@mandriva.com> 0.16-1mdv2007.0
- initial Mandriva release


