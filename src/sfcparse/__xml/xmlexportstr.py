# xmlexportstr
#########################################################################################################
# Imports
import xml.etree.ElementTree as __xml_etree


#########################################################################################################
# Export xml str
def xmlexportstr(data: __xml_etree.Element) -> str:
    """
    Exports xml Element obj to a string

    Returns a str. Assign the output to var

    [Example Use]

    xmlexportstr(Element)

    This is using the native xml library via etree shipped with the python standard libray.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
    # Check for Error
    __err_msg_etree = f"xmlexportstr - Only Element is allowed for data: {repr(data)}"

    if not isinstance(data, __xml_etree.Element): raise TypeError(__err_msg_etree)

    # Export Data
    return __xml_etree.tostring(data).decode()
