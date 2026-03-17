def ana_menuyu_goster():
    print("\n================================")
    print("         HESAP MAKİNESİ")
    print("================================")
    print("1 - Toplama")
    print("2 - Çıkarma")
    print("3 - Çarpma")
    print("4 - Bölme")
    print("5 - Yüzde Hesaplama")
    print("    1. Bir sayının yüzdesini bul")
    print("    2. Yüzde artış hesapla")
    print("6 - Ortalama Hesaplama")
    print("    1. 2 sayının ortalaması")
    print("    2. 3 sayının ortalaması")
    print("    3. İstenilen kadar sayının ortalaması")
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
            print("Hata: Bir sayı 0'a bölünemez.")
        else:
            print(f"Sonuç: {sayi1 / sayi2}")
    except ValueError:
        print("Lütfen geçerli sayı girin.")


def yuzde_hesaplama_menusu():
    while True:
        print("\n-----------------------------")
        print("      YÜZDE HESAPLAMA")
        print("-----------------------------")
        print("1 - Bir sayının yüzdesini bul")
        print("2 - Yüzde artış hesapla")
        print("0 - Ana menüye dön")
        print("-----------------------------")

        secim = input("Seçiminiz nedir? ")

        if secim == "1":
            try:
                sayi = float(input("Sayıyı girin: "))
                yuzde = float(input("Yüzde değerini girin: "))
                sonuc = (sayi * yuzde) / 100
                print(f"Sonuç: {sonuc}")
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
        print("\n-----------------------------")
        print("    ORTALAMA HESAPLAMA")
        print("-----------------------------")
        print("1 - 2 sayının ortalaması")
        print("2 - 3 sayının ortalaması")
        print("3 - İstenilen kadar sayının ortalaması")
        print("0 - Ana menü")

    if __name__=="__main__":
        ana_program()