from General import Functions


class Subject:

    def __init__(self, course_list):

        self.id = course_list[0].subject_id

        self.course_list = course_list

    def update_course_parents(self):
        for course in self.course_list:
            course.subject_parent = self

    def __str__(self, **kwargs):
        ret_str = "Subject ID: {}, course count: {}".format(self.id, len(self.course_list))
        if kwargs.get("print_course_list"):
            for course in self.course_list:
                ret_str += "\n" + Functions.tab_string(course.__str__(**kwargs))
        return ret_str
