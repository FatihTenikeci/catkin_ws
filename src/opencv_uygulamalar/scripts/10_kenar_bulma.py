#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Canny Kenar BUlma Algoritması

# Algoritmanın aşamaları:

# 1. Giriş görüntüsündeki gürültüleri azaltmak için bir Gauss filtresi kullanma

# 2. GÖrüntünün yatay ve diket yönlerindeki kenarlarını belirlemek için gradyan
# büyüklüğünü ve açılarını hesaplama.

# Görüntüde istenmeyen kenarları kaldırmak için maksimum olmayan kenarları bastırma
# işlemini uygulama

# 4. kenarları algılamak için çift eşikleme yöntemini (histeresis prosedürü) kullanma

# cv2.Canny(imge, eşik1, eşik2,boyut)


# Bu sözdiziminde, imge gri seviye giriş görüntüsünü, eşik1 histeresis prosedürü
# için ilk eşik değerini, eşik2 histeresis prosedürü için ikinci eşik değerini ve 
# boyut gradyanları bulmak için kullanılan Sobel çekirdeğinin boyutudur ve 
# varsayılan olarak 3'tür.





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
        

        # mono8 kullanarak grayscale dönüşümü yapıyoruz. 
        img = self.bridge.imgmsg_to_cv2(mesaj,"mono8")
        kenarlar = cv2.Canny(img,100,200,5)

        cv2.imshow("robot kamerasi",img)
        cv2.imshow("canny kenarlar",kenarlar)
        



        








        # her bir görselin 1 milisaniye ekran kalmasını sağlıyoruz.
        cv2.waitKey(1)


Kamera()
