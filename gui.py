from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image

from Stevens import Stevens

from GUIElements import SelectorGroup, SelectorLayout, LayoutFactory


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
        self.selector_group.add_widget(
            SelectorLayout.SelectorLayout(selector_group=self.selector_group, stevens=self.stevens)
        )
        self.selector_group.add_widget(self)


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
        section_list = []
        for selector_layout in self.selector_group.children[1:]:
            section_list += selector_layout.get_section_list()

        for section in section_list:
            print("{}".format(section.section))
            print("{}".format(section.__str__(print_section_dicts=True)))
        print("------------------")

class MyApp(App):

    def __init__(self):

        super().__init__()

        self.stevens = Stevens.Stevens(term_key="2020S")
        self.selector_group = self.get_selector_group()

    def build(self):

        gui_layout = LayoutFactory.make_layout(BoxLayout)(
            orientation="vertical",
            spacing=15,
            padding=10,
            background_color=(255, 255, 255)
        )

        gui_layout.add_widget(
            Image(
                source="Images/stevens_logo.jpg",
                size_hint=(1, None)
            )
        )
        gui_layout.add_widget(self.selector_group)
        self.selector_group.add_widget(
            AddSelectorButton(stevens=self.stevens, selector_group=self.selector_group)
        )
        gui_layout.add_widget(
            StartButton(stevens=self.stevens, selector_group=self.selector_group)
        )

        return gui_layout

    def get_selector_group(self):
        selector_group = SelectorGroup.SelectorGroup()
        for i in range(5):
            selector_group.add_widget(
                SelectorLayout.SelectorLayout(selector_group, stevens=self.stevens)
            )
        return selector_group


Window.size = (400, 700)
MyApp().run()
