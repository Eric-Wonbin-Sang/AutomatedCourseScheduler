from General import Functions


class Course:

    def __init__(self, parent_subject, section_list):

        self.subject_id = section_list[0].subject_id
        self.id = section_list[0].course_id
        self.parent_subject = parent_subject

        self.section_list = section_list

    def update_section_parents(self):
        for section in self.section_list:
            section.course_parent = self

    def __str__(self, **kwargs):
        ret_str = "Course ID: {}, section count: {}".format(self.id, len(self.section_list))
        if kwargs.get("print_section_list"):
            for section in self.section_list:
                ret_str += "\n" + Functions.tab_string(section.__str__(**kwargs))
        return ret_str
