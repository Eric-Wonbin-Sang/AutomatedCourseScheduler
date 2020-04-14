from kivy.uix.boxlayout import BoxLayout

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

        label = Kiveasy.Label(
            text="No schedules generated",
            color=[0, 0, 0]
        )

        Functions.add_to_layout(
            self,
            label
        )

    def update_schedule(self, schedule):

        Functions.clear_layout(self)

        Functions.add_to_layout(
            self,
            Kiveasy.Label(
                text="{}: {}".format(self.page_two.curr_schedule_index,
                                     schedule.url),
                color=[0, 0, 0]
            )
        )
