# PixcelArt

N×N ピクセルのピクセルアートを作成するプログラム

# 環境構築方法

1. 仮想環境を立てる

   ```
   python -m venv .venv
   ```

1. vscode 上の Python の拡張機能が、実行する Python を仮想環境のものにするか聞いてくるので Yes を選択する

1. pip の更新

   ```
   python.exe -m pip install --upgrade pip
   ```

1. ライブラリをインストールする
   ```
   pip install -r requirements.txt
   ```

# 処理順序

1. セレクトメニューで縦・横のピクセルの数を選択する
1. ボタンを押して次の画面へ
1. ピクセルをクリックすると色を選択できるようになる
1. 色を選択する
1. 3.4.をくりかえり
1. Criate ボタンで画像を生成
1. Back ボタンで最初の画面へ

# 使っているライブラリ

requirements.txt

```text
numpy==2.0.0
opencv-python==4.10.0.84
pillow==10.4.0
```

# 自分の環境

- OS
  windows11
- Python
  3.11.1
