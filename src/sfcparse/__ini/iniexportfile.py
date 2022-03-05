# iniexportfile
#########################################################################################################
# Imports
from configparser import ConfigParser as __ConfigParser


#########################################################################################################
# Export ini file

# Create hollow reference name for "ini_data" to denote ini data needs to be exported for hinting exports
class __dummy_ini:
    """Not meant to be used"""
    class ini_data:
        """Not meant to be used"""

def iniexportfile(filename: str, data: __dummy_ini.ini_data) -> None:
    """
    Exports a new file from a ini data (ConfigParser) obj
    
    Enter new filename as str. Pass ini data for output to file
    
    [Example Use]

    iniexportfile('path/to/filename.ini', data)

    This is using the native configparser library shipped with the python standard libray. Using ConfigParser method.
    For more information on the configparser library, visit: https://docs.python.org/3/library/configparser.html
    """
    __err_msg_parser = f"iniexportfile - Invalid data to export, type, or nothing specified: {filename}"
    __err_msg_str = f"iniexportfile - Only str is allowed for filename: {filename}"

    if not isinstance(filename, str):
        raise TypeError(__err_msg_str)
        
    if isinstance(data, __ConfigParser):
        with open(filename, 'w') as f:
            data.write(f)
        return None
    
    raise TypeError(__err_msg_parser)
