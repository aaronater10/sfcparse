# xmlimportstr
#########################################################################################################
# Imports
import xml.etree.ElementTree as __xml_etree


#########################################################################################################
# Import xml str
def xmlimportstr(data: str) -> __xml_etree.Element:
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
