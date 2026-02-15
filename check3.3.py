from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
import random  # <--- 1. เพิ่ม import random

class ScatterTextWidget(BoxLayout):
    # 2. เพิ่มฟังก์ชันสำหรับเปลี่ยนสี
    def change_label_color(self, *args):
        # สุ่มสี R, G, B และกำหนด Alpha เป็น 1 (ทึบแสง)
        colour = [random.random() for i in range(3)] + [1]
        # อ้างอิงไปที่ Label ในไฟล์ kv ผ่าน id: my_label
        label = self.ids['my_label']
        label.color = colour

class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()

if __name__ == "__main__":
    TutorialApp().run()