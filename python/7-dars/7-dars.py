# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 23:18:56 2024

@author: user
"""

#Ro'yxat bilan ishlash.O'zgarmas ro'yxatlar (Tubles)

#RO'YXATNI TARTIBLASH
#cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
#cars.sort()
#print(cars)

#Ro'yxatni teskari tartibda saqlash
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort(reverse=True)
print(cars)

#elementlarning ketma-ketligini buzmagan holda ro'yxatni tartiblash
#mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
#print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
#print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)

#sorted() funktsiyasi yordamida teskari tartiblash uchun ham reverse=True argumentini beramiz
#print(sorted(mehmonlar, reverse=True))

#Sonli ro'yxatlarni ham tartiblash
#ages = [12, 98, 34, 65, 34, 76, 11]
#ages.sort()
#print(ages)
#print(sorted(ages, reverse=True))

#RO'YXATNI AYLANTIRISH
#fruits = ['pear','banana','apple','watermelon','lemon']
#fruits.reverse()
#print(fruits)

#RO'YXATNING UZUNLIGINI BILISH
#fruits = ['pear','banana','apple','watermelon','lemon']
#print("Elementlar soni:",len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi

#range() FUNKTSIYASI
#Sonlar ketma-ketligini yaratish
#sonlar = list(range(0,10)) # 
#print(sonlar)

#range() yordamida qadamni ham berish
#juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
#toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
#print("Juft sonlar: ", juft_sonlar)
#print("Toq sonlar: ", toq_sonlar)

#SONLI RO'YXAT USTIDA SODDA AMALLAR
#sodda amallarni bajarish,eng kichik min() ,eng katta max() , yig'indisini topish sum()   
#narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
#arzon = min(narhlar)
#qimmat = max(narhlar)
#jami = sum(narhlar)
#print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

#RO'YXATNI KESISH
#cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
#my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
#print(my_cars) 
#print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)

#Agar boshlang'ich indeksni bermasangiz, Python avtomat ravishda 0 indeksdan boshlab kesadi. Agar 2-indeksni kiritmasangiz, ro'yxat oxirigacha kesadi
#print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
#print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

#RO'YXATDAN NUSXA OLISH
#sonlar = [1, 2, 3, 4, 5] # sonlar degan ro'yxat yaratamiz
#sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
#sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
#sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
#print("Bu sonlar ro'yxati:", sonlar)
#print("Bu sonlar2 ro'yxati:", sonlar2)
#Unda, qanday qilib ro'yxatdan nusxa olamiz? Buning uchun yuoqirdagi ka'bi ro'yxatni kesish usulidan foydalanamiz. Faqatgina, kvadrat qavs ichida ikkala indeksni ham ko'rsatmasdan, bo'sh qoldiramiz:
#sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
#sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi
#sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
#sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
#print("Bu sonlar ro'yxati:", sonlar)
#print("Bu sonlar2 ro'yxati:", sonlar2)    
    
#TUPLES - O'ZGARMAS RO'YXAT
#Dastur yaratish davomida o'zgarmas ro'yxat tuzish tuples deb yuritiladi.oddiy qavslar () ishlatiladi:
#tomonlar = (20, 30, 55.2)
#print(tomonlar)

#toys = ('bus','car','bear','dino','snake','lizard')
#print(toys[0])
#print(toys[-1])
#print(toys[2:5])

#Tuple ichidagi qiymatini o'zgartirish list()
#toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
#toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
## Ro'yxatga o'zgartirishlar kiritamiz
#toys.append('dragon')
#toys.remove('bus')
#toys[1] = 'mcqueen'
#toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
#print(toys)