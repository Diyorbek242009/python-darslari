# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 21:43:50 2024

@author: user
"""

#if-else shartlari va tarmoqlanish

#if OPERATORI:
 
#avtolar = ['audi','bmw','volvo','kia','hyundai']

#for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#        print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#    else: # aks holda ... 
#        print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.

#==tengmi belgisini bildirdi
#=!teng emasm belgisini bildiradi

#avtolar = ['audi','bmw','volvo','kia','hyundai']
#for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#        print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#    else: # aks holda ... 
#        print(avto.title()) # avto nomini faqat birinchi harfini katta bilan yoz.

#TRUE/FALSE

#TRUE to'g'ri haqiqiy
#FALSE noto'g'ri yol'gon

#ism='Ali'
#print(ism=='Ali')#to'g'ri
#print(ism=='Anvar')#noto'g'ri

#MATNLARNI SOLISHTIRISH
#lower()#metodi

#ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
#if ism.lower() != 'diyorbek': # Agar ism Aliga teng bo'lmasa ...
#    print(f"Uzr, {ism.title()} biz Diyorbekni kutayapmiz.") # quyidagi xabar chiqadi
#else:
#    print("Salom, Ali")

#SONLARNI SOLISHTIRISH

#Sonlarni solishtirishda yuqoridagi teng (==) va teng emas (!=) lardan foydalanamiz

#javob = float(input("12x6 nechiga teng?>>>"))
#if javob!=72:
#    print("Javob xato!")
#else:    
#    print("Javob to'g'ri")
    
#yosh = int(input("Yoshingiz nechida?>>>"))
#if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
#    print('Xush kelibsiz!')
#else: # ask holda
#    print('Kirish mumkin emas!')   
    
#login = input("Yangi login tanlang:")
#if len(login)<=5: # login uzunligini tekshiramiz
#    print("Login 5 harfdan ko'proq bo'lishi shart!")   
    
#yil = int(input("Tug'ilgan yilingizni kiriting:"))
#if 2024-yil<18: # foydalanuvchining yoshini hisoblaymiz
#    print(f"Yoshingiz {2024-yil}da ekan.")
#    print("Kirish mumkin emas!")
#else:
#    print("Xush kelibsiz!")

#BIR QATOR if/else
    
#yosh = int(input("Yoshingiz nechida?>>>"))
#if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")   
    
#x, y = 25, 50 # x=25 va y=50
#print("x>y") if x>y else print("x<y")   
    
    