# savefile
#########################################################################################################
# Imports
from ast import literal_eval as __literal_eval__
from os import path as __path
from typing import Union as __Union
from ..error import SfcparseError
from .importfile import SfcparseFileData as __SfcparseFileData
from .exportfile import exportfile as __exportfile
from .appendfile import appendfile as __appendfile
from .cleanformat import cleanformat as __cleanformat

# Exception for Module
class SaveFile(SfcparseError): __module__ = SfcparseError.set_module_name()

#########################################################################################################
# Save Data to File
def savefile(
    filename: str, 
    data: __Union['__SfcparseFileData', dict], 
    write_mode: str = 'w',
    indent_level: int = 1,
    indentation_on: bool = True
    ) -> None:
    """
    savefile
    """
    
    # Save Data to File
    __build_data_output = ""
    __assignment_operators = ('=', '$=', '==', '$==')
    __skip_object_key = '_SfcparseFileData'
    __locked_attr_list_key =  '_SfcparseFileData__assignment_locked_attribs'
    __reference_attr_list_key =  '_SfcparseFileData__assignment_reference_attribs'

    # Check if SfcparseFileData
    if isinstance(data, __SfcparseFileData):
        # Build Data
        for key,value in data.__dict__.items():
            if not key.startswith(__skip_object_key):
                # Check Operator Type and Build Accordingly

                # Reference Name and Locked
                if (key in data.__dict__[__reference_attr_list_key]) and (key in data.__dict__[__locked_attr_list_key]):
                    __build_data_output += f'{key} {__assignment_operators[3]} {data.__dict__[__reference_attr_list_key][key]}\n'
                    continue
                # Reference Name Only
                if key in data.__dict__[__reference_attr_list_key]:
                    __build_data_output += f'{key} {__assignment_operators[2]} {data.__dict__[__reference_attr_list_key][key]}\n'
                    continue
                # Locked Only
                if key in data.__dict__[__locked_attr_list_key]:
                    if __multiline_check(value) and indentation_on:
                        value = __cleanformat(value, indent_level)
                        __build_data_output += f'{key} {__assignment_operators[1]} {value}\n'
                    else: __build_data_output += f'{key} {__assignment_operators[1]} {repr(value)}\n'
                    continue
                # Normal Assignment
                if __multiline_check(value) and indentation_on:
                    value = __cleanformat(value, indent_level)
                    __build_data_output += f'{key} {__assignment_operators[0]} {value}\n'
                else: __build_data_output += f'{key} {__assignment_operators[0]} {repr(value)}\n'

        # Strip Last \n Char
        __build_data_output = __build_data_output[:-1]

        # Write New File Mode
        if write_mode == 'w':
            __exportfile(filename, __build_data_output)
        # Append Append File Mode
        if write_mode == 'a':
            __appendfile(filename, __build_data_output)

        return None

    # Check if dict
    if isinstance(data, dict):
        # Build Data
        for key,value in data.items():
            # Multline Assignment from Indentation
            if indentation_on:
                if __multiline_check(value):
                    value = __cleanformat(value, indent_level)
                    __build_data_output += f'{key} {__assignment_operators[0]} {value}\n'
                    continue
            # Single Line Assignment
            __build_data_output += f'{key} {__assignment_operators[0]} {repr(value)}\n'

        # Strip Last \n Char
        __build_data_output = __build_data_output[:-1]

        # Write New File Mode
        if write_mode == 'w':
            __exportfile(filename, __build_data_output)
        # Append Append File Mode
        if write_mode == 'a':
            __appendfile(filename, __build_data_output)

        return None

    # Report if required types not correct


# Functions
def __multiline_check(data: __Union[list, dict, tuple, set]) -> bool:
    if isinstance(data, list) \
    or isinstance(data, dict) \
    or isinstance(data, tuple) \
    or isinstance(data, set):
        return True
    return False

