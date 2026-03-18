def menu_goster():
    print()
    print("╔══════════════════════════════╗")
    print("║        ÇİZİMLER MENÜSÜ       ║")
    print("╠══════════════════════════════╣")
    print("║ 1 - Kalp Çizimi              ║")
    print("║ 2 - Baklava Çizimi           ║")
    print("║ 3 - Elmas Çizimi             ║")
    print("║ 0 - Çıkış                    ║")
    print("╚══════════════════════════════╝")


def kalp_ciz():
    print("\nKALP ÇİZİMİ\n")

    ust_kisim = [1, 3]
    for i in ust_kisim:
        bosluk = " " * (3 - i)
        yildiz = "*" * (2 * i + 1)
        print(bosluk + yildiz + " " + yildiz)

    for i in range(4, 0, -1):
        bosluk = " " * (5 - i)
        yildiz = "*" * (2 * i - 1)
        print(bosluk + yildiz)


def baklava_ciz():
    print("\nBAKLAVA ÇİZİMİ\n")

    for i in range(1, 5):
        bosluk = " " * (4 - i)
        if i == 1:
            print(bosluk + "*")
        else:
            ic_bosluk = " " * (2 * i - 3)
            print(bosluk + "" + ic_bosluk + "")

    for i in range(3, 0, -1):
        bosluk = " " * (4 - i)
        if i == 1:
            print(bosluk + "*")
        else:
            ic_bosluk = " " * (2 * i - 3)
            print(bosluk + "" + ic_bosluk + "")


def elmas_ciz():
    print("\nELMAS ÇİZİMİ\n")

    for i in range(1, 5):
        bosluk = " " * (4 - i)
        yildiz = "*" * (2 * i - 1)
        print(bosluk + yildiz)

    for i in range(3, 0, -1):
        bosluk = " " * (4 - i)
        yildiz = "*" * (2 * i - 1)
        print(bosluk + yildiz)


while True:
    menu_goster()
    secim = input("Seçiminiz: ")

    if secim == "1":
        kalp_ciz()
    elif secim == "2":
        baklava_ciz()
    elif secim == "3":
        elmas_ciz()
    elif secim == "0":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Hatalı seçim yaptınız. Tekrar deneyin.")