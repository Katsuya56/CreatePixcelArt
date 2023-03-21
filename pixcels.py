# Canvasで升目を作るプログラム

import tkinter
import tkinter.ttk as ttk

WIDTH = 900
HEIGHT = 800
M = 5
LENGTH = 600
LENG = LENGTH//M


def change_color(event):
    ID = event.widget.find_closest(event.x, event.y)
    # print(event.widget.itemconfig())
    print(event.widget.itemconfig('0,0'))
    event.widget.itemconfig(
        ID,
        fill="#ff0000"
    )


root = tkinter.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title('Combobox 1')

# Frame
frame_pixcels = tkinter.Frame(root)
frame_pixcels.place(x=WIDTH//2, y=HEIGHT//2, anchor=tkinter.CENTER)

canvas = tkinter.Canvas(
    frame_pixcels,
    width=600,
    height=600
)
# canvas.place(x=WIDTH//2, y=HEIGHT//2+10, anchor=tkinter.CENTER)
canvas.pack()
for i in range(M):
    for j in range(M):
        tag = "{},{}".format(i, j)
        print(tag)
        canvas.create_rectangle(
            LENG*i, LENG*j, LENG*i+LENG, LENG*j+LENG,
            fill="#ffffff",
            tag=tag
        )
        canvas.tag_bind(
            tag,
            "<ButtonPress>",
            change_color,
        )

# メインループ
root.mainloop()
