#!/usr/bin/tclsh

set arch "x86_64"
set base "VecTcl-0.3"
set fileurl "https://github.com/auriocus/VecTcl/archive/v0.3.tar.gz"

set var [list wget2 $fileurl -O $base.tar.gz]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES
file copy -force makefile.patch build/SOURCES
file copy -force intconv.h.patch build/SOURCES
file copy -force configure.in.patch build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb vectcl.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force $base.tar.gz
