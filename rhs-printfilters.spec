Summary:	Red Hat print filters, for use with the printtool
Summary(pl):	Filtry do drukarek z Red Hata, do u¿ytku z printtoolem
Summary(es):	Sistema de filtro de impresión Red Hat
Summary(pt_BR):	Sistema de filtro de impressão Red Hat
Name:		rhs-printfilters
Version:	1.81
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	fe4b738a1386906eab8ab955fa90558e
BuildRequires:	transfig
Requires:	mpage >= 2.4
Requires:	LPRng
Requires:	ghostscript >= 5.10
Requires:	findutils >= 4.1-23
Requires:	diffutils
Requires:	sed
Requires:	fileutils
Conflicts:	libgr-progs < 2.0.9-7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The rhs-printfilters package contains a set of print filters which are
primarily meant to be used with the Red Hat printtool. These print
filters provide an easy way for users to handle printing numerous file
formats.

%description -l es
El sistema de filtros de impresión Red Hat nos ofrece una manera fácil
de manipular la impresión de varios formatos de archivos. Se lo hizo,
primeramente, para ser usado en conjunto con el RedHat printtool.

%description -l pl
Pakiet rhs-printfilters zawiera zestaw filtrów do drukowania
przeznaczonych g³ównie do u¿ytku z redhatowym printtoolem. Te filtry
daj± ³atwy dla u¿ytkowników sposób obs³ugi wydruków plików w ró¿nych
formatach.

%description -l pt_BR
O sistema de filtros de impressão Red Hat oferece uma maneira fácil de
manipular a impressão de vários formatos de arquivos. Feito
primariamente para ser usado em conjunto com o RedHat printtool.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d INSTALL_DIR=$RPM_BUILD_ROOT%{_libdir}/rhs/rhs-printfilters
%{__make} INSTALLBIN="install -m0755" INSTALLDATA="install -m0644" \
	INSTALL_DIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%pre
PRINTCAP='/etc/printcap'
MASTER_FILTER='/usr/lib/rhs/rhs-printfilters/master-filter'
if [ -f $PRINTCAP ] && [ -f $MASTER_FILTER ]
then
	cat $PRINTCAP | (
	while read -r line;
	do
		if echo ${line} | grep -q -E -e '^[^#]{0}[[:space:]]*:if='
		then
			FILTER=`echo ${line} | sed -e 's/^:if=//; s/:.*//'`
			if diff $MASTER_FILTER $FILTER > /dev/null
			then
				rm -f $FILTER
				ln -s $MASTER_FILTER $FILTER
			fi
		fi
	done
	)
fi

%files
%defattr(644,root,root,755)
%doc README CHANGES
%dir %{_libdir}/rhs/rhs-printfilters
%{_libdir}/rhs/rhs-printfilters/asc-to-printer.fpi
%{_libdir}/rhs/rhs-printfilters/asc-to-ps.fpi
%{_libdir}/rhs/rhs-printfilters/general.cfg.in
%{_libdir}/rhs/rhs-printfilters/master-filter
%{_libdir}/rhs/rhs-printfilters/postscript.cfg.in
%config(noreplace) %{_libdir}/rhs/rhs-printfilters/printerdb
%{_libdir}/rhs/rhs-printfilters/ps-to-printer.fpi
%{_libdir}/rhs/rhs-printfilters/rpm-to-asc.fpi
%{_libdir}/rhs/rhs-printfilters/ncpprint
%{_libdir}/rhs/rhs-printfilters/ppaprint
%{_libdir}/rhs/rhs-printfilters/smbprint
%{_libdir}/rhs/rhs-printfilters/directprint
%{_libdir}/rhs/rhs-printfilters/testpage.asc
%{_libdir}/rhs/rhs-printfilters/testpage.ps
%{_libdir}/rhs/rhs-printfilters/testpage-a4.ps
%{_libdir}/rhs/rhs-printfilters/textonly.cfg.in
