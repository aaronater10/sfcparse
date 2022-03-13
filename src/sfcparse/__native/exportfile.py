# exportfile
#########################################################################################################
# Imports
from typing import Any as __Any
from ..error import SfcparseError

# Exception for Module
class _Exportfile: 
    class exportfile(SfcparseError): __module__ = SfcparseError.set_module_name()


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
    __err_msg_bytes = f"Only bytes is allowed if using byte_data=True: {data}"

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
                raise _Exportfile.exportfile(__err_msg_bytes, f'"{data}"')

        with open(filename, 'wb') as f:
            for data_to_write in data:
                f.write(data_to_write)
