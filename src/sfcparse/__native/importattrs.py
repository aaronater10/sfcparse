# importattrs
#########################################################################################################
# Imports
from ..error import SfcparseError
from .importfile import importfile as __importfile

# Exception for Module
class ImportAttrs(SfcparseError): __module__ = SfcparseError.set_module_name()

#########################################################################################################
# Import Attributes from File
class __SfcparseDummy:
    class Class: """dummy class for hinting"""

def importattrs(filename: str, class_object: '__SfcparseDummy.Class') -> None:
    """
    importattrs - done in-place
    """
    
    # Keys
    __skip_object_key = '_SfcparseFileData'

    # Import Attrs from File and Inject into Given Class Object
    __imported_data = __importfile(filename)
    for key,value in __imported_data.__dict__.items():
        if key.startswith(__skip_object_key): continue
        setattr(class_object, key, value)
    
    return None