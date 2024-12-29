import json
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path


def xml_to_dict(element):
    result = {}
    for child in element:
        if len(child) == 0:
            result[child.tag] = child.attrib
        else:
            result[child.tag] = xml_to_dict(child)
    return result


def main():
    # Extract zip file
    with zipfile.ZipFile("export.zip", "r") as zip_ref:
        zip_ref.extractall("temp_extract")

    # Read XML file
    xml_path = Path("temp_extract/apple_health_export/export.xml")
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Convert to dict then JSON
    data = xml_to_dict(root)

    # Pretty print JSON
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
