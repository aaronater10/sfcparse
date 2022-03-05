# jsonimportfile
#########################################################################################################
# Imports
from os import path as __path
import json as __json


#########################################################################################################
# Import json file
def jsonimportfile(filename: str) -> dict:
    """
    Imports json data from a file

    Returns a dict. Assign the output to var

    Enter json file location as str to import.

    [Example Use]

    jsonimportfile('path/to/filename.json')

    This is using the native json libray shipped with the python standard libray. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html
    """
    __err_msg = f"jsonimportfile - Invalid data imported, type, or nothing specified: {filename}"
    # Import json file    
    try:
        with open(filename, 'r') as f:
            # Check if file empty. Returns empty dict if empty
            if __path.getsize(filename) == 0:                
                raise SyntaxError(__err_msg)
            return __json.load(f)
    except FileNotFoundError: raise
    except OSError: raise OSError(__err_msg)
    except __json.decoder.JSONDecodeError: raise SyntaxError(__err_msg)
