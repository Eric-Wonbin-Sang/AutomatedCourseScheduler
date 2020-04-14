from kivy.uix.boxlayout import BoxLayout

from GUIElements import LayoutFactory

from General import Functions, Kiveasy


class ScheduleGraphicLayout(LayoutFactory.make_layout(BoxLayout)):

    def __init__(self, schedule):

        super().__init__(
            orientation="vertical",
            spacing=15,
            padding=10,
            size_hint=(1, 1),
            background_color=(235, 235, 235),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.schedule = schedule

        self.do_init_setup()

    def do_init_setup(self):

        label = Kiveasy.Label(
            text="No schedules generated",
            color=[0, 0, 0]
        )

        Functions.add_to_layout(
            self,
            label
        )
