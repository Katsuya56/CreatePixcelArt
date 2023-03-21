# 画面遷移のサンプルコード

# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk

def make():
    global frame

    # frame_app.destroy()

    # メインフレームの作成と設置
    frame = ttk.Frame(root)
    frame.pack(fill = tk.BOTH, pady=20)

    # 各種ウィジェットの作成
    label1_frame = ttk.Label(frame, text="メインウィンドウ")
    entry1_frame = ttk.Entry(frame)
    button_change = ttk.Button(frame, text="Change", command=lambda:[frame.destroy(), change()])

    # 各種ウィジェットの設置
    label1_frame.pack()
    entry1_frame.pack()
    button_change.pack()

# command=lambda:[funcA(), funcB(), funcC()]
def change():
    global frame_app

    # frame.destroy()

    # メインフレームの作成と設置
    frame_app = ttk.Frame(root)
    frame_app.pack(fill = tk.BOTH, pady=20)

    # 各種ウィジェットの作成
    label1_frame_app = ttk.Label(frame_app, text="アプリウィンドウ")
    entry1_frame_app = ttk.Entry(frame_app)
    button_change_frame_app = ttk.Button(frame_app, text="Buck", command=lambda:[frame_app.destroy(), make()])

    # 各種ウィジェットの設置
    label1_frame_app.pack()
    entry1_frame_app.pack()
    button_change_frame_app.pack()

if __name__ == "__main__":
    # rootメインウィンドウの設定
    root = tk.Tk()
    root.title("tkinter application")
    root.geometry("300x150")
    make()
    root.mainloop()