# savefile
#########################################################################################################
# Imports
from ast import literal_eval as __literal_eval__
from os import path as __path
from typing import Union as __Union
from ..error import SfcparseError
from .importfile import SfcparseFileData as __SfcparseFileData

# Exception for Module
class SaveFile(SfcparseError): __module__ = SfcparseError.set_module_name()

#########################################################################################################
# Save Data to File
def savefile(filename: str, data: __Union['__SfcparseFileData', dict]) -> None:
    """
    savefile
    """
    pass