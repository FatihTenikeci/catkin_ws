#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Morfolojik işlemler, görüntünün şekline dayalı yapılan işlemlerdir.

# thresh uygulanmış görüntüler üzerinde gerçekleştirilir.

# Morfolojik işlemlerde orjinal imge ve işlemin doğasına karar veren yapılandırma
# öğesine(kernel) ihtiyaç duyulur.

# Yapılandırma elemanları numpy kütüphanesi yardımıyla veya Opencv içinde bulunan
# cv2.getStructuringElement(tip, boyut) fonksiyonu ile yapılabilir.

# bu fonksiyonda bulunan tip yerine
    # cv2.MORPH_RECT: dikdörtgen kernel
    # cv2.MORPH_ELLIPSE: eliptik kernel
    # cv2.MORPH_CROSS: çarpı şeklindeki kernel

# boyut kısmına kernel boyutu (x,x) yazılır.



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


        # tresh işlemimizi yapıyoruz.
        ret,esiklenmis = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

        # kernelimizi tanımlıyoruz.
        kernel = np.ones((11,11),np.uint8)

        # erode fonksiyonunu kullanıyoruz.
        e_img = cv2.erode(esiklenmis,kernel)

        # dilate fonksiyonunu kullanıyoruz.
        d_img = cv2.dilate(esiklenmis,kernel)

        # morfolojik gradyanı elde etmek için bu iki işlemi birbirinden 
        # çıkartıyoruz ve sonuçların çıktısını alıyoruz.
        f_img = d_img - e_img

        cv2.imshow("robot kamerasi", img)
        cv2.imshow("esiklenmis", esiklenmis)
        cv2.imshow("e_img", e_img)
        cv2.imshow("d_img", d_img)
        cv2.imshow("morfolojik gradyan", f_img)






        # opening işlemi erosion işleminden sonra dilation işleminin uygulanmasıdır.
        # closing işlemi dilation işleminden sonra erosion işleminin uygulanmasıdır.

        # bu iki morfolojik işlemi şimdi fonksiyonlar vasıtasıyla deneyelim.

        o_img = cv2.morphologyEx(esiklenmis,cv2.MORPH_OPEN,kernel)
        c_img = cv2.morphologyEx(esiklenmis,cv2.MORPH_CLOSE,kernel)

        cv2.imshow("o_img",o_img)
        cv2.imshow("c_img",c_img)



        # her bir görselin 1 milisaniye ekran kalmasını sağlıyoruz.
        cv2.waitKey(1)


Kamera()
