from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class TutorialApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        # Top: TextInput (white background)
        t = TextInput(
            text="Hello",
            font_size=80,
            foreground_color=(0,0,0,1),
            background_color=(1,1,1,1),
            multiline=False
        )

        # Bottom: Label (black background)
        l = Label(
            text="Hello",
            font_size=80,
            color=(1,1,1,1)
        )

        # Bind text
        t.bind(text=l.setter('text'))

        # Layout order: top -> bottom
        root.add_widget(t)
        root.add_widget(l)

        return root

if __name__ == "__main__":
    TutorialApp().run()
