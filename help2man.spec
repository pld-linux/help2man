%include	/usr/lib/rpm/macros.perl
Summary:	help2man - automatic manual page generation
Summary(pl):	help2man - automatyczne generowanie stron manuala
Name:		help2man
Version:	1.35.2
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://ftp.debian.org/debian/pool/main/h/help2man/%{name}_%{version}.tar.gz
# Source0-md5:	0581005bc093306ea1038f495f021bc2
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/help2man/
BuildRequires:	gettext-devel
BuildRequires:	perl-Locale-gettext
BuildRequires:	rpm-perlprov
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
help2man is a tool for automatically generating simple manual pages
from program output. This program is intended to provide an easy way
for software authors to include a manual page in their distribution
without having to maintain that document. Given a program which
produces reasonably standard `--help' and `--version' outputs,
help2man can re-arrange that output into something which resembles
a manual page.

%description -l pl
help2man to narz�dzie do automatycznego generowania prostych stron
manuala na podstawie wyj�cia z programu. Ten program ma za zadanie
da� autorom oprogramowania �atwy spos�b na do��czanie stron manuala
bez opiekowania si� nimi. Po wskazaniu programu, kt�ry daje w miar�
standardowe wyj�cie dla opcji --help i --version, help2man potrafi
przekszta�ci� to wyj�cie na co� przypominaj�cego stron� manuala.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/hacklocaledir.so
%{_infodir}/*.info*
%{_mandir}/man1/*.1*
%lang(fr) %{_mandir}/fr/man1/*.1*
%lang(pl) %{_mandir}/pl/man1/*.1*
