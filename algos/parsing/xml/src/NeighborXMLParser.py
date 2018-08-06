from Neighbor import Neighbor


class NeighborXMLParser:

     def get_neighbors(self, country_xml):
        neighbors_xml = country_xml.findall('neighbor')
        neighbors = [] * (len(neighbors_xml))

        for neighbor_xml in neighbors_xml:
            name = neighbor_xml.get('name')
            direction = neighbor_xml.get('direction')
            neighbor = Neighbor(name, direction)
            neighbors.append(neighbor)

        return neighbors
