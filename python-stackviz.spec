# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pname stackviz

%global common_desc \
A visualization utility to help analyze the performance of \
DevStack setup and Tempest executions

Name:           python-%{pname}
Version:        XXX
Release:        XXX
Summary:        Visualization utility

License:        ASL 2.0
URL:            http://git.openstack.org/cgit/openstack/%{pname}
Source0:        http://tarballs.openstack.org/%{name}/%{pname}-master.tar.gz

BuildArch:      noarch

BuildRequires:  git
BuildRequires:  python%{pyver}-subunit
%if %{pyver} == 2
BuildRequires:  python-testrepository
BuildRequires:  python-docutils
%else
BuildRequires:  python%{pyver}-testrepository
BuildRequires:  python%{pyver}-docutils
%endif
BuildRequires:  python%{pyver}-testtools
BuildRequires:  python%{pyver}-subunit2sql
BuildRequires:  openstack-macros

# Test requirements

BuildRequires:  python%{pyver}-sphinx
BuildRequires:  python%{pyver}-oslotest
BuildRequires:  python%{pyver}-openstackdocstheme

%description
%{common_desc}

%package -n     python%{pyver}-%{pname}
Summary:        Tempest visualization utility
%{?python_provide:%python_provide python%{pyver}-%{pname}}

Requires:       python%{pyver}-subunit
%if %{pyver} == 2
Requires:       python-testrepository
%else
Requires:       python%{pyver}-testrepository
%endif
Requires:       python%{pyver}-testtools
Requires:       python%{pyver}-subunit2sql

%description -n python%{pyver}-%{pname}
%{common_desc}

%prep
%autosetup -n stackviz-%{upstream_version} -S git

%py_req_cleanup

%build
%{pyver_build}

%install

%{pyver_install}

%check
%if %{pyver} == %{python3_pkgversion}
export PYTHON=/usr/bin/python3
%endif
%{pyver_bin} setup.py test

%files -n python%{pyver}-%{pname}
%license LICENSE
%doc README.rst
%{_bindir}/stackviz-export
%{pyver_sitelib}/stackviz
%{pyver_sitelib}/stackviz*.egg-info

%changelog
