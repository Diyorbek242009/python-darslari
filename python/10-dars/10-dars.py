# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 22:48:28 2024

@author: user
"""

#if-elif-else

#yosh = int(input('Yoshingiz nechida? '))
#if yosh<=4:
#    print('Sizga kirish bepul.')
#elif yosh<=12:
#    print('Sizga kirish 5000 so\'m')
#else:
#    print("Sizga kirish 10000 so'm")

#yosh = int(input('Yoshingiz nechida? '))
#if yosh<=4:
#    price = 0
#elif yosh<=12:
#    price = 5000
#else:
#    price = 10000
    
#print(f"Sizga kirish {price} so'm")

#yosh = int(input('Yoshingiz nechida? '))
#if yosh<=4: # yosh bolalarga bepul
#    price = 0
#elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
#    price = 5000
#elif yosh<65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
#    price = 10000
#else: # qariyalarga esa 8000 so'm
#    price = 8000
#print(f"Sizga kirish {price} so'm")

#yosh = int(input('Yoshingiz nechida? '))
#if yosh<=4:
#    price = 0
#elif yosh<=12:
#    price = 5000
#elif yosh<65:
#    price = 10000
#elif yosh>=65:
#    price = 8000    
#print(f"Sizga kirish {price} so'm")

#AND, OR OPERATORLARI
#OR OPERATOI

#kun = input("Bugun nima kun?>>>")
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#    print('Bugun dam olish kuni.')
#else:
#    print('Bugun ish kuni.')

#kun = input("Bugun nima kun?>>>")
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#    print('Bugun dam olish kuni.')
#else:
#    print('Bugun ish kuni.')

#AND OPERATORI

#kun = input("Bugun nima kun?")
#harorat = float(input("Havo harorati qanday?"))
#if kun.lower()=='yakshanba' and harorat>=30:
#    print("Cho'milgani ketdik!")
#elif kun.lower()=='yakshanba' and harorat<30:
#    print("Uyda dam olamiz!")

#kun = input("Bugun nima kun?")
#harorat = float(input("Havo harorati qanday?"))
#if kun.lower()=='yakshanba' and harorat>=30:
#    print("Cho'milgani ketdik!")
#elif kun.lower()=='yakshanba' and harorat<30:
#    print("Uyda dam olamiz!")

#BIR NECHTA SHARTLARNI KETMA-KET YOZISH

#kun = input("Bugun nima kun?")
#harorat = float(input("Havo harorati qanday?"))
#if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#    print("Cho'milgani ketdik!")
#elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#    print("Uyda dam olamiz!")

#BOOLEAN MA'LUMOTLAR TURI

#narh = 15000 # mijoz 15000 so'mga taom oldi.
#choy = True # mijoz choy ham oldi
#salat = False # mijoz salat olmadi

#if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
#    narh = narh + 10000 # narhga 10000 so'm qo'shamiz
#elif choy or salat: # agar choy yoki salat olgan bo'lsa
#    narh = narh + 5000 # narhga 5000 so'm qo'shamiz

#print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz

#SHARTLARNI KETMA-KET TEKSHIRISH

#narh = 15000 # mijoz 15 so'mga ovqat oldi
#choy = True
#salat = False
#non = True
#kompot = True
#assorti = False
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
#if choy:   # agar choy olsa
#    print("Mijoz choy oldi.")
#    narh = narh + 3000
#if salat:  # agar salat olsa
#    print("Mijoz salat oldi.")
#    narh = narh + 5000
#if non:    # agar non olsa
#    print("Mijoz non oldi.")
#    narh = narh + 2000
#if kompot: # agar kompot olsa
#    print("Mijoz kompot oldi.")
#    narh = narh + 5000
#if assorti: # agar assorti olsa
#    print("Mijoz assorti oldi.")
#    narh = narh + 15000
    
#print(f"Jami {narh} so'm")

#RO'YXAT TARKIBINI TEKSHIRISH
#in OPERATORI

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#'manti' in menu # menu da manti bormi?

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#'osh' in menu # menu da osh bormi?

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#ovqat = input('Nima ovqat yeysiz?>>>')
#if ovqat.lower() in menu:
#    print('Buyurtma qabul qilindi.')
#else:
#    print('Afsuski bizda bunday ovqat yo\'q')

#not in OPERATORI

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#'manti' not in menu # menu da manti yo'qmi?

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#'osh' not in menu # menu da osh yo'qmi?

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#ovqat = input('Nima ovqat yeysiz?>>>')
#if ovqat.lower() not in menu:
#    print('Afsuski bizda bunday ovqat yo\'q')
#else:
#    print('Buyurtma qabul qilindi.')

#IKKI RO'YXATNI SOLISHTIRISH

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#buyurtmalar = ["osh","somsa","manti", "shashlik"]

#for taom in buyurtmalar:
#    if taom in menu:
#        print(f"Menuda {taom} bor")
#    else:
#        print(f"Kechirasiz, menuda {taom} yo'q")

#RO'YXAT BO'SH EMASLIGINI TEKSHIRISH

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#buyurtmalar = ["osh","somsa","manti", "shashlik"]

#if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f"Menuda {taom} bor")
#        else:
#            print(f"Kechirasiz, menuda {taom} yo'q")
#else: # agar ro'yxat bo'sh bo'lsa
#    print("Savatchangiz bo'sh!")
