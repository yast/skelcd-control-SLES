#
# spec file for package yast2-installation-control-SLES
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


Name:           yast2-installation-control-SLES
Version:        3.1.0
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

Summary:        YaST2 - Control file for SLES
License:        GPL-2.0
Group:          System/YaST
Url:            https://github.com/yast/yast-installation-control-SLE

BuildRequires:  yast2-devtools >= 3.1.10

# RNG schema
BuildRequires:  yast2-installation-control

# xmllint for validation
BuildRequires:  libxml2-tools

# xsltproc for generating some XML files
BuildRequires:  libxslt-tools

# add SLES specific requirements for the installation-images here:
# Requires:       <nothing specific yet>

BuildArch:      noarch

%description
This package contains the control file SUSE Linux Enterprise Server (SLES) product.

%package -n yast2-installation-control-SLED
Summary:        YaST2 - Control file for SLED
Group:          System/YaST
# add SLED specific requirements for the installation-images here:
# Requires:       <nothing specific yet>

%description -n yast2-installation-control-SLED
This package contains the control file SUSE Linux Enterprise Desktop (SLED) product.

%package -n yast2-installation-control-SLES-for-VMware
Summary:        YaST2 - Control file for SLES-for-VMware
Group:          System/YaST
# add SLES-for-VMware specific requirements for the installation-images here:
# Requires:       <nothing specific yet>

%description -n yast2-installation-control-SLES-for-VMware
This package contains the control file SUSE Linux Enterprise Server for VMware
(SLES-for-VMware) product.

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install

%files
%defattr(-,root,root)
%yast_controldir/control.SLES.xml

%doc %{yast_docdir}

%files -n yast2-installation-control-SLED
%defattr(-,root,root)
%yast_controldir/control.SLED.xml

%files -n yast2-installation-control-SLES-for-VMware
%defattr(-,root,root)
%yast_controldir/control.SLES-for-VMware.xml

%changelog
