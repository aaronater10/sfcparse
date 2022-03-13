# importrawfile
#########################################################################################################
# Imports
from os import path as __path
from ..error import SfcparseError

# Exception for Module
class _Importrawfile: 
    class importrawfile(SfcparseError): __module__ = SfcparseError.set_module_name()


#########################################################################################################
# Import raw data from file
def importrawfile(filename: str, byte_data: bool=False) -> str:
    """
    Imports any raw data from a file.

    Returns a str. Assign the output to var

    [Options]
    byte_data: Set to True if importing byte data

    [Example Use]

    importrawfile('path/to/filename')
    """
    # Validate file exists. Import File then return the raw data
    if not byte_data:
        try:
            with open(filename, 'r') as f:
                if __path.getsize(filename) == 0:
                    return ''
                return f.read()
        except FileNotFoundError as __err_msg: raise _Importrawfile.importrawfile(str(__err_msg))
    
    if byte_data:
        try:
            with open(filename, 'rb') as f:
                if __path.getsize(filename) == 0:
                    return b''
                return f.read()
        except FileNotFoundError as __err_msg: raise _Importrawfile.importrawfile(str(__err_msg))
