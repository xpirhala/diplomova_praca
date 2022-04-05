from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

from PIL import Image




def decode(im,name) :
  # Find barcodes and QR codes
  im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  #im = cv2.medianBlur(im, 5)
  #im_gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)

  #th, im_gray_th_otsu = cv2.threshold(im_gray, 128, 192, cv2.THRESH_OTSU)
  decodedObjects = pyzbar.decode(im)
  cv2.imshow(name, im)
  # Print results
  for obj in decodedObjects:
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')

  return decodedObjects

# Display barcode and QR code location
def display(im, decodedObjects,name):

  # Loop over all decoded objects
  for decodedObject in decodedObjects:
    points = decodedObject.polygon

    # If the points do not form a quad, find convex hull
    if len(points) > 4 :
      hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else :
      hull = points

    # Number of points in the convex hull
    n = len(hull)

    # Draw the convext hull
    for j in range(0,n):
      cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)

  # Display results
  cv2.imshow(name, im)
  

# Main
if __name__ == '__main__':

  # Read image

  vid0 = cv2.VideoCapture(0)
  vid1 = cv2.VideoCapture(1)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret0, frame0 = vid0.read()
    ret1, frame1 = vid1.read()
    #im = cv2.imread('QR1.jpg')

    decodedObjects0 = decode(frame0,"frame0+0")
    decodedObjects1 = decode(frame1,"frame1+1")
    #display(im, decodedObjects)
    display(frame0, decodedObjects0,"frame0")
    display(frame1, decodedObjects1,"frame1")
    #cv2.imshow('frame0', frame0)
    #cv2.imshow('frame1', frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid0.release()
vid1.release()
# Destroy all the windows
cv2.destroyAllWindows()

