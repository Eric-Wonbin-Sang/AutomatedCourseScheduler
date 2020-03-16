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

from General import Functions, Constants


class SelectorPopup(Popup):

    def __init__(self, selector_button, stevens):

        self.selector_button = selector_button
        self.stevens = stevens

        self.curr_course = self.get_init_course()
        self.popup_layout, self.section_layout = self.get_layouts()

        super().__init__(
            title="Section Selector",
            content=self.popup_layout,
            size_hint=(.9, .9),
            auto_dismiss=False
        )

    def get_init_course(self):
        return self.stevens.get_rand_course() if Constants.do_rand_course else None

    def get_layouts(self):
        popup_layout = BoxLayout(
            orientation='vertical',
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=15,
            padding=10
        )

        section_layout = BoxLayout(
            orientation='vertical',
            spacing=15,
            padding=10
        )

        popup_layout.add_widget(CourseInput(pop_up=self, section_layout=section_layout))

        Functions.add_to_layout(popup_layout, section_layout, PopupCloseButton(pop_up=self))
        return popup_layout, section_layout


class CourseInput(TextInput):

    def __init__(self, pop_up, section_layout):

        self.pop_up = pop_up
        self.section_layout = section_layout
        self.stevens = self.pop_up.stevens

        self.init_text = self.get_init_text()

        super().__init__(
            text=self.init_text,
            size_hint=(1, .1),
            pos_hint={'center_x': .5, 'center_y': .5},
            multiline=False
        )

        self.course_list, self.option_list = self.get_option_list()
        self.drop_down = self.get_drop_down()
        self.bind(text=self.update_drop_down)
        self.bind(on_text_validate=self.auto_complete)

    def get_init_text(self):
        if self.pop_up.curr_course:
            self.update_section_layout_from_course(self.pop_up.curr_course)
            return self.pop_up.curr_course.get_name()
        return ""

    def get_option_list(self):
        option_list, course_list = [], []
        for subject in self.stevens.term.subject_list:
            for course in subject.course_list:
                course_list.append(course)
                option_list.append(course.get_name())
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
        self.pop_up.selector_button.text = course.get_name()

        Functions.clear_layout(self.section_layout)

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

            activity_layout.add_widget(ChoiceLayout(label_text="All", check_box_status=True))
            for section in course.activity_dict[activity_key]:
                activity_layout.add_widget(ChoiceLayout(label_text=section.id, check_box_status=False))

            scroll_view = ScrollView(
                size_hint=(1, 1),
                pos_hint={'center_x': .5, 'center_y': .5},
                do_scroll_x=False,
            )
            scroll_view.add_widget(activity_layout)
            grid_layout.add_widget(scroll_view)

        self.section_layout.add_widget(grid_layout)

    def update_drop_down(self, *args):
        self.drop_down.dismiss()
        self.drop_down = self.get_drop_down()
        if self.text != self.init_text:
            self.drop_down.open(self)


class ChoiceLayout(BoxLayout):

    def __init__(self, label_text, check_box_status):

        super().__init__(
            orientation='horizontal',
            size_hint=(None, None),
            height=30,
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=15,
            padding=10
        )

        self.label = Label(text=label_text)
        self.check_box = CheckBox(active=check_box_status)

        self.add_components()

    def add_components(self):
        self.add_widget(self.label)
        self.add_widget(self.check_box)

    def get_text(self):
        return self.label.text if self.label else "No label"

    def is_selected(self):
        return self.check_box.state == "down"

    def __str__(self):
        if self.__dict__.get("label") and self.__dict__.get("check_box"):
            ret_str = "ChoiceLayout: "
            ret_str += "Label: {}\t\t".format(self.get_text())
            ret_str += "CheckBox: {}".format(self.is_selected())
            return ret_str
        return super().__str__()


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
