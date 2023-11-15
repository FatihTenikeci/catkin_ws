#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#               --------- duz_git_v2.py ------------
# ----------- Uygulama 2: Tek Eksen Boyunca Hareket 2 -------------



import rospy 
from geometry_msgs.msg import Twist

# from nav_msgs.msg import Odometry ifadesi, ROS (Robot Operating System) içinde nav_msgs paketi altındaki Odometry mesaj türünü içe aktarır. 
# Bu mesaj türü, robotların konum ve hız bilgilerini içeren bir tür navigasyon
# verisi taşımak için kullanılır. Bu verilerden en önemli iki tanesi aşağıdakilerdir.

    # Pose (Konum): Pose verisi, robotun 3 boyutlu konumunu ve yönelimini içerir. 
    # Bu bilgiler, geometry_msgs/PoseWithCovariance türünden bir veri içinde bulunur. Bu veri aşağıdaki bileşenleri içerir:

    # Pozisyon (position): X, Y ve Z koordinatları ile konumu tanımlar.
    # Yönelim (orientation): X, Y, Z ve W bileşenleri ile robotun 3D dönme açısını tanımlar.


    # Twist (Hız): Twist verisi, robotun doğrusal ve açısal hız bilgilerini içerir. Bu bilgiler,
    # geometry_msgs/TwistWithCovariance türünden bir veri içinde bulunur. Bu veri aşağıdaki bileşenleri içerir:

    # Doğrusal hız (linear): X, Y ve Z bileşenleri ile robotun doğrusal hızını tanımlar (m/s cinsinden).
    # Açısal hız (angular): X, Y ve Z bileşenleri ile robotun açısal hızını tanımlar (rad/s cinsinden).

from nav_msgs.msg import Odometry


# kendimizin hazırlamış olduğu message türünü import ediyoruz

from basit_uygulamalar.msg import Mesafe




class HedefeGit():
    def __init__(self):

        rospy.init_node("node_git")  # ROS düğümümüzü başlatmak için "rospy.init_node" kullanıyoruz.
        
        self.hedef_konum = 0.0        # hedef konumumuzu belirtiyoruz.
        self.guncel_konum = 0.0        # güncel konumumuzu belirtiyoruz.
        self.kontrol = True          



        # rospy.Subscriber, ROS (Robot Operating System) içinde bir topic'i dinlemek ve o konudan gelen
        # mesajları işlemek için kullanılan bir classdır. Topicler, ROS düğümleri arasında veri iletişimi sağlayan önemli bir mekanizmadır. 
        # rospy.Subscriber ile bir topice abone olabilirsiniz ve o topic üzerinden yayımlanan mesajları dinleyebilirsiniz.


        # "topic_name": Abone olunacak topic adını belirtir. string olarak verilir ve dinlenen topic ile aynı ad olmalıdır.


        # MessageClass: Konu üzerinde yayımlanan mesajların türünü belirtir. Bu, özel bir mesaj türünü temsil eden bir Python sınıfıdır.
        # Örneğin, geometry_msgs.msg.Twist veya sensor_msgs.msg.LaserScan gibi.


        # callback_function: topicten yeni bir mesaj geldiğinde çağrılacak bir işlevi belirtir. Bu işlev, gelen mesajları işlemek için kullanılır.
        # İşlev, tipik olarak iki argüman alır: message (gelen mesaj) ve user_data (kullanıcı verileri).

        rospy.Subscriber("odom",Odometry,self.odomCallback)
        rospy.Subscriber("mesafe_git",Mesafe,self.mesafeCallback)


        pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
        hiz_mesaji = Twist()
        
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            if self.kontrol:
                hiz_mesaji.linear.x = 0.5
                pub.publish(hiz_mesaji)
            else:
                hiz_mesaji.linear.x = 0.0
                pub.publish(hiz_mesaji)
                rospy.loginfo("Hedefe varildi !")
            rate.sleep()

    def odomCallback(self, mesaj):
        self.guncel_konum = mesaj.pose.pose.position.x
        if self.guncel_konum <= self.hedef_konum:
            self.kontrol = True
        else:
            self.kontrol = False

    def mesafeCallback(self,mesaj):
        self.hedef_konum = mesaj.Mesafe
try:
    HedefeGit()
except rospy.ROSInterruptException:
    print("dugum sonlandi!!")