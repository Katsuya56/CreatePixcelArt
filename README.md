# PixcelArt
N×Nピクセルのピクセルアートを作成するプログラム

# 概要
tkinterを使ってN×NマスのGUIを操作してピクセルアートを作成します

OpenCVを使ってnumpy配列から画像を作成しています

# 備考
そのままDockerで実行すると以下のエラーが出た
```
ImportError: libGL.so.1: cannot open shared object file: No such file or directory
```
以下のコマンドで解決した
```
apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
```

# 参考記事
[stackoverflow ImportError: libGL.so.1: cannot open shared object file: No such file or directory](https://stackoverflow.com/questions/55313610/importerror-libgl-so-1-cannot-open-shared-object-file-no-such-file-or-directo)
