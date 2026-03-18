import turtle
import math


def kar_tanesi():
    pencere = turtle.Screen()
    pencere.title("Kar Tanesi")
    pencere.bgcolor("white")

    t = turtle.Turtle()
    t.speed(10)
    t.pensize(2)
    t.pencolor("blue")

    uzunluk = int(input("Kar tanesi için uzunluk giriniz: "))

    for i in range(8):
        t.forward(uzunluk)
        t.backward(uzunluk)
        t.right(45)

    turtle.done()


def kalp():
    pencere = turtle.Screen()
    pencere.title("Dolu Kalp")
    pencere.bgcolor("white")

    t = turtle.Turtle()
    t.speed(10)
    t.pensize(3)
    t.pencolor("red")
    t.fillcolor("red")

    boyut = int(input("Kalp için boyut giriniz: "))

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
    pencere = turtle.Screen()
    pencere.title("Renk Geçişli Spiral")
    pencere.bgcolor("white")

    t = turtle.Turtle()
    t.speed(10)
    t.pensize(3)

    baslangic = int(input("Spiral için başlangıç uzunluğu giriniz: "))

    renkler = ["red", "orange", "yellow", "green", "blue", "purple"]
    uzunluk = baslangic

    for i in range(60):
        t.pencolor(renkler[i % len(renkler)])
        t.forward(uzunluk)
        t.right(45)
        uzunluk += 4

    turtle.done()


def virus():
    pencere = turtle.Screen()
    pencere.title("Virüs")
    pencere.bgcolor("white")

    t = turtle.Turtle()
    t.speed(10)
    t.pensize(2)
    t.pencolor("purple")

    yaricap = int(input("Virüs için merkez yarıçapı giriniz: "))

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


while True:
    print("\n" + "═" * 42)
    print("            ANA MENÜ")
    print("═" * 42)
    print("1 - Kar Tanesi")
    print("2 - Dolu Kalp")
    print("3 - Renk Geçişli Spiral")
    print("4 - Virüs")
    print("0 - Çıkış")
    print("═" * 42)

    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        kar_tanesi()
        break
    elif secim == "2":
        kalp()
        break
    elif secim == "3":
        spiral()
        break
    elif secim == "4":
        virus()
        break
    elif secim == "0":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Hatalı seçim yaptınız. Tekrar deneyin.")