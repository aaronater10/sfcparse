# xmlexportfile
#########################################################################################################
# Imports
from ..__native.exportfile import exportfile
from .xmlexportstr import xmlexportstr
import xml.etree.ElementTree as __xml_etree


#########################################################################################################
# Export xml file
def xmlexportfile(filename: str, data: __xml_etree.Element) -> None:
    """
    Exports a new file from xml Element obj as xml data
    
    Enter new filename as str. Pass ElementTree data for output to file
    
    [Example Use]

    xmlexportfile('path/to/filename.xml', Element_data)

    This is using the native xml library via etree shipped with the python standard libray.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
    # Check for Error
    __err_msg_str = f"xmlexportfile - Only str is allowed for filename: {repr(filename)}"
    __err_msg_etree = f"xmlexportfile - Only Element is allowed for data: {repr(data)}"

    if not isinstance(data, __xml_etree.Element): raise TypeError(__err_msg_etree)    
    if not isinstance(filename, str): raise TypeError(__err_msg_str)

    # Export Data
    data = xmlexportstr(data)
    exportfile(filename, data)
