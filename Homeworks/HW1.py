# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 00:21:12 2021

@author: AYSEL
"""
### 0-100 arasında bulunan asal sayılarla 3X3' lük bir matris oluşturulması.
import random

primeNumbers = []                    

# 0-100 arasında bulunan asal sayıların primeNumbers listesine eklenmesi.
for i in range(0, 100):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            primeNumbers.append(i)

# Matrisin satır ve sütun sayıları atandı.
column = 3                                                      
line = 3

# primeNumbers listesinde tutulan asal sayılar rastgele olarak for döngüsü ile matrix listesine atandı.
# random.coice() metodu kullanılarak liste içerisinden rastgele eleman seçimi sağlandı.
matrix = [print([random.choice(primeNumbers) for i in range(column)]) for j in range(line)]
