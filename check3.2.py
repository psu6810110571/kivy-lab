from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
# ในใบงานมีการ import widget อื่นๆ ทิ้งไว้ด้วย แต่ถ้าใช้ kv แล้ว ใน py ไม่ต้อง import ก็ได้
# แต่เพื่อความชัวร์ ใส่ไว้ตามใบงานก็ได้ครับ
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

class ScatterTextWidget(BoxLayout):
    pass

class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()

if __name__ == "__main__":
    TutorialApp().run()