from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from Stevens import Stevens

from GUIElements import Selector, AddSelectorButton, StartButton


class MyApp(App):

    def __init__(self):
        super().__init__()

        self.stevens = Stevens.Stevens(term_key="2020S")

        self.selector_layout = self.get_selector_layout()

    def build(self):
        gui_layout = BoxLayout(
            orientation="vertical",
            spacing=15,
            padding=10
        )

        gui_layout.add_widget(self.selector_layout)
        gui_layout.add_widget(AddSelectorButton.AddSelectorButton(self.stevens, self.selector_layout))
        gui_layout.add_widget(StartButton.StartButton(self.stevens, self.selector_layout))

        return gui_layout

    def get_selector_layout(self):
        selector_layout = BoxLayout(
            orientation="vertical",
            spacing=15,
            padding=10
        )
        selector_layout.add_widget(Selector.Selector(selector_layout, stevens=self.stevens))

        print(selector_layout.spacing)
        return selector_layout


MyApp().run()
