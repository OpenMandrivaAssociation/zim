%define name zim
%define rname Zim
%define version 0.25
%define release %mkrel 1

Summary: A desktop wiki and outliner
Name: %{name}
Version: %{version}
Release: %{release}
Source: http://www.zim-wiki.org/downloads/Zim-%version.tar.gz
License: Artistic
Group: Editors
Url: http://pardus-larus.student.utwente.nl/~pardus/projects/zim/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-Module-Build
BuildRequires: desktop-file-utils
BuildRequires: perl-Gtk2-Spell
BuildRequires: perl-File-MimeInfo
BuildRequires: perl-File-BaseDir
BuildRequires: perl-File-DesktopEntry
BuildArch: noarch

%description
Zim is a WYSIWYG text editor written in Gtk2-Perl which aims to bring
the concept of a wiki to your desktop. Every page is saved as a text
file with wiki markup. Pages can contain links to other pages, and are
saved automatically. Creating a new page is as easy as linking to a
non-existing page. Pages are ordered in a hierarchical structure that
gives it the look and feel of an outliner. This tool is intended to
keep track of TODO lists or to serve as a personal scratch book.

%prep
%setup -q -n %{rname}-%{version}

%build
perl ./Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

desktop-file-install --vendor='' \
	--dir=%buildroot%_datadir/applications \
	--remove-category='Application' \
	%buildroot%_datadir/applications/*.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%update_desktop_database
%update_mime_database
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_desktop_database
%clean_mime_database
%endif

%files
%defattr(-,root,root)
%doc Changes
%{_bindir}/%{name}
%{perl_vendorlib}/*
%{_mandir}/*/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/zim.desktop
%{_datadir}/pixmaps/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/mime/packages/zim.xml
