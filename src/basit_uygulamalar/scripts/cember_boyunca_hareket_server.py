#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#          --------- cember_boyunca_hareket.py ------------
# ----------- Uygulama 3: ÇEMBER Boyunca Hareket - server düğümü -------------

# Bu uygulamada servis yapısı kullanacağız.

# ilk önce CemberHareket.srv adında bir servis dosyası açıyoruz.


# float64 yaricap         // yazıyoruz
# ---                     //

# servis yapısı iki kısımdan oluşur. Birinci birim istek(request) ikinci birim ise yanıttır(responce)
# servis yapısı sunucu mantığı ile çalışır. İstek geldiği durumlarda belirlenen yanıtı iletir.

# ufak bir örnek vermek gerekirse;

# int64 A
# int64 B
# ---
# int64 Sum


# bu işlemlerden sonra CMakeList ile package.xml içerisinde düzenlemeler yapmamız gerekmekte.

# CMakelist içerisinde // add_service_files(FILES CemberHareket.srv)  // şeklinde değişikliği yapıyoruz.
# generate_messages()  catkin_package(CATKIN_DEPENDS message_runtime()  halihazırda eklendiği için dokunmuyoruz.


# şimdi package.xml dosyasında bir takım değişiklikler yapacağız.
# message_generation ve message_runtime eklenmesi gerekmekte bunları ekliyoruz.


# Bu işlemleri gerçekleştridikten sonra workspace'i derliyoruz.

import rospy
from geometry_msgs.msg import Twist
from basit_uygulamalar.srv import CemberHareket
# from basit_uygulamalar.srv import CemberHareketRequest, CemberHareketResponse    FATİH BURALARI KURSTAN SONRA ARAŞTIR ÖĞREN 



# fonksiyonumuzu tanımlıyoruz. istek 
def cemberFonksiyonu(istek):
    # yapmak istediğimiz gelen istek üzerinde yarıçap boyunca hareketini sağlamak.

    # ilk olarak TWist tipinde bir hız mesajı tanımlıyoruz.
    hiz_mesaji = Twist()
    # robotumuz artık sadece lineer bir hız değil aynı zamanda açısal
    # bir hızada sahip olacak.
    
    lineer_hiz = 0.5
    hiz_mesaji.linear.x = lineer_hiz
    yaricap = istek.yaricap
    
    # w(açısal hız) = v / r 
    hiz_mesaji.angular.z = lineer_hiz / yaricap



    while not rospy.is_shutdown():
        # sonsuza kadar yayınlıyoruz.
        pub.publish(hiz_mesaji)





# cember_hareket adında bir düğüm oluşturalım.
rospy.init_node("cember_hareket")

# hız yayınlamak istiyoruz dolayısıyla 
# cmd_vel topic'inde Twist tipinde publishing yapıyoruz.
pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)

# servisimizin adını cember_servis olarak ayarlıyoruz.
# servisimizin tipini CemberHareket olarak belirliyoruz.
# istek geldiğinde ne yapacağımızı 3. parametrede belirtiyoruz. yani cemberFonksiyonunu çalıştırıyoruz.

rospy.Service("cember_servis",CemberHareket,cemberFonksiyonu)

# bu işlemin süreklşi gerçekleşmesi için rospy.Spin methodunu kullanıyoruz.
rospy.spin()


