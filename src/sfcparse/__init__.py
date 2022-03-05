"""
Simple File Configuration Parse - by aaronater10
More info: https://github.com/aaronater10/sfcparse

Version 1.1.0

A simple library to import custom config/data files for your python program or script,
and export any data to disk simply!. Also contains a feature for easily formatting data
types for clean multiline output when exporting data to files.

Importing [Python types only]: returns a class with attributes from the file keeping python's natural
recognition of data types, including comments being ignored.

Exporting/Appending: it simply sends str data to a file. It may be used for any str data file output.

CleanFormat: simply formats any dict, list, set, or tuple to a clean multiline structure, and returned as str

Accepted Import Data Types: str, int, float, bool, list, dict, tuple, set, nonetype, bytes
"""
#########################################################################################################
# Imports

# Native Lib
from .__native.importfile import importfile
from .__native.importrawfile import importrawfile
from .__native.exportfile import exportfile
from .__native.appendfile import appendfile
from .__native.cleanformat import cleanformat

# Hash Lib
from .__hash.createfilehash import createfilehash
from .__hash.comparefilehash import comparefilehash

# JSON Lib
from .__json.jsonimportfile import jsonimportfile
from .__json.jsonimportstr import jsonimportstr
from .__json.jsonexportfile import jsonexportfile
from .__json.jsonexportstr import jsonexportstr

# YAML Lib
from .__yaml.yamlimportfile import yamlimportfile
from .__yaml.yamlexportfile import yamlexportfile

# INI Lib
from .__ini.iniimportfile import iniimportfile
from .__ini.iniexportfile import iniexportfile
from .__ini.inibuildauto import inibuildauto
from .__ini.inibuildmanual import inibuildmanual

# XML Lib
from .__xml.xmlimportfile import xmlimportfile
from .__xml.xmlimportstr import xmlimportstr
from .__xml.xmlexportfile import xmlexportfile
from .__xml.xmlexportstr import xmlexportstr
from .__xml.xmlbuildmanual import xmlbuildmanual
