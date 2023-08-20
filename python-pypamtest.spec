Summary:	PamTest module for Python 2.x
Summary(pl.UTF-8):	Moduł PamTest dla Pythona 2.x
Name:		python-pypamtest
# 1.1.4 is the last pam_wrapper version with python2 support; newer versions in pam_wrapper.spec
Version:	1.1.4
Release:	2
License:	GPL v3+
Group:		Libraries
Source0:	https://www.samba.org/ftp/cwrap/pam_wrapper-%{version}.tar.gz
# Source0-md5:	c54539f0506cf6f1caa5a93847908dd6
URL:		https://cwrap.org/pam_wrapper.html
BuildRequires:	cmake >= 3.5.0
# for tests
#BuildRequires:	cmocka-devel
BuildRequires:	pam-devel
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	pam_wrapper >= %{version}
Requires:	python-libs >= 1:2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PamTest module for Python 2.x.

%description -l pl.UTF-8
Moduł PamTest dla Pythona 2.x.

%prep
%setup -q -n pam_wrapper-%{version}

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# package only python 2 module
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.so* \
	$RPM_BUILD_ROOT%{_includedir}/libpamtest.h \
	$RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc \
	$RPM_BUILD_ROOT%{_mandir}/man[18]/*

%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/pam_wrapper \
	$RPM_BUILD_ROOT%{_libdir}/cmake/{pam_wrapper,pamtest}
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README.md
%attr(755,root,root) %{py_sitedir}/pypamtest.so
