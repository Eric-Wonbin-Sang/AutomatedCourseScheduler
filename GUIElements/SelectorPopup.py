from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from GUIElements import Buttons


class SelectorPopup(Popup):

    def __init__(self, stevens):

        self.stevens = stevens
        self.popup_layout = BoxLayout(
            orientation='vertical',
            # size_hint=(1, .2),
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=15,
            padding=10
        )

        self.section_layout = BoxLayout(
            orientation='vertical',
            # size_hint=(1, .2),
            # pos_hint={'center_x': .5, 'center_y': .5},
            spacing=15,
            padding=10
        )

        self.popup_layout.add_widget(CourseInput(self.section_layout, self.stevens))
        self.popup_layout.add_widget(self.section_layout)
        self.popup_layout.add_widget(Buttons.PopupCloseButton(self))

        super().__init__(
            title="Section Selector",
            content=self.popup_layout,
            size_hint=(.9, .9),
            auto_dismiss=False
        )

    def set_popup_layout(self):
        self.content = self.get_popup_layout()


class CourseInput(TextInput):

    def __init__(self, section_layout, stevens):

        self.section_layout = section_layout
        self.stevens = stevens

        super().__init__(
            size_hint=(1, .1),
            pos_hint={'center_x': .5, 'center_y': .5},
            multiline=False
        )

        self.course_list, self.option_list = self.get_option_list()
        self.drop_down = self.get_drop_down()
        self.bind(text=self.update_drop_down)

    def get_option_list(self):
        option_list = []
        course_list = []
        for subject in self.stevens.term.subject_list:
            for course in subject.course_list:
                course_list.append(course)
                button_text = "{} {} - {}".format(course.subject_id, course.id, "title")
                option_list.append(button_text)
        return course_list, option_list

    def get_drop_down(self):
        drop_down = DropDown()
        if len(self.text) > 0:
            for option in self.option_list:
                if self.text.lower() in option.lower():
                    button = Button(
                        text=option,
                        size_hint_y=None, height=40
                    )
                    button.bind(on_release=lambda btn: drop_down.select(btn.text))
                    drop_down.add_widget(button)
            drop_down.bind(on_select=lambda instance, x: self.update_section_layout(x))
        return drop_down

    def update_section_layout(self, text):
        self.text = text
        self.drop_down.dismiss()

        for child in self.section_layout.children:
            self.section_layout.remove_widget(child)

        course = None
        for i, option in enumerate(self.option_list):
            if option == self.text:
                course = self.course_list[i]
                break

        grid_layout = GridLayout(
            cols=len(course.activity_dict.keys()),
            # size_hint=(1, .2),
            pos_hint={'center_x': .5, 'center_y': .5},
            # spacing=15,
            # padding=10
        )

        for activity_key in course.activity_dict:
            grid_layout.add_widget(Label(text=activity_key))

        for activity_key in course.activity_dict:

            activity_layout = BoxLayout(orientation="vertical")

            for i, section in enumerate(course.activity_dict[activity_key]):
                choice_layout = BoxLayout(
                    orientation='horizontal',
                    # size_hint=(1, .2),
                    pos_hint={'center_x': .5, 'center_y': .5},
                    # spacing=15,
                    # padding=10
                )
                choice_layout.add_widget(Label(text=section.id))
                choice_layout.add_widget(CheckBox(active=True if i == 0 else False))
                activity_layout.add_widget(choice_layout)

            grid_layout.add_widget(activity_layout)

        self.section_layout.add_widget(grid_layout)

    def update_drop_down(self, *args):
        print("CHANGED -", self.text)
        self.drop_down.dismiss()
        self.drop_down = self.get_drop_down()
        if self.text != "":
            self.drop_down.open(self)
