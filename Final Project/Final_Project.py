# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:30:15 2021

@author: AYSEL
"""
### 3 Adet yemek tarifinin OOP kullanarak oluşturulması.

class Recipe:
    def __init__(self,foodName):
        self.foodName = foodName
        
    # Karıştırma
    def mix(self):
        print("Malzemeleri karıştırın!")
    
    # Pişirme
    def cook(self,timee, foodName):
        self.timee = timee
        print(f"{timee}, {foodName} hazır.")
    
    # Afiyet Olsun
    def bonAppetit(self):
        print("Afiyet Olsun :)")
        
# Sütlaç Tarifi
class Sutlac(Recipe):
    def __init__(self, foodName):
        super().__init__(foodName)
        self.milk = "süt"
        self.rice = "pirinç"
        self.ricefloor = "pirinç unu"
        self.water = "su"
        self.sugar = "şeker"
        
    # Yapılışı
    def materialsAdd(self, glass = "su bardağı", tablespoon = "yemek kaşığı"):
        print(f"Malzemeler: {self.milk}, {self.rice}, {self.ricefloor}, {self.water}, {self.sugar}.")
        print("Yapılışı:")
        print(f"*2 {glass} su ile 1/2 {glass} pirinci kaynatın.\n"
              f"*Pirinç suyu çekince 5 {glass} sütü ekleyin.\n"
              f"*Süt kaynadıktan sonra 1 {glass} şekeri ekleyin.\n"
              f"*Pirinç ununu 1 {glass} su ile karıştırın.")
        super().mix()
    # Pişirme
    def cook(self, timee = "Kaynamaya başladıktan sonra", foodName = "Sütlaç"):
        super().cook(timee, foodName)
        
    # Bekleme
    def wait(self):
        print("Dolapta 1-2 saat beklettikten sonra tüketebilirsiniz!")
        super().bonAppetit()
        
# Karnı Yarık Tarifi
class KarniYarik(Recipe):
    def __init__(self, foodName):
        super().__init__(foodName)
        self.eggplant = "patlican"
        self.oliveOil = "zeytin yağı"
        self.onion = "kuru soğan"
        self.pepper = "biber"
        self.mince = "kıyma"
        self.garlic = "sarımsak"
        self.sauce = "salça"
        self.tomato = "domates"
        self.salt = "tuz"
        self.blackPepper = "karabiber"

    # Yapılışı
    def materialsAdd(self,tablespoon = "yemek kaşığı", piece = "tane", gram = "gram", handful = "avuç"):
        print(f"Malzemeler: {self.eggplant}, {self.oliveOil}, {self.onion}, {self.pepper}, {self.mince} "
              f"{self.garlic}, {self.sauce}, {self.tomato}, {self.salt}, {self.blackPepper}") 
        print("Yapılışı:")
        print(f"*6 {piece} patlıcanı soyun ve tuzlu suda bekletin.\n"
              f"*3 {tablespoon} zeytinyağı ile birlikte doğranmış 1 {piece} soğanla kavurun.\n"
              f"*2 {piece} doğranmış yeşil biber ile 350 {gram} kıymayı ilave edin.")
        super().mix()
        print(f"*2 {piece} diş sarımsağı ve salçayı ekleyin.\n"
              f"*1/4 {tablespoon} tuz ve karabiber ekleyin.\n"
              f"*2 {piece} doğranmış domatesi ekleyin.")
        super().mix()   
        print("*Patlıcanları kızartın.\n"
              "*Hazırladığınız malzemeleri patlıcanların aralarını bölerek ekleyin.")
    # Pişirme
    def cook(self, timee ="20-25 Dakika kaynadıktan sonra,", foodName = "Karnı Yarık"):
        super().cook(timee, foodName)
        super().bonAppetit()

class Cacik(Recipe):
    def __init__(self,foodName):
        super().__init__(foodName)
        self.yoghurt = "yoğurt"
        self.water = "su"
        self.cucumber = "salatalık"
        self.garlic = "sarımsak"
        self.salt = "tuz"
     
    # Yapılışı
    def materialsAdd(self, piece = "tane", glass = "su bardağı"):
        print(f"Malzemeler: {self.yoghurt}, {self.water}, {self.cucumber}, {self.garlic}, {self.salt}.")
        print("Yapılışı:")
        print(f"*4 {piece} salatalığı soyup rendeleyin.\n"
              f"*2 {glass} yoğurt ile 1 {glass} suyu karıştırın.\n"
              f"*Yoğurda 2 {piece} diş sarımsağı ve salatalığı katın.")
        super().mix()
         
    def cook(self, timee ="Malzemeleri karıştırdıktan sonra",foodName = "Cacık"):
        super().cook(timee, foodName)
        super().bonAppetit()
        
foodName1 = "Sütlaç"
foodName2 = "Cacık"
foodName3 = "Karnı Yarık"
print(f"1 --> {foodName1} Tarifi\n"
      f"2 --> {foodName2} Tarifi\n"
      f"3 --> {foodName3} Tarifi")

try: 
    choose = int(input("Lütfen bakmak istediğiniz tarife tıklayın!(1-2-3) : "))
    print("\n")
    if (choose == 1):
        Sutlac(foodName1).materialsAdd()
        Sutlac(foodName1).cook()
        Sutlac(foodName1).wait()
    
    elif (choose == 2):
        Cacik(foodName2).materialsAdd()
        Cacik(foodName1).cook()
    
    elif (choose == 3):
        KarniYarik(foodName3).materialsAdd()
        KarniYarik(foodName3).cook()

    if (choose != 1 and choose != 2 and choose != 3):
        print("Hatali Kodlama Yaptiniz!")
        
except ValueError:
    print("\nLUTFEN GECERLI BIR DEGER GIRIN!!")
finally:
    
    print("\nCikis Yapiliyor...")
