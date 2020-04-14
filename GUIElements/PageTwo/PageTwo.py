from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from GUIElements import LayoutFactory
from GUIElements.PageTwo import ForwardButton, BackButton
from General import Functions


class PageTwo(LayoutFactory.make_layout(BoxLayout)):

    def __init__(self, acs_app, stevens):

        super().__init__(
            orientation="vertical",
            spacing=15,
            padding=10,
            size_hint=(1, 1),
            background_color=(255, 255, 255),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.acs_app = acs_app
        self.stevens = stevens

        self.schedule_arrow_group = self.get_schedule_arrow_group()
        self.curr_schedule_index = 0
        self.schedule_layout = self.get_schedule_layout()

        self.add_components()

    def get_schedule_arrow_group(self):

        schedule_arrow_group = LayoutFactory.make_layout(BoxLayout)(
            orientation="horizontal",
            spacing=15,
            padding=10,
            size_hint=(1, 1),
            background_color=(255, 255, 255),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        Functions.add_to_layout(
            schedule_arrow_group,
            BackButton.BackButton(acs_app=self.acs_app, page_two=self),
            ForwardButton.ForwardButton(acs_app=self.acs_app, page_two=self)
        )

        return schedule_arrow_group

    def get_schedule_layout(self):

        schedule_layout = LayoutFactory.make_layout(BoxLayout)(
            orientation="vertical",
            spacing=15,
            padding=10,
            size_hint=(1, 1),
            background_color=(235, 235, 235),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        label = Label(text="No schedules generated")

        Functions.add_to_layout(
            schedule_layout,
            label
        )

        return schedule_layout

    def add_components(self):
        Functions.add_to_layout(
            self,
            self.schedule_arrow_group,
            self.schedule_layout
        )
