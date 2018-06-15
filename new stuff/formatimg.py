import numpy as np
import cv2
import os
import PIL.ImageOps  
from PIL import Image
import segment
from PIL import ImageFilter
import segment as seg

np.set_printoptions(threshold=np.nan)

def euclidean(r,g,b,rav,gav,bav):
	return(((r-rav)**2)+((g-gav)**2)+((b-bav)**2))

# for f in os.listdir("img2"):
def form(gray, color, original, box, stringimg):
	## Gets absolute bound of shape
	w,h = gray.size
	img = PIL.ImageOps.invert(gray)
	mat = np.array(img)
	left = right = top = bottom = 0
	for col_num in range(w):
		if 255 in mat[:, col_num]:
			right = col_num
			if left == 0:
				left = col_num
	for row_num in range(h):
		if 255 in mat[row_num, :]:
			bottom = row_num
			if top == 0:
				top = row_num

	meanEuclid = ind = 0

	letter = np.zeros((max(right-left, bottom-top),max(right-left, bottom-top)))
	cropped = img.crop((left, top, left+max(right-left, bottom-top), top + max(right-left, bottom-top))) # crop the grayscale
	croppedColor = original.crop((left, top, left+max(right-left, bottom-top), top + max(right-left, bottom-top)))
	rav=gav=bav=0
	for x in range(max(right-left, bottom-top)):
		for y in range(max(right-left, bottom-top)):
			if cropped.getpixel((x,y)) == 255:
				r, g, b = croppedColor.getpixel((x, y))
				rav+=r
				gav+=g
				bav+=b
				ind+=1
	rav/=ind
	gav/=ind
	bav/=ind

	ind=0
	for x in range(max(right-left, bottom-top)):
		for y in range(max(right-left, bottom-top)):
			if cropped.getpixel((x,y)) == 255:
				r, g, b = croppedColor.getpixel((x, y))
				ind += 1
				meanEuclid += euclidean(r,g,b,rav,gav,bav)
	meanEuclid = meanEuclid/ind
	for x in range(max(right-left, bottom-top)):
		for y in range(max(right-left, bottom-top)):
			if cropped.getpixel((x,y)) == 255:
				r, g, b = croppedColor.getpixel((x, y))
				if euclidean(r,g,b,rav,gav,bav) >= meanEuclid*2:
					letter[y][x] = 255

	let = Image.fromarray(letter)
	let = let.filter(ImageFilter.MedianFilter(size=3))
	# let is your image

	w,h = let.size # switch?
	left = right = top = bottom = 0

	## Get average color of mask (again)
	rav=gav=bav=ind=0
	arrLet = np.array(let)
	for col_num in range(w):
		if 255 in arrLet[:, col_num]:
			right = col_num
			if left == 0:
				left = col_num
	for row_num in range(h):
		if 255 in arrLet[row_num, :]:
			bottom = row_num
			if top == 0:
				top = row_num
	margin = 5
	cropped = let.crop(
		   (max(left-margin,0), 
			max(top-margin,0), 
			min(left+max(right-left, bottom-top)+margin,w),
			min(top + max(right-left, bottom-top)+margin,h)))
	for x in range(w):
		for y in range(h):
			if let.getpixel((x,y)) == 255:
				b,g,r = croppedColor.getpixel((x, y))
	
				rav+=r
				gav+=g
				bav+=b
				ind+=1
	rav/=ind
	gav/=ind
	bav/=ind
	return(let,seg.minEuclideanDist(rav,gav,bav))
	# ind=0
	# for x in range(w):
	# 	for y in range(h):
	# 		if let.getpixel((x,y)) == 255:
	# 			r, g, b = croppedColor.getpixel((x, y))
	# 			ind += 1
	# 			meanEuclid += euclidean(r,g,b,rav,gav,bav)
	# meanEuclid = meanEuclid/ind
	# letter = np.zeros((w,h))
	# for x in range(w):
	# 	for y in range(h):
	# 		if let.getpixel((x,y)) == 255:
	# 			r, g, b = croppedColor.getpixel((x, y))
	# 			if euclidean(r,g,b,rav,gav,bav) <= meanEuclid*3:
	# 				letter[x][y] = 255
	# img = Image.fromarray(np.uint8(letter) , 'L')
	# print(right)
	# print(left)
	# print(top)
	# print(bottom)

	# cropped = let.crop((left, top, left+max(right-left, bottom-top), top + max(right-left, bottom-top)))
	# padded = np.array(cropped)
	# shape = padded.shape
	# padded = np.vstack([padded, np.zeros((2,shape[0]))])
	# padded = np.vstack([np.zeros((2,shape[0])), padded])
	# padded = np.hstack([padded, np.zeros((shape[0]+4,2))])
	# padded = np.hstack([np.zeros((shape[0]+4,2)), padded])
	# img = Image.fromarray(np.uint8(padded) , 'L')
	# img.show()
	# img = img.resize((28,28))
	# img.show()
#	img = img.filter(ImageFilter.BoxBlur(1))

	# return img
	
# gray = segment.seg()[1]
# h,w = gray.shape
# ret,binarized_img = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# n = -((np.array(binarized_img)/255)-1)
# img = Image.fromarray(np.uint8(n * 255) , 'L')
# mat = np.array(img)
# left = right = top = bottom = 0
# for col_num in range(w):
# 	if 255 in mat[:, col_num]:
# 		right = col_num
# 		if left == 0:
# 			left = col_num
# for row_num in range(h):
# 	if 255 in mat[row_num, :]:
# 		bottom = row_num
# 		if top == 0:
# 			top = row_num

# cropped = img.crop((left, top, left+max(right-left, bottom-top), top + max(right-left, bottom-top)))
# padded = np.array(cropped)/255
# shape = padded.shape
# padded = np.vstack([padded, np.zeros((5,shape[0]))])
# padded = np.vstack([np.zeros((5,shape[0])), padded])
# padded = np.hstack([padded, np.zeros((shape[0]+10,5))])
# padded = np.hstack([np.zeros((shape[0]+10,5)), padded])
# img = Image.fromarray(np.uint8(padded * 255) , 'L')
# cv2.imshow("h",img)
# cv2.waitKey(0)