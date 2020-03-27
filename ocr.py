# Using Tesseract OCR with Python
# TO RUN THE CODE: python ocr.py --image sample_images/example_01.png


# import the  necessary packages
from PIL import Image
import pytesseract
import argparse
from cv2 import cv2
import os

# 3.26.20 -- going to comment this out for now until I get a beter handle on 
# the pdf->image->OCR the image->reassemble pipeline
import pdf_page_to_image


# construct the argument parser 
# NOTE: that by importing pdf_page_to_image  you now require new args (-p, --pdf)
# NOTE: set the required=False as I don't have any images yet when I'm trying to use 
# pdf_page_to_image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False, 
    help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
    help="type of preprocessing to be done")
args = vars(ap.parse_args())


# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# check to see if we should apply thresholding to preprocess the image
if args["preprocess"] == "thresh":
    gray = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# make a check to see if median blurring should be done to remove noise
elif args["preprocess"] == "blur":
    gray == cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temporary file so we can apply OCR 
# to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temp file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

# show the output images
cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)