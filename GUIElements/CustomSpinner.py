from kivy.uix.spinner import Spinner


class CustomSpinner(Spinner):

    def __init__(self, **kwargs):

        super().__init__(
            size_hint=(.4, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5},
            **kwargs
        )
