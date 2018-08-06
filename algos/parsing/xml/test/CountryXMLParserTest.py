from XMLLoader import XMLLoader



class CountryXMLParserTest():
    def setUp(self):
        self.xml_loader = XMLLoader()

    def test_assert_XML(self):
        actual_xml = self.xml_loader.loadFile("resources/countries.xml")
        expect_xml = "<?xml version=\"1.0\"?><data>    <country name=\"Liechtenstein\">        <rank>1</rank>        <year>2008</year>        <gdppc>141100</gdppc>        <neighbor name=\"Austria\" direction=\"E\"/>        <neighbor name=\"Switzerland\" direction=\"W\"/>    </country>    <country name=\"Singapore\">        <rank>4</rank>        <year>2011</year>        <gdppc>59900</gdppc>        <neighbor name=\"Malaysia\" direction=\"N\"/>    </country>    <country name=\"Panama\">        <rank>68</rank>        <year>2011</year>        <gdppc>13600</gdppc>        <neighbor name=\"Costa Rica\" direction=\"W\"/>        <neighbor name=\"Colombia\" direction=\"E\"/>    </country></data>"
        self.assertEqual(expect_xml, actual_xml)
        self.xml = actual_xml

    def test_parse_country(self):
        pass

    def test_parse_countries(self):
        pass

