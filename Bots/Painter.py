import keyboard
import mouse
import time
import os

paint_path = "C:\WINDOWS\system32\mspaint.exe"
os.startfile(paint_path)
# wait for paint to start
time.sleep(2)

mouse.move(-100000, -1000000, absolute=False, duration=0.1)
mouse.move(200, 200, absolute=False, duration=0.1)

mouse.drag(0, 0, 600, 0, absolute=False, duration=0.3)
mouse.drag(0, 0, 0, 350, absolute=False, duration=0.3)
mouse.drag(0, 0, -600, 0, absolute=False, duration=0.3)
mouse.drag(0, 0, 0, -350, absolute=False, duration=0.3)
mouse.drag(0, 350/3, 600, 0, absolute=False, duration=0.3)
mouse.drag(0, 350/3, -600, 0, absolute=False, duration=0.3)
mouse.drag(300, 0, 0, -350/3, absolute=False, duration=0.3)
mouse.drag(-350/6, 350/6, 350/3, 0, absolute=False, duration=0.3)


#circle
mouse.move(-100000, -1000000, absolute=False, duration=0.1)
mouse.move(391, 57, absolute=False, duration=0.1)
mouse.click('left')
mouse.drag(50, 260, 350/3, 337/3, absolute=False, duration=0.2)
#fill
mouse.move(-100000, -1000000, absolute=False, duration=0.1)
mouse.move(252, 67, absolute=False, duration=0.1)
mouse.click('left')
mouse.move(798-252, -7, absolute=False, duration=0.1)
mouse.click('left')
mouse.move(-200, 200, absolute=False, duration=0.1)
mouse.click('left')
mouse.move(240, -200, absolute=False, duration=0.1)
mouse.click('left')
mouse.move(-240, 450, absolute=False, duration=0.1)
mouse.click('left')
mouse.move(285, -450, absolute=False, duration=0.1)
mouse.click('left')
mouse.move(-395, 270, absolute=False, duration=0.1)
mouse.click('left')
mouse.move(30, 0, absolute=False, duration=0.1)
mouse.click('left')
mouse.move(0, 60, absolute=False, duration=0.1)
mouse.click('left')
mouse.move(-50, 0, absolute=False, duration=0.1)
mouse.click('left')

#type
mouse.move(-100000, -1000000, absolute=False, duration=0.1)
mouse.move(271, 61, absolute=False, duration=0.1)
mouse.click('left')
mouse.drag(-99, 510 , 800, 70, absolute=False, duration=0.1)
keyboard.write("Feeling a Proud Indian Army!!")
mouse.move(10, 10, absolute=False, duration=0.1)
mouse.click('left')




