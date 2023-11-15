#!/usr/bin/env python3
# -*- coding: utf-8 -*-



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

      
        img = self.bridge.imgmsg_to_cv2(mesaj,"bgr8")
        cv2.line(img,(0,0),(250,250),(255,0,0))
        cv2.rectangle(img,(250,175),(500,125),(123,23,200),5)
        cv2.circle(img,(100,100),10,(0,0,255),-1)
        cv2.putText(img,"ROS",(0,150),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),2)

        cv2.imshow("robot kamerasi",img)


        # her bir görselin 1 milisaniye ekran kalmasını sağlıyoruz.
        cv2.waitKey(1)


Kamera()
