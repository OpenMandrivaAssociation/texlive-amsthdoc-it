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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Italian translation of amsthdoc: Using the amsthm package

