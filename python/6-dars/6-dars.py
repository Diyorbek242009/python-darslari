# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:47:21 2024

@author: user
"""

#Lists (Ro'yxatlar)

mevalar = ['olma','anjir','shaftoli',"o'rik"] # mevalar ro'yxati (matnlar)
#narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
#sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
#ismlar =[] # bo'sh ro'yxat

#print(mevalar[0])
#print(mevalar[2])
#print(sonlar[-1])

#mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
#print("Birinchi meva: ", mevalar[0])
#print("Ikkinchi meva: ", mevalar[1])

#Metodlar
#print(mevalar[0].title())
#print("Birinchi meva: ", mevalar[0].title())#metodlar
#print("Ikkinchi meva: ", mevalar[1].upper())#metodlar

#print(narhlar[2] + narhlar[3])

#Elementlarni o'zgartirish
#mevalar[0] = 'anor'
#print(mevalar)
#narhlar = [12000, 18000, 10900, 22000]
#narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
#narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
#narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
#print(narhlar)

#Yangi element qo'shish
#mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
#print(mevalar)

#Bo'sh ro'yxatni to'ldirish
#cars = [] # bo'sh ro'yxat yaratamiz
#cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
#cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
#cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
#print(cars)


#Istalgan joyiga yangi element qo'shish
#cars = ['Lacetti', 'Nexia 3', 'Cobalt']
#cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
#cars.insert(2, 'Damas') # 3-o'ringa yangi qiymat qo'shamiz
#print(cars) 

#Elementlarni o'chirish
#mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
#del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
#print(mevalar)

#Element qiymati bo'yichi o'chirish
#mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
#mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
#(mevalar)

#hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
#hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
#print(hayvonlar)

#Elementni sug'urib olish
#bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
#mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
#print("Men " + mahsulot + " sotib oldim")
#print("Olinmagan mahsulotlar: ", bozorlik)
