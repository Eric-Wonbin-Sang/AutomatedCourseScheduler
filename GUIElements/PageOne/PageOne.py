from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from ScheduleFiles import ScheduleTests

from GUIElements import LayoutFactory
from GUIElements.PageOne import SelectorGroup, SelectorLayout, StartButton, AddSelectorButton
from General import Functions, Constants


class PageOne(LayoutFactory.make_layout(BoxLayout)):

    def __init__(self, acs_app, stevens):

        super().__init__(
            orientation="vertical",
            spacing=15,
            padding=10,
            size_hint=(1, 1),
            background_color=(255, 255, 255)
        )

        self.test_schedule = ScheduleTests.test_schedule_0

        self.acs_app = acs_app
        self.stevens = stevens
        self.banner_image_path = "Images/stevens_logo.jpg"

        self.banner_image = self.get_banner_image()
        self.selector_group = self.get_selector_group()
        self.start_button = StartButton.StartButton(acs_app=self.acs_app,
                                                    stevens=self.stevens,
                                                    selector_group=self.selector_group)

        self.add_components()

    def get_banner_image(self):
        return Image(
            source=self.banner_image_path,
            size_hint=(1, None)
        )

    def get_selector_group(self):
        selector_group = SelectorGroup.SelectorGroup()

        if self.test_schedule:
            for course_name in self.test_schedule:
                selector_group.add_widget(
                    SelectorLayout.SelectorLayout(selector_group=selector_group,
                                                  stevens=self.stevens,
                                                  spec_course_name=course_name)
                )
        else:
            for i in range(Constants.selection_start_count):
                selector_group.add_widget(
                    SelectorLayout.SelectorLayout(selector_group=selector_group,
                                                  stevens=self.stevens,
                                                  spec_course_name="")
                )
        return selector_group

    def add_components(self):
        Functions.add_to_layout(
            self,
            self.banner_image,
            Functions.add_to_layout(
                self.selector_group,
                AddSelectorButton.AddSelectorButton(stevens=self.stevens, selector_group=self.selector_group)),
            self.start_button
        )
