Name:		texlive-jupynotex
Version:	56715
Release:	1
Summary:	Include whole or partial Jupyter notebooks in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jupynotex
License:	apache2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jupynotex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jupynotex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a python3 script and a LaTeX .sty file
which can be used together to include Jupyter Notebooks (all of
them, or some specific cells) as part of a LaTeX document. It
will convert the Jupyter Notebook format to proper LaTeX so it
gets included seamlessly, supporting text, LaTeX, images, etc.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/jupynotex
%doc %{_texmfdistdir}/doc/latex/jupynotex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
