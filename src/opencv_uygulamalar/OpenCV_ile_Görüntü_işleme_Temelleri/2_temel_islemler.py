#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Temel İslemler

import cv2
img = cv2.imread("gorseller/python.png")
cv2.imshow("görüntü",img)
# sıfır değerini girersek görüntü biz kapatana kadar açık kalır.



print(img.shape)
print(img.size)
print(img.dtype)

img[50:70,50:70] = [0,0,0]

roi = img[0:80,0:180]

cv2.imshow("degistirilmiş",img)
cv2.imshow("roi",roi)


cv2.imwrite("gorseller/roi.png",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()