# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 19:56:42 2021

@author: AYSEL
"""
### 0-500 arasındaki asal sayıları prime_first ve 
### 500-1000 arasındaki asal sayıları prime_second fonksiyonu ile ekrana yazdırılması.


# 0-500 arasında ki asal sayıları ekrana yazdıran fonksiyon.
def prime_first(number_1):
    print(f"prime_fist fonksiyonu çalışıyor!! Sayı: {number_1}")

# 500-1000 arasında ki asal sayıları ekrana yazdıran fonksiyon.
def prime_second(number_2):
    print(f"prime_second fonksiyonu çalışıyor!! Sayı: {number_2}")

# 0-1000 arasındaki asal sayıları bulan döngü
for i in range(0, 1000):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:  
            if (i < 500):
                prime_first(i)
                if (i == 499):
                    print("\n")
                    
            elif (i >= 500):
                prime_second(i)
