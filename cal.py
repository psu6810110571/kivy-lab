# นำเข้า App หลักของ Kivy
from kivy.app import App

# นำเข้า BoxLayout เพื่อใช้เป็น layout หลัก
from kivy.uix.boxlayout import BoxLayout


# คลาส Calculator เป็น widget หลักของเครื่องคิดเลข
# เชื่อมกับ <Calculator> ในไฟล์ calculator.kv
class Calculator(BoxLayout):

    # ตัวแปร label ใช้เก็บค่าข้อความ (ผูกกับ Label ใน kv)
    label = ''

    # ฟังก์ชันลบทั้งหมด (ปุ่ม C)
    # instance คือข้อความปัจจุบันที่ส่งมาจาก kv
    def delete(self, instance):
        # instance[:0] = ตัดข้อความให้เหลือค่าว่าง
        self.display.text = instance[:0]

    # ฟังก์ชันลบทีละ 1 ตัวอักษร (ปุ่ม CE)
    def del1(self, instance):
        # instance[:-1] = ตัดอักษรตัวสุดท้ายออก
        self.display.text = instance[:-1]

    # ฟังก์ชันคำนวณผลลัพธ์ (ปุ่ม =)
    def calc(self, instance):
        try:
            # eval() ใช้ประเมินนิพจน์ทางคณิตศาสตร์จาก string
            # เช่น "1+2*3" -> 7
            result = eval(instance)

            # แสดงผลลัพธ์ที่หน้าจอหลัก
            self.display.text = str(result)

            # แสดงผลลัพธ์ที่แถบบน (result)
            self.result.text = str(result)

        except Exception:
            # ถ้ามี error (เช่น syntax ผิด)
            self.display.text = '0'
            self.result.text = 'ERROR'


# คลาส App หลักของโปรแกรม
class CalculatorApp(App):

    # ตัวแปร trigger ใช้ควบคุมการกดปุ่มต่าง ๆ
    trigger = False
    triggerC = False
    triggerD = False

    # สร้างหน้าจอหลักของแอป
    def build(self):
        # คืนค่า widget Calculator
        return Calculator()


# จุดเริ่มต้นของโปรแกรม
if __name__ == '__main__':
    # สั่งรันแอป
    CalculatorApp().run()
