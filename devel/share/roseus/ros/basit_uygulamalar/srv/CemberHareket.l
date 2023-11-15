;; Auto-generated. Do not edit!


(when (boundp 'basit_uygulamalar::CemberHareket)
  (if (not (find-package "BASIT_UYGULAMALAR"))
    (make-package "BASIT_UYGULAMALAR"))
  (shadow 'CemberHareket (find-package "BASIT_UYGULAMALAR")))
(unless (find-package "BASIT_UYGULAMALAR::CEMBERHAREKET")
  (make-package "BASIT_UYGULAMALAR::CEMBERHAREKET"))
(unless (find-package "BASIT_UYGULAMALAR::CEMBERHAREKETREQUEST")
  (make-package "BASIT_UYGULAMALAR::CEMBERHAREKETREQUEST"))
(unless (find-package "BASIT_UYGULAMALAR::CEMBERHAREKETRESPONSE")
  (make-package "BASIT_UYGULAMALAR::CEMBERHAREKETRESPONSE"))

(in-package "ROS")





(defclass basit_uygulamalar::CemberHareketRequest
  :super ros::object
  :slots (_yaricap ))

(defmethod basit_uygulamalar::CemberHareketRequest
  (:init
   (&key
    ((:yaricap __yaricap) 0.0)
    )
   (send-super :init)
   (setq _yaricap (float __yaricap))
   self)
  (:yaricap
   (&optional __yaricap)
   (if __yaricap (setq _yaricap __yaricap)) _yaricap)
  (:serialization-length
   ()
   (+
    ;; float64 _yaricap
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _yaricap
       (sys::poke _yaricap (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _yaricap
     (setq _yaricap (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass basit_uygulamalar::CemberHareketResponse
  :super ros::object
  :slots (_stop ))

(defmethod basit_uygulamalar::CemberHareketResponse
  (:init
   (&key
    ((:stop __stop) nil)
    )
   (send-super :init)
   (setq _stop __stop)
   self)
  (:stop
   (&optional (__stop :null))
   (if (not (eq __stop :null)) (setq _stop __stop)) _stop)
  (:serialization-length
   ()
   (+
    ;; bool _stop
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _stop
       (if _stop (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _stop
     (setq _stop (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass basit_uygulamalar::CemberHareket
  :super ros::object
  :slots ())

(setf (get basit_uygulamalar::CemberHareket :md5sum-) "1842f19c2847b8db283a737da466af32")
(setf (get basit_uygulamalar::CemberHareket :datatype-) "basit_uygulamalar/CemberHareket")
(setf (get basit_uygulamalar::CemberHareket :request) basit_uygulamalar::CemberHareketRequest)
(setf (get basit_uygulamalar::CemberHareket :response) basit_uygulamalar::CemberHareketResponse)

(defmethod basit_uygulamalar::CemberHareketRequest
  (:response () (instance basit_uygulamalar::CemberHareketResponse :init)))

(setf (get basit_uygulamalar::CemberHareketRequest :md5sum-) "1842f19c2847b8db283a737da466af32")
(setf (get basit_uygulamalar::CemberHareketRequest :datatype-) "basit_uygulamalar/CemberHareketRequest")
(setf (get basit_uygulamalar::CemberHareketRequest :definition-)
      "float64 yaricap
---
bool stop

")

(setf (get basit_uygulamalar::CemberHareketResponse :md5sum-) "1842f19c2847b8db283a737da466af32")
(setf (get basit_uygulamalar::CemberHareketResponse :datatype-) "basit_uygulamalar/CemberHareketResponse")
(setf (get basit_uygulamalar::CemberHareketResponse :definition-)
      "float64 yaricap
---
bool stop

")



(provide :basit_uygulamalar/CemberHareket "1842f19c2847b8db283a737da466af32")


