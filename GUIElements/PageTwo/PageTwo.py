from kivy.uix.boxlayout import BoxLayout

from GUIElements import LayoutFactory
from GUIElements.PageTwo import ScheduleGraphicLayout, ScheduleArrowGroup, PageOneButton
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

        self.page_one_button = PageOneButton.PageOneButton(acs_app=self.acs_app)
        self.curr_schedule_index = 0
        self.schedule_arrow_group = ScheduleArrowGroup.ScheduleArrowGroup(page_two=self, acs_app=self.acs_app)
        self.schedule_layout = ScheduleGraphicLayout.ScheduleGraphicLayout(page_two=self, schedule=None)

        self.add_components()

    def add_components(self):
        Functions.add_to_layout(
            self,
            self.schedule_arrow_group,
            self.schedule_layout,
            self.page_one_button
        )
