Summary:	Red Hat print filters, for use with the printtool
Summary(de):	Red-Hat-Druckfiltersystem
Summary(fr):	Système de filtres d'impression de Red Hat
Summary(pl):	Filtry dla drukarek, do u¿ytku z programem printtool
Summary(tr):	Red Hat yazýcý süzgeçleri
Name:		rhs-printfilters
Version:	1.73
Release:	1
License:	GPL
Group:		Applications/Publishing
Group(pl):	Aplikacje/Publikowanie
Source0:	%{name}-%{version}.tar.gz
Requires:	mpage >= 2.4
Requires:	LPRng
Requires:	ghostscript >= 5.10
Requires:	findutils >= 4.1-23
BuildRequires:	transfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The rhs-printfilters package contains a set of print filters which are
primarily meant to be used with the Red Hat printtool. These print
filters provide an easy way for users to handle printing numerous file
formats.

%description -l de
Das Red Hat-Druckfiltersystem verarbeitet auf einfache Weise das
Drucken vieler Dateiformate. Ist vor allem für die Verwendung mit dem
Druck-Tool von Red Hat gedacht.

%description -l fr
Les filtres d'impression RedHat offrent une maniére simple de gérer
l'impression de nombreux formats de fichiers. Ceci est surtout destiné
a être utilisé avec l'utilitaire RedHat printool.

#%description -l pl

%description -l tr
Red Hat tarafýndan geliþtirilen bu süzgeçler sayesinde deðiþik
formatlardaki belgelerin yazýcýya uygun olarak biçimlendirilebilir. Bu
süzgeçler Red Hat'in printtool yazýlýmý ile kullanýlmak üzere
geliþtirilmiþlerdir.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
    INSTALLBIN="install -m 775" \
    INSTALLDATA="install -m 644" \
    INSTALL_DIR=$RPM_BUILD_ROOT \
    install

gzip -9nf README CHANGES

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{_libdir}/rhs/rhs-printfilters
%config(noreplace) %{_libdir}/rhs/rhs-printfilters/printerdb
%attr(755,root,root) %{_libdir}/rhs/rhs-printfilters/asc-to-printer.fpi
%attr(755,root,root) %{_libdir}/rhs/rhs-printfilters/asc-to-ps.fpi
%attr(755,root,root) %{_libdir}/rhs/rhs-printfilters/master-filter
%attr(755,root,root) %{_libdir}/rhs/rhs-printfilters/ps-to-printer.fpi
%attr(755,root,root) %{_libdir}/rhs/rhs-printfilters/rpm-to-asc.fpi
%attr(755,root,root) %{_libdir}/rhs/rhs-printfilters/ncpprint
%attr(755,root,root) %{_libdir}/rhs/rhs-printfilters/smbprint
%attr(755,root,root) %{_libdir}/rhs/rhs-printfilters/directprint
%{_libdir}/rhs/rhs-printfilters/general.cfg.in
%{_libdir}/rhs/rhs-printfilters/postscript.cfg.in
%{_libdir}/rhs/rhs-printfilters/ppaprint
%{_libdir}/rhs/rhs-printfilters/testpage.asc
%{_libdir}/rhs/rhs-printfilters/testpage.ps
%{_libdir}/rhs/rhs-printfilters/testpage-a4.ps
%{_libdir}/rhs/rhs-printfilters/textonly.cfg.in
