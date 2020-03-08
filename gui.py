from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

from Stevens import Stevens

from GUIElements import Selector, AddSelectorButton, StartButton


class SelectorLayout(BoxLayout):
    def __init__(self):
        super().__init__(
            orientation="vertical",
            spacing=15,
            padding=10
        )
        with self.canvas.before:
            self.color_widget = Color(50/255, 132/255, 171/255)
            self._rectangle = Rectangle()

    def on_size(self, *args):
        self._rectangle.size = self.size
        self._rectangle.pos = self.pos


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
        selector_layout = SelectorLayout()

        selector_layout.add_widget(Selector.Selector(selector_layout, stevens=self.stevens))

        return selector_layout


MyApp().run()
