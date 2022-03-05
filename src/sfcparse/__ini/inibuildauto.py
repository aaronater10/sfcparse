# inibuildauto
#########################################################################################################
# Imports
from configparser import ConfigParser as __ConfigParser
from configparser import ExtendedInterpolation as __ExtendedInterpolation


#########################################################################################################
# Auto Build ini data
def inibuildauto(data: dict) -> __ConfigParser:
    """
    Auto converts python dict to ini data structure.

    Returns a ConfigParser obj with your data. Assign the output to var

    Enter correctly structured python dict to convert to ini.

    [Example Python dict]

    {
        'section1': python_dict,
        'section2': python_dict    
    }

    This is using the native configparser library shipped with the python standard libray. Using ConfigParser method
    with ExtendedInterpolation enabled by default. For more information on the configparser library, 
    visit: https://docs.python.org/3/library/configparser.html
    """
    __err_msg_syntax = f"inibuildauto - Structure of dict is incorrect: {repr(data)}"
    __err_msg_dict = f"inibuildauto - Invalid data, type, or nothing specified: {repr(data)}"

    if not isinstance(data, dict):
        raise TypeError(__err_msg_dict)

    # Auto Build INI data structure
    __ini_data = __ConfigParser(interpolation=__ExtendedInterpolation())

    try:
        for key,value in data.items():
            __ini_data[key] = value
        return __ini_data
    except AttributeError: raise SyntaxError(__err_msg_syntax)
