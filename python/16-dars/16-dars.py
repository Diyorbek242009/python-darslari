# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 18:59:55 2024

@author: user
"""
#Funksiyalar

# FUNKSIYA YARATAMIZ

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")

# salom_ber()

#FUNKSIYAGA QIYMAT UZATISH

# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")

#salom_ber('hasan')

#DOCSTRING

# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib, 
#         unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")

#print(salom_ber.__doc__)

#salom_ber('hasan')
#salom_ber('olim')

#ARGUMENT VA PARAMETER
#FUNKSIYAGA BIR NECHTA ARGUMENT UZATISH
#TO'G'RI TARTIBDA UZATISH

# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")

#toliq_ism('olim','hakimov')
#toliq_ism('hakimov','olim')

# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2020-tugilgan_yil} yoshda")

# yosh_hisobla('olim', 1997)

#KALIT SO'Z BILAN UZATISH

#yosh_hisobla(tugilgan_yil=1997, ism='olim')

#toliq_ism(familiya='hakimov',ism='olim')

#STANDART QIYMAT

# def yosh_hisobla(tugilgan_yil, joriy_yil=2020): # joriy yil uchun st.qiymat 2020
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# yosh_hisobla(1995,2020)
# yosh_hisobla(1993)

#FUNKSIYAGA MUROJAT QILISHDA XATOLIKLAR

# def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# tyil = input("Tug'ilgan yilingizni kiriting: ")
# yosh_hisobla(tyil)

# def yosh_hisobla(tugilgan_yil, joriy_yil):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# yosh_hisobla(1993)

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")

# salom_ber('hasan')

# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
 
#  toliq_ism('olim hakimov')    