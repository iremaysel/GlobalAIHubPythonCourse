# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 23:10:09 2021

@author: AYSEL
"""
### Kullanıcıdan alınan, öğrenci ad-soyad bilgilerinin ve notlarının 
### sözlük veri tipine aktararak en başarılı öğrencinin bulunması

print("Öğrencinin ad, soyad ve not bilgilerini giriniz!")

# Öğrenci sayısı ve not sayısı
numberOfStudent, numberOfNote = 5 , 3

# Öğrenci bilgilerinin ve not değerlerinin tutulduğu listeler.
students = [[0 for i in range(2)] for j in range(numberOfStudent)]
note = [[0 for i in range(numberOfNote)] for j in range(numberOfStudent)]

# Tüm bilgilerin tutulacağı sözlük yapısı.
information = {}

for i in range(0, numberOfStudent):
    print(f"{i+1}. Ogrenci:")
    students[i][0] = input("Adı : ").title()
    students[i][1] = input("Soyadı : ").title()
    for j in range(0, numberOfNote):
        if (j == 0):
            try:
                note[i][j] = int(input("Arasinav Notu : "))
            except ValueError:
                # Eğer integer veri tipinden başka değer girilirse not değeri 0 kabul edilecek.
                print("GEÇERSİZ DEĞER! NOT = 0")
                note[i][j] = 0                
        elif (j == 1):
            try:
                note[i][j] = int(input("Final Notu : "))
            except ValueError:
                print("GEÇERSİZ DEĞER! NOT = 0")
                note[i][j] = 0  
        elif (j == 2):
            try:
                note[i][j] = int(input("Odev Notu : "))
            except ValueError:
                print("GEÇERSİZ DEĞER! NOT = 0")
                note[i][j] = 0  
    # Sözlük yapısının key değerlerine 'students' liste elemanları atandı.
    # Sözlük yapısının value değerlerine 'note' liste elemanları atandı.
    information[students[i][0]+ " " + students[i][1]] = note[i]
print(information)

# En yüksek ortalamaya sahip öğrenciyi bulmak için for yapısı.
max = 0
key = ""
total = 0
for k,v in information.items():
    for i in range(len(v)):
        total += v[i]
    # 3 notun ortalaması average değişkenine atandı.
    average = total/3 
    if (max < average):
        max = average
        key = k
print(f"{key}, {max} ortalamayla 1. olmuştur. Tebrikler :) ")
