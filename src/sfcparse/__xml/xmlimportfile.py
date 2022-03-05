# xmlimportfile
#########################################################################################################
# Imports
import xml.etree.ElementTree as __xml_etree


#########################################################################################################
# Import xml file
def xmlimportfile(filename: str) -> __xml_etree.Element:
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
