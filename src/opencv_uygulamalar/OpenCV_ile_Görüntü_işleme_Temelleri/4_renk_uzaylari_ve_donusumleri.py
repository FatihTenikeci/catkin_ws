#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Renk uzayı renklerin farklı şekillerde temsil edildiği sistemlerdir.

# BGR renk uayında görüntüdeki her piksel değeri; mavi(B), yeşil(G), kırmızı(R)
# temsil etmektedir.

# HSV renk uzayında görüntüdeki her piksel renk özü (H), doygunluk (S), parlaklık(V)
# ile temsil edilir. 



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
        img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img3 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


        # imshow fonk. ile ekranda çıktı alıyoruz.
        cv2.imshow("BGR",img)
        cv2.imshow("GRAY",img2)
        cv2.imshow("HSV",img3)


        # her bir görselin 1 milisaniye ekran kalmasını sağlıyoruz.
        cv2.waitKey(1)


Kamera()