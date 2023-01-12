from matplotlib import pyplot as plt
import numpy as np
import tkinter as tk

window = tk.Tk()
window.geometry("500x400")
window.title("Merhaba! Şekil alan hesabı modülüne hoşgeldiniz")
entry = tk.Entry(window, bg = "red", fg = "black")
entry.pack()
window.mainloop()

def üçgen():
    x = int(input("Üçgenin taban uzunluğunu giriniz...:"))  # Değer Girilir.;
    y = int(input("Üçgenin yükseklik uzunluğunu giriniz...:"))  # Değer Girilir.;
    print("Üçgenin Alanı....:", int(x * y / 2))  # Değerler Çarpılır, 2'ye bölünür.
    buttona.pack()


def kare():
    x = int(input("Karenin bir kenarını giriniz...:"))  # Değer Girilir.;
    print("Karenin Alanı....:", x ** 2)  # Değerin Karesi Alınır..: Kare alma işlemi '**' ile yapılır.


def dikdörtgen():
    x = int(input("Dikdörtgenin birinci kenarını giriniz...:"))  # Değer Girilir.;
    y = int(input("Dikdörtgenin ikinci kenarını giriniz...:"))  # Değer Girilir.;
    print("Dikdörtgenin Alanı....:", x * y)  # Değerler Çarpılır.



def paralelkenar():
    x = int(input("Paralel Kenarın taban uzunluğunu giriniz...:"))  # Değer Girilir.;
    y = int(input("Paralel Kenarın yükseklik uzunluğunu giriniz...:"))  # Değer Girilir.;
    print("Paralel Kenarın Alanı....:", x * y)  # Değerler Çarpılır.

def daire():
    x = int(input("Dairenin yarıçap uzunluğunu giriniz...:"))  # Değer Girilir.;
    print("Dairenin Alanı....:", x ** 2 * 3)  # Yarıçapın Karesi alınır ve 3(π) ile Çarpılır

def quit():
    window.destroy()


buttona = tk.Button(window,text="üçgen alanı", command=üçgen())
buttona.pack()

buttonb = tk.Button(window, text="kare alanı", command=kare())
buttonb.pack()

button3 = tk.Button(window,text="didörtgen alanı", command=dikdörtgen())
button3.pack()

button4 = tk.Button(window,text="paralelkenar alanı", command=paralelkenar())
button4.pack()

button5 = tk.Button(window,text="daire alanı", command=daire())
button5.pack()

button6 = tk.Button(window, text="Çıkış", command=quit())
button6.pack()

window.mainloop()










