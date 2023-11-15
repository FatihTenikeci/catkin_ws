#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#    
#     --------- devriye_gezme.py ------------
# ----------- Uygulama 4: Devriye Gezme -------------


import rospy 
from geometry_msgs.msg import Twist

def volta():

    # volta_at adında bir düğüm oluşturalım.
    rospy.init_node("volta_at")

    # cmd_vel topic'inde Twist tipinde yayın yapmak için obje oluşturuyoruz.
    pub = rospy.Publisher("cmd_vel",Twist,queue_size = 10)

    # Twist tipinde hiz_mesaji tanımlıyoruz.
    hiz_mesaji = Twist()


    robot_hiz = 0.25

    # yaml dosyasında belirlediğimiz VoltaUzunluk ve VoltaSayısı adındaki parametreleri çağırıyoruz.
    volta_uzunluk = rospy.get_param("/VoltaUzunluk")
    volta_sayisi = rospy.get_param("/VoltaSayisi")


    sayici = 0

    # devriye başladığına dair bilgilerndirme yapıyoruz.
    rospy.loginfo("devriye gezmeye başladi")

    while sayici < volta_sayisi:
        # başlangıç saatini belirliyoruz.
        t0 = rospy.Time.now().to_sec()


        yer_degistirme = 0
        # sayicinin tekliği ve çiftliğine göre aracın gideceği yönü 
        # belirliyoruz.
        if sayici %2 == 0:
            hiz_mesaji.linear.x = robot_hiz
        else:
            hiz_mesaji.linear.x = -robot_hiz
        
        # yer değiştirmemiz istediğimiz veolta uzunluğuna ulaşana kadar
        # hız mesajını yayınlıyoruz.
        while yer_degistirme < volta_uzunluk:
            pub.publish(hiz_mesaji)
            t1 = rospy.Time.now().to_sec()
            yer_degistirme = robot_hiz * (t1-t0)

        # istediğimiz uzunluğa ulaşınca aracın hızını kesiyoruz ve bu mesajı birdaha 
        # yayınlıyoruz.
        hiz_mesaji.linear.x = 0
        pub.publish(hiz_mesaji)
        sayici = sayici + 1

    # devriyemiz tamamlandığı zaman bunu haber veriyoruz.
    rospy.loginfo("devriye tamamlandi !")
    rospy.is_shutdown()


volta()