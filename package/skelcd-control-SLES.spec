#
# spec file for package skelcd-control-SLES
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


######################################################################
#
# IMPORTANT: Please do not change the control file or this spec file
#   in build service directly, use
#   https://github.com/yast/skelcd-control-SLES repository
#
#   See https://github.com/yast/skelcd-control-SLES/blob/master/CONTRIBUTING.md
#   for more details.
#
######################################################################

Name:           skelcd-control-SLES
# xmllint (for validation)
BuildRequires:  libxml2-tools
# RNG validation schema
BuildRequires:  yast2-installation-control
Url:            https://github.com/yast/skelcd-control-SLES
AutoReqProv:    off
Version:        12.0.1
Release:        0
Summary:        SLES control file needed for installation
License:        MIT
Group:          Metapackages
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         %{name}-%{version}.tar.bz2

%description
SLES control file needed for installation

%prep

%setup -n %{name}-%{version}

%check
#
# Verify syntax
#
make -C control check

%install
#
# Add control file 
#
mkdir -p $RPM_BUILD_ROOT/CD1
install -m 644 control/control.SLES.xml $RPM_BUILD_ROOT/CD1/control.xml

%files
%defattr(644,root,root,755)
/CD1

%changelog
