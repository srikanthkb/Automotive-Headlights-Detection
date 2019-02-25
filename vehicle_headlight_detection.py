import numpy as np
from matplotlib import pyplot as plt
import cv2
import time


def wait(t):
    time.sleep(t)


#List includes path for images representing different scenarios
mylist=['bus_coming.jpg','going.jpg','both.jpg']



#Condition: No vehicle
def scenario(condition):
    image = cv2.imread(condition)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray_image.png',gray_image)
    cv2.imshow('color_image',image)
     
     
    blur_image=cv2.blur(gray_image,(15,15))
    cv2.imwrite('blur_image.png',blur_image)
    
    ret,thresh = cv2.threshold(blur_image,150,255,0)
    contour_image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(blur_image, contours, -1, (0,255,0), 3)
    cv2.imshow('blur_image.png',blur_image)
    
    
    
    moments=[cv2.moments(cnt) for cnt in contours]
    y_centroids = [int(round(m['m01']/m['m00']))  for m in moments]

    
    x=len(y_centroids)

    i=0
    while i<x:
        y_centroids[i]=y_centroids[i]//10
        i=i+1
    

    flag=0
    i=0
    while i<x:
        j=i+1
        while j<x:
            if y_centroids[i]==y_centroids[j]:
                flag=1
                break
            j=j+1
        i=i+1
    if flag==1:
        print('Car found')
    else:
        print('Car not found')

    cv2.waitKey(0)
    cv2.destroyAllWindows()




#Loop through the list to depict each scenario and its outcome
for _ in mylist:
    scenario('no_vehicle.jpg')
    wait(3)
    scenario(_)
    wait(3)




















    

















    




 




    
