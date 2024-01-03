import xml.etree.ElementTree as ET

# ./APP/res/values/strings

def extract_strings(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    strings_dict = {}

    for string_element in root.findall('.//string'):
        key = string_element.get('name')
        value = string_element.text.strip() if string_element.text is not None else ''
        strings_dict[key] = value
    
    return strings_dict


