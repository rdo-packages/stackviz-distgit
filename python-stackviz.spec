%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pname stackviz

%global common_desc \
A visualization utility to help analyze the performance of \
DevStack setup and Tempest executions

Name:           %{pname}
Version:        XXX
Release:        XXX
Summary:        Visualization utility

License:        ASL 2.0
URL:            http://git.openstack.org/cgit/openstack/%{pname}
Source0:        http://tarballs.openstack.org/%{name}/%{pname}-master.tar.gz

BuildArch:      noarch

BuildRequires:  git
BuildRequires:  python2-subunit
BuildRequires:  python-testrepository
BuildRequires:  python2-testtools
BuildRequires:  python2-subunit2sql
BuildRequires:  openstack-macros

# Test requirements

BuildRequires:  python-docutils
BuildRequires:  python2-sphinx
BuildRequires:  python2-oslotest
BuildRequires:  python2-openstackdocstheme

%description
%{common_desc}

%package -n     python2-%{pname}
Summary:        Tempest visualization utility
%{?python_provide:%python_provide python2-%{pname}}

Requires:       python2-subunit
Requires:       python-testrepository
Requires:       python2-testtools
Requires:       python2-subunit2sql

%description -n python2-%{pname}
%{common_desc}

%if 0%{?with_python3}
%package -n     python3-%{pname}
Summary:        Tempest visualization utility
%{?python_provide:%python_provide python3-%{pname}}

BuildRequires:  python3-subunit
BuildRequires:  python3-testrepository
BuildRequires:  python3-testtools
BuildRequires:  python3-subunit2sql

Requires:       python3-subunit
Requires:       python3-testrepository
Requires:       python3-testtools
Requires:       python3-subunit2sql

%description -n python3-%{pname}
%{common_desc}

%endif

%prep
%autosetup -n stackviz-%{upstream_version} -S git

%py_req_cleanup

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python3}
%py3_install
cp %{buildroot}/%{_bindir}/stackviz-export %{buildroot}/%{_bindir}/stackviz-export-3
ln -sf %{_bindir}/stackviz-export-3 %{buildroot}/%{_bindir}/stackviz-export-%{python3_version}
%endif

%py2_install
cp %{buildroot}/%{_bindir}/stackviz-export %{buildroot}/%{_bindir}/stackviz-export-2
ln -sf %{_bindir}/stackviz-export-2 %{buildroot}/%{_bindir}/stackviz-export-%{python2_version}

%check
%{__python2} setup.py test
%if 0%{?with_python3}
%{__python3} setup.py test
%endif

%files -n python2-%{pname}
%license LICENSE
%doc README.rst
%{_bindir}/stackviz-export
%{_bindir}/stackviz-export-2
%{_bindir}/stackviz-export-%{python2_version}
%{python2_sitelib}/stackviz
%{python2_sitelib}/stackviz*.egg-info

%if 0%{?with_python3}
%files -n python3-%{pname}
%license LICENSE
%doc README.rst
%{_bindir}/stackviz-export
%{_bindir}/stackviz-export-3
%{_bindir}/stackviz-export-%{python3_version}
%%{python3_sitelib}/stackviz
%{python3_sitelib}/stackviz*.egg-info

%endif

%changelog