from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle


def make_layout(layout_class):

    class NewClass(layout_class):

        def __init__(self, *args, **kwargs):

            self.background_color = kwargs.get("background_color")

            new_kwargs = {}
            for key in kwargs:
                if key != "background_color":
                    new_kwargs[key] = kwargs[key]

            super().__init__(*args, **new_kwargs)

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
