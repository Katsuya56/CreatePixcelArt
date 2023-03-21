# home画面単体のコード

import tkinter
import tkinter.ttk as ttk

WIDTH = 900
HEIGHT = 800

numbers = [2, 3, 4, 5]

root = tkinter.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title('Combobox 1')

# Frame 
frame = ttk.Frame(root, padding=10)
frame.place(x=WIDTH//2,y=HEIGHT//2,anchor=tkinter.CENTER)

# Combobox
v = tkinter.StringVar()
cb = ttk.Combobox(
    frame,
    textvariable=v,
    state="readonly",              
    values=numbers,
    width=10
)
cb.set(numbers[0])
cb.grid(row=0, column=0)

# Button
button1 = tkinter.Button(
    frame, text='OK', command=lambda: print('v=%s' % v.get()))
button1.grid(row=0, column=1)

root.mainloop()