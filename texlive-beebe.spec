%global tl_name beebe
%global tl_revision 79891

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A collection of bibliographies
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/biblio
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beebe.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of BibTeX bibliographies on TeX-related topics (including,
for example, spell-checking and SGML). Each includes a LaTeX wrapper
file to typeset the bibliography.

