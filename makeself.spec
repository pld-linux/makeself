Summary:	Make self-extractable archives on Unix
Name:		makeself
Version:	2.1.5
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://megastep.org/makeself/%{name}-%{version}.run
# Source0-md5:	85f03bd3602fd55debec6ae449f7c15c
URL:		http://megastep.org/makeself/
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
makeself.sh is a small shell script that generates a self-extractable
tar.gz archive from a directory. The resulting file appears as a shell
script (many of those have a .run suffix), and can be launched as is.
The archive will then uncompress itself to a temporary directory and
an optional arbitrary command will be executed (for example an
installation script).  This is pretty similar to archives generated
with WinZip Self-Extractor in the Windows world. Makeself archives
also include checksums for integrity self-validation (CRC and/or MD5
checksums).
			
%prep
%setup -qcT
cd ..
/bin/sh %{SOURCE0} --noexec

%build
%{__sed} -i -e 's|^HEADER=.*|HEADER=%{_datadir}/misc/makeself-header.sh|' makeself.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/misc}

install -p makeself.sh $RPM_BUILD_ROOT%{_bindir}
install -p makeself-header.sh $RPM_BUILD_ROOT%{_datadir}/misc
install -p makeself.1 $RPM_BUILD_ROOT%{_mandir}/man1

ln -s makeself.sh $RPM_BUILD_ROOT%{_bindir}/makeself

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/makeself*
%{_datadir}/misc/makeself-header.sh
%{_mandir}/man1/makeself.1*
