# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 09:20:55 2024

@author: user
"""

# Modullar

# # MODUL YARATAMIZ

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# def avto_kirit():
#     """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
#     avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
#     while True:
#         print("\nQuyidagi ma'lumotlarni kiriting",end='')
#         kompaniya=input("Ishlab chiqaruvchi: ")
#         model=input("Modeli: ")
#         rangi=input("Rangi: ")
#         korobka=input("Korobka: ")
#         yili=input("Ishlab chiqarilgan yili: ")
#         narhi=input("Narhi: ")    
#         #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#         #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#         avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))    
#         # Yana avto qo'shish-qo'shmaslikni so'raymiz
#         javob = input("Yana avto qo'shasizmi? (yes/no): ")
#         if javob=='no':
#             break
#     return avtolar

# def info_print(avto_info):
#     """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
#     print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
#           f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
#           f"{avto_info['yil']}-yil, {avto_info['narh']}$")


# MODULNI CHAQIRIB OLISH

# import avto_info_mod # avto_info_mod faylini (modulini) chaqiramiz

# avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# avto_info_mod.info_print(avto1)

# MODULGA QISQA NOM BERISH

# import avto_info_mod as aim # avto_info_mod ni qisqa nom aim bilan chaqiramiz

# avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# aim.info_print(avto1)

# math MODULI

# sqrt() - qavs ichida berilgan qiymatning kvadrat ildizini qaytaradi

# import math

# x=400
# print(math.sqrt(x))

# pow(x,y) - x ning y-darajasini qaytaradi

# print(pow(5,5))

# pi - ning qiymatini saqlovchi o'zgaruvchi

# from math import pi
# print(pi)

# log2(x) va log10(x) - x` ning 2 va 10-lik logorifmini qaytaruvchi funksiyalar

# print(math.log2(8))
# print(math.log10(100))

# random MODULI

# import random as r # random modulini r deb chaqirayapmiz

# randint(a,b)

# son = r.randint(0,100) # 0 va 100 oralig'ida tasodifiy son
# print(son)

# choice(x)

# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
# print(ism)
# print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz

# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))

# shuffle(x)

# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)

