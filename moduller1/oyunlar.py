import random
def cizgi ():
    print("="*40)

def menu_goster():
print()
print(" ╔═════════════════════╗")
print(" ║    OYUNLAR MENÜSÜ   ║")
print(" ╠═════════════════════╣")
print(" ║  1-Taş Kağıt Makas  ║")
print(" ║  2-Sayı Tahmini     ║")
print(" ║  3-Zar Oyunu        ║")
print(" ║  0-Çıkış            ║")
print(" ║   Seçiminiz?        ║")
print(" ╚═════════════════════╝")

def tas_kagit_makas():
    while True:
        print("\nTAŞ KAĞIT MAKAS OYUNU")
        cizgi()
        print("1 - Taş")
        print("2 - Kağıt")
        print("3 - Makas")
        cizgi()

        secim = input("Seçiminizi yapın (1/2/3): ")

        if secim not in ["1", "2", "3"]:
            print("Geçersiz seçim yaptınız. Tekrar deneyin.")
            continue

        oyuncu = int(secim)
        bilgisayar = random.randint(1, 3)

        secimler = {
            1: "Taş",
            2: "Kağıt",
            3: "Makas"
        }

        print(f"\nSenin seçimin: {secimler[oyuncu]}")
        print(f"Bilgisayarın seçimi: {secimler[bilgisayar]}")

        if oyuncu == bilgisayar:
            print("Sonuç: Berabere!")
        elif (oyuncu == 1 and bilgisayar == 3) or \
             (oyuncu == 2 and bilgisayar == 1) or \
             (oyuncu == 3 and bilgisayar == 2):
            print("Sonuç: Kazandın! 🎉")
        else:
            print("Sonuç: Bilgisayar kazandı!")

        tekrar = input("\nTekrar oynamak ister misin? (e/h): ").lower()
        if tekrar != "e":
            break


def sayi_tahmin():
    print("\nSAYI TAHMİN OYUNU")
    cizgi()
    print("1 ile 10 arasında bir sayı tuttum.")
    print("3 tahmin hakkın var.")
    cizgi()

    tutulan_sayi = random.randint(1, 10)
    hak = 3

    while hak > 0:
        try:
            tahmin = int(input(f"Tahmininizi girin ({hak} hak kaldı): "))

            if tahmin == tutulan_sayi:
                print("Tebrikler! Doğru tahmin ettin 🎉")
                return
            elif tahmin < tutulan_sayi:
                print("Daha büyük bir sayı gir.")
            else:
                print("Daha küçük bir sayı gir.")

            hak -= 1

        except ValueError:
            print("Lütfen geçerli bir sayı gir.")

    print(f"Hakkın bitti. Doğru sayı: {tutulan_sayi}")


def zar_oyunu():
    while True:
        print("\nZAR OYUNU")
        cizgi()
        input("Zar atmak için Enter'a bas...")

        oyuncu_zar = random.randint(1, 6)
        bilgisayar_zar = random.randint(1, 6)

        print(f"\nSenin zarın: {oyuncu_zar}")
        print(f"Bilgisayarın zarı: {bilgisayar_zar}")

        if oyuncu_zar > bilgisayar_zar:
            print("Sonuç: Kazandın! 🎉")
        elif oyuncu_zar < bilgisayar_zar:
            print("Sonuç: Bilgisayar kazandı!")
        else:
            print("Sonuç: Berabere!")

        tekrar = input("\nTekrar oynamak ister misin? (e/h): ").lower()
        if tekrar != "e":
            break


while True:
    print("\n")
    menu_goster()
    secim = input("Bir seçim yapın: ")

    if secim == "1":
        tas_kagit_makas()
    elif secim == "2":
        sayi_tahmin()
    elif secim == "3":
        zar_oyunu()
    elif secim == "0":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Hatalı seçim yaptınız. Tekrar deneyin.")