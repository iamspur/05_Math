```
โจทย์แบบฝึกหัดนี้เอามาจาก markpruet เพื่อใช้ฝึกฝนเขียนโปรแกรม
1.
จงเขียนโปรแกรมเพื่อแปลงเลขจำนวนเต็มลบ ให้เป็นจำนวนเต็มบวก 
n = int(input("ป้อนจำนวนเต็ม: "))
print(abs(n))
2.
จงเขียนโปรแกรมเพื่อแปลงเลขจำนวนจริงลบ แสดงตัวเลขที่ปัดทศนิยมขึ้น และเป็นจำนวนเต็มบวก
import math
n = float(input("ป้อนตัวเลขจำนวนจริง: "))
print(math.ceil(abs(n)))
3.
จงเขียนโปรแกรมเพื่อคำนวณหาพื้นที่วงกลมและเส้นรอบวงของวงกลมที่มีรัศมี r  
กำหนดให้ข้อมูลเข้าเป็นเลขจำนวนเต็มเท่านั้น แสดงพื้นที่และเส้นรอบวงเป็นเลขจำนวนจริงทศนิยมสองตำแหน่ง
import math
r = int(input("Enter a radius: "))
area = math.pi * (r ** 2)
circum = 2 * math.pi * r
print(f"Area of a circle with radius {r} is {area:.2f}")
print(f"Circumference of a circle with radius {r} is {circum:.2f}")
