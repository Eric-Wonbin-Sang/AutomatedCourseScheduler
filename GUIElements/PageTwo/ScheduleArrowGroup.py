from kivy.uix.boxlayout import BoxLayout

from GUIElements import LayoutFactory
from GUIElements.PageTwo import BackButton, ScheduleIndicatorLabel, ForwardButton

from General import Functions


class ScheduleArrowGroup(LayoutFactory.make_layout(BoxLayout)):

    def __init__(self, page_two, acs_app):

        super().__init__(
            orientation="horizontal",
            spacing=15,
            padding=10,
            size_hint=(1, .2),
            background_color=(255, 255, 255),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.page_two = page_two
        self.acs_app = acs_app

        self.back_button = BackButton.BackButton(acs_app=self.acs_app, page_two=self.page_two)
        self.schedule_indicator_label = ScheduleIndicatorLabel.ScheduleIndicatorLabel(page_two=self.page_two)
        self.forward_button = ForwardButton.ForwardButton(acs_app=self.acs_app, page_two=self.page_two)

        self.do_init_setup()

    def do_init_setup(self):
        Functions.add_to_layout(
            self,
            self.back_button,
            self.schedule_indicator_label,
            self.forward_button
        )
