from kivy.uix.label import Label as KivyLabel


class Label(KivyLabel):

    def __init__(self, text, background_color=None):

        super().__init__(text=text,
                         color=background_color)
