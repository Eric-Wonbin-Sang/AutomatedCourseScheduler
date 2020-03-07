from GUIElements import CustomSpinner


class SubjectSpinner(CustomSpinner.CustomSpinner):

    def __init__(self, stevens, course_spinner, section_spinner, **kwargs):

        self.stevens = stevens

        super().__init__(values=[subject.id for subject in self.stevens.term.subject_list],
                         **kwargs)

        self.text = self.values[0]

        self.course_spinner = course_spinner
        self.section_spinner = section_spinner

    def _on_dropdown_select(self, instance, data, *largs):
        self.text = data
        self.is_open = False
        curr_subject = [subject for subject in self.stevens.term.subject_list if subject.id == self.text][0]

        self.course_spinner.update_from_subject(curr_subject)
