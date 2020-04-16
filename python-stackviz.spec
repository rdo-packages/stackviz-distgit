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
Source0:        http://tarballs.openstack.org/%{name}/%{pname}-%{upstream_version}.tar.gz

BuildArch:      noarch

BuildRequires:  git
BuildRequires:  python3-subunit
BuildRequires:  python3-docutils
BuildRequires:  python3-stestr
BuildRequires:  python3-testrepository
BuildRequires:  python3-testtools
BuildRequires:  python3-subunit2sql
BuildRequires:  openstack-macros

# Test requirements

BuildRequires:  python3-sphinx
BuildRequires:  python3-oslotest
BuildRequires:  python3-openstackdocstheme

%description
%{common_desc}

%package -n     python3-%{pname}
Summary:        Tempest visualization utility
%{?python_provide:%python_provide python3-%{pname}}

Requires:       python3-six
Requires:       python3-subunit
Requires:       python3-stestr
Requires:       python3-testrepository
Requires:       python3-testtools
Requires:       python3-subunit2sql

%description -n python3-%{pname}
%{common_desc}

%prep
%autosetup -n stackviz-%{upstream_version} -S git

%py_req_cleanup

%build
%{py3_build}

%install

%{py3_install}

%check
%if 3 > 2
export PYTHON=/usr/bin/python3
%endif

stestr-3 run

%files -n python3-%{pname}
%license LICENSE
%doc README.rst
%{_bindir}/stackviz-export
%{python3_sitelib}/stackviz
%{python3_sitelib}/stackviz*.egg-info

%changelog
