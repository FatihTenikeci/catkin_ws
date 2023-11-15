#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot_kontrol.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(540, 360)
        Dialog.setMinimumSize(QtCore.QSize(540, 360))
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.hiz_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hiz_label.setFont(font)
        self.hiz_label.setObjectName("hiz_label")
        self.gridLayout_2.addWidget(self.hiz_label, 0, 1, 1, 1)
        self.kontrol_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.kontrol_label.setFont(font)
        self.kontrol_label.setObjectName("kontrol_label")
        self.gridLayout_2.addWidget(self.kontrol_label, 1, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.line_lineer = QtWidgets.QLineEdit(Dialog)
        self.line_lineer.setReadOnly(True)
        self.line_lineer.setObjectName("line_lineer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_lineer)
        self.etiket_acisal = QtWidgets.QLabel(Dialog)
        self.etiket_acisal.setObjectName("etiket_acisal")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.etiket_acisal)
        self.line_acisal = QtWidgets.QLineEdit(Dialog)
        self.line_acisal.setReadOnly(True)
        self.line_acisal.setObjectName("line_acisal")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_acisal)
        self.etiket_lineer = QtWidgets.QLabel(Dialog)
        self.etiket_lineer.setObjectName("etiket_lineer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.etiket_lineer)
        self.gridLayout_2.addLayout(self.formLayout, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.buton_sol = QtWidgets.QPushButton(Dialog)
        self.buton_sol.setObjectName("buton_sol")
        self.gridLayout.addWidget(self.buton_sol, 1, 0, 1, 1)
        self.buton_ileri = QtWidgets.QPushButton(Dialog)
        self.buton_ileri.setObjectName("buton_ileri")
        self.gridLayout.addWidget(self.buton_ileri, 0, 1, 1, 1)
        self.buton_geri = QtWidgets.QPushButton(Dialog)
        self.buton_geri.setObjectName("buton_geri")
        self.gridLayout.addWidget(self.buton_geri, 2, 1, 1, 1)
        self.buton_dur = QtWidgets.QPushButton(Dialog)
        self.buton_dur.setObjectName("buton_dur")
        self.gridLayout.addWidget(self.buton_dur, 1, 1, 1, 1)
        self.buton_sag = QtWidgets.QPushButton(Dialog)
        self.buton_sag.setObjectName("buton_sag")
        self.gridLayout.addWidget(self.buton_sag, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.konum_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.konum_label.setFont(font)
        self.konum_label.setObjectName("konum_label")
        self.gridLayout_2.addWidget(self.konum_label, 2, 1, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.konumx_label = QtWidgets.QLabel(Dialog)
        self.konumx_label.setObjectName("konumx_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.konumx_label)
        self.line_x = QtWidgets.QLineEdit(Dialog)
        self.line_x.setReadOnly(True)
        self.line_x.setObjectName("line_x")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_x)
        self.konumy_label = QtWidgets.QLabel(Dialog)
        self.konumy_label.setObjectName("konumy_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.konumy_label)
        self.line_y = QtWidgets.QLineEdit(Dialog)
        self.line_y.setReadOnly(True)
        self.line_y.setObjectName("line_y")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_y)
        self.gridLayout_2.addLayout(self.formLayout_2, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Robot Kontrol Arayüzü"))
        self.hiz_label.setText(_translate("Dialog", "                   HIZ GÖSTERGESİ"))
        self.kontrol_label.setText(_translate("Dialog", "                    ROBOT KONTROL"))
        self.etiket_acisal.setText(_translate("Dialog", "acisal Hız (rad/s)"))
        self.etiket_lineer.setText(_translate("Dialog", "Lineeer Hız (m/s)"))
        self.buton_sol.setText(_translate("Dialog", "sol"))
        self.buton_ileri.setText(_translate("Dialog", "ileri"))
        self.buton_geri.setText(_translate("Dialog", "geri"))
        self.buton_dur.setText(_translate("Dialog", "dur"))
        self.buton_sag.setText(_translate("Dialog", "sağ"))
        self.konum_label.setText(_translate("Dialog", "                           KONUM"))
        self.konumx_label.setText(_translate("Dialog", "konum X:"))
        self.konumy_label.setText(_translate("Dialog", "konum Y:"))


        rospy.init_node("robot_arayuz")
        self.pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
        self.hiz_mesaji = Twist()
        rospy.Subscriber("odom",Odometry,self.odomCallback)

        self.buton_dur.clicked.connect(self.robotDur)
        self.buton_ileri.clicked.connect(self.ileriGit)
        self.buton_geri.clicked.connect(self.geriGit)
        self.buton_sol.clicked.connect(self.solGit)
        self.buton_sag.clicked.connect(self.sagaGit)


        self.line_acisal.setText(str(0.0))
        self.line_lineer.setText(str(0.0))
        self.line_x.setText(str(0.0))
        self.line_y.setText(str(0.0))


    def odomCallback(self,mesaj):
        self.line_x.setText(str(round(mesaj.pose.pose.position.x)))
        self.line_y.setText(str(round(mesaj.pose.pose.position.y)))

    
    def robotDur(self):
        self.hiz_mesaji.linear.x = 0.0
        self.hiz_mesaji.angular.z = 0.0
        self.pub.publish(self.hiz_mesaji)
        self.line_lineer.setText(str(self.hiz_mesaji.linear.x))
        self.line_acisal.setText(str(self.hiz_mesaji.angular.z))

    def ileriGit(self):
        self.hiz_mesaji.linear.x = 1.0
        self.hiz_mesaji.angular.z = 0.0
        self.pub.publish(self.hiz_mesaji)
        self.line_lineer.setText(str(self.hiz_mesaji.linear.x))
        self.line_acisal.setText(str(self.hiz_mesaji.angular.z))


    def geriGit(self):
        self.hiz_mesaji.linear.x = -1.0
        self.hiz_mesaji.angular.z = 0.0
        self.pub.publish(self.hiz_mesaji)
        self.line_lineer.setText(str(self.hiz_mesaji.linear.x))
        self.line_acisal.setText(str(self.hiz_mesaji.angular.z))


    def solGit(self):
        self.hiz_mesaji.linear.x
        self.hiz_mesaji.angular.z = 0.5
        self.pub.publish(self.hiz_mesaji)
        self.line_lineer.setText(str(self.hiz_mesaji.linear.x))
        self.line_acisal.setText(str(self.hiz_mesaji.angular.z))


    def sagaGit(self):
        self.hiz_mesaji.linear.x
        self.hiz_mesaji.angular.z = -0.5
        self.pub.publish(self.hiz_mesaji)
        self.line_lineer.setText(str(self.hiz_mesaji.linear.x))
        self.line_acisal.setText(str(self.hiz_mesaji.angular.z))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
