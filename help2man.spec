%include	/usr/lib/rpm/macros.perl
Summary:	help2man - automatic manual page generation
Summary(pl.UTF-8):   help2man - automatyczne generowanie stron manuala
Name:		help2man
Version:	1.36.4
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://ftp.debian.org/debian/pool/main/h/help2man/%{name}_%{version}.tar.gz
# Source0-md5:	d31a0a38c2ec71faa06723f6b8bd3076
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

%description -l pl.UTF-8
help2man to narzędzie do automatycznego generowania prostych stron
manuala na podstawie wyjścia z programu. Ten program ma za zadanie
dać autorom oprogramowania łatwy sposób na dołączanie stron manuala
bez opiekowania się nimi. Po wskazaniu programu, który daje w miarę
standardowe wyjście dla opcji --help i --version, help2man potrafi
przekształcić to wyjście na coś przypominającego stronę manuala.

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
%lang(fi) %{_mandir}/fi/man1/*.1*
%lang(fr) %{_mandir}/fr/man1/*.1*
%lang(pl) %{_mandir}/pl/man1/*.1*
%lang(sv) %{_mandir}/sv/man1/*.1*
