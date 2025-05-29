Summary: A utility which lists open files on a Linux/UNIX system
Name: lsof
Version: 4.99.4
Release: 1
License: zlib
Source0: %{name}-%{version}.tar.bz2
URL: https://github.com/sailfishos/lsof

%description
Lsof stands for LiSt Open Files, and it does just that: it lists
information about files that are open by the processes running on a
UNIX system.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
./Configure -n linux

make DEBUG="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
install -p -m 0755 lsof ${RPM_BUILD_ROOT}%{_sbindir}

%files
%{_sbindir}/lsof
# License is duplicated in a couple of files but no single file containing only that
%license 00README
