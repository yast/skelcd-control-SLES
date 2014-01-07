# Makefile.am for yast2-installation-control-SLE/control
#

control_DATA = \
	control.SLED.xml \
	control.SLES.xml \
	control.SLES-for-VMware.xml

CLEANFILES = control.SLES-for-VMware.xml

# generate the control.SLES-for-VMware.xml control file
control.SLES-for-VMware.xml: control.SLES-for-VMware.xsl control.SLES.xml
	xsltproc control.SLES-for-VMware.xsl control.SLES.xml > control.SLES-for-VMware.xml

EXTRA_DIST = $(control_DATA)

include $(top_srcdir)/Makefile.am.common

# checks only those control files that belong to this package
check-local: $(control_DATA)
	xmllint --relaxng /usr/share/YaST2/control/control.rng --noout $(control_DATA)
