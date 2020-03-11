from kivy.uix.boxlayout import BoxLayout

from GUIElements import Buttons


class Selector(BoxLayout):

    def __init__(self, parent_layout, stevens):
        super().__init__(
            orientation='horizontal',
            size_hint=(1, .2),
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=15,
            padding=10
        )

        self.parent_layout = parent_layout
        self.stevens = stevens

        self.selector_button = Buttons.SelectorButton(stevens=self.stevens)
        self.remove_button = Buttons.RemoveSelectorButton(self, parent_layout)

        self.add_elements()

    def add_elements(self):
        self.add_widget(self.selector_button)
        self.add_widget(self.remove_button)

    # def get_section_list(self):
    #     if self.section_spinner.text != "Any":
    #         return [section for subject in self.stevens.term.subject_list
    #                 for course in subject.course_list
    #                 for section in course.section_list
    #                 if subject.id == self.subject_spinner.text and
    #                 course.id == self.course_spinner.text and
    #                 section.id == self.section_spinner.text]
    #
    #     section_list = []
    #     for subject in self.stevens.term.subject_list:
    #         for course in subject.course_list:
    #             if subject.id == self.subject_spinner.text and course.id == self.course_spinner.text:
    #                 section_list += course.section_list
    #     return section_list
