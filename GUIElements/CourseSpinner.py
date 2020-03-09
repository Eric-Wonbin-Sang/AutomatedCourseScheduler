from GUIElements import CustomSpinner


class CourseSpinner(CustomSpinner.CustomSpinner):

    def __init__(self, stevens, section_popup, **kwargs):

        self.stevens = stevens

        self.curr_course = self.stevens.term.subject_list[0].course_list[0]

        super().__init__(values=[course.id for course in self.stevens.term.subject_list[0].course_list],
                         **kwargs)

        self.text = self.values[0]

        self.section_popup = section_popup

    def update_from_subject(self, subject):
        self.values = [course.id for course in subject.course_list]
        self.text = self.values[0]

        self.section_popup.set_popup_layout(subject.course_list[0])

    def _on_dropdown_select(self, instance, data, *largs):
        self.text = data
        self.is_open = False
        curr_course = [course for subject in self.stevens.term.subject_list
                       for course in subject.course_list if course.id == self.text][0]

        self.section_popup.set_popup_layout(curr_course)
