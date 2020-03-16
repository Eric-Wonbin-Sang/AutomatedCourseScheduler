from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

from General import Functions


def make_layout(layout_class):

    class NewClass(layout_class):

        def __init__(self, *args, **kwargs):

            self.background_color = kwargs.get("background_color")

            super().__init__(*args, **Functions.remove_from_dict(kwargs, "background_color"))

            if self.background_color:
                with self.canvas.before:
                    self.color_widget = \
                        Color(self.background_color[0] / 255,
                              self.background_color[1] / 255,
                              self.background_color[2] / 255)
                    self._rectangle = Rectangle()

        def on_size(self, *args):
            self._rectangle.size = self.size
            self._rectangle.pos = self.pos

    return NewClass
