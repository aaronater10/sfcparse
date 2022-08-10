# savefile
#########################################################################################################
# Imports
from ast import literal_eval as __literal_eval__
from os import path as __path
from typing import Any as _Any
from ..error import SfcparseError

# Exception for Module
class SaveFile(SfcparseError): __module__ = SfcparseError.set_module_name()

#########################################################################################################
# Save Data to File
def savefile():
    """
    savefile
    """
    pass