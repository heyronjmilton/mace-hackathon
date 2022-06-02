# Python code for Multiple Color Detection


import numpy as np
import cv2,csv
import os,time


# Capturing video through webcam
webcam = cv2.VideoCapture(2)

def put1 (a):
    with open("QINDEX.csv",mode='w') as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerow([int(a)]) 
        csvfile.close()
        print("done")

# Start a while loop
while(1):

	yellowarea=float(0.0)
	greenarea=float(0.0) 
	ygare=float(0.0)
	brownarea=float(0.0)
	blackarea=float(0.0)
	# Reading the video from the
	# webcam in image frames
	_, imageFrame = webcam.read()

	# Convert the imageFrame in
	# BGR(RGB color space) to
	# HSV(hue-saturation-value)
	# color space
	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)


	# Set range for green color and
	# define mask
	green_lower = np.array([70/360*255, 20/100*255, 29/100*255], np.uint8)
	green_upper = np.array([144/360*255, 48/100*255, 40/100*255], np.uint8)
	green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)


	# Set range for black color and
	# define mask
	black_lower = np.array([60/360*255, 9/100*255, 19/100*255], np.uint8)
	black_upper = np.array([144/360*255, 20/100*255, 27/100*255], np.uint8)
	black_mask = cv2.inRange(hsvFrame, black_lower, black_upper)



    	# Set range for yellow color and
	# define mask
	yellow_lower = np.array([50/360*255, 30/100*255, 35/100*255], np.uint8)
	yellow_upper = np.array([80/360*255, 50/100*255, 60/100*255], np.uint8)
	yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)


	    	# Set range for brown color and
	# define mask
	brown_lower = np.array([10.625, 76.5, 68.85], np.uint8)
	brown_upper = np.array([15.83,127.5, 153.5], np.uint8)
	brown_mask = cv2.inRange(hsvFrame, brown_lower, brown_upper)

	    	# Set range for yellow-green color and
	# define mask
	yg_lower = np.array([24.79,161.415, 89.25], np.uint8)
	yg_upper = np.array([34, 229.5, 140], np.uint8)
	yg_mask = cv2.inRange(hsvFrame, yg_lower, yg_upper)
	
	
	# Morphological Transform, Dilation
	# for each color and bitwise_and operator
	# between imageFrame and mask determines
	# to detect only that particular color
	kernal = np.ones((5, 5), "uint8")
	

	# For green color
	green_mask = cv2.dilate(green_mask, kernal)
	res_green = cv2.bitwise_and(imageFrame, imageFrame,
								mask = green_mask)
	

    # For yellow color
	yellow_mask = cv2.dilate(yellow_mask, kernal)
	res_yellow = cv2.bitwise_and(imageFrame, imageFrame,
							mask = yellow_mask)


    # For yellow-green color
	yg_mask = cv2.dilate(yg_mask, kernal)
	res_yg = cv2.bitwise_and(imageFrame, imageFrame,
							mask = yg_mask)


       # For brown color
	brown_mask = cv2.dilate(brown_mask, kernal)
	res_brown = cv2.bitwise_and(imageFrame, imageFrame,
							mask = brown_mask)

	 # For black color
	black_mask = cv2.dilate(black_mask, kernal)
	res_black = cv2.bitwise_and(imageFrame, imageFrame,
							mask = black_mask)

	# Creating contour to track yelloe color
	contours, hierarchy = cv2.findContours(yellow_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		yellowarea=cv2.contourArea(contour)+yellowarea


# Creating contour to track brown color
	contours, hierarchy = cv2.findContours(brown_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		brownarea=cv2.contourArea(contour)+brownarea

	# Creating contour to track black color
	contours, hierarchy = cv2.findContours(black_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		blackarea=cv2.contourArea(contour)+blackarea


	# Creating contour to track green color
	contours, hierarchy = cv2.findContours(green_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		greenarea=cv2.contourArea(contour)+greenarea

	# Creating contour to track yellow-green color
	contours, hierarchy = cv2.findContours(yg_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		ygarea= cv2.contourArea(contour)
		if(area > 300):
			x, y, w, h = cv2.boundingRect(contour)
			imageFrame = cv2.rectangle(imageFrame, (x, y),
									(x + w, y + h),
									(0, 255, 0), 2)
			
			cv2.putText(imageFrame, "yellow-Green Colour", (x, y),
						cv2.FONT_HERSHEY_SIMPLEX,
						1.0, (0, 255, 0))

	# Program Termination
	resizeg = cv2.resize(green_mask, (500, 250)) 
	resizey = cv2.resize(yellow_mask, (500, 250)) 
	resizeb = cv2.resize(black_mask, (500, 250)) 
	resizef = cv2.resize(imageFrame, (500, 250)) 
	cv2.imshow("green", resizeg)
	cv2.imshow("yellow", resizey)
	cv2.imshow("black", resizeb)
	cv2.imshow("webcam", resizef)

    

	if greenarea>yellowarea and greenarea>1000:
		if blackarea>2000:
			print("LEAF MIGHT HAVE DISEASE")
			time.sleep(1)
			os.system("cls")
			put1(6)
		else:
			print("LEAF IS HEALTHY")
			put1(5)
			time.sleep(0.1)
			os.system("cls")




	
	if greenarea<yellowarea and yellowarea>1000 :
		print("LEAF HAS MOISTURE PROBLEM")
		put1(3)
		time.sleep(0.1)
		os.system("cls")

	if greenarea<1000 and yellowarea<1000 :
		print("no leaf")
		put1(0)
		time.sleep(0.1)
		os.system("cls")
	

    
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
    


