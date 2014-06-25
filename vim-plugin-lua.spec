Summary:	Write and run Lua-scripts using menus and hotkeys
Name:		vim-plugin-lua
Version:	1.1
Release:	0.1
License:	vim
Group:		Applications/Editors/Vim
Source0:	http://carme.pld-linux.org/~uzsolt/sources/%{name}-%{version}.zip
# Source0-md5:	dc5c7f39f4eac33be7b7772751a26496
Source1:	http://lug.fh-swf.de/vim/vim-doc/luasupport.html
# Source1-md5:	f9be025278e98144378c1ad4af9bee05
URL:		http://www.vim.org/scripts/script.php?script_id=1763
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/vim
Requires:	vim-rt >= 4:7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
Write and run Lua-scripts using menus and hotkeys.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}

install -d $RPM_BUILD_ROOT%{_vimdatadir}/ftplugin
cp -a ftplugin/lua.vim $RPM_BUILD_ROOT%{_vimdatadir}/ftplugin

install -d $RPM_BUILD_ROOT%{_vimdatadir}/plugin
cp -a plugin/lua-support.vim $RPM_BUILD_ROOT%{_vimdatadir}/plugin

install -d $RPM_BUILD_ROOT%{_vimdatadir}/doc
cp -a doc/luasupport.txt $RPM_BUILD_ROOT%{_vimdatadir}/doc

install -d $RPM_BUILD_ROOT%{_vimdatadir}/lua-support
cp -a lua-support/{codesnippets,rc,scripts,templates,wordlists} \
	$RPM_BUILD_ROOT%{_vimdatadir}/lua-support

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -a %{SOURCE1} lua-support/doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo 'helptags %{_vimdatadir}/doc' | vim -e -s -V0 -R -n --noplugin

%postun
echo 'helptags %{_vimdatadir}/doc' | vim -e -s -V0 -R -n --noplugin

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%{_vimdatadir}/ftplugin/*
%{_vimdatadir}/plugin/*
%{_vimdatadir}/doc/*
%{_vimdatadir}/lua-support
