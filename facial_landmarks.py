# import packages
from imutils import face_utils
import numpy as np 
import argparse 
import imutils 
import dlib 
import cv2 

# construct the argument parser and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
    help="path to dlib's facial landmark predictor")
ap.add_argument("-i", "--image", required=True,
    help="path to input image")
args = vars(ap.parse_args())

# initalize dlib's face detector (HOG-based)
# then create the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# load the input image, resize it, and convert to grayscale
image = cv2.imread(args["image"])
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the grayscale image
rects = detector(gray, 1)

# loop over the face detections
for i, rect in enumerate(rects):
    # determine the facial landmarks for the face region,
    # then convert the facial landmark (x, y)-coordinates to a 
    # numpy array
    shape = predictor(gray, rect)
    shape = face_utils.shape_to_np(shape)

    # convert dlib's rectangle to an OpenCV-style
    # bounding box (x, y, w, h) then draw the bounding box
    (x, y, w, h) = face_utils.rect_to_bb(rect)
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)

    # show the face number
    cv2.putText(image, "Face #{}".format(i+1), (x - 10, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
    
    # loop over the (x, y)-coordinates for the facial landmarks
    # and draw them on the image
    for (x, y) in shape:
        cv2.circle(image, (x, y), 1, (245, 66, 221), -1)
    
# show the output image with the face detectinos + facial landmarks
cv2.imshow("Output", image)
cv2.waitKey(0)
