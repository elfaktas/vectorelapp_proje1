dimport turtle
import math


def ekran_ayarla():
    ekran = turtle.Screen()
    ekran.title("Şekil Çizdirme Menüsü")
    ekran.bgcolor("white")


def kaplumbaga_olustur(hiz=10, kalinlik=2):
    t = turtle.Turtle()
    t.speed(hiz)
    t.pensize(kalinlik)
    return t


def kar_tanesi():
    uzunluk = int(input("Kar tanesi için uzunluk giriniz: "))

    ekran_ayarla()
    t = kaplumbaga_olustur(10, 2)
    t.pencolor("blue")

    for i in range(8):
        t.forward(uzunluk)
        t.backward(uzunluk)
        t.right(45)

    turtle.done()


def kalp():
    boyut = int(input("Kalp için boyut giriniz: "))

    ekran_ayarla()
    t = kaplumbaga_olustur(10, 3)
    t.pencolor("red")
    t.fillcolor("red")

    t.begin_fill()
    t.left(140)
    t.forward(boyut)

    for i in range(200):
        t.right(1)
        t.forward(boyut * 0.018)

    t.left(120)

    for i in range(200):
        t.right(1)
        t.forward(boyut * 0.018)

    t.forward(boyut)
    t.end_fill()

    turtle.done()


def spiral():
    baslangic = int(input("Spiral için başlangıç uzunluğu giriniz: "))

    ekran_ayarla()
    t = kaplumbaga_olustur(10, 3)

    renkler = ["red", "orange", "yellow", "green", "blue", "purple"]

    uzunluk = baslangic

    for i in range(60):
        t.pencolor(renkler[i % len(renkler)])
        t.forward(uzunluk)
        t.right(45)
        uzunluk += 4

    turtle.done()


def virus():
    yaricap = int(input("Virüs için merkez yarıçapı giriniz: "))

    ekran_ayarla()
    t = kaplumbaga_olustur(10, 2)
    t.pencolor("purple")

    t.penup()
    t.goto(0, -yaricap)
    t.pendown()
    t.circle(yaricap)

    for i in range(16):
        aci = i * 22.5
        x = yaricap * math.cos(math.radians(aci))
        y = yaricap * math.sin(math.radians(aci))

        t.penup()
        t.goto(x, y)
        t.setheading(aci)
        t.pendown()
        t.forward(25)
        t.dot(12, "purple")

    turtle.done()


print("\n" + "=" * 40)
print("         ŞEKİL ÇİZDİRME MENÜSÜ")
print("=" * 40)
print("1 - Kar Tanesi")
print("2 - Dolu Kalp")
print("3 - Renk Geçişli Spiral")
print("4 - Virüs")
print("0 - Çıkış")
print("=" * 40)

secim = input("Seçiminizi yapın: ")

if secim == "1":
    kar_tanesi()
elif secim == "2":
    kalp()
elif secim == "3":
    spiral()
elif secim == "4":
    virus()
elif secim == "0":
    print("Programdan çıkılıyor...")
else:
    print("Hatalı seçim yaptınız.")