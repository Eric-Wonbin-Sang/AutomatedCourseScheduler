from General import Functions


class Subject:

    def __init__(self, parent_term, course_list):

        self.parent_term = parent_term
        self.id = course_list[0].subject_id

        self.course_list = course_list
        self.update_course_parents()

    def update_course_parents(self):
        for course in self.course_list:
            course.parent_subject = self

    def __str__(self, **kwargs):
        ret_str = "Subject ID: {}, course count: {}".format(self.id, len(self.course_list))
        if kwargs.get("print_course_list"):
            for course in self.course_list:
                ret_str += "\n" + Functions.tab_string(course.__str__(**kwargs))
        return ret_str
