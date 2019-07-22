#tkinterで作成したGUI上で移動ロボットのモータを動かすプログラム

import tkinter
#import smbus
import time

#i2c = smbus.SMBus(1)
#adr1 = 0x64
#adr2 = 0x63


# 正転
logic = 0b01
iniMotor = 5

root = tkinter.Tk()
val1 = tkinter.IntVar()
val1.set(iniMotor)

val2 = tkinter.IntVar()
val2.set(iniMotor)
#i2c.write_byte_data(adr1, 0, iniMotor)
#i2c.write_byte_data(adr2, 0, iniMotor)

def right(scl1):
    Motor1 = (int(scl1)<<2 | logic)
#    i2c.write_byte_data(adr1, 0, Motor1)
    print('右モータ: {}'.format(Motor1))

def left(scl2):
    Motor2 = (int(scl2) << 2 | logic)
#    i2c.write_byte_data(adr2, 0, Motor2)
    print('左モータ: {}'.format(Motor2))

label = tkinter.Label(root, text = 'モータ制御')
label.pack()


s1 = tkinter.Scale(root, label = '右モータ', orient = 'h', from_=iniMotor, to = 63,
                   showvalue = True, variable = val1, command = right, length = 600)
s1.pack()

s2 = tkinter.Scale(root, label = '左モータ', orient = 'h', from_=iniMotor, to = 63,
                   showvalue = True, variable = val2, command = left, length = 600)
s2.pack()

root.mainloop()

