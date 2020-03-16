from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.pagelayout import PageLayout

from Stevens import Stevens
import ScheduleCreator

from GUIElements import SelectorGroup, SelectorLayout, LayoutFactory
from General import Functions, Constants


class PageOne(LayoutFactory.make_layout(BoxLayout)):

    def __init__(self, stevens):

        super().__init__(
            orientation="vertical",
            spacing=15,
            padding=10,
            size_hint=(1, 1),
            background_color=(255, 255, 255)
        )

        self.stevens = stevens
        self.banner_image_path = "Images/stevens_logo.jpg"

        self.banner_image = self.get_banner_image()
        self.selector_group = self.get_selector_group()
        self.start_button = StartButton(stevens=self.stevens, selector_group=self.selector_group)

        self.add_components()

    def get_banner_image(self):
        return Image(
            source=self.banner_image_path,
            size_hint=(1, None)
        )

    def get_selector_group(self):
        selector_group = SelectorGroup.SelectorGroup()
        for i in range(Constants.selection_start_count):
            selector_group.add_widget(
                SelectorLayout.SelectorLayout(selector_group=selector_group, stevens=self.stevens)
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


class PageTwo(LayoutFactory.make_layout(BoxLayout)):

    def __init__(self, stevens):

        super().__init__(
            orientation="vertical",
            spacing=15,
            padding=10,
            size_hint=(1, 1),
            background_color=(255, 255, 255),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.stevens = stevens
        self.loading_image_path = "Images/loading.gif"
        self.loading_image = self.get_loading_image()

        self.add_components()

    def get_loading_image(self):
        return Image(
            source=self.loading_image_path,
            size_hint=(1, None)
        )

    def add_components(self):
        Functions.add_to_layout(
            self,
            self.loading_image
        )


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
            SelectorLayout.SelectorLayout(selector_group=self.selector_group, stevens=self.stevens),
            self
        )


class StartButton(Button):

    def __init__(self, stevens, selector_group):

        super().__init__(
            text="Start Schedule Creation",
            size_hint=(.6, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.stevens = stevens
        self.selector_group = selector_group

    def on_press(self):
        section_list_list = []
        for selector_layout in self.selector_group.children[1:]:
            section_list_list += selector_layout.get_section_list_list()

        schedule_list = ScheduleCreator.get_schedule_list(section_list_list=section_list_list)

        for schedule in schedule_list:
            print(schedule.get_url(self.stevens.term_key))
        print("------------------")


class MyApp(App):

    def __init__(self):

        super().__init__()

        self.stevens = Stevens.Stevens(term_key="2020S")
        self.page_layout = PageLayout(
            size_hint=(1, 1),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.page_one = PageOne(stevens=self.stevens)
        self.page_two = PageTwo(stevens=self.stevens)

    def build(self):

        # return Functions.add_to_layout(
        #     self.page_layout,
        #     self.page_one,
        #     self.page_two,
        # )

        return self.page_one


Window.size = (400, 700)
MyApp().run()
