Name:		texlive-expkv-def
Version:	61796
Release:	2
Summary:	A key-defining frontend for expkv
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/expkv-def
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expkv-def.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expkv-def.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expkv-def.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a key=val interface to define keys for
expkv. This is done to provide a simple frontend to define
different common key types, similar to how keys are defined in
other well established key=value packages like pgfkeys or
l3keys. expkv-def is generic code and only requires expkv for
its parsing. There is a LaTeX package expkv-def.sty included to
play nicely on LaTeX's package loading system, but that package
is not needed and does not provide more functionality than the
generic code in expkv-def.tex.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/expkv-def
%{_texmfdistdir}/tex/latex/expkv-def
%{_texmfdistdir}/tex/generic/expkv-def
%{_texmfdistdir}/tex/context/third/expkv-def
%doc %{_texmfdistdir}/doc/latex/expkv-def

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
