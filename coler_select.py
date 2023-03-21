# Scaleを使った色選択のサンプルコード(ライブラリがあったため使わなかった)

import tkinter

hoge = 10
WIDTH = 900
HEIGHT = 800
M = 5
LENGTH = 600
LENG = LENGTH//M

def coler_select(event):
    r=int(val_red.get())
    g=int(val_green.get())
    b=int(val_blue.get())
    canvas['bg']="#{:02x}{:02x}{:02x}".format(r,g,b)

window = tkinter.Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")
window.title('Combobox 1')

# Frame 
frame = tkinter.Frame(window)
frame.place(x=WIDTH//2,y=HEIGHT//2,anchor=tkinter.CENTER)

# Red
lavel_red = tkinter.Label(
    frame,text="Red"
)
lavel_red.grid(row=0,column=0)
val_red = tkinter.DoubleVar()
sc_red = tkinter.Scale(
    frame,
    variable=val_red,
    orient=tkinter.HORIZONTAL,
    length=200,
    from_=0,
    to=255,
    command=coler_select
)
sc_red.grid(row=0,column=1)
# Green
lavel_green = tkinter.Label(
    frame,text="Green"
)
lavel_green.grid(row=1,column=0)
val_green = tkinter.DoubleVar()
sc_green = tkinter.Scale(
    frame,
    variable=val_green,
    orient=tkinter.HORIZONTAL,
    length=200,
    from_=0,
    to=255,
    command=coler_select
)
sc_green.grid(row=1,column=1)
# Blue
lavel_blue = tkinter.Label(
    frame,text="Blue"
)
lavel_blue.grid(row=2,column=0)
val_blue = tkinter.DoubleVar()
sc_blue = tkinter.Scale(
    frame,
    variable=val_blue,
    orient=tkinter.HORIZONTAL,
    length=200,
    from_=0,
    to=255,
    command=coler_select
)
sc_blue.grid(row=2,column=1)

# Button
button1 = tkinter.Button(
    frame,
    text='OK',
    command=lambda: print('R:%4d\nG:%4d\nB:%4d\n' % (val_red.get(),val_green.get(),val_blue.get()))
)
button1.grid(row=4,column=3)
canvas = tkinter.Canvas(
    frame,
    # width=100,
    height=50,

    bg="#000000"
)
canvas.grid(row=3,column=0,columnspan=2,sticky = tkinter.EW)

window.mainloop()
