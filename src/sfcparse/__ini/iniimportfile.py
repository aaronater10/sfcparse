# iniimportfile
#########################################################################################################
# Imports
from configparser import ConfigParser as __ConfigParser
from configparser import ExtendedInterpolation as __ExtendedInterpolation


#########################################################################################################
# Import ini file
def iniimportfile(filename: str) -> __ConfigParser:
    """
    Imports ini data from a file.

    Returns a ConfigParser obj. Assign the output to var

    Enter ini file location as str to import.

    [Example Use]

    iniimportfile('path/to/filename.ini')

    This is using the native configparser library shipped with the python standard libray. Using ConfigParser method
    with ExtendedInterpolation enabled by default. For more information on the configparser library, 
    visit: https://docs.python.org/3/library/configparser.html
    """
    __err_msg_str = f"iniimportfile - Only str is allowed for filename: {filename}"

    if not isinstance(filename, str):
        raise TypeError(__err_msg_str)

    __parser = __ConfigParser(interpolation=__ExtendedInterpolation())
    __parser.read(filename)
    return __parser
