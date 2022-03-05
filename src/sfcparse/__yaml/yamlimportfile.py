# yamlimportfile
#########################################################################################################
# Imports
from os import path as __path
import yaml as __yaml


#########################################################################################################
# Import yaml file
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
