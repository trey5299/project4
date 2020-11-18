from cis301.phonebill.phonebill_parser import PhoneBillParser


class TextParser(PhoneBillParser):
    pass

    def setUp(self):
        self.parser = TextParser()
        super(TextParserTestCase, self).setUp()

    def test_PhoneCall(self):
        parsed = self.parser.parse(self.category_url)
        self.assertEqual(parsed, self.category_embed)

    def test_Phonebill(self):
        parsed = self.parser.parse('Testing %s' % self.category_url)
        self.assertEqual(parsed, self.category_embed)