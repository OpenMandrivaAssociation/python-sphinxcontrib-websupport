%define module sphinxcontrib_websupport

Summary:	Web support for the Sphinx documentation generator
Name:		python-%{module}
Version:	2.0.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		https://sphinx-doc.org/
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
Obsoletes:	python2-%{module} < 1.2.4-2

# rename for hyphenated package name
%rename python-sphinxcontrib-websupport

%description
Web support for the Sphinx documentation generator.

%files
%{py_puresitedir}/sphinxcontrib*
