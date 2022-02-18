"""
Simple File Configuration Parse - by aaronater10
More info: https://github.com/aaronater10/sfcparse

Version 1.1.0

A simple library to import custom config/data files for your python program or script,
and export any data to disk simply!. Also contains a feature for easily formatting data
types for clean multiline output when exporting data to files.

Importing [Python types only]: returns a class with attributes from the file keeping python's natural
recognition of data types, including comments being ignored.

Exporting/Appending: it simply sends str data to a file. It may be used for any str data file output.

CleanFormat: simply formats any dict, list, set, or tuple to a clean multiline structure, and returned as str

Accepted Import Data Types: str, int, float, bool, list, dict, tuple, set, nonetype, bytes
"""
#########################################################################################################
# Imports
from ast import literal_eval as __literal_eval__
from typing import Any as __Any
from typing import Union as __Union
from os import path as __path
import json as __json
import yaml as __yaml
from configparser import SafeConfigParser as __SafeConfigParser
from configparser import ExtendedInterpolation as __ExtendedInterpolation
import hashlib as __hashlib
import xml.etree.ElementTree as __xml_etree


#########################################################################################################
# Import py Data from File

# Create hollow reference name for "class" to denote a class returned for hinting on imports
class __dummy_class:
    """Not meant to be used"""
    class Class:
        """Not meant to be used"""

# Import File Data
def importfile(filename: str) -> __dummy_class.Class:
    """
    Imports saved python data from any text file.

    Returns a class of attributes. Assign the output to var

    Enter file location as str to import.

    Accepted data types: str, int, float, bool, list, dict, tuple, set, nonetype, bytes

    [Example Use]
    importfile('filename.test' or 'path/to/filename.test')
    """

    # Validate file exists. Open and Import Config File into Class Object then return the object    
    try:
        with open(filename, 'r') as f:
            # Check if file empty. Returns empty class with same name if empty
            if __path.getsize(filename) == 0:
                class file_data: pass
                return file_data()
            f = f.read().splitlines()
    except FileNotFoundError: raise


    class file_data:

        # Syntax Error Message
        __py_syntax_err_msg = "importfile - Must have valid Python data types to import, or file is not formatted correctly"
        
        # Data Build Setup and Switches        
        __is_building_data_sw = False
        __body_build_data_sw = False
        __end_data_build_sw = False
        __build_data = ''

        # Markers
        __start_markers = {'[','{','('}
        __end_markers = {']','}',')'}
        __skip_markers = {'',' ','#','\n'}
        __eof_marker = f[-1]

        # Main File Loop
        for __file_data_line in f:

            # Set Skip Marker
            try: __skip_marker = __file_data_line[0]
            except IndexError: __skip_marker = ''

            # Skip Comments, Blank Lines, and potential New Lines
            if (__is_building_data_sw == False) and (__skip_marker in __skip_markers): continue

            # Set Syntax Check
            try: __syntax_check = __file_data_line.split()[1]
            except IndexError: __syntax_check = ''

            # Basic Syntax Check
            if (__syntax_check == '=') or (__is_building_data_sw):

                if not __is_building_data_sw:
                    __var_token = __file_data_line.split('=')[0].strip()
                    __value_token = __file_data_line.split('=')[1].strip()
                    __value_token_multi = __file_data_line.split('=')[1].split()[0].strip()
                    __last_token = __file_data_line.split('=')[-1].strip()
                    try: __start_skip_token = __file_data_line.split('=')[1].split()[1][0].strip()
                    except IndexError: __start_skip_token = ''
                    
                if __is_building_data_sw:
                    try: __end_token = __file_data_line[0]
                    except IndexError: __end_token = ''
                
                # START BUILD: Check if value in file line is only Start Marker. Check if Multiline or Single Line
                if (__value_token_multi in __start_markers) and ((__last_token in __start_markers) or (__start_skip_token[0] in __skip_markers)) and (__is_building_data_sw == False):
                    __build_data = __value_token
                    
                    # Turn ON Data Build Switches
                    __is_building_data_sw = True
                    __body_build_data_sw = True
                    __end_data_build_sw = True
                    continue
                
                # END BUILD: Check if line of file is an End Data Build Marker. Import Built Data Type if Valid. Check if EOF in case File Missing End Marker.
                elif (__end_data_build_sw) and ((__end_token in __end_markers) or (f"{__eof_marker}" == f"{__file_data_line}")):
                    __build_data += f"\n{__file_data_line}"
                    
                    try: locals()[__var_token] = __literal_eval__(__build_data)
                    except SyntaxError: raise SyntaxError(__py_syntax_err_msg)

                    # Turn OFF Data Build Switches
                    __is_building_data_sw = False
                    __body_build_data_sw = False
                    __end_data_build_sw = False
                    __build_data = ''
                    continue

                # CONT BUILD: Continue to Build Data
                elif __body_build_data_sw:
                    __build_data += f"\n{__file_data_line}"
                    
                # IMPORT SINLGE LINE VALUES: If not multiline, assume single
                else:
                    try: locals()[__var_token] = __literal_eval__(__value_token)
                    except ValueError: raise ValueError(__py_syntax_err_msg)
            
            else: raise SyntaxError(__py_syntax_err_msg)

    # Return Final Import
    return file_data()


#########################################################################################################
# Export Data to File
def exportfile(filename: str, *data: __Any, byte_data: bool=False):
    """
    Exports a new file with the new data.
    
    Enter new filename as str, Pass any data type for output to file.

    [Options]
    byte_data: Set to True if converting byte data to it's actual value to file
    
    [Example Use]
    Normal: exportfile('path/of/filename', 'data')

    Byte Data: exportfile('path/of/filename', b'data', byte_data=True)
    """
    __err_msg_bytes = f"exportfile - Only bytes is allowed for data: {data}"

    # Export data to new file

    # Raw Data to File
    if not byte_data:
        with open(filename, 'w') as f:
            for data_to_write in data:
                f.writelines(str(data_to_write))
    # Byte Data Converted to File
    if byte_data:
        for data_to_write in data:
            if not isinstance(data_to_write, bytes):
                raise TypeError(__err_msg_bytes)

        with open(filename, 'wb') as f:
            for data_to_write in data:
                f.write(data_to_write)


#########################################################################################################
# Append Data to File
def appendfile(filename: str, *data: __Any):
    """
    Appends any data to a file.

    Enter existing filename as str, Pass any data type for output to file.

    [Example Use]
    appendfile('filename.test' or 'path/to/filename.test', 'data1', 'data2')
    """

    # Append data to file
    __new_line = '\n'

    # Check if file empty. Throws error if file not found
    if __path.getsize(filename) == 0: __new_line = ''
    with open(filename, 'a') as f:
        for data_to_write in data:
            f.writelines(f"{__new_line}{data_to_write}")


#########################################################################################################
# Format/Prep Dictionary, List, Tuple, or Set Data for Export
def cleanformat(datatype: __Union[dict,list,tuple,set], indent_level: int=1) -> str:
    """
    Formats a (single) dictionary, list, tuple, or set, to have a clean multiline output for exporting to a file.

    Returned output will be a str

    Note: Higher indent levels will decrease performance. Indentation is applied to the main data set only.

    Tip: Changing indent level to 0 increases cleaning performance by 5%, but output will have no indentation (Default = 1).

    Accepted data types: dict, list, tuple, set 

    [Example Use]
    var = cleanformat(datatype)
    """
    # Set indent level
    if not isinstance(indent_level, int):
        raise TypeError('cleanformat - Only int is allowed for indent level.')
    indent_level = '\t'*indent_level

    # Format Data Type and Return as str
    __build_data = ""

    # Dict
    if isinstance(datatype, dict):
        for key,value in datatype.items():
            __build_data += f"\n{indent_level}{repr(key)}: {repr(value)},"
        __build_data = f"{{{__build_data}\n}}"
        return __build_data

    # List
    elif isinstance(datatype, list):
        for value in datatype:
            __build_data += f"\n{indent_level}{repr(value)},"
        __build_data = f"[{__build_data}\n]"
        return __build_data

    # Tuple
    elif isinstance(datatype, tuple):
        for value in datatype:
            __build_data += f"\n{indent_level}{repr(value)},"
        __build_data = f"({__build_data}\n)"
        return __build_data

    # Set
    elif isinstance(datatype, set):
        for value in datatype:
            __build_data += f"\n{indent_level}{repr(value)},"
        __build_data = f"{{{__build_data}\n}}"
        return __build_data

    # Raise Error
    else:
        raise TypeError(
            """cleanformat - Only dict, list, tuple, or set are allowed.
           If tuple, it must be empty, have a single value with a "," [e.g. (1,)], or have >= 2 values
            """
        )


#########################################################################################################
# Import raw data from file
def importrawfile(filename: str) -> str:
    """
    Imports any raw data from a file.

    Returns a str. Assign the output to var

    [Example Use]

    importrawfile('path/to/filename')
    """
    # Validate file exists. Import File then return the raw data   
    try:
        with open(filename, 'r') as f:
            if __path.getsize(filename) == 0:
                return ''
            return f.read()
    except FileNotFoundError: raise


#########################################################################################################
# JSON: Export & Import json files and strings
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


#########################################################################################################
# YAML: Export & Import yaml files
def yamlimportfile(filename: str) -> dict:
    """
    Imports yaml data from a file.

    Returns a dict. Assign the output to var

    Enter yaml file location as str to import.

    [Example Use]

    yamlimportfile('path/to/filename.yml')

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_load" method to protect from untrusted input.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/
    """
    __err_msg = f"yamlimportfile - Invalid data imported, type, or nothing specified: {filename}"
    # Import yaml file
    try:
        with open(filename, 'r') as f:
            # Check if file empty. Returns empty dict if empty
            if __path.getsize(filename) == 0:                
                return None
            return __yaml.safe_load(f)
    except FileNotFoundError: raise
    except OSError: raise OSError(__err_msg)
    except __yaml.scanner.ScannerError: raise SyntaxError(__err_msg)


def yamlexportfile(filename: str, data: __Any) -> None:
    """
    Exports a new file from python type to yaml data.
    
    Enter new filename as str. Pass any general data for output to file
    
    [Example Use]

    yamlexportfile('path/to/filename.yml', data)    

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_dump" method, which only supports standard YAML tags and cannot represent an arbitrary Python object.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/
    
    """
    __err_msg = f"yamlexportfile - Invalid data exported or type: {data}"

    # Export dict data to yaml file
    try:
        with open(filename, 'w') as f:
            __yaml.safe_dump(data, f)
    except __yaml.representer.RepresenterError: raise TypeError(__err_msg)


#########################################################################################################
# INI: Build ini data. Export, and Import ini files
def inibuildauto(data: dict) -> __SafeConfigParser:
    """
    Auto converts python dict to ini data structure.

    Returns a ConfigParser obj with your data. Assign the output to var

    Enter correctly structured python dict to convert to ini.

    [Example Python dict]

    {
        'section1': python_dict,
        'section2': python_dict    
    }

    This is using the native configparser library shipped with the python standard libray. Using SafeConfigParser method.
    For more information on the configparser library, visit: https://docs.python.org/3/library/configparser.html
    """
    __err_msg_syntax = f"inibuildauto - Structure of dict is incorrect: {repr(data)}"
    __err_msg_dict = f"inibuildauto - Invalid data, type, or nothing specified: {repr(data)}"

    if not isinstance(data, dict):
        raise TypeError(__err_msg_dict)

    # Auto Build INI data structure
    __ini_data = __SafeConfigParser(interpolation=__ExtendedInterpolation())

    try:
        for key,value in data.items():
            __ini_data[key] = value
        return __ini_data
    except AttributeError: raise SyntaxError(__err_msg_syntax)


def inibuildmanual() -> __SafeConfigParser:
    """    
    Returns an empty ConfigParser obj to manually build ini data
    
    Assign the output to var

    This is using the native configparser library shipped with the python standard libray. Using SafeConfigParser method.
    For more information on the configparser library, visit: https://docs.python.org/3/library/configparser.html
    """
    return __SafeConfigParser(interpolation=__ExtendedInterpolation())


def iniimportfile(filename: str) -> __SafeConfigParser:
    """
    Imports ini data from a file.

    Returns a ConfigParser obj. Assign the output to var

    Enter ini file location as str to import.

    [Example Use]

    iniimportfile('path/to/filename.ini')

    This is using the native configparser library shipped with the python standard libray. Using SafeConfigParser method.
    For more information on the configparser library, visit: https://docs.python.org/3/library/configparser.html
    """
    __err_msg_str = f"iniimportfile - Only str is allowed for filename: {filename}"

    if not isinstance(filename, str):
        raise TypeError(__err_msg_str)

    __parser = __SafeConfigParser(interpolation=__ExtendedInterpolation())
    __parser.read(filename)
    return __parser


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

    This is using the native configparser library shipped with the python standard libray. Using SafeConfigParser method.
    For more information on the configparser library, visit: https://docs.python.org/3/library/configparser.html
    """
    __err_msg_parser = f"iniexportfile - Invalid data to export, type, or nothing specified: {filename}"
    __err_msg_str = f"iniexportfile - Only str is allowed for filename: {filename}"

    if not isinstance(filename, str):
        raise TypeError(__err_msg_str)
        
    if isinstance(data, __SafeConfigParser):
        with open(filename, 'w') as f:
            data.write(f)
        return None
    
    raise TypeError(__err_msg_parser)


#########################################################################################################
# XML: Build xml data. Export, and Import xml files

# Dummy classes for xml hinting
class __dummy_xml:
    """Not meant to be used"""
    class ElementTree:
        """Not meant to be used"""
    class Element:
        """Not meant to be used"""



def xmlbuildmanual() -> __dummy_xml.ElementTree:
    """
    Returns a empty xml ElementTree obj to build/work with xml data
    
    Assign the output to var

    This is using the native xml library via etree shipped with the python standard libray.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
    return __xml_etree


def xmlimportfile(filename: str) -> __dummy_xml.ElementTree:
    """
    Imports xml data from a file.

    Returns a xml Parsed ElementTree obj with the root. Assign the output to var

    Enter xml file location as str to import.

    [Example Use]

    xmlimportfile('path/to/filename.xml')

    This is using the native xml library via etree shipped with the python standard libray.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
    __err_msg_str = f"xmlimportfile - Only str is allowed for filename: {filename}"
    __err_msg_file = f"xmlimportfile - {filename}"

    if not isinstance(filename, str): raise TypeError(__err_msg_str)

    try: return __xml_etree.parse(filename).getroot()
    except FileNotFoundError: raise FileNotFoundError(__err_msg_file)


def xmlimportstr(data: str) -> __dummy_xml.Element:
    """
    Imports xml data from a string

    Returns a xml Element. Assign the output to var

    [Example Use]

    xmlimportstr('<tag>data</tag>')

    This is using the native xml library via etree shipped with the python standard libray.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
    __err_msg_str = f"xmlimportstr - Only str is allowed for data: {repr(data)}"

    if not isinstance(data, str): raise TypeError(__err_msg_str)

    return __xml_etree.fromstring(str(data))


def xmlexportstr(data: __dummy_xml.ElementTree) -> str:
    """
    Exports xml ElementTree to a string

    Returns a str. Assign the output to var

    [Example Use]

    xmlexportstr(ElementTree)

    This is using the native xml library via etree shipped with the python standard libray.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
    # Check for Error
    __err_msg_etree = f"xmlexportstr - Only ElementTree is allowed for data: {repr(data)}"

    __dummy_element_str = "<dummy>dummy</dummy>"
    __dummy_element = __xml_etree.Element(__dummy_element_str)
    if not type(data) == type(__dummy_element): raise TypeError(__err_msg_etree) 

    # Export Data
    return __xml_etree.tostring(data).decode()


def xmlexportfile(filename: str, data: __dummy_xml.ElementTree) -> None:
    """
    Exports a new file from xml ElementTree obj as xml data
    
    Enter new filename as str. Pass ElementTree data for output to file
    
    [Example Use]

    xmlexportfile('path/to/filename.xml', ElementTree_data)

    This is using the native xml library via etree shipped with the python standard libray.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
    # Check for Error
    __err_msg_str = f"xmlexportfile - Only str is allowed for filename: {repr(filename)}"
    __err_msg_etree = f"xmlexportfile - Only ElementTree is allowed for data: {repr(data)}"

    __dummy_element_str = "<dummy>dummy</dummy>"
    __dummy_element = __xml_etree.Element(__dummy_element_str)    

    if not type(data) == type(__dummy_element): raise TypeError(__err_msg_etree)    
    if not isinstance(filename, str): raise TypeError(__err_msg_str)

    # Export Data
    data = xmlexportstr(data)
    exportfile(filename, data)


#########################################################################################################
# HASH: Create & Compare file hashes
def createfilehash(file_to_hash: str, file_to_store_hash: __Union[str,bool], hash_algorithm: str='sha256') -> str:
    """
    Creates a hash of any file, and stores the hash data to a new created file

    Always returns a str of the hash as well. Assign the output to var

    Enter file locations as str

    [Options]
    file_to_store_hash: Set to False if you do not want hash data stored to a file. Hash data is always returned whether or not this is set

    hash_algorithm: Already set to default of 'sha256', but supported to set 'sha512' or 'sha384'

    [Example Use]

    Default: createfilehash('path/to/src_filename', 'path/to/dst_hash_filename')
    Hash only, no file: hash_data = createfilehash('path/to/filename', False)

    This is using the hashlib libray shipped with the python standard libray.
    """
    __ALGO_OPTIONS = ('sha256', 'sha512', 'sha384')

    __err_msg = f"createfilehash - Invalid data to export, type, or nothing specified."
    __err_msg_str_file_src = f"createfilehash - Only str is allowed for file_to_hash: {file_to_hash}"
    __err_msg_file_dst = f"createfilehash - Only str|bool is allowed for file_to_store_hash: {file_to_store_hash}"
    __err_msg_str_hash = f"createfilehash - Only str is allowed for hash_algorithm: {hash_algorithm}"
    __err_msg_hash = f"createfilehash - Invalid or no hash option chosen for hash_algorithm: {hash_algorithm}"

    if not isinstance(file_to_hash, str): raise TypeError(__err_msg_str_file_src)
    if not ((isinstance(file_to_store_hash, str)) or (isinstance(file_to_store_hash, bool))): raise TypeError(__err_msg_file_dst)
    if not isinstance(hash_algorithm, str): raise TypeError(__err_msg_str_hash)
    if not hash_algorithm in __ALGO_OPTIONS: raise ValueError(__err_msg_hash)

    try: 
        # sha256
        if hash_algorithm == __ALGO_OPTIONS[0]:
            __sha256 = __hashlib.sha256()
            # Read source file data and hash
            with open(file_to_hash, 'rb') as f:
                for __readbytes in f:
                    __sha256.update(__readbytes)
            # Store hash to file
            __sha256 = __sha256.hexdigest()
            if bool(file_to_store_hash):
                exportfile(file_to_store_hash, f'hash_data = "{__sha256}"')
            return __sha256

        # sha512
        if hash_algorithm == __ALGO_OPTIONS[1]:
            __sha512 = __hashlib.sha512()
            # Read source file data and hash
            with open(file_to_hash, 'rb') as f:
                for __readbytes in f:
                    __sha512.update(__readbytes)
            # Store hash to file
            __sha512 = __sha512.hexdigest()
            if bool(file_to_store_hash):
                exportfile(file_to_store_hash, f'hash_data = "{__sha512}"')
            return __sha512

        # sha384
        if hash_algorithm == __ALGO_OPTIONS[2]:
            __sha384 = __hashlib.sha384()
            # Read source file data and hash
            with open(file_to_hash, 'rb') as f:
                for __readbytes in f:
                    __sha384.update(__readbytes)
            # Store hash to file
            __sha384 = __sha384.hexdigest()
            if bool(file_to_store_hash):
                exportfile(file_to_store_hash, f'hash_data = "{__sha384}"')
            return __sha384
    except FileNotFoundError: raise

    raise TypeError(__err_msg)


def comparefilehash(file_to_hash: str, stored_hash_file: str, hash_algorithm: str='sha256') -> bool:
    """
    Compares hash of any file by importing the previously stored hash file data from using "createfilehash"

    Returns a bool if the hash does/doesn't match

    Enter file locations as str

    [Options]

    hash_algorithm: Already set to default of 'sha256', but supported to set 'sha512' or 'sha384'

    [Example Use]
    
    comparefilehash('path/to/src_filename', 'path/to/src_hash_filename')

    This is using the hashlib libray shipped with the python standard libray.
    """
    __ALGO_OPTIONS = ('sha256', 'sha512', 'sha384')

    __err_msg = f"comparefilehash - Invalid data to export, type, or nothing specified."
    __err_msg_str_file_src = f"comparefilehash - Only str is allowed for file_to_hash: {file_to_hash}"
    __err_msg_hash_file = f"comparefilehash - Only str is allowed for stored_hash_file: {stored_hash_file}"
    __err_msg_str_hash = f"comparefilehash - Only str is allowed for hash_algorithm: {hash_algorithm}"
    __err_msg_hash = f"comparefilehash - Invalid or no hash option chosen for hash_algorithm: {hash_algorithm}"

    if not isinstance(file_to_hash, str): raise TypeError(__err_msg_str_file_src)
    if not isinstance(stored_hash_file, str): raise TypeError(__err_msg_hash_file)
    if not isinstance(hash_algorithm, str): raise TypeError(__err_msg_str_hash)
    if not hash_algorithm in __ALGO_OPTIONS: raise ValueError(__err_msg_hash)

    try: 
        # sha256
        if hash_algorithm == __ALGO_OPTIONS[0]:
            __sha256 = createfilehash(file_to_hash, False, hash_algorithm)
            # Import hash from file
            __hash_data = importfile(stored_hash_file)
            return (__sha256 == __hash_data.hash_data)

        # sha512
        if hash_algorithm == __ALGO_OPTIONS[1]:
            __sha512 = createfilehash(file_to_hash, False, hash_algorithm)
            # Import hash from file
            __hash_data = importfile(stored_hash_file)
            return (__sha512 == __hash_data.hash_data)

        # sha384
        if hash_algorithm == __ALGO_OPTIONS[2]:
            __sha384 = createfilehash(file_to_hash, False, hash_algorithm)
            # Import hash from file
            __hash_data = importfile(stored_hash_file)
            return (__sha384 == __hash_data.hash_data)
    except FileNotFoundError: raise

    raise TypeError(__err_msg)