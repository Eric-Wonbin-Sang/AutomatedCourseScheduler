import requests
import xml.etree.ElementTree as Et
import random

from Stevens import Term

from General import Functions, Constants


class Stevens:

    def __init__(self, **kwargs):

        self.term_key = get_term_key(**kwargs)
        self.term = self.get_term()

    def get_term(self):

        xml_file_name = self.term_key + ".xml"
        if Functions.is_connected():
            xml = requests.get(Constants.term_url_dict[self.term_key], allow_redirects=True)
            open(xml_file_name, 'wb').write(xml.content)

        return Term.Term(Et.parse(xml_file_name))

    def get_rand_course(self):
        course_list = [course for subject in self.term.subject_list for course in subject.course_list]
        return course_list[int(random.random() * (len(course_list) - 1))]

    def get_spec_course(self, spec_course_name):
        course_list = [course for subject in self.term.subject_list for course in subject.course_list]
        for course in course_list:
            if (course.subject_id + course.id).replace(" ", "").lower() == spec_course_name.replace(" ", "").lower():
                return course
        return None

    def __str__(self, **kwargs):
        return self.term.__str__(**kwargs)


def get_term_key(**kwargs):
    return kwargs.get("term_key", list(Constants.term_url_dict.keys())[-1])
