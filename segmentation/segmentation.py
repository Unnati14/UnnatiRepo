import numpy as np
import cv2

def thresholding(input_image):
    height, width = input_image.shape[:2]
    th2 = cv2.adaptiveThreshold(input_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    # Uncomment following for Gaussian Apadtive Thresholding
    # th2 = cv2.adaptiveThreshold(input_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    image, contours, _ = cv2.findContours(th2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        x, y, w, h = cv2.boundingRect(contour)
        if ( area < 50 or x < 10 or (x+w) > (width-1) ):
            th2[y:y+h,x:x+w] = 0

    # cv2.imwrite("processedImage.jpeg",th2)
    th2 = cv2.morphologyEx(th2,cv2.MORPH_DILATE, kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))
    # cv2.imwrite("closedImage.jpeg",th2)
    image, contours, _ = cv2.findContours(th2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Remove smallest component
    # Find maximum area
    area_max = 0
    for c in contours:
        area = cv2.contourArea(c)
        if area > area_max:
            area_max = area

    mask = np.ones(th2.shape[:2], dtype="uint8") * 255
    for c in contours:
        area = cv2.contourArea(c)
        if area != area_max:
            cv2.drawContours(mask, [c], -1, 0, -1)
        else:
            x,y,w,h = cv2.boundingRect(c)
    image = cv2.bitwise_and(th2, th2, mask=mask)
    th2 = cv2.morphologyEx(image,cv2.MORPH_ERODE, kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)))
    return th2

def main():
    image = cv2.imread('ImageProc_flyingman.jpg', 0)
    Image_binary = thresholding(image)
    cv2.imwrite("Segmeneted_Binary_Image.jpeg",Image_binary)
    cv2.imshow('Segmented binary image',Image_binary)


if __name__ == "__main__":
    main()