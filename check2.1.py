from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class TutorialApp(App):
    def build(self):
        b = BoxLayout()
        t = TextInput(
            font_size=80,
            hint_text="Type here...",       
            foreground_color=(0,0,0,1),          
            background_color=(1,1,1,1),
            multiline=False         
        )

        f = FloatLayout()
        s = Scatter()
        l = Label(text="Hello!",
                  font_size=150)
        
        t.bind(text=lambda instance, value: setattr(l, 'text' , value))

        f.add_widget(s)
        s.add_widget(l)

        b.add_widget(f)
        b.add_widget(t)
        return b

if __name__ == "__main__":
    TutorialApp().run()
