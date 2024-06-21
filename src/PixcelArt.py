# ピクセルアートを作成するためのプログラム
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import colorchooser
import numpy as np
import cv2

# 定数
WIDTH = 900  # 幅
HEIGHT = 900  # 高さ
LENGTH = 800  # 画像の大きさ
SELL_NUM = 2  # セルの数
DFRGB = "#ffffff"

# セルの数の選択画面


def home():
	# セルの数を設定
	def get_sell_num():
		global SELL_NUM
		SELL_NUM = int(v.get())
	# Frame
	frame_home = ttk.Frame(root, padding=10)
	frame_home.place(x=WIDTH//2, y=HEIGHT//2, anchor=tk.CENTER)

	# セルの数の種類
	numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

	# Combobox
	v = tk.StringVar()
	cb = ttk.Combobox(
		frame_home, state="readonly", textvariable=v,
		values=numbers, width=10
	)
	cb.set(numbers[0])
	cb.grid(row=0, column=0)

	# Button
	button1 = tk.Button(
		frame_home,
		text='OK',
		command=lambda: [get_sell_num(), frame_home.destroy(), pixcels()]
	)
	button1.grid(row=0, column=1)

# セルの編集画面


def pixcels():
	# 画像の作成
	def criate_image():
		# coler_list	RBG
		# image 	BGR
		width = LENGTH
		height = LENGTH
		square_length = LENGTH//SELL_NUM
		image = np.full((width, height, 3), 0, dtype=np.uint8)
		for h in range(height):
			for w in range(width):
				image[h][w][0] = coler_list[h // square_length][w//square_length][1]
				image[h][w][1] = coler_list[h //square_length][w//square_length][2]
				image[h][w][2] = coler_list[h //square_length][w//square_length][0]
		cv2.imwrite("image/Art.png", image)

	# 色変更
	def change_color(event):
		ID = event.widget.find_closest(event.x, event.y)
		tag = event.widget.gettags(ID)
		h, w = (int(i) for i in tag[0].split(","))
		c = colorchooser.askcolor()
		coler_list[h][w][0] = np.uint8(c[0][0])
		coler_list[h][w][1] = np.uint8(c[0][1])
		coler_list[h][w][2] = np.uint8(c[0][2])
		event.widget.itemconfig(
			ID,
			fill=c[1]
		)

	coler_list = np.full((SELL_NUM, SELL_NUM, 3), 255, dtype=np.uint8)
	LENG = LENGTH//SELL_NUM

	# Frame
	frame_pixcels = ttk.Frame(root, padding=10)
	frame_pixcels.place(x=WIDTH//2, y=HEIGHT//2, anchor=tk.CENTER)

	# Canvas
	canvas = tk.Canvas(
		frame_pixcels,
		width=LENGTH,
		height=LENGTH
	)
	canvas.pack()
	for i in range(SELL_NUM):
		for j in range(SELL_NUM):
			tag = "{},{}".format(j, i)
			canvas.create_rectangle(
				LENG*i, LENG*j, LENG*i+LENG, LENG*j+LENG,
				fill=DFRGB,
				tag=tag
			)
			canvas.tag_bind(
				tag,
				"<ButtonPress>",
				change_color,
			)

	# close_button
	close_button = tk.Button(
		frame_pixcels,
		text='Close',
		command=lambda: [frame_pixcels.destroy(), home()]
	)
	close_button.pack()

	# criate_button
	criate_button = tk.Button(
		frame_pixcels,
		text='Criate',
		command=lambda: [criate_image()]
	)
	criate_button.pack()


# rootメインウィンドウの設定
root = tk.Tk()
root.title("tk application")
root.geometry(f"{WIDTH}x{HEIGHT}")
home()
root.mainloop()
