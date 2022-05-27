
#基本没啥用，只适合简单的图片

#这些代码用于解析验证码

'''import tesserocr
from PIL import Image
image = Image.open('/Users/yujunxiong/Desktop/1.gif')
result = tesserocr.image_to_text(image)
print(result)'''

'''import tesserocr
print(tesserocr.file_to_text('/Users/yujunxiong/Desktop/RandCode.gif'))
'''



'''import tesserocr
from PIL import Image

image = Image.open('/Users/yujunxiong/Desktop/1.jpeg')

image.show()  # 可以打印出图片，供预览
print(tesserocr.image_to_text(image))
'''

'''import tesserocr
from PIL import Image
image=Image.open('test.png')
image=image.convert("L")#convert()方法传参L，即可将图片转为灰度图。   传入1即可完成二值化
threshold=80
table=[]
for i in range(256):
    if i <threshold:
        table.append(0)
    else:
        table.append(1)
image=image.point(table,'1')
image.show()
print(tesserocr.image_to_text(image))'''
