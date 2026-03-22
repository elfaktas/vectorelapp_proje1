import turtle


def cizgi():
    print("=" * 42)


def menu_goster():
    print()
    print("┌──────────────────────────────────────┐")
    print("│             CIZIM MENUSU             │")
    print("├──────────────────────────────────────┤")
    print("│ 1 - Spiral Yildiz                    │")
    print("│ 2 - Mandala                          │")
    print("│ 3 - Fraktal Agac                     │")
    print("│ 4 - ELIF Yazisi                      │")
    print("│ 5 - Kalp Cizimi                      │")
    print("│ 0 - Cikis                            │")
    print("└──────────────────────────────────────┘")


def ekran_hazirla(baslik="Turtle Cizim", arka_plan="white"):
    ekran = turtle.Screen()
    ekran.bgcolor(arka_plan)
    ekran.setup(width=900, height=700)
    ekran.title(baslik)

    kalem = turtle.Turtle()
    kalem.hideturtle()
    kalem.speed(0)

    return ekran, kalem


def spiral_yildiz():
    ekran, kalem = ekran_hazirla("Spiral Yildiz", "white")

    n = 50
    kalem.speed(0)
    kalem.pensize(2)
    kalem.color("black")

    for i in range(n):
        kalem.forward(i * 10)
        kalem.right(144)

    print("\nSpiral yildiz acildi.")
    print("Cizim penceresine tiklayinca kapanir.")
    ekran.exitonclick()


def mandala_ciz():
    ekran, kalem = ekran_hazirla("Mandala", "white")

    renkler = ["purple", "blue", "deeppink", "orange", "green", "red"]
    kalem.pensize(2)

    for i in range(72):
        kalem.color(renkler[i % len(renkler)])
        for _ in range(6):
            kalem.forward(110)
            kalem.right(60)
        kalem.right(5)

    print("\nMandala acildi.")
    print("Cizim penceresine tiklayinca kapanir.")
    ekran.exitonclick()


def fraktal_agac():
    ekran, kalem = ekran_hazirla("Fraktal Agac", "lightblue")

    kalem.color("brown")
    kalem.pensize(3)
    kalem.penup()
    kalem.goto(0, -260)
    kalem.setheading(90)
    kalem.pendown()

    def dal(uzunluk):
        if uzunluk < 12:
            kalem.color("green")
            kalem.dot(8)
            kalem.color("brown")
            return

        kalem.forward(uzunluk)

        kalem.right(25)
        dal(uzunluk - 15)

        kalem.left(50)
        dal(uzunluk - 15)

        kalem.right(25)
        kalem.backward(uzunluk)

    dal(95)

    print("\nFraktal agac acildi.")
    print("Cizim penceresine tiklayinca kapanir.")
    ekran.exitonclick()


def elif_yazisi():
    ekran, kalem = ekran_hazirla("ELIF Yazisi", "lavender")

    kalem.color("purple")
    kalem.pensize(7)

    # E
    kalem.penup()
    kalem.goto(-300, -60)
    kalem.setheading(90)
    kalem.pendown()
    kalem.forward(140)
    kalem.right(90)
    kalem.forward(70)
    kalem.backward(70)
    kalem.right(90)
    kalem.forward(70)
    kalem.left(90)
    kalem.forward(55)
    kalem.backward(55)
    kalem.right(90)
    kalem.forward(70)
    kalem.left(90)
    kalem.forward(70)

    # L
    kalem.penup()
    kalem.goto(-160, -60)
    kalem.setheading(90)
    kalem.pendown()
    kalem.forward(140)
    kalem.backward(140)
    kalem.right(90)
    kalem.forward(70)

    # I
    kalem.penup()
    kalem.goto(-40, -60)
    kalem.setheading(90)
    kalem.pendown()
    kalem.forward(140)

    # F
    kalem.penup()
    kalem.goto(60, -60)
    kalem.setheading(90)
    kalem.pendown()
    kalem.forward(140)
    kalem.right(90)
    kalem.forward(70)
    kalem.backward(70)
    kalem.left(90)
    kalem.backward(70)
    kalem.right(90)
    kalem.forward(55)

    print("\nELIF yazisi acildi.")
    print("Cizim penceresine tiklayinca kapanir.")
    ekran.exitonclick()


def kalp_ciz():
    ekran, kalem = ekran_hazirla("Kalp Cizimi", "white")

    kalem.speed(3)
    kalem.color("red", "pink")
    kalem.pensize(2)

    def curve():
        for _ in range(200):
            kalem.right(1)
            kalem.forward(1)

    kalem.penup()
    kalem.goto(0, -100)
    kalem.pendown()

    kalem.begin_fill()
    kalem.left(140)
    kalem.forward(111.65)
    curve()
    kalem.left(120)
    curve()
    kalem.forward(111.65)
    kalem.end_fill()

    print("\nKalp cizimi acildi.")
    print("Cizim penceresine tiklayinca kapanir.")
    ekran.exitonclick()


while True:
    menu_goster()
    secim = input("Seciminizi girin: ").strip()

    if secim == "1":
        cizgi()
        print("Spiral yildiz secildi.")
        cizgi()
        spiral_yildiz()

    elif secim == "2":
        cizgi()
        print("Mandala secildi.")
        cizgi()
        mandala_ciz()

    elif secim == "3":
        cizgi()
        print("Fraktal agac secildi.")
        cizgi()
        fraktal_agac()

    elif secim == "4":
        cizgi()
        print("ELIF yazisi secildi.")
        cizgi()
        elif_yazisi()

    elif secim == "5":
        cizgi()
        print("Kalp cizimi secildi.")
        cizgi()
        kalp_ciz()

    elif secim == "0":
        cizgi()
        print("Program kapatildi.")
        cizgi()
        break

    else:
        cizgi()
        print("Gecersiz secim yaptiniz. Tekrar deneyin.")
        cizgi()