#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Aynı renk veya yoğunluğa sahip tüm sürekli noktaları
# birleştiren eğriler görüntüdeki contourları oluşturur.

# sınır, hiyerarsi = cv2.findCounters(imge,mod,metot)

# burada sınır algılanan sınırları, hiyerarşi görüntü
# topolojisi hakkında bilgi içeren isteğe bağlı
# çıkış vektörünü, imge siyah-beyaz giriş görüntüsünü,
# mod sınır alma modunu, metot sınır yaklaşım yöntemini
# belirtir.



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
        
        img = self.bridge.imgmsg_to_cv2(mesaj,"mono8")
        img2 = self.bridge.imgmsg_to_cv2(mesaj,"bgr8")

      

        esiklenmis = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY,11,2)
        cv2.imshow("esiklenmis",esiklenmis)



        # kernel = np.ones((11,11),np.uint8)
        # dilate = cv2.dilate(esiklenmis,kernel)
        # cv2.imshow("dilate",dilate)


        
        sinirlar, hiyerarsi = cv2.findContours(img,cv2.RETR_EXTERNAL,
                                                cv2.CHAIN_APPROX_SIMPLE)

        for i in sinirlar:
            cv2.drawContours(img2,sinirlar,-1,(0,255,0),3)


        cv2.imshow("Robot Kamerasi",img2)



        # elde ettiğimiz contours verileri ile birçok başka istediğimiz
        # bilgilere erişebiliriz. Örnek olarak;

        # Moment : Momentler görüntünün kütle merkezi gibi bazı özelliklerini
        # hesaplamaya yarar. Syantax :  M = cv2.moments(cnts) 

        # Merkez Noktalar: Moment bilgisi kullanılarak görüntünün merkez
        # noktaları (centroid) bulunabilir.
        # cx = int(M["m10"]/M["m00"])
        # cy = int(M["m01"]/M["m00"])

        # Alan : Sınır alanını bulmaya yarar.
        # cv2.contourArea(cnt)

        # Çevre : Sınır çevresini bulmaya yarar.
        # cv2.arcLength(cnt)


        # elde ettiğimiz kontulardan ilk kontur değerini alıyoruz.
        #print("sinirlar[0] : ",sinirlar[0])

        cnt = sinirlar[0]

        cv2.drawContours(img2,cnt,-1,(0,255,0),5)
        cv2.imshow("Robot Kamerasi",img2)

        # moment değerini bulup çıktısını alıyoruz.
        # M = cv2.moments(cnt)
        # cx = int(M["m10"]/M["m00"])
        # cy = int(M["m01"]/M["m00"])
        # cv2.circle(img2,(cx,cy), 5,(255,255,255),-1)


        # şimdi çevre hesaplaması yapıp çıktısını alalım.
        #print(cv2.arcLength(cnt,True))
        # ardından alan hesabı yapıp çıktısını alalım.
        #print(cv2.contourArea(cnt))




        # uç noktalar nesnenin en üst, en alt, en sağ, ve en soldaki 
        # noktalarını belirlemeye yarar.

        # sol = tuple(cnt[cnt[:,:,0].argmin()][0])
        # sag = tuple(cnt[cnt[:,:,0].argmax()][0])
        # ust = tuple(cnt[cnt[:,:,1].argmin()][0])
        # alt = tuple(cnt[cnt[:,:,1].argmax()][0])

        # sol = tuple(cnt[cnt[:,:,0].argmin()][0])
        # sag = tuple(cnt[cnt[:,:,0].argmax()][0])
        # ust = tuple(cnt[cnt[:,:,1].argmin()][0])
        # alt = tuple(cnt[cnt[:,:,1].argmax()][0])




        # Minumum sınırlayıcı çember nesnenin sınırları kullanılarak minimum
        # çevreleyen çember içine alınmasını sağlar.
        # (x,y),cap = cv2.minEnclosingCircle(cnt)
        # merkez = (int(x),int(y))
        # cap = int(radius)
        # cv2.circle(imge,merkez,cap,renk,kalınlık)

        # (x,y), r = cv2.minEnclosingCircle(cnt)
        # merkez = (int(x),int(y))
        # r = int(r)
        # cv2.circle(img2,merkez,r,(255,0,0),2)




        # Sınırlayıcı dikdörtgen nesnenin sınırları kullanılarak dikdörtgen içine
        # alınmasını sağlar

        # x,y,w,h = cv2.boundingRect(cnt)
        #cv2.rectangle(imge(x,y),(x+w,y+h),renk,kalınlık)


        # x,y,w,h =cv2.boundingRect(cnt)
        # cv2.rectangle(img2,(x+y),(x+w))

        cv2.imshow("robot kamerasi",img2)


        # her bir görselin 1 milisaniye ekran kalmasını sağlıyoruz.
        cv2.waitKey(1)


Kamera()
