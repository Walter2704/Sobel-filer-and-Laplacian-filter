# 匯入library
import numpy as np
from PIL import Image

# 讀lena且轉成灰階
im = Image.open('lena.jpg').convert('L')
# 取得圖片長寬
size = im.size
# new 新圖
temp = Image.new("L", size)
temp1 = Image.new("L", size)
output = Image.new("L", size)
# 設定mask 大小
maskSize = 3

# 算一階微分和二階微分
for i in range(0 + int(maskSize / 2), size[0] - int(maskSize / 2)):
	for j in range(0 + int(maskSize / 2), size[1] - int(maskSize / 2)):
		first = abs((im.getpixel((i-1,j+1)) + 2*im.getpixel((i,j+1)) + im.getpixel((i+1,j+1))) - (im.getpixel((i-1,j-1)) + 2*im.getpixel((i,j-1)) + im.getpixel((i+1,j-1)))) + abs((im.getpixel((i+1,j-1)) + 2*im.getpixel((i+1,j)) + im.getpixel((i+1,j+1))) - (im.getpixel((i-1,j-1)) + 2*im.getpixel((i-1,j)) + im.getpixel((i-1,j+1))))
		second = (-1*im.getpixel((i-1, j-1)) + -1*im.getpixel((i, j-1)) + -1*im.getpixel((i+1, j-1)) + -1*im.getpixel((i-1, j)) + 8*im.getpixel((i, j)) + -1*im.getpixel((i+1, j)) + -1*im.getpixel((i-1, j+1)) + -1*im.getpixel((i, j+1)) + -1*im.getpixel((i+1, j+1)))
		temp.putpixel((i,j),first)
		temp1.putpixel((i,j),second)


# 把一階微分算平均濾波器且正規化並乘上二階微分，最後加上原圖
for i in range(0 + int(maskSize / 2), size[0] - int(maskSize / 2)):
	for j in range(0 + int(maskSize / 2), size[1] - int(maskSize / 2)):
		average = int(temp1.getpixel((i, j)) * ((temp.getpixel((i-1,j-1)) + temp.getpixel((i,j-1)) + temp.getpixel((i+1,j-1)) + temp.getpixel((i-1,j)) + temp.getpixel((i,j)) + temp.getpixel((i+1,j)) + temp.getpixel((i-1,j+1)) + temp.getpixel((i,j+1)) + temp.getpixel((i+1,j+1))) / 9 / 255)) + im.getpixel((i,j))
		output.putpixel((i,j),average)

# 把結果存起來
output.save("output.jpg")