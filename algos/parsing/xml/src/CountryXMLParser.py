# Credit towards  https://docs.python.org/2/library/xml.etree.elementtree.html
from  xml.etree import ElementTree
from Country import Country
from NeighborXMLParser import NeighborXMLParser


class CountryXMLParser:
    def __init__(self, xml):
        tree = ElementTree.fromstring(xml)
        self.country_xml = tree.getroot()

    def get_countries(self):
        countries_xml = self.country_xml.findall('country')
        countries = list(len(countries_xml))

        for country in countries_xml:
            name = country.get('name')
            year = country.find('year')
            rank = country.find('rank').text
            neighbor_xml_parser = NeighborXMLParser()
            neighbors = neighbor_xml_parser.get_neighbors(country)
            country = Country(name, year, rank, neighbors)
            countries.append(country)

        return countries




