from GUIElements import CustomSpinner


class SectionSpinner(CustomSpinner.CustomSpinner):

    def __init__(self, stevens, **kwargs):

        self.stevens = stevens

        super().__init__(values=["Any"] + [section.id for section in
                                           self.stevens.term.subject_list[0].course_list[0].section_list],
                         **kwargs)

        self.text = self.values[0]

    def update_from_course(self, course):
        self.values = ["Any"] + [section.id for section in course.section_list]
        self.text = self.values[0] if self.values else "None"
