#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#######

#          --------- cember_boyunca_hareket.py ------------
# ----------- Uygulama 3: ÇEMBER Boyunca Hareket - istemci düğümü -------------

import rospy
from basit_uygulamalar.srv import CemberHareket

# burada cember_servis adını verdiğimiz servisi bekleyeceğiz.
rospy.wait_for_service("cember_servis")

try:
    # kullanıcıdan yariçap bilgisini alıyoruz.
    yaricap = float(input("yaricap giriniz: "))
    # serviceProxy ile servisi çağırıyoruz.
    servis = rospy.ServiceProxy("cember_servis",CemberHareket)

    servis(yaricap)




except rospy.ServiceException:
    print("Servisle alakali bir hata meydana geldi")
