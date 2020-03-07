import requests
import xml.etree.ElementTree as Et

from Stevens import Term

from General import Constants


class Stevens:

    def __init__(self, **kwargs):

        self.term_key = kwargs.get("term_key", list(Constants.term_url_dict.keys())[-1])

        self.term = self.get_term()

        print(self.term.__str__())

    def get_term(self):
        xml = requests.get(Constants.term_url_dict[self.term_key], allow_redirects=True)
        xml_file_name = self.term_key + ".xml"
        open(xml_file_name, 'wb').write(xml.content)

        return Term.Term(Et.parse(xml_file_name))

    def __str__(self, **kwargs):
        return self.term.__str__(**kwargs)
