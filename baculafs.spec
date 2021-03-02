%define		pypi_name	BaculaFS
Summary:	Exposes the Bacula catalog and storage as a Filesystem in USErspace
Name:		baculafs
Version:	0.1.7
Release:	2
License:	GPL v3+
Group:		Networking/Utilities
Source0:	https://pypi.python.org/packages/source/B/BaculaFS/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	50dcca4d11eeaa98fe0382dfd58243db
URL:		https://code.google.com/p/baculafs/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python >= 1:2.6.6
BuildRequires:	python-fuse >= 0.2.1
BuildRequires:	python-pexpect >= 2.3
Requires:	attr >= 2.4.44
Requires:	bacula-sd
Requires:	libfuse >= 2.8.4
Requires:	python >= 1:2.6.6
Requires:	python-MySQLdb >= 1.2.2
Requires:	python-fuse >= 0.2.1
Requires:	python-pexpect >= 2.3-7
Requires:	python-psycopg2 >= 2.0.13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BaculaFS is a tool, developed independently of Bacula, that represents
the Bacula catalog and backup storage media as a read-only filesystem
in userspace.

BaculaFS is specifically designed to cater for the following
use-cases:
- maintaining a remote snapshot of the files in the backup storage
  using rsync or duplicity
- auditing the contents of backup jobs, without resorting to SQL
  queries
- comparing backup jobs (using several mount points)

Note that BaculaFS is a maintenance tool - its operation may interfere
with the normal operation of a live Bacula setup.

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
%{__rm} -r %{pypi_name}.egg-info

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/baculafs
%dir %{py_sitescriptdir}/baculafs
%{py_sitescriptdir}/baculafs/*.py[co]
%{py_sitescriptdir}/BaculaFS-%{version}-py*.egg-info
