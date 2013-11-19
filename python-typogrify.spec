%define		module	typogrify

Summary:	Typography related template filters for Django & Jinja2 applications
Name:		python-%{module}
Version:	2.0.0
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/t/typogrify/%{module}-%{version}.tar.gz
# Source0-md5:	ef4dc943e947ff57814bcda8d259a3f0
URL:		https://github.com/mintchaos/typogrify
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Typography related template filters for Django & Jinja2 applications.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/*.egg-info

