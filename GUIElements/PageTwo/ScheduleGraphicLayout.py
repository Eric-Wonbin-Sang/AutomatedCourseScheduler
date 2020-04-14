from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
import random

from GUIElements import LayoutFactory

from General import Functions, Kiveasy


class ScheduleGraphicLayout(LayoutFactory.make_layout(BoxLayout)):

    def __init__(self, page_two, schedule):

        super().__init__(
            orientation="vertical",
            spacing=15,
            padding=10,
            size_hint=(1, 1),
            background_color=(235, 235, 235),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.page_two = page_two
        self.schedule = schedule

        self.do_init_setup()

    def do_init_setup(self):

        Functions.clear_layout(self)

        Functions.add_to_layout(
            self,
            Kiveasy.Label(
                text="No schedules could be generated"
            )
        )

    def update_schedule(self, schedule):

        Functions.clear_layout(self)

        self.schedule = schedule

        section_label_layout_list = []
        for section in self.schedule.section_list:
            section_label_layout_list.append(Functions.add_to_layout(
                LayoutFactory.make_layout(BoxLayout)(
                    orientation="horizontal",
                    spacing=15,
                    padding=10,
                    size_hint=(1, .2),
                    background_color=(235, 235, 235),
                    pos_hint={'center_x': .5, 'center_y': .5}
                ),
                Kiveasy.Label(
                    text="{} - {}".format(section.section, section.title),
                    pos_hint={'center_x': .5, 'center_y': .5}
                ),
                Kiveasy.Label(
                    text="{} - {}".format(Functions.time_to_nice_str(section.start_time),
                                          Functions.time_to_nice_str(section.end_time)),
                    size_hint=(.5, None),
                    pos_hint={'center_x': .5, 'center_y': .5}
                )
            ))

        Functions.add_to_layout(
            self,
            Image(
                source="Images/Schedule Mockup {}.jpg".format(random.randint(0, 4)),
            ),
            *section_label_layout_list,
            Kiveasy.Label(
                text="Total Credit: {}".format(self.schedule.credit_sum),
                bold=True,
                size_hint=(None, .2),
                pos_hint={'center_x': .5, 'center_y': .5}
            )
        )
