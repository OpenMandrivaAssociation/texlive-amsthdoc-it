Name:		texlive-amsthdoc-it
Version:	45662
Release:	2
Summary:	TeXLive amsthdoc-it package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsthdoc-it.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsthdoc-it.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive amsthdoc-it package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/amsthdoc-it/README
%doc %{_texmfdistdir}/doc/latex/amsthdoc-it/amsthdoc_it.pdf
%doc %{_texmfdistdir}/doc/latex/amsthdoc-it/amsthdoc_it.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
