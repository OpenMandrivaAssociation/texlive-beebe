%global tl_name beebe
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A collection of bibliographies
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/biblio
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beebe.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of BibTeX bibliographies on TeX-related topics (including,
for example, spell-checking and SGML). Each includes a LaTeX wrapper
file to typeset the bibliography.

%prep
%setup -q -c
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bib
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/bibtex/bib/beebe
%dir %{_datadir}/texmf-dist/tex/generic/beebe
%{_datadir}/texmf-dist/bibtex/bib/beebe/epodd.bib
%{_datadir}/texmf-dist/bibtex/bib/beebe/font.bib
%{_datadir}/texmf-dist/bibtex/bib/beebe/litprog.bib
%{_datadir}/texmf-dist/bibtex/bib/beebe/printing-history.bib
%{_datadir}/texmf-dist/bibtex/bib/beebe/serif.bib
%{_datadir}/texmf-dist/bibtex/bib/beebe/stanford-cstr.bib
%{_datadir}/texmf-dist/bibtex/bib/beebe/texbook1.bib
%{_datadir}/texmf-dist/bibtex/bib/beebe/texbook2.bib
%{_datadir}/texmf-dist/bibtex/bib/beebe/texbook3.bib
%{_datadir}/texmf-dist/bibtex/bib/beebe/texgraph.bib
%{_datadir}/texmf-dist/bibtex/bib/beebe/texjourn.bib
%{_datadir}/texmf-dist/bibtex/bib/beebe/texnique.bib
%{_datadir}/texmf-dist/bibtex/bib/beebe/tugboat.bib
%{_datadir}/texmf-dist/bibtex/bib/beebe/type.bib
%{_datadir}/texmf-dist/bibtex/bib/beebe/typeset.bib
%{_datadir}/texmf-dist/tex/generic/beebe/bibnames.sty
%{_datadir}/texmf-dist/tex/generic/beebe/texnames.sty
%{_datadir}/texmf-dist/tex/generic/beebe/tugboat.def
