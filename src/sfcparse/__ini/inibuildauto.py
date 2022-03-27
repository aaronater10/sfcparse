# inibuildauto
#########################################################################################################
# Imports
from configparser import ConfigParser as __ConfigParser
from configparser import ExtendedInterpolation as __ExtendedInterpolation
from ..error import SfcparseError

# Exception for Module
class _Inilimportfile: 
    class iniimportfile(SfcparseError): __module__ = SfcparseError.set_module_name()


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
    # Auto Build INI data structure
    __ini_data = __ConfigParser(interpolation=__ExtendedInterpolation())

    try:
        for section,dict_value in data.items():
            bad_value = [v for _,v in dict_value.items()]
            __ini_data[section] = dict_value
        return __ini_data
    except AttributeError as __err_msg: raise _Inilimportfile.iniimportfile(f'{__err_msg} - Please send correct dict structure', f'\nDATA:{data}')
    except TypeError as __err_msg: raise _Inilimportfile.iniimportfile(__err_msg, f'\nDATA:{data} \nBAD_VALUE: {bad_value[0]}')
