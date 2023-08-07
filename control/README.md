Control file validation:
------------------------

Run command

    xmllint --noout --relaxng /usr/share/YaST2/control/control.rng *.xml

or simply

    make check



Control file location
---------------------

This package contains only the diff to the common files.

For the main control file, see
https://github.com/yast/skelcd-control-leanos/tree/master/control
