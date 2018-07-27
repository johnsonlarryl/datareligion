import unittest
from XMLLoader import XMLLoader


class CountryXMLParserTest(unittest.TestCase):
    def setUp(self):
        xml_loader = XMLLoader()
        xml = xml_loader.loadFile("resources/countries.xml")
        print(xml)

    def testParseCountry(self):
        pass

    def testParseCountries(self):
        pass

