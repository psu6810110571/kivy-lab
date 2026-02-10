from kivy.app import App
from kivy.uix.label import Label

class HelloApp(App):
    def build(self):
        return Label(text='maxZA', font_size=150)


if __name__ == '__main__':
    HelloApp().run()
