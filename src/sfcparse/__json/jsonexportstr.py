# jsonexportstr
#########################################################################################################
# Imports
import json as __json


#########################################################################################################
# Export json str
def jsonexportstr(data: dict, indent_level: int=4) -> str:
    """
    Exports dictionary data to json string

    Returns a str. Assign the output to var

    [Example Use]

    jsonexportstr(dict, [optional] indent_level)

    This is using the native json libray shipped with the python standard libray. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html
    
    """
    __err_msg_int = f"jsonexportstr - Only int is allowed for indent_level: {repr(indent_level)}"
    __err_msg_dict = f"jsonexportstr - Only dict is allowed for data: {repr(data)}"

    if not isinstance(data, dict):
        raise TypeError(__err_msg_dict)

    if not isinstance(indent_level, int):
        raise TypeError(__err_msg_int)

    # Export dict data to json string
    return __json.dumps(data, indent=indent_level)
