import turtle


def ekran_hazirla(baslik):
    ekran = turtle.Screen()
    ekran.title(baslik)
    ekran.bgcolor("white")
    ekran.setup(width=900, height=700)
    return ekran


def kalem_olustur(hiz=0, kalinlik=2):
    t = turtle.Turtle()
    t.speed(hiz)
    t.pensize(kalinlik)
    return t


def dolu_kalp():
    boyut = int(input("Kalp için boyut giriniz (örn: 120): "))

    ekran_hazirla("Dolu Kalp")
    t = kalem_olustur(0, 3)

    t.color("red", "deeppink")
    t.penup()
    t.goto(0, -120)
    t.pendown()

    t.begin_fill()
    t.left(140)
    t.forward(boyut)

    for _ in range(200):
        t.right(1)
        t.forward(boyut * 0.018)

    t.left(120)

    for _ in range(200):
        t.right(1)
        t.forward(boyut * 0.018)

    t.forward(boyut)
    t.end_fill()

    t.hideturtle()
    turtle.done()


def mandala():
    uzunluk = int(input("Mandala için uzunluk giriniz (örn: 120): "))

    ekran_hazirla("Mandala")
    t = kalem_olustur(0, 2)

    renkler = [
        "purple", "deep pink", "red", "orange",
        "gold", "green", "turquoise", "blue"
    ]

    for i in range(72):
        t.pencolor(renkler[i % len(renkler)])

        for _ in range(6):
            t.forward(uzunluk)
            t.right(60)
            t.circle(18)

        t.right(5)

    t.hideturtle()
    turtle.done()


def renkli_spiral():
    baslangic = int(input("Spiral için başlangıç uzunluğu giriniz (örn: 5): "))

    ekran_hazirla("Renkli Spiral")
    t = kalem_olustur(0, 3)

    renkler = [
        "red", "orange", "gold", "lime green",
        "cyan", "dodger blue", "blue violet", "magenta"
    ]

    uzunluk = baslangic

    for i in range(120):
        t.pencolor(renkler[i % len(renkler)])
        t.forward(uzunluk)
        t.right(91)
        uzunluk += 3

    t.hideturtle()
    turtle.done()


def ic_ice_kareler():
    baslangic = int(input("İlk kare uzunluğunu giriniz (örn: 40): "))

    ekran_hazirla("İç İçe Kareler")
    t = kalem_olustur(0, 2)

    renkler = [
        "navy", "purple", "deep pink", "tomato",
        "orange", "gold", "green", "deepskyblue"
    ]

    uzunluk = baslangic

    for i in range(30):
        t.pencolor(renkler[i % len(renkler)])

        for _ in range(4):
            t.forward(uzunluk)
            t.right(90)

        t.penup()
        t.goto(t.xcor() - 5, t.ycor() - 5)
        t.pendown()

        uzunluk += 10

    t.hideturtle()
    turtle.done()


while True:
    print("\n" + "═" * 46)
    print("               ANA MENÜ")
    print("═" * 46)
    print("╔════╦════════════════════════════════════╗")
    print("║ 1  ║ Dolu Kalp                         ║")
    print("║ 2  ║ Mandala                           ║")
    print("║ 3  ║ Renkli Spiral                     ║")
    print("║ 4  ║ İç İçe Kareler                    ║")
    print("║ 0  ║ Çıkış                             ║")
    print("╚════╩════════════════════════════════════╝")

    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        dolu_kalp()
        break
    elif secim == "2":
        mandala()
        break
    elif secim == "3":
        renkli_spiral()
        break
    elif secim == "4":
        ic_ice_kareler()
        break
    elif secim == "0":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Hatalı seçim yaptınız. Tekrar deneyin.")