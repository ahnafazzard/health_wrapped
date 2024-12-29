import json
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path


class HealthDataExtractor:
    @staticmethod
    def xml_to_dict(element):
        result = {}
        for child in element:
            if len(child) == 0:
                result[child.tag] = child.attrib
            else:
                result[child.tag] = HealthDataExtractor.xml_to_dict(child)
        return result

    def __init__(self, zip_path: str):
        self.zip_path = Path(zip_path)
        self.data = None
        self._extract_and_parse()

    def _extract_and_parse(self):
        with zipfile.ZipFile(self.zip_path, "r") as zip_ref:
            zip_ref.extractall("temp_extract")

        xml_path = Path("temp_extract/apple_health_export/export.xml")
        tree = ET.parse(xml_path)
        root = tree.getroot()
        self.data = self.xml_to_dict(root)

    def get_data_dict(self):
        return self.data

    def get_data_json(self, indent=2):
        return json.dumps(self.data, indent=indent)


# Example usage
if __name__ == "__main__":
    extractor = HealthDataExtractor("export.zip")
    print(extractor.get_data_json())
