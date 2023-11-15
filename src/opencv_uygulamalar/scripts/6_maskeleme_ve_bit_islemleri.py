#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# kameradan gelen veri ROS düğümü haırlama 

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

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
        '''
        kirmizi = cv2.imread("kirmizi.png")
        kirmizi = cv2.resize(kirmizi,(640,480))

        print("--------||------original---||--------------")

        print(img[0,0])
        print(kirmizi[0,0])

        print("--------||------original---||--------------")

        and_is = cv2.bitwise_and(img,kirmizi)
        or_is = cv2.bitwise_or(img,kirmizi)
        xor_is = cv2.bitwise_xor(img,kirmizi)
        not_is = cv2.bitwise_not(img)

        print("--------||------bitwise-islemleri---||--------------")

        print(and_is[0,0])
        print(or_is[0,0])
        print(xor_is[0,0])
        print(not_is[0,0])

        print("--------||------bitwise-islemleri---||--------------")

        '''



        gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret, maske = cv2.threshold(gri,50,255,cv2.THRESH_BINARY_INV)
        and_is = cv2.bitwise_and(img,img,mask=maske)

        # imshow fonk. ile ekranda çıktı alıyoruz.
        cv2.imshow("Robot Kamerasi",and_is)
        # her bir görselin 1 milisaniye ekran kalmasını sağlıyoruz.
        cv2.waitKey(1)


Kamera()
