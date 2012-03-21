%include	/usr/lib/rpm/macros.perl
Summary:	help2man - automatic manual page generation
Summary(pl.UTF-8):	help2man - automatyczne generowanie stron manuala
Name:		help2man
Version:	1.40.7
Release:	1
License:	GPL v3+
Group:		Applications/Text
Source0:	http://ftp.debian.org/debian/pool/main/h/help2man/%{name}_%{version}.tar.gz
# Source0-md5:	8abef49b3cbbb1a7c599341d9ab1bd0f
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
help2man can re-arrange that output into something which resembles a
manual page.

%description -l pl.UTF-8
help2man to narzędzie do automatycznego generowania prostych stron
manuala na podstawie wyjścia z programu. Ten program ma za zadanie dać
autorom oprogramowania łatwy sposób na dołączanie stron manuala bez
opiekowania się nimi. Po wskazaniu programu, który daje w miarę
standardowe wyjście dla opcji --help i --version, help2man potrafi
przekształcić to wyjście na coś przypominającego stronę manuala.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-nls

%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README THANKS debian/changelog
%attr(755,root,root) %{_bindir}/help2man
%dir %{_libdir}/help2man
%attr(755,root,root) %{_libdir}/help2man/bindtextdomain.so
%{_infodir}/help2man.info*
%{_mandir}/man1/help2man.1*
%lang(de) %{_mandir}/de/man1/help2man.1*
%lang(el) %{_mandir}/el/man1/help2man.1*
%lang(eo) %{_mandir}/eo/man1/help2man.1*
%lang(fi) %{_mandir}/fi/man1/help2man.1*
%lang(fr) %{_mandir}/fr/man1/help2man.1*
%lang(it) %{_mandir}/it/man1/help2man.1*
%lang(ja) %{_mandir}/ja/man1/help2man.1*
%lang(pl) %{_mandir}/pl/man1/help2man.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/help2man.1*
%lang(ru) %{_mandir}/ru/man1/help2man.1*
%lang(sr) %{_mandir}/sr/man1/help2man.1*
%lang(sv) %{_mandir}/sv/man1/help2man.1*
%lang(uk) %{_mandir}/uk/man1/help2man.1*
%lang(vi) %{_mandir}/vi/man1/help2man.1*
