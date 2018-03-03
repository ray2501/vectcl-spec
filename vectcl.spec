%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          vectcl
Summary:       A numerical array extension for Tcl
Version:       0.2
Release:       1
License:       TCL
Group:         Development/Libraries/Tcl
Source:        VecTcl-%{version}.tar.gz
Patch0:        makefile.patch
URL:           https://github.com/auriocus/tksvg
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel
Requires:      tcl
BuildRoot:     %{buildroot}

%description
This package provides a numerical array extension for Tcl with
support for vectors, matrices and higher-rank tensors of integers,
floating point and complex numbers. It has builtin support for
basic array shaping, slicing and linear algebra subroutines and
is designed to integrate seamlessly with Tcl.

%package devel
Summary:        Development package for VecTcl
Group:          Development/Libraries/Tcl
Requires:       %{name} = %version

%description devel
This package provides a numerical array extension for Tcl with
support for vectors, matrices and higher-rank tensors of integers,
floating point and complex numbers. It has builtin support for
basic array shaping, slicing and linear algebra subroutines and
is designed to integrate seamlessly with Tcl.
 
This package contains development files for VecTcl.

%prep
%setup -q -n VecTcl-%{version}
%patch0

%build
%{__autoconf}
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib} \
%ifarch x86_64
	--enable-64bit=yes \
%endif
	--with-tcl=%{directory}/%{_lib}
make 

%install
make DESTDIR=%{buildroot} pkglibdir=%tcl_noarchdir/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
/usr/lib64/libvectcl0.2.so
%tcl_noarchdir/%{name}%{version}

%files devel
%defattr(-,root,root)
/usr/lib64/vectclConfig.sh
/usr/lib64/libvectclstub0.2.a
/usr/include/hsfft.h
/usr/include/nacomplex.h
/usr/include/vectcl.h

