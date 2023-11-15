#!/usr/bin/env python3
# -*- coding: utf-8 -*-



 

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import numpy as np

class Kamera():
    def __init__(self):
        # düğümümüzü oluşturuyoruz.
        rospy.init_node("kamera_dugumu")

        # cv2 kütüphanesini kullanabilmek için köprü oluşturmamız gerekmekte bunun 
        # sebebi cv2 kütüphanesi bizim bilgisayarımızda çalışırken ros farklı bir
        # ortamda çalışmakta dolayısıyla iki ortam arasında köprü kurulması gerekmekte.
        self.bridge = CvBridge()

        # camera/rgb/image_raw adlı topiğe Image tipinde olmak üzere ve kameraCallback'i
        # çalıştıracak biçimde subscribe oluyoruz.
        rospy.Subscriber("camera/rgb/image_raw",Image,self.kameraCallback)
        # fonk. sürekli dönmesi için spin() methodunu kullanıyoruz.
        rospy.spin()

    def kameraCallback(self,mesaj):

        # obje olarak img'yi tanımlarken CvBridge class'ının methodu olan 
        # imgmsg_to_cv2'u kullanıyoruz.
        # imgmsg_to_cv2 mesajı alır ve opencv'nin işleyebileceği bir biçime
        # çevirir buradaki standartı "bgr8" olarak belirledik.
        
        img = self.bridge.imgmsg_to_cv2(mesaj,"bgr8")


        k1 = np.float32([[30,500],[200,500],[30,600]])
        k2 = np.float32([[15,500],[100,500],[15,600]])
        M = cv2.getAffineTransform(k1,k2)
        afin = cv2.warpAffine(img,M,(640,480))
        cv2.imshow("robot kamerasi",img)
        cv2.imshow("afin donusum",afin)
       

        # her bir görselin 1 milisaniye ekran kalmasını sağlıyoruz.
        cv2.waitKey(1)


Kamera()
