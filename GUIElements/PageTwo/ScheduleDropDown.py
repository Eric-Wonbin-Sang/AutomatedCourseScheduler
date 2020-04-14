from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

from General import Kiveasy


class ScheduleDropDown(DropDown):

    def __init__(self, page_two):

        super().__init__(
            size_hint=(.6, None),
            # size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.page_two = page_two
        self.schedule_list = []
        self.create_options()

    def create_options(self):

        self.add_widget(Kiveasy.Label(
            text="No schedules"
        ))
        self.bind(on_select=lambda instance, x: self.update_section_layout(x))

        # if len(self.schedule_list) == 0:
        #     self.add_widget(Kiveasy.Label(
        #         text="No schedules"
        #     ))
        # else:
        #     for i, schedule in enumerate(self.schedule_list):
        #         button = Button(
        #             text="Schedule " + str(i),
        #             size_hint_y=None,
        #             height=30
        #         )
        #         # button.bind(on_release=lambda btn: self.select(btn.text))
        #         self.add_widget(button)
        #     # self.bind(on_select=lambda instance, x: self.update_section_layout(x))

    def update(self, schedule_list):

        self.schedule_list = schedule_list
        self.create_options()
