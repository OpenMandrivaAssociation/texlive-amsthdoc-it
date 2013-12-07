# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-amsthdoc-it
Version:	20111103
Release:	6
Summary:	TeXLive amsthdoc-it package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsthdoc-it.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsthdoc-it.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 749247
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 717829
- texlive-amsthdoc-it
- texlive-amsthdoc-it
- texlive-amsthdoc-it
- texlive-amsthdoc-it

