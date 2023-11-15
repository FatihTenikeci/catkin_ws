#!/usr/bin/env python3
# -*- coding: utf-8 -*-



#               --------- duz_git_v1.py ------------
# ----------- Uygulama 1: Tek Eksen Boyunca Hareket 1 -------------

import rospy 
# rospy kütüphanesi ROS düğümleri oluşturmaya ve ROS içerisindeki diğer düğümler
# ile iletişim kurmanıza olanak sağlar.


# ROS'un geometry_msgs paketi içindeki Twist mesaj türünü içe aktarır. Bu mesaj türü,
# robot hareketi ve hız kontrolü gibi kinematik verileri temsil etmek için kullanılır
from geometry_msgs.msg import Twist





def hareket():

    # rospy.init_node bir ROS düğümünü başlatmak için kullanılır

    # node_name: Başlatılacak ROS düğümünün adını belirtir. Ad genellikle bir dize (string) olarak verilir. 
    # Her ROS düğümünün benzersiz bir adı olmalıdır. Düğüm adı, başka ROS düğümleri ile iletişim
    # kurarken ve ROS konularını veya hizmetlerini tanımlarken kullanılır.

    # anonymous (isteğe bağlı): Bu, düğümün adının benzersiz olup olmadığını belirtir. Varsayılan olarak 
    # False olarak ayarlanır. Eğer True olarak ayarlanırsa, düğüm adının sonuna rastgele bir sayı eklenir 
    # ve böylece düğüm adı benzersiz hale gelir. Bu, birden fazla aynı düğüm adına sahip düğümün aynı anda çalışmasını sağlar.


    rospy.init_node("duz_git")

    # rospy.Publisher belli bir topic'e mesaj göndermenizi sağlar

    # name: Yayımlanacak konunun adını (topic name) belirtir. Bu, bir dize (string) olarak verilir. Örneğin, "cmd_vel" veya "sensor_data" gibi.

    # data_class: Bu, yayımlanan mesajların veri türünü tanımlar. Mesaj türü, genellikle geometry_msgs.msg 
    # veya sensor_msgs.msg içinde tanımlanan bir veri türüdür. Örneğin, geometry_msgs.msg.Twist veya sensor_msgs.msg.LaserScan gibi.

    # queue_size (isteğe bağlı): Bu parametre, konuya gönderilen mesajların kuyruğunun ne kadar büyük olacağını belirtir.
    # Varsayılan olarak, queue_size parametresi None olarak ayarlanır ve tüm mesajlar bellekte saklanır. Eğer belirli 
    # bir boyutta bir mesaj havuzu isteniyorsa, bu parametre ayarlanabilir.

    pub = rospy.Publisher("cmd_vel",Twist, queue_size=10)


    # Twist, ROS (Robot Operating System) içinde hareket ve hız kontrolü için kullanılan bir veri türüdür.

    # Twist mesajı, bir robotun doğrusal hareket ve dönme hareketi için hız bilgilerini taşır. 
    # genellikle hareket komutları göndermek veya robotun hızını belirlemek için kullanılır.

    # Twist mesajının iç yapısı iki önemli bileşen içerir:

    # angular bileşeni, robotun dönme hareketini temsil eder. Bu bileşen, bir üç boyutlu vektör olarak tanımlanır
    # ve genellikle x, y, ve z bileşenlerinden oluşur. Ancak, çoğu durumda x ve y bileşenleri kullanılmaz ve sıfır
    # olarak ayarlanır. Sadece z bileşeni önemlidir. z bileşeni, robotun saat yönünde veya saat yönünün tersine
    # dönme hızını rad/saniye cinsinden ifade eder. Eğer z pozitif bir değere sahipse, robot saat yönünde dönerken,
    # eğer negatif bir değere sahipse, robot saat yönünün tersine döner.

    # linear bileşeni, robotun doğrusal hareketini temsil eder. Yine bu bileşen de bir üç boyutlu vektör olarak tanımlanır 
    # ve x, y, ve z bileşenlerinden oluşur. x bileşeni, robotun ileri veya geri doğru hareket hızını temsil eder. y ve z 
    # bileşenleri ise genellikle kullanılmaz ve sıfır olarak ayarlanır. x bileşeni pozitif bir değere sahipse, robot ileri 
    # doğru hareket eder. Eğer x negatif bir değere sahipse, robot geriye doğru hareket eder.

    hiz_mesaji = Twist()
    hiz_mesaji.linear.x = 0.5


    mesafe = 5 
    yer_degistirme = 0

    # rospy.Time, ROS (Robot Operating System) içinde zaman verisini barındıran bir class'tır.

    # rospy.Time.now(): Bu method mevcut ROS zamanını temsil eden bir rospy. Time objesi oluşturur. 

    # to_sec(): Bu yöntem, zamanı saniye cinsinden ifade eden bir ondalık (float) sayı olarak döndürür.
    # to_nsec(): Bu yöntem, zamanı nanosaniye cinsinden ifade eden bir tamsayı (int) olarak döndürür.

    # from_sec(seconds): Bu yöntem, saniye cinsinden bir zamanı temsil eden bir rospy.Time objesi oluşturur.
    # from_nsec(nanoseconds): Bu yöntem, nanosaniye cinsinden bir zamanı temsil eden bir rospy.Time objesi oluşturur.

    t0 = rospy.Time.now().to_sec()


    while (yer_degistirme < mesafe):
        pub.publish(hiz_mesaji)
        t1 = rospy.Time.now().to_sec()
        yer_degistirme = hiz_mesaji.linear.x*(t1-t0)



    hiz_mesaji.linear.x = 0.0
    pub.publish(hiz_mesaji)


    # rospy.loginfo is a function used in ROS (Robot Operating System) for logging information-level messages. It's a way to record and display 
    # informational messages while a ROS application is running. Logging messages are used to monitor important information and aid
    # in debugging ROS applications.
    
    rospy.loginfo("hedefe varildi")

hareket()
