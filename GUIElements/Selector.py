from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from GUIElements.SelectorPopup import SelectorPopup


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

        self.selector_button = SelectorButton(stevens=self.stevens)
        self.remove_button = RemoveSelectorButton(self, parent_layout)

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


class RemoveSelectorButton(Button):

    def __init__(self, selector, selector_layout):
        super().__init__(
            text="Remove",
            size_hint=(.2, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.selector = selector
        self.selector_layout = selector_layout

    def on_press(self):
        if self.selector_layout.children:
            self.selector_layout.remove_widget(self.selector)


class SelectorButton(Button):

    def __init__(self, stevens):

        super().__init__(
            text="No Course Selected",
            size_hint=(.4, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.stevens = stevens
        self.selector_popup = SelectorPopup(selector_button=self, stevens=self.stevens)

    def on_press(self):
        self.selector_popup.open()
