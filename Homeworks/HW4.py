# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 13:52:08 2021

@author: AYSEL
"""
import random

print("\n***HANGMAN***\n")
print("HOŞGELDİNİZ\n")
print("OYUNUN KURALLARI!\n"
      ">5 adet tahmin hakkınız vardır.\n"
      ">Her seferinde tek harf girmelisiniz.\n"
      ">Aksi takdirde 1 can kaybınız olur!\n")

class HangMan:
    def __init__(self):
        # Yanlış tahmin yapıldıkça ekrana bastırılacak şekil.
        self.figure = ['''
            +---+     
            |   |
            O   |
           /|\  |
           / \  |
                |
        =========''','''
            +---+
            |   |
            O   |
           /|\  |
                |
                |
        =========''','''
            +---+
            |   |
            O   |
            |   |
                |
                |
        =========''','''
            +---+
            |   |
            O   |
                |
                |
                |
        =========''','''
            +---+
            |   |
                |
                |
                |
                |
        =========''']

        self.label = True

        # txt uzantılı dosyadan çekilen kelimeler bu listeye aktarılacak.
        self.wordList = list()

        # Oluşturduğum wordList.txt dosyası listeye aktarıldı.
        with open("wordList.txt", "r", encoding="utf-8") as file:
            self.fileContent = file.read()
            self.wordList = (self.fileContent).split("\n")
                           
        # Oyun Hakkı
        self.life = 5

    # Listeden random kelime çeker.
    def randomWord(self):
        word = random.choice(self.wordList)
        # listeden alınan kelimenin her harfini küçük yap.
        self.word = word.lower()
        
    # Kelimeyi işaretler
    def starMarking(self):
        starWord = list()
        for i in range(0, len(self.word)):
            starWord.append("#")
        self.starWord = starWord
        print("".join(starWord))
        self.starWord = starWord
        return None
        
    # Kullancıdan Harf tahimini alan fonksiyon
    def letter(self):
        guessLetter = input("Bir Harf Girin: ")
        guessLetter = guessLetter.lower()
        self.guessLetter = guessLetter

    # Sayaç kontrolü
    def counter(self):
        if (self.life) >= 1:
            print(f"{self.life} hakkınız kaldı!")   
        elif (self.life) == 0:
            print("Oyun Bitti!")
         
    # Oyun kontrolleri
    def play(self):
        if len(self.guessLetter) > 1 or len(self.guessLetter) == 0:
            print(f"{len(self.guessLetter)} ADET KARAKTER GİRDİNİZ. LÜTFEN 1 TANE HARF GİRİN.\n")
            self.life -= 1

        elif self.guessLetter not in self.word:
            self.life -=1
            print(f"Yanlış Tahmin! :( {self.life} hakkınız kaldı. ") 
            print(self.figure[self.life])

        elif self.guessLetter.isalpha() == False:
            print(f"Alfanümerik olmayan bir değer girdiniz. \n{self.life} hakkınız kaldı.")

        else: 
            print("Doğru Tahmin :)\n")
            for i in range(0, len(self.word)):
                if self.guessLetter == self.word[i]:
                    self.starWord[i] = self.guessLetter
        
        print("".join(self.starWord))
        
    # Kazanma durumu
    def win(self):
        if "#" not in self.starWord:
            print(f"Tebrikler :) {self.word} kelimesini buldunuz.")
            return True

    # Kaybetme durumu
    def loss(self):
        if "#" in self.starWord:
            print(f"Kaybettiniz.\nBulunamayan kelime : {self.word}")
   
    # Devam ya da Tamam kısmı
    def byeOrContinue(self):
        try:
            print("\nTekrar oynamak isterseniz 'e' ye basın!\nÇıkmak isterseniz 'q' harfine basın!")
            state = input(">>e ya da q : ")

            if state == "e" or state == "E":
                againGame = HangMan()
                return againGame.go()
            elif state == "q" or state == "Q":
                print("Çıkış Yapılıyor...")
                return False
            else: 
                print("Yanlış Tuşlama Yaptınız!. Tekrar Deneyin.")
                return HangMan().byeOrContinue()
        except:
            print("Yanlış Tuşlama Yaptınız!. Tekrar Deneyin.")
            return HangMan().byeOrContinue()

    # Durum 
    def status(self):
        self.label = HangMan().byeOrContinue()
        return self.label
    
    # Oyunu başlatır.
    def go(self):
        game = HangMan()

        while game.label == True:

            game.randomWord()
            game.starMarking()
            game.counter()

            while game.life > 0:

                game.letter()
                game.play()
                game.counter()

                if game.win() == True:
                    break

            # Kaybetme ve devam durumuna gel.
            game.loss()
            game.status()

game = HangMan()
game.go()