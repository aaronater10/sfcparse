# jsonexportstr
#########################################################################################################
# Imports
import json as __json
from ..error import SfcparseError
from typing import Union

# Exception for Module
class _Jsonexportstr: 
    class jsonexportstr(SfcparseError): __module__ = SfcparseError.set_module_name()


#########################################################################################################
# Export json str
def jsonexportstr(data: Union[str, int, float, bool, list, dict, tuple, None], indent_level: int=4) -> str:
    """
    Exports multiple data types to json string

    Returns a str. Assign the output to var

    [Example Use]

    jsonexportstr(str | int | float | bool | list | dict | tuple | None, [optional] indent_level)

    This is using the native json library shipped with the python standard library. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html
    
    """
    try:
        # Export dict data to json string
        return __json.dumps(data, indent=indent_level)
    except TypeError as __err_msg: raise _Jsonexportstr.jsonexportstr(__err_msg, f'\nDATA:{data} \nINDENT_LEVEL:{indent_level}')
    except ValueError as __err_msg: raise _Jsonexportstr.jsonexportstr(__err_msg, f'\nDATA:{data} \nINDENT_LEVEL:{indent_level}')

