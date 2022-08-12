# savefile
#########################################################################################################
# Imports
from ast import literal_eval as __literal_eval__
from typing import Union as __Union
from typing import Any as __Any
from ..error import SaveFile, ExportFile, AppendFile
from .importfile import SfcparseFileData as __SfcparseFileData
from .exportfile import exportfile as __exportfile
from .appendfile import appendfile as __appendfile
from .cleanformat import cleanformat as __cleanformat

#########################################################################################################
# Save Data to File
class __SfcparseDummy:
    class Class: """dummy class for hinting"""

def savefile(
    filename: str, 
    data: __Union['__SfcparseFileData', dict, '__SfcparseDummy.Class'], 
    write_mode: str = 'w',
    indent_level: int = 1,
    indentation_on: bool = True
    ) -> None:
    """
    savefile
    """
    # Error Checks
    __err_msg_general_error = "Error has occurred and cannot proceed"
    __err_msg_type_str_filename = "Only str is allowed for filename"
    __err_msg_type_str_write_mode = "Only str is allowed for write_mode"
    __err_msg_type_int_indent_level = "Only int is allowed for indent_level"
    __err_msg_type_bool_indentation_on = "Only bool is allowed for indentation_on"

    if not isinstance(filename, str): raise SaveFile(__err_msg_type_str_filename, f'\nFILE: "{filename}"')
    if not isinstance(write_mode, str): raise SaveFile(__err_msg_type_str_write_mode, f'\nFILE: "{filename}" \nDATA: {write_mode}')
    if not isinstance(indent_level, int): raise SaveFile(__err_msg_type_int_indent_level, f'\nFILE: "{filename}" \nDATA: {indent_level}')
    if not isinstance(indentation_on, bool): raise SaveFile(__err_msg_type_bool_indentation_on, f'\nFILE: "{filename}" \nDATA: {indentation_on}')


    # Save Data to File
    __build_data_output = ""
    __assignment_operators = ('=', '$=', '==', '$==')
    __skip_object_key = ('_SfcparseFileData', '__sfcparse_file_format_id')
    __locked_attr_list_key =  '_SfcparseFileData__assignment_locked_attribs'
    __reference_attr_list_key =  '_SfcparseFileData__assignment_reference_attribs'
    __sfcparse_file_format_id_match = "a55acb6b-f87b-4f89-ad11-c9d23eb1307d-7797537e-fb5d-4c69-b84f-2b4da59c04c1"


    ### SFCPARSE FILE DATA: Check if SfcparseFileData ###

    # Build Out Data
    if (isinstance(data, __SfcparseFileData)) and (data.__sfcparse_file_format_id__ == __sfcparse_file_format_id_match):
        for key,value in data.__dict__.items():
            # If Match Prefixes, Skip
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
        __build_data_output = __build_data_output.rstrip()

        # Write File Data
        __write_file_data(filename, __build_data_output, write_mode)

        return None


    ### DICT: Check if dict ###
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
        __build_data_output = __build_data_output.rstrip()

        # Write File Data
        __write_file_data(filename, __build_data_output, write_mode)

        return None


    ### CLASS: Check if any Class Object with Attributes
    if (not isinstance(data, str)) \
    and (not isinstance(data, int)) \
    and (not isinstance(data, float)) \
    and (not isinstance(data, bool)) \
    and (not isinstance(data, list)) \
    and (not isinstance(data, tuple)) \
    and (not isinstance(data, set)) \
    and (not isinstance(data, type(None))) \
    and (not isinstance(data, bytes)) \
    and (not isinstance(data, complex)) \
    and (not isinstance(data, range)) \
    and (not isinstance(data, frozenset)) \
    and (not isinstance(data, bytearray)) \
    and (not isinstance(data, memoryview)):
        # Build Data
        for key,value in data.__dict__.items():            
            # Normal Assignment
            if __multiline_check(value) and indentation_on:
                value = __cleanformat(value, indent_level)
                __build_data_output += f'{key} {__assignment_operators[0]} {value}\n'
            else: __build_data_output += f'{key} {__assignment_operators[0]} {repr(value)}\n'

        # Strip Last \n Char
        __build_data_output = __build_data_output.rstrip()

        # Write File Data
        __write_file_data(filename, __build_data_output, write_mode)

        return None


    # Report if Error not Definable
    raise SaveFile(__err_msg_general_error, f'\nDATA: {data}')


#########################################################################################################
# Functions

# Multiline Check
def __multiline_check(data: __Union[list, dict, tuple, set]) -> bool:
    """
    Check if Multiline Type to Assist for Indentation
    """
    if isinstance(data, list) \
    or isinstance(data, dict) \
    or isinstance(data, tuple) \
    or isinstance(data, set):
        return True
    return False


# Write File Data
def __write_file_data(filename: str, data: __Any, write_mode: str) -> None:
    """
    Write New or Append Data to File
    """
    __err_msg_write_mode = 'Bad write mode'
    __write_mode_allowed_list = ['w', 'a']
    try:
        # Write New File Mode
        if write_mode == 'w':
            __exportfile(filename, data)
        # Append Append File Mode
        if write_mode == 'a':
            __appendfile(filename, data)        
        # Raise Exception if No Match
        if not write_mode in __write_mode_allowed_list:
            raise SaveFile(__err_msg_write_mode, f'\nFILE: "{filename}" \nDATA: {write_mode}')
    except ExportFile as __err: raise SaveFile(__err, '')
    except AppendFile as __err: raise SaveFile(__err, '')
