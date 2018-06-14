import segment as seg
import formatimg as form
import formatog
import augmentedcnn as acnn
import testbatch as test
import numpy as np
import cv2
import letterseg as ls
from PIL import Image

imgstr = ["input/test1.png","input/test2.png","input/test3.png"]
for im in imgstr:
	box = test.runit(im) # return [tuple tl, tuple br, string label]
	imgs = seg.seg(box,im) # return [Image img1, Image img2, triple rgb, Image pil, string color]

	formatted = form.form(imgs[1],imgs[2],imgs[3], box, im) # return [Image img]
	letterImg = formatted[0].resize((28,28))
	### Return data ###
	coords = (np.mean([box[0][0],box[1][0]]),np.mean([box[0][1],box[1][1]]))
	shape = box[2]
	shapeColor = imgs[4]
	letterColor = formatted[1]
	letter = acnn.acnn(letterImg)[0]
	rotation = acnn.acnn(letterImg)[1]
	print(im)
	print("coords:" + str(coords))
	print("shape:" + shape)
	print("shape color:" + shapeColor)
	print("letter:" + letter)
	print("rotation:" + rotation)
	print("letter color:" + letterColor)

'''
Good: 
- Localization
- color - shape

ish: 
- color - letter

Not good: 
- letter ID/orientation
- shape ID (good with stars and circles tho)

'''