from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

from Stevens import Section


class SelectorPopup(Popup):

    def __init__(self, selector_button, stevens):

        self.selector_button = selector_button
        self.stevens = stevens

        self.popup_layout, self.section_layout = self.get_layouts()
        self.curr_course = None

        super().__init__(
            title="Section Selector",
            content=self.popup_layout,
            size_hint=(.9, .9),
            auto_dismiss=False
        )

    def get_layouts(self):
        popup_layout = BoxLayout(
            orientation='vertical',
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=15,
            padding=10
        )
        popup_layout.add_widget(CourseInput(self, self.stevens))

        section_layout = BoxLayout(
            orientation='vertical',
            spacing=15,
            padding=10
        )

        popup_layout.add_widget(section_layout)
        popup_layout.add_widget(PopupCloseButton(pop_up=self))
        return popup_layout, section_layout


class CourseInput(TextInput):

    def __init__(self, pop_up, stevens):

        self.pop_up = pop_up
        self.stevens = stevens

        super().__init__(
            size_hint=(1, .1),
            pos_hint={'center_x': .5, 'center_y': .5},
            multiline=False
        )

        self.course_list, self.option_list = self.get_option_list()
        self.drop_down = self.get_drop_down()
        self.bind(text=self.update_drop_down)
        self.bind(on_text_validate=self.auto_complete)

    def get_option_list(self):
        option_list = []
        course_list = []
        for subject in self.stevens.term.subject_list:
            for course in subject.course_list:
                course_list.append(course)
                button_text = "{} {} - {}".format(course.subject_id, course.id, course.section_list[0].title)
                option_list.append(button_text)
        return course_list, option_list

    def get_drop_down(self):
        drop_down = DropDown()
        if len(self.text) > 0:
            for option in self.option_list:
                if self.text.lower().replace(" ", "") in option.lower().replace(" ", ""):
                    button = Button(
                        text=option,
                        size_hint_y=None,
                        height=30
                    )
                    button.bind(on_release=lambda btn: drop_down.select(btn.text))
                    drop_down.add_widget(button)
            drop_down.bind(on_select=lambda instance, x: self.update_section_layout(x))
        return drop_down

    def auto_complete(self, *args):
        for i, option in enumerate(self.option_list):
            if self.text.lower().replace(" ", "") in option.lower().replace(" ", ""):
                self.text = option
                self.drop_down.dismiss()
                self.update_section_layout_from_course(self.course_list[i])
                break

    def get_curr_course(self):
        for i, option in enumerate(self.option_list):
            if option == self.text:
                return self.course_list[i]
        return None

    def update_section_layout(self, text):
        self.text = text
        self.drop_down.dismiss()
        self.update_section_layout_from_course(self.get_curr_course())

    def update_section_layout_from_course(self, course):

        self.pop_up.curr_course = course

        for child in self.pop_up.section_layout.children:
            self.pop_up.section_layout.remove_widget(child)

        grid_layout = GridLayout(
            cols=len(course.activity_dict.keys()),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        for activity_key in course.activity_dict:
            grid_layout.add_widget(
                Label(
                    text=Section.Section.activity_dict[activity_key],
                    size_hint=(1, .1),
                    pos_hint={'center_x': .5, 'center_y': .5}
                )
            )

        for activity_key in course.activity_dict:
            activity_layout = BoxLayout(
                orientation="vertical",
                padding=10,
                spacing=10,
                size_hint=(1, None),
                pos_hint={'center_x': .5, 'center_y': .5}
            )
            activity_layout.bind(minimum_height=activity_layout.setter('height'))

            for i, section in enumerate(course.activity_dict[activity_key]):
                choice_layout = BoxLayout(
                    orientation='horizontal',
                    size_hint=(None, None),
                    height=30,
                    pos_hint={'center_x': .5, 'center_y': .5},
                    spacing=15,
                    padding=10
                )

                choice_layout.add_widget(Label(text=section.id))
                choice_layout.add_widget(CheckBox(active=True if i == 0 else False))
                activity_layout.add_widget(choice_layout)

            scroll_view = ScrollView(
                size_hint=(1, 1),
                pos_hint={'center_x': .5, 'center_y': .5},
                do_scroll_x=False,
            )
            scroll_view.add_widget(activity_layout)
            grid_layout.add_widget(scroll_view)

        self.pop_up.section_layout.add_widget(grid_layout)

    def update_drop_down(self, *args):
        self.drop_down.dismiss()
        self.drop_down = self.get_drop_down()
        if self.text != "":
            self.drop_down.open(self)


class PopupCloseButton(Button):

    def __init__(self, pop_up):

        super().__init__(
            text="Close",
            size_hint=(.6, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.pop_up = pop_up

    def on_press(self):
        self.pop_up.dismiss()
        if self.pop_up.curr_course:
            self.pop_up.selector_button.text = "{} {} - {}".format(
                self.pop_up.curr_course.subject_id,
                self.pop_up.curr_course.id,
                self.pop_up.curr_course.section_list[0].title
            )
