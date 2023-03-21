# 01でカラーコードを設定して画像を生成するサンプルコード

import numpy as np
import cv2
from PIL import Image


def get_gradient_3d(length, square, coler_list):
    width = length
    height = length
    square_length = length//square
    image = np.full((width, height, 3),0,dtype=np.uint8)
	
    for w in range(width):
        for h in range(height):
            image[h][w][0] = coler_list[h//square_length][w//square_length][0]
            image[h][w][1] = coler_list[h//square_length][w//square_length][1]
            image[h][w][2] = coler_list[h//square_length][w//square_length][2]
    return image

length = 600
square_num = 3
# gradient_image_path = "C:/Users/inkat/Code/python/PixcelArtSelf/Art.png"
gradient_image_path = "./Art1.png"
coler_list = np.full((square_num, square_num, 3),0,dtype=np.uint8)
# False
# False
coler_list[0][0][0] = np.uint8(0)
coler_list[0][0][1] = np.uint8(0)
coler_list[0][0][2] = np.uint8(0)

coler_list[0][1][0] = np.uint8(255)
coler_list[0][1][1] = np.uint8(255)
coler_list[0][1][2] = np.uint8(255)

coler_list[0][2][0] = np.uint8(0)
coler_list[0][2][1] = np.uint8(0)
coler_list[0][2][2] = np.uint8(0)


coler_list[1][0][0] = np.uint8(255)
coler_list[1][0][1] = np.uint8(255)
coler_list[1][0][2] = np.uint8(255)

coler_list[1][1][0] = np.uint8(0)
coler_list[1][1][1] = np.uint8(0)
coler_list[1][1][2] = np.uint8(0)

coler_list[1][2][0] = np.uint8(255)
coler_list[1][2][1] = np.uint8(255)
coler_list[1][2][2] = np.uint8(255)


coler_list[2][0][0] = np.uint8(0)
coler_list[2][0][1] = np.uint8(0)
coler_list[2][0][2] = np.uint8(0)

coler_list[2][1][0] = np.uint8(255)
coler_list[2][1][1] = np.uint8(255)
coler_list[2][1][2] = np.uint8(255)

coler_list[2][2][0] = np.uint8(0)
coler_list[2][2][1] = np.uint8(0)
coler_list[2][2][2] = np.uint8(0)
# グラデーションの生成
# BGR
gradient = get_gradient_3d(length, square_num, coler_list)
# グラデーション画像の保存
cv2.imwrite(gradient_image_path, gradient)