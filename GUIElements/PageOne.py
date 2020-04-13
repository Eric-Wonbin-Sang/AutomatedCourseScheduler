from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager

from Stevens import Stevens
from ScheduleFiles import ScheduleCreator, ScheduleTests

from GUIElements import SelectorGroup, SelectorLayout, LayoutFactory, AppScreen
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
        self.start_button = StartButton(acs_app=self.acs_app, stevens=self.stevens, selector_group=self.selector_group)

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
                AddSelectorButton(stevens=self.stevens, selector_group=self.selector_group)),
            self.start_button
        )


class StartButton(Button):

    def __init__(self, acs_app, stevens, selector_group):

        super().__init__(
            text="Start Schedule Creation",
            size_hint=(.6, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.acs_app = acs_app
        self.stevens = stevens
        self.selector_group = selector_group

    def on_press(self):
        section_list_list = []
        for selector_layout in self.selector_group.children[1:]:
            section_list_list += selector_layout.get_section_list_list()

        schedule_list = ScheduleCreator.get_schedule_list(section_list_list=section_list_list)

        for i, schedule in enumerate(schedule_list):
            print("{})\t{}".format(i + 1, schedule.url))
            # for section in schedule.section_list:
            #     print("\t{}: \t{} - \t{}".format(section.section,
            #                                      section.start_time.strftime('%I:%M %p'),
            #                                      section.end_time.strftime('%I:%M %p')))
        print("------------------")

        # self.acs_app.screen_manager.current = "two"


class AddSelectorButton(Button):

    def __init__(self, stevens, selector_group):

        super().__init__(
            text="+",
            size_hint=(.2, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.stevens = stevens
        self.selector_group = selector_group

    def on_press(self):
        self.selector_group.remove_widget(self)
        Functions.add_to_layout(
            self.selector_group,
            SelectorLayout.SelectorLayout(selector_group=self.selector_group,
                                          stevens=self.stevens,
                                          spec_course_name=""),
            self
        )
