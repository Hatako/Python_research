import tkinter

root = tkinter.Tk()

val = tkinter.IntVar()
val.set(0)

def func(scl):
    label.config(text = 'value = {}'.format(int(scl)))
    print(val.get())

label = tkinter.Label(root, text = 'value = {}'.format(val.get()))
label.pack()

s = tkinter.Scale(root, label = 'scale', orient ='h', from_ = 0, to = 1000, showvalue = True, variable = val, command = func, length = 1000)
s.pack()

root.mainloop()
