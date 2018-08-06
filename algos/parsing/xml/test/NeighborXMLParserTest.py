from XMLLoader import XMLLoader
from Neighbor import Neighbor
from NeighborXMLParser import NeighborXMLParser
from xml.etree import ElementTree
import unittest


class NeighborXMLParserTest(unittest.TestCase):
    def setUp(self):
        self.xml_loader = XMLLoader()
        xml = self.xml_loader.loadFile("resources/neighbors.xml")
        self.country_xml = ElementTree.fromstring(xml)

    def test_parse_neighbors(self):
        expect_neighbors = [0]*2
        first_neighbor = Neighbor("Costa Ricya", "W")
        second_neighbor = Neighbor("Colombia", "E")
        expect_neighbors[0] = first_neighbor
        expect_neighbors[1] = second_neighbor
        neighbor_xml_parser = NeighborXMLParser()
        actuaL_neighbors = neighbor_xml_parser.get_neighbors(self.country_xml)
        is_true = self.assert_list_equals(expect_neighbors, actuaL_neighbors)
        self.assertTrue(is_true)

    def assert_neighbors(self):
         [entry for tag in list1 for entry in list2 if tag in entry]