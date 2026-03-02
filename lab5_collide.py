from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.clock import Clock

# --- 🟢 ส่วนที่เพิ่มเข้ามาใน Step 3 (จุดที่ 1): ฟังก์ชันตรวจสอบการชน ---
# รับพารามิเตอร์ 2 ตัว คือ rect1 (ตัวเรา) และ rect2 (ศัตรู)
def collides(rect1, rect2):
    r1x, r1y = rect1[0] # พิกัด X, Y ของตัวเรา
    r1w, r1h = rect1[1] # ความกว้าง, ความสูง ของตัวเรา
    r2x, r2y = rect2[0] # พิกัด X, Y ของศัตรู
    r2w, r2h = rect2[1] # ความกว้าง, ความสูง ของศัตรู

    # สูตรคณิตศาสตร์ เช็คว่าขอบเขตของกล่อง 2 ใบ ล่วงล้ำทับซ้อนกันหรือไม่
    if (r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y):
        return True # ถ้าทับกัน ส่งค่ากลับเป็น True (ชนแล้ว)
    return False # ถ้าไม่ทับ ส่งค่ากลับเป็น False (ยังไม่ชน)
# --- 🟢 สิ้นสุดฟังก์ชันตรวจสอบการชน ---

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        
        self.pressed_keys = set()
        Clock.schedule_interval(self.move_step, 0)
        
        with self.canvas:
            # วาดตัวละครของเรา (โคนัน)
            self.hero = Rectangle(source='hero.png', pos=(0, 0), size=(100, 100))
            
            # วาดศัตรู (กล่องสีแดง) ไว้ตรงกลางหน้าจอ
            Color(1, 0, 0, 1) 
            self.enemy = Rectangle(pos=(400, 300), size=(100, 100))

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.pressed_keys.add(text)

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.pressed_keys:
            self.pressed_keys.remove(text)

    def move_step(self, dt):
        cur_x = self.hero.pos[0]
        cur_y = self.hero.pos[1]
        step = 300 * dt
        
        if 'w' in self.pressed_keys:
            cur_y += step
        if 's' in self.pressed_keys:
            cur_y -= step
        if 'a' in self.pressed_keys:
            cur_x -= step
        if 'd' in self.pressed_keys:
            cur_x += step
            
        self.hero.pos = (cur_x, cur_y)

        # --- 🟢 ส่วนที่เพิ่มเข้ามาใน Step 3 (จุดที่ 2): เรียกใช้เช็คการชน ---
        # แพ็คข้อมูล พิกัด (pos) และ ขนาด (size) ของทั้งคู่ ส่งไปให้ฟังก์ชันเช็ค
        rect1 = (self.hero.pos, self.hero.size)
        rect2 = (self.enemy.pos, self.enemy.size)
        
        # ถ้าฟังก์ชัน collides ส่งค่ากลับมาเป็น True ให้ทำงานใน if นี้
        if collides(rect1, rect2):
            print("Colliding! ชนแล้วจ้า!") 
        # --- 🟢 สิ้นสุดการเรียกใช้เช็คการชน ---

class MyApp(App):
    def build(self):
        return GameWidget()

if __name__ == '__main__':
    app = MyApp()
    app.run()