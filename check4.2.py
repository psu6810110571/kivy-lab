from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # Checkpoint 4.2: เปลี่ยนกล่องเป็นรูปภาพ และปรับ pos, size
            Rectangle(source='hero.png', pos=(150, 200), size=(200, 200))

class MyApp(App):
    def build(self):
        return GameWidget()

if __name__ == '__main__':
    app = MyApp()
    app.run()