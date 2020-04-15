
from StevensFiles import Subject, Course, Section

from General import Functions


class Term:

    def __init__(self, xml):

        self.xml = xml

        self.main_attrib_dict = xml.getroot().attrib
        self.id = self.get_id()

        self.subject_list = self.get_subject_list()

    def get_id(self):
        return self.main_attrib_dict.get("Semester", None)

    def get_section_list(self):
        return [Section.Section(parent_course=None, xml=child_xml) for child_xml in self.xml.getroot()]

    def get_course_list(self):
        course_id_to_section_list_dict = {}
        for section in self.get_section_list():
            key = (section.subject_id, section.course_id)
            if key not in course_id_to_section_list_dict:
                course_id_to_section_list_dict[key] = [section]
            else:
                course_id_to_section_list_dict[key] += [section]

        return [Course.Course(parent_subject=None, section_list=course_id_to_section_list_dict[course_id])
                for course_id in course_id_to_section_list_dict]

    def get_subject_list(self):
        subject_id_to_course_list_dict = {}
        for course in self.get_course_list():
            if course.subject_id not in subject_id_to_course_list_dict:
                subject_id_to_course_list_dict[course.subject_id] = [course]
            else:
                subject_id_to_course_list_dict[course.subject_id] += [course]

        return [Subject.Subject(parent_term=self, course_list=subject_id_to_course_list_dict[subject_id])
                for subject_id in subject_id_to_course_list_dict]

    def __str__(self, **kwargs):
        ret_str = "Term ID: {}, subject count: {}".format(self.id, len(self.subject_list))
        if kwargs.get("print_subject_list"):
            for subject in self.subject_list:
                ret_str += "\n" + Functions.tab_string(subject.__str__(**kwargs))
        return ret_str

    # def get_stats(self):
    #
    #     subject_count = len(self.subject_list)
    #     course_count = 0
    #     section_count = 0
    #     for subject in self.subject_list:
    #         course_count += len(subject.course_list)
    #         for course in subject.course_list:
    #             section_count += len(course.section_list)
    #
    #     str_ret = "Term Stats: " + self.code + "\n" + Functions.line + "\n"
    #     str_ret += "\t" + "subject_count: " + str(subject_count) + "\n"
    #     str_ret += "\t" + "course_count: " + str(course_count) + "\n"
    #     str_ret += "\t" + "section_count: " + str(section_count) + "\n" + Functions.line
    #
    #     return str_ret

    # def match_input_to_course_list(self, search_course_name):
    #
    #     simple_search_course_name = Functions.simplify_string(search_course_name)
    #     simple_base_search_course_name = search_course_name_to_base_course_name(simple_search_course_name)
    #
    #     specific_section_cond = False
    #     if Functions.string_num_letter_switch_count(simple_search_course_name) > 1:
    #         specific_section_cond = True
    #
    #     for subject in self.subject_list:
    #         for course in subject.course_list:
    #             simple_course_name = Functions.simplify_string(course.name)
    #             if simple_course_name == simple_base_search_course_name:
    #                 if specific_section_cond:
    #                     for section in course.section_list:
    #                         simple_section_name = Functions.simplify_string(section.main_attrib_dict["Section"])
    #                         if simple_section_name == simple_search_course_name:
    #                             return [section]
    #                 else:
    #                     return course.section_list
    #     return []


# def search_course_name_to_base_course_name(search_course_name):
#     simple_search_course_name = Functions.simplify_string(search_course_name)
#     sectioned_list = Functions.string_to_alternating_letter_to_num(simple_search_course_name)[0:2]
#     ret_str = ""
#     for sectioned in sectioned_list:
#         ret_str += sectioned
#     return ret_str
#
#
# def subject_name_to_title(name_title_dict, name):
#     for key in name_title_dict:
#         if key == name:
#             return name_title_dict[key]
#     return "Title Not Available"
