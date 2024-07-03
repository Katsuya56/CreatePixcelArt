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
DFRGB = "#ffffff"	# デフォルトの色

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
	combobox = ttk.Combobox(
		frame_home,
		state="readonly",
		textvariable=v,
		values=numbers, 
		width=10
	)
	combobox.set(numbers[0])
	combobox.grid(row=0, column=0)

	# Button
	select_button = tk.Button(
		frame_home,
		text='OK',
		command=lambda: [get_sell_num(), frame_home.destroy(), pixcels()]
	)
	select_button.grid(row=0, column=1)

# セルの編集画面
def pixcels():
	# 画像の作成
	def criate_image():
		# coler_list	RBG
		# image BRG
		width = LENGTH
		height = LENGTH
		square_length = LENGTH//SELL_NUM
		image = np.full((width, height, 3), 0, dtype=np.uint8)
		for x in range(height):
			for y in range(width):
				image[x][y][0] = coler_list[x // square_length][y//square_length][1]
				image[x][y][1] = coler_list[x // square_length][y//square_length][2]
				image[x][y][2] = coler_list[x // square_length][y//square_length][0]
		cv2.imwrite("image/Art.png", image)

	# 色変更
	def change_color(event):
		ID = event.widget.find_closest(event.x, event.y)
		tag = event.widget.gettags(ID)
		x, y = (int(i) for i in tag[0].split(","))
		color = colorchooser.askcolor()
		"""colorchooser.askcolor()の返り値
			((255, 255, 255), '#ffffff')
			color[0]: RGBの整数のタプル
			color[1]: カラーコードの文字列
		"""
		coler_list[x][y][0] = np.uint8(color[0][0])
		coler_list[x][y][1] = np.uint8(color[0][1])
		coler_list[x][y][2] = np.uint8(color[0][2])
		event.widget.itemconfig(
			ID,
			fill=color[1]
		)

	# 画像用のnumpy配列を作成
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
	for x in range(SELL_NUM):
		for y in range(SELL_NUM):
			tag = "{},{}".format(x, y)
			# キャンバスの設定
			canvas.create_rectangle(
				LENG*x, LENG*y, LENG*x+LENG, LENG*y+LENG,
				fill=DFRGB,
				tag=tag
			)
			# キャンバスをクリック時の設定
			canvas.tag_bind(
				tag,
				"<ButtonPress>",
				change_color,
			)

	# ホームウィンドウに戻る
	close_button = tk.Button(
		frame_pixcels,
		text='Back',
		command=lambda: [frame_pixcels.destroy(), home()]
	)
	close_button.pack()

	# 画像を生成
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
