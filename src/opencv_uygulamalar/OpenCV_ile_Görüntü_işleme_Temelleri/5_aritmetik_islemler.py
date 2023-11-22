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

        # görselimizi okuyoruz.
        kirmizi = cv2.imread("kirmizi.png")
        # toplama işlemi yapabilmek için iki görselinde yani robottan gelen görüntü
        # ile elimizdeki görüntünün boyutları eşit olması gerekmekte bu sebeple
        # elimizdeki görsele resize işlemi uyguladıktan sonra boyutları tekrar kontrol ediyoruz.
        yeni_kirmizi = cv2.resize(kirmizi,(640,480))

        print("robot kamera",img.shape)
        print("kirmiziPNG",yeni_kirmizi.shape)

        # toplama işlemini aşağıdaki gibi add fonk. ile gerçekleştiriyoruz.
        toplama = cv2.add(img,yeni_kirmizi)

        # addWeighted ile hangi görüntünün baskın olabileceğini ayarlayabilmekteyiz.
        # aşağıdaki gibi ağırlıkları belirliyoruz
        a_toplama = cv2.addWeighted(img,0.9,yeni_kirmizi,0.1,0)

        # şimdide subtract ile çıkarma işlemini yapıyoruz.
        cikarma = cv2.subtract(img,yeni_kirmizi)

        # imshow fonk. ile ekranda çıktı alıyoruz.
        cv2.imshow("Robot Kamerasi",cikarma)
        # her bir görselin 1 milisaniye ekran kalmasını sağlıyoruz.
        cv2.waitKey(1)


Kamera()