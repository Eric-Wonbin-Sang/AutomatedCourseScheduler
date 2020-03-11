from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp


class ButtonSelector(Button):

    def __init__(self):

        super().__init__(
            text='Hello',
            size_hint=(None, None),
            pos=(350, 300)
        )

        self.drop_down = self.get_drop_down()
        self.bind(on_release=self.drop_down.open)

    def get_drop_down(self):
        drop_down = DropDown()
        for i in range(10):
            button = Button(text='Value % d' % i, size_hint_y=None, height=40)
            button.bind(on_release=lambda btn: drop_down.select(btn.text))
            drop_down.add_widget(button)
        drop_down.bind(on_select=lambda instance, x: setattr(self, 'text', x))
        return drop_down

    def on_press(self):
        self.on_press()
        print("on_press")

    def on_release(self):
        self.on_release()
        print("on_release")


runTouchApp(ButtonSelector())
