# revision 33039
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-beebe
Version:	20140317
Release:	2
Summary:	TeXLive beebe package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beebe.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive beebe package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/beebe/gut.bib
%{_texmfdistdir}/bibtex/bib/beebe/komoedie.bib
%{_texmfdistdir}/bibtex/bib/beebe/texbook1.bib
%{_texmfdistdir}/bibtex/bib/beebe/texbook2.bib
%{_texmfdistdir}/bibtex/bib/beebe/texbook3.bib
%{_texmfdistdir}/bibtex/bib/beebe/texgraph.bib
%{_texmfdistdir}/bibtex/bib/beebe/texjourn.bib
%{_texmfdistdir}/bibtex/bib/beebe/texnique.bib
%{_texmfdistdir}/bibtex/bib/beebe/tugboat.bib
%{_texmfdistdir}/bibtex/bst/beebe/aaai-named.bst
%{_texmfdistdir}/bibtex/bst/beebe/abstract.bst
%{_texmfdistdir}/bibtex/bst/beebe/annotate.bst
%{_texmfdistdir}/bibtex/bst/beebe/annotation.bst
%{_texmfdistdir}/bibtex/bst/beebe/apa.bst
%{_texmfdistdir}/bibtex/bst/beebe/apalike2.bst
%{_texmfdistdir}/bibtex/bst/beebe/astron.bst
%{_texmfdistdir}/bibtex/bst/beebe/authordate1.bst
%{_texmfdistdir}/bibtex/bst/beebe/authordate2.bst
%{_texmfdistdir}/bibtex/bst/beebe/authordate3.bst
%{_texmfdistdir}/bibtex/bst/beebe/authordate4.bst
%{_texmfdistdir}/bibtex/bst/beebe/bbs.bst
%{_texmfdistdir}/bibtex/bst/beebe/bibtoref.bst
%{_texmfdistdir}/bibtex/bst/beebe/cbe.bst
%{_texmfdistdir}/bibtex/bst/beebe/chicagoa.bst
%{_texmfdistdir}/bibtex/bst/beebe/humanbio.bst
%{_texmfdistdir}/bibtex/bst/beebe/humannat.bst
%{_texmfdistdir}/bibtex/bst/beebe/is-abbrv.bst
%{_texmfdistdir}/bibtex/bst/beebe/is-alpha.bst
%{_texmfdistdir}/bibtex/bst/beebe/is-plain.bst
%{_texmfdistdir}/bibtex/bst/beebe/is-unsrt.bst
%{_texmfdistdir}/bibtex/bst/beebe/jas99.bst
%{_texmfdistdir}/bibtex/bst/beebe/jbact.bst
%{_texmfdistdir}/bibtex/bst/beebe/jmb.bst
%{_texmfdistdir}/bibtex/bst/beebe/jtb.bst
%{_texmfdistdir}/bibtex/bst/beebe/jthcarsu.bst
%{_texmfdistdir}/bibtex/bst/beebe/named.bst
%{_texmfdistdir}/bibtex/bst/beebe/namunsrt.bst
%{_texmfdistdir}/bibtex/bst/beebe/nar.bst
%{_texmfdistdir}/bibtex/bst/beebe/newapa.bst
%{_texmfdistdir}/bibtex/bst/beebe/phaip.bst
%{_texmfdistdir}/bibtex/bst/beebe/phapalik.bst
%{_texmfdistdir}/bibtex/bst/beebe/phcpc.bst
%{_texmfdistdir}/bibtex/bst/beebe/phiaea.bst
%{_texmfdistdir}/bibtex/bst/beebe/phjcp.bst
%{_texmfdistdir}/bibtex/bst/beebe/phnf.bst
%{_texmfdistdir}/bibtex/bst/beebe/phnflet.bst
%{_texmfdistdir}/bibtex/bst/beebe/phpf.bst
%{_texmfdistdir}/bibtex/bst/beebe/phppcf.bst
%{_texmfdistdir}/bibtex/bst/beebe/phreport.bst
%{_texmfdistdir}/bibtex/bst/beebe/phrmp.bst
%{_texmfdistdir}/bibtex/bst/beebe/plainyr.bst
%{_texmfdistdir}/bibtex/bst/beebe/refer.bst
%{_texmfdistdir}/bibtex/bst/beebe/xbtxbst.doc
%{_texmfdistdir}/tex/generic/beebe/bibnames.sty
%{_texmfdistdir}/tex/generic/beebe/texnames.sty
%{_texmfdistdir}/tex/generic/beebe/tugboat.def

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex %{buildroot}%{_texmfdistdir}
