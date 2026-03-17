def ana_menuyu_goster():
    print("\n================================")
    print("         HESAP MAKİNESİ")
    print("================================")
    print("1 - Toplama")
    print("2 - Çıkarma")
    print("3 - Çarpma")
    print("4 - Bölme")
    print("5 - Yüzde Hesaplama")
    print("6 - Ortalama Hesaplama")
    print("0 - Çıkış")
    print("================================")


def iki_sayi_al():
    sayi1 = float(input("1. sayıyı girin: "))
    sayi2 = float(input("2. sayıyı girin: "))
    return sayi1, sayi2


def toplama():
    try:
        sayi1, sayi2 = iki_sayi_al()
        print(f"Sonuç: {sayi1 + sayi2}")
    except ValueError:
        print("Lütfen geçerli sayı girin.")


def cikarma():
    try:
        sayi1, sayi2 = iki_sayi_al()
        print(f"Sonuç: {sayi1 - sayi2}")
    except ValueError:
        print("Lütfen geçerli sayı girin.")


def carpma():
    try:
        sayi1, sayi2 = iki_sayi_al()
        print(f"Sonuç: {sayi1 * sayi2}")
    except ValueError:
        print("Lütfen geçerli sayı girin.")


def bolme():
    try:
        sayi1, sayi2 = iki_sayi_al()
        if sayi2 == 0:
            print("Bir sayı 0'a bölünemez.")
        else:
            print(f"Sonuç: {sayi1 / sayi2}")
    except ValueError:
        print("Lütfen geçerli sayı girin.")


def yuzde_hesaplama_menusu():
    while True:
        print("\n--- YÜZDE HESAPLAMA ---")
        print("1 - Bir sayının yüzdesini bul")
        print("2 - Yüzde artış hesapla")
        print("0 - Ana menüye dön")

        secim = input("Seçiminiz nedir? ")

        if secim == "1":
            try:
                sayi = float(input("Sayıyı girin: "))
                yuzde = float(input("Yüzdeyi girin: "))
                print(f"Sonuç: {(sayi * yuzde) / 100}")
            except ValueError:
                print("Lütfen geçerli sayı girin.")

        elif secim == "2":
            try:
                eski_deger = float(input("Eski değeri girin: "))
                artis_yuzdesi = float(input("Artış yüzdesini girin: "))
                yeni_deger = eski_deger + (eski_deger * artis_yuzdesi / 100)
                print(f"Yeni değer: {yeni_deger}")
            except ValueError:
                print("Lütfen geçerli sayı girin.")

        elif secim == "0":
            break
        else:
            print("Geçersiz seçim yaptınız.")


def ortalama_hesaplama_menusu():
    while True:
        print("\n--- ORTALAMA HESAPLAMA ---")
        print("1 - 2 sayının ortalaması")
        print("2 - 3 sayının ortalaması")
        print("3 - İstenilen kadar sayının ortalaması")
        print("0 - Ana menüye dön")

        secim = input("Seçiminiz nedir? ")

        if secim == "1":
            try:
                s1 = float(input("1. sayıyı girin: "))
                s2 = float(input("2. sayıyı girin: "))
                print(f"Ortalama: {(s1 + s2) / 2}")
            except ValueError:
                print("Lütfen geçerli sayı girin.")

        elif secim == "2":
            try:
                s1 = float(input("1. sayıyı girin: "))
                s2 = float(input("2. sayıyı girin: "))
                s3 = float(input("3. sayıyı girin: "))
                print(f"Ortalama: {(s1 + s2 + s3) / 3}")
            except ValueError:
                print("Lütfen geçerli sayı girin.")

        elif secim == "3":
            try:
                adet = int(input("Kaç sayı gireceksiniz? "))
                if adet <= 0:
                    print("Sayı adedi 0'dan büyük olmalı.")
                    continue

                toplam = 0
                for i in range(1, adet + 1):
                    sayi = float(input(f"{i}. sayıyı girin: "))
                    toplam += sayi

                print(f"Ortalama: {toplam / adet}")
            except ValueError:
                print("Lütfen geçerli sayı girin.")

        elif secim == "0":
            break
        else:
            print("Geçersiz seçim yaptınız.")


def ana_program():
    print("Program başladı")

    while True:
        ana_menuyu_goster()
        secim = input("Seçiminiz nedir? ")

        if secim == "1":
            toplama()
        elif secim == "2":
            cikarma()
        elif secim == "3":
            carpma()
        elif secim == "4":
            bolme()
        elif secim == "5":
            yuzde_hesaplama_menusu()
        elif secim == "6":
            ortalama_hesaplama_menusu()
        elif secim == "0":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim yaptınız.")


if _name_ == "_main_":
    ana_program()

    