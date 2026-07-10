%global tl_name amsthdoc-it
%global tl_revision 45662

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Italian translation of amsthdoc: Using the amsthm package
Group:		Publishing
URL:		https://www.ctan.org/pkg/amsthdoc-it
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amsthdoc-it.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amsthdoc-it.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Italian translation of amsthdoc: Using the amsthm package

%prep
%setup -q -c -a1
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
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/doc/latex/amsthdoc-it
%doc %{_datadir}/texmf-dist/doc/latex/amsthdoc-it/README
%doc %{_datadir}/texmf-dist/doc/latex/amsthdoc-it/amsthdoc_it.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsthdoc-it/amsthdoc_it.tex
