import cv2
import numpy as np
#import matplotlib.pyplot as plt
#from picamera import PiCamera


def image_processing(img_direction):
	img = cv2.imread(img_direction)
	image = cv2.bitwise_not(src=img)
	gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	res, dst = cv2.threshold(gray,0 ,255, cv2.THRESH_OTSU)
	element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3, 3))
	dst = cv2.morphologyEx(dst,cv2.MORPH_OPEN,element)
	contours, hierarchy = cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(dst,contours,-1,(120,0,0),2)
	return contours, img

def count(contours, img):
	count = 0
	ares_avrg = 0
	final_cont = 0 

	for cont in contours:
		ares = cv2.contourArea(cont)
		if ares>50:
			count += 1
			ares_avrg += ares
			print("{},{}".format(count,ares),end="\n")
			"""
			# draw the box around each worms
			rect = cv2.boundingRect(cont)
			print("x:{} y:{}".format(rect[0],rect[1]))
			cv2.rectangle(img,rect,(0,0,0xff),1)
			y=10 if rect[1]<10 else rect[1]
			cv2.putText(img,str(count), (rect[0], y), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 255, 0), 1)
			"""

	print("Average area:{}".format(round(ares_avrg/ares,2)))
	final_cont = final_cont + count
	print(final_cont)
	#cv2.namedWindow("imagshow", 2)
	#cv2.imshow('imagshow', img)
	return final_cont

# test code on PC	
image_direction = "C:\\Users\\TIR\\Desktop\\project\\image.jpg"
contours, img = image_processing(image_direction)
final_cont = count(contours, img)
cv2.waitKey()

"""
# test code on Pi
camera = PiCamera()
counter = 0
while counter < 20:
	image_direction = camera.capture('/home/pi/Desktop/image.jpg')
	countours, img = image_processing(image_direction)
	final_cont = count(contours, img)
	final_cont += final_cont
	counter += 1
avg_num = final_cont / counter
print("Avarage number of worms:{}".format(round(avg_num)))
"""	