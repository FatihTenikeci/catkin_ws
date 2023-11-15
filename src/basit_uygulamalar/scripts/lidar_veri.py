#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#    
#                      --------- lidar_veri.py ------------
# ----------- Uygulama 5: Lidardan Gelen Verilerin Kullanımı -------------

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
class LazerVerisi():
    def __init__(self):
        # lazer_dugumu adındaki düğümümüzü oluşturuyoruz.
        rospy.init_node("lazer_dugumu")

        # cmd_vel üzerinden Twist tipinde yayın yapıyoruz.
        self.pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)

        # Twist tipinde hız mesajı tanımlıyoruz.
        self.hiz_mesaji = Twist()

        # scan topiğinden LaserScan tipinde gelen veriye subscribe oluyoruz.
        # Ve self.lazerCallback fonksiyonunu çağırıyoruz.
        rospy.Subscriber("scan",LaserScan,self.lazerCallback)
        # ve bu işlemlerin sonsuz döngüde devam etmesi için spin() methodunu kullanıyoruz
        rospy.spin()

# lidar verilerinde yönleri belirlemek için 360 derecelik bir çember düşünülmesi gerekir.
# bu çemberin her bir derecesi bir değer aralığına denk gelmektedir.


    def lazerCallback(self,mesaj):
        # ön kısmı sağ_ön ve sol_ön olmak üzere iki kısma ayırıp on değişkenine atıyoruz.
        sol_on = list(mesaj.ranges[0:9])
        sag_on = list(mesaj.ranges[350:359])

        on = sol_on + sag_on

        # sol kısmı sol sağ kısmı ise sağ ismindeki değişkenlerle tanımlıyoruz.
        sol = list(mesaj.ranges[80:100])
        sag = list(mesaj.ranges[260:280])

        # aynı şekilde arka kısmın aralıklarını belirleyip atamasını yapıyoruz.
        arka = list(mesaj.ranges[170:190])
        
        # burada gelen 20'şerli veriyi tek bir veriye indirgiyoruz.
        # bunu yapmamızın sebebi cisimle lidar arasındaki minimum mesafeyi belirlemek

        min_on = min(on)
        min_arka = min(arka)
        min_sol = min(sol)
        min_sag = min(sag)


        print("min_arka : " , min_arka)
        print("arka : " , arka)

        print("min_on : " , min_on)
        print("on : ", on)

        print("min_sol : ", min_sol)
        print("sol",sol)
        
        print("min_sag : ", min_sag)
        print("sag",sag)

        # lidar verimiz 1.0 altına düştüğü takdirde aracımızın hızını 0'a
        # çekip hız verimizi yayınlıyoruz. Aksi takdirde hızımızı 0.25 olacak şekilde
        # ayarlıyoruz
        
        if min_on < 1.0:
            self.hiz_mesaji.linear.x = 0.0
            self.pub.publish(self.hiz_mesaji)

        else:
            self.hiz_mesaji.linear.x = 0.25
            self.pub.publish(self.hiz_mesaji)

nesne = LazerVerisi()