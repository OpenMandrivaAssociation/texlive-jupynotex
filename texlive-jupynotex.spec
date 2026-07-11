%global tl_name jupynotex
%global tl_revision 75037

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Include whole or partial Jupyter notebooks in LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jupynotex
License:	apache2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jupynotex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jupynotex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a python3 script and a LaTeX .sty file which can
be used together to include Jupyter Notebooks (all of them, or some
specific cells) as part of a LaTeX document. It will convert the Jupyter
Notebook format to proper LaTeX so it gets included seamlessly,
supporting text, LaTeX, images, etc.

