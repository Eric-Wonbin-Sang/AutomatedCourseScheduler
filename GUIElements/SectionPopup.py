from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button


class SectionButton(Button):

    def __init__(self, stevens):

        super().__init__(
            text="Section Selector",
            size_hint=(.4, .1),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.stevens = stevens
        self.section_popup = SectionPopup(self.stevens)

    def on_press(self):

        self.section_popup.open()


class SectionPopup(Popup):

    def __init__(self, stevens):

        self.stevens = stevens
        self.popup_layout = self.get_popup_layout(stevens.term.subject_list[0].course_list[0])

        super().__init__(
            title="Section Selector",
            content=self.popup_layout,
            size_hint=(None, None),
            size=(400, 400)
        )

    def get_popup_layout(self, course):

        popup_layout = BoxLayout(
            orientation='horizontal',
            # size_hint=(1, .2),
            pos_hint={'center_x': .5, 'center_y': .5},
            # spacing=15,
            # padding=10
        )

        for activity_key in course.activity_dict:
            activity_layout = BoxLayout(
                orientation='vertical',
                # size_hint=(1, .2),
                pos_hint={'center_x': .5, 'center_y': .5},
                # spacing=15,
                # padding=10
            )
            activity_layout.add_widget(Label(text=activity_key))

            print(activity_key, course.activity_dict[activity_key])
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
            popup_layout.add_widget(activity_layout)

        return popup_layout

    def set_popup_layout(self, course):
        self.content = self.get_popup_layout(course)
