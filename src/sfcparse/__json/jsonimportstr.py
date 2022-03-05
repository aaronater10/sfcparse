# jsonimportstr
#########################################################################################################
# Imports
import json as __json


#########################################################################################################
# Import json string
def jsonimportstr(json_str_data: str) -> dict:
    """
    Imports json data from a string

    Returns a dict. Assign the output to var

    Enter json string as str to import.

    [Example Use]

    jsonimportstr('string with json data')

    This is using the native json libray shipped with the python standard libray. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html
    """
    __err_msg = f"jsonimportstr - Invalid data imported, type, or nothing specified: {json_str_data}"    

    # Import json string    
    try:
        return __json.loads(json_str_data)
    except __json.decoder.JSONDecodeError: raise SyntaxError(__err_msg)
