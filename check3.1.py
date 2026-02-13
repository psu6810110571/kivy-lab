from kivy.app import App
from kivy.core.window import Window
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class TutorialApp(App):
    def build(self):
        # สร้าง BoxLayout แนวตั้ง
        b = BoxLayout(orientation='vertical')
        
        # สร้าง TextInput (ช่องกรอกข้อความ)
        t = TextInput(text='Hello',
                      font_size=150,
                      size_hint_y=None,
                      height=200)
        
        # สร้าง Label (ข้อความแสดงผล)
        l = Label(font_size=150,
                  text='Hello')
        
        # สร้าง FloatLayout และ Scatter
        f = FloatLayout()
        s = Scatter(pos=(0, 0), size=(Window.size[0], Window.size[1]/2)) # ปรับตำแหน่งและขนาด
        
        f.add_widget(s)
        s.add_widget(l)
        
        b.add_widget(t)
        b.add_widget(f)
        
        # Binding: เมื่อพิมพ์ใน TextInput ให้ Label เปลี่ยนตาม
        t.bind(text=l.setter('text'))
        
        return b

if __name__ == "__main__":
    TutorialApp().run()