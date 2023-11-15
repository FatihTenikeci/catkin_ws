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

        img = self.bridge.imgmsg_to_cv2(mesaj,"bgr8")

        # ölçeklendirme işi için resize fonksiyonuu kullanmaktayız.
        olceklenmis = cv2.resize(img,(100,100))

        # ötelenme ölçüsünü ayarlayabilmek için matris şekilde 
        # öteleme ölçüsünü belirliyoruz.

        M = np.float32([[1,0,50],[0,1,200]])
        # görselimi ve matrisi girdikten sonra işlem sonrası elde edeceğim görselin
        # hangi boyutta olması gerekiyorsa o boyutları giriyoruz.
        # biz şuan orjinal boyutları girdik.
        otelenmis = cv2.warpAffine(img,M,(640,480))

        # döndüreme işlemi yapmak için öncelikle görselin merkezini
        # belirliyoruz. ardından dönüş açısını ve aynı ölçekte kalması için
        # 1 parametresini girdik.
        N = cv2.getRotationMatrix2D((320,240),90,1)
        dondurulmus = cv2.warpAffine(img,N,(640,480))

        # affine dönüşümleri nedir ayrıntılı bir şekilde araştırılacak.

        cv2.imshow("robot kamerasi",img)
        cv2.imshow("olceklenmis",olceklenmis)
        cv2.imshow("otelenmis",otelenmis)
        cv2.imshow("dondurulmus",dondurulmus)


        # her bir görselin 1 milisaniye ekran kalmasını sağlıyoruz.
        cv2.waitKey(1)


Kamera()
