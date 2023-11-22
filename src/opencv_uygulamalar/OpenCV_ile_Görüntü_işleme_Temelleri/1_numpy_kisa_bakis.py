#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# numpy paketi #

import numpy as np


# dtype parametresini "i" olacak şekilde ayarladığımızda tüm 
# değerler integer olarak dönecektir.
# dizi = np.array([1,2,3,4,5,6.613],dtype="i")
# print(dizi)

# dizimizin tipini ve dataların tipini yazdırıyoruz.
# print(type(dizi))
# print(dizi.dtype)


#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

# matrisimizin dimention, shape ve size'ını yazdırıyoruz.
# matris = np.array([[1,2,3],[4,5,6]])

# print(matris)
# print(matris.ndim) ## boyut çıktısı olarak 2 alıyoruz.
# print(matris.shape) ## shape çıktısı oalrak (2,3) çıktısı alıyoruz.
# print(matris.size) ## size çıktısı olarak 6 çıktısını alıyoruz.



#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------


# sıfırlardan oluşan bir dizi oluşturmak istediğimizde;
# print(np.zeros(3))
# print("*********")

# birlerden oluşan 3x3'lük bir matris oluşturmak istediğimizde;
# print(np.ones((3,3)))
# print("*********")

# köşegenlerde 1 değeri olmasını istedğimizde;
# print(np.eye(3))
# print("*********")

# 3 elemanlı bir diziyi istediğimiz değerde oluşturmak için;
# print(np.full(3,2))
# print("*********")

# 3x2'lik 10 ile 20 arasında random olacak şekilde bir matris 
# oluşturmak için;

# print(np.random.randint(10,20,(3,2)))
# print("*********")

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------


# # matrisimizin dimention, shape ve size'ını yazdırıyoruz.
# matris = np.array([[1,2,3],[4,5,6]])


# # matrisin çıktısını alalım
# print(matris)


# # matrisin 0'ıncı satırının 1. sütunundaki değerin çıktısını alıyoruz.
# print(matris[0,1])

# # matrisin 0'ıncı satırının 1. sütunundaki değeri 25 ile değiştiriyoruz.
# matris[0,1] = 25
# # ardından çıktısını alıyoruz.
# print(matris)

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------



matris = np.array([[1,2,3,23,24,25],[4,5,6,26,27,28]])
# birinci satırın birinci elemanından 4. elemanına kadar olan tüm 
# elemanların çıktısını alabilmek için;
# print(matris[1,1:4])
# print("*********")


# matristeki her bir elemanı teker teker dönebilmek için 
# aşağıdaki bloğu yazıyoruz.

# for satir in matris:
#     for eleman in satir:
#         print(eleman)




# matris içerisindeki belirli bir değeri bulabilmek için
# where methodunu kullanıyoruz. 
# çıktı olarak verilen değer bize elemanın hangi satırda kaçıncı
# eleman olduğu bilgisini döndürmekte
print(np.where(matris==23))


# 20 den küçük olan deeğrlerin boolean ile çıktısını almak için;
print(matris < 20)


# 20'den küçük olan değerlerin çıktısını ekranda alıyoruz.
matris_yeni = matris[matris < 20]
print(matris_yeni)


#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------