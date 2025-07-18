Summary:	help2man - automatic manual page generation
Summary(pl.UTF-8):	help2man - automatyczne generowanie stron manuala
Name:		help2man
Version:	1.49.3
Release:	1
License:	GPL v3+
Group:		Applications/Text
Source0:	http://ftp.debian.org/debian/pool/main/h/help2man/%{name}_%{version}.tar.xz
# Source0-md5:	2a0ffaa1822df5b6971f486a4fe1a4d1
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/help2man/
BuildRequires:	gettext-tools
BuildRequires:	perl-base >= 1:5.8
BuildRequires:	perl-Locale-gettext
BuildRequires:	po4a
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRequires:	xz
Requires:	perl-base >= 1:5.8
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
%patch -P0 -p1

# completeness percentage is too low (as of 1.49.3)
%{__rm} po-texi/zh_CN.po

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
%lang(de) %{_infodir}/help2man-de.info*
%lang(es) %{_infodir}/help2man-es.info*
%lang(fr) %{_infodir}/help2man-fr.info*
%lang(pl) %{_infodir}/help2man-pl.info*
%lang(pt_BR) %{_infodir}/help2man-pt_BR.info*
%lang(ro) %{_infodir}/help2man-ro.info*
%lang(sr) %{_infodir}/help2man-sr.info*
%lang(sv) %{_infodir}/help2man-sv.info*
%lang(uk) %{_infodir}/help2man-uk.info*
#%lang(zh_CN) %{_infodir}/help2man-zh_CN.info*
%{_mandir}/man1/help2man.1*
%lang(da) %{_mandir}/da/man1/help2man.1*
%lang(de) %{_mandir}/de/man1/help2man.1*
%lang(el) %{_mandir}/el/man1/help2man.1*
%lang(eo) %{_mandir}/eo/man1/help2man.1*
%lang(es) %{_mandir}/es/man1/help2man.1*
%lang(fi) %{_mandir}/fi/man1/help2man.1*
%lang(fr) %{_mandir}/fr/man1/help2man.1*
%lang(hr) %{_mandir}/hr/man1/help2man.1*
%lang(hu) %{_mandir}/hu/man1/help2man.1*
%lang(it) %{_mandir}/it/man1/help2man.1*
%lang(ja) %{_mandir}/ja/man1/help2man.1*
%lang(ko) %{_mandir}/ko/man1/help2man.1*
%lang(nb) %{_mandir}/nb/man1/help2man.1*
%lang(pl) %{_mandir}/pl/man1/help2man.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/help2man.1*
%lang(ro) %{_mandir}/ro/man1/help2man.1*
%lang(ru) %{_mandir}/ru/man1/help2man.1*
%lang(sr) %{_mandir}/sr/man1/help2man.1*
%lang(sv) %{_mandir}/sv/man1/help2man.1*
%lang(ta) %{_mandir}/ta/man1/help2man.1*
%lang(uk) %{_mandir}/uk/man1/help2man.1*
%lang(vi) %{_mandir}/vi/man1/help2man.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/help2man.1*
