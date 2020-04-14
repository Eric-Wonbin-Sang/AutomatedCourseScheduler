from kivy.uix.label import Label as KivyLabel


class Label(KivyLabel):

    def __init__(self, text, color=None, **kwargs):

        if color is None:
            color = [0, 0, 0]
        color = [x/255 for x in color] + [1]

        super().__init__(
            text=text,
            color=color,
            **kwargs
        )
