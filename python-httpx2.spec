Name:		python-httpx2
Version:	2.13.1
Release:	2
Summary:	The next generation HTTP client
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/pydantic/httpx2
Source0:	https://files.pythonhosted.org/packages/source/h/httpx2/httpx2-%{version}.tar.gz
# uv-dynamic-versioning is not packaged. Without a git checkout the
# sdist would be stamped 0.0.0, and the readme hook points at a
# monorepo path that is not shipped in the sdist.
Patch0:		httpx2-static-version.patch
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)

%description
httpx2 is a fully featured HTTP client for Python, with sync and
async APIs. It is the Pydantic-maintained continuation of HTTPX.
The import name is httpx2, and this package installs alongside
python-httpx.

%files
%doc README.md CHANGELOG.md
%license LICENSE.md
%{_bindir}/httpx2
%{py_sitedir}/httpx2
%{py_sitedir}/httpx2-*.*-info
