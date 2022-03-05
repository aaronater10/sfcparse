# jsonexportfile
#########################################################################################################
# Imports
import json as __json


#########################################################################################################
# Export json file
def jsonexportfile(filename: str, data: dict) -> None:
    """
    Exports a new file from a dictionary to json data.
    
    Enter new filename as str. Pass dict data for output to file
    
    [Example Use]

    jsonexportfile('path/to/filename.json', data)    

    This is using the native json libray shipped with the python standard libray. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html
    
    """
    __err_msg_dict = f"jsonexportfile - Only dict is allowed for data: {repr(data)}"
    __err_msg_str = f"jsonexportfile - Only str is allowed for filename: {filename}"

    if not isinstance(filename, str):
        raise TypeError(__err_msg_str)

    if not isinstance(data, dict):
        raise TypeError(__err_msg_dict)

    # Export dict data to json file
    with open(filename, 'w') as f:
        __json.dump(data, f)
