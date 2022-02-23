%define module sphinxcontrib-websupport

Summary:	Web support for the Sphinx documentation generator
Name:		python-%{module}
Version:	1.2.4
Release:	3
Source0:	https://github.com/sphinx-doc/%{module}/archive/%{module}-%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		http://sphinx-doc.org/
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
Obsoletes:	python2-%{module} < 1.2.4-2

%description
Web support for the Sphinx documentation generator.

%prep
%autosetup -n %{module}-%{version} -p1

%install
PYTHONDONTWRITEBYTECODE=1 python setup.py install --root=%{buildroot}

%files
%{py_puresitedir}/sphinxcontrib*
