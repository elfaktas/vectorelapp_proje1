def menu():
    print("\n==============================")
    print("     HESAP MAKİNESİ APP")
    print("==============================")
    print("1 -> Toplama")
    print("2 -> Çıkarma")
    print("3 -> Çarpma")
    print("4 -> Bölme")
    print("5 -> Yüzde Hesaplama")
    print("6 -> Ortalama Hesaplama")
    print("7 -> Çıkış")
    print("==============================")

while True:
    menu()
    secim = input("Seçiminizi girin: ")

    if secim == "5":
        print("Program kapatıldı.")
        break

    if secim not in ["1", "2", "3", "4"]:
        print("Geçersiz seçim yaptınız.")
        continue

    sayi1 = float(input("Birinci sayı: "))
    sayi2 = float(input("İkinci sayı: "))

    if secim == "1":
        print("Sonuç:", sayi1 + sayi2)
    elif secim == "2":
        print("Sonuç:", sayi1 - sayi2)
    elif secim == "3":
        print("Sonuç:", sayi1 * sayi2)
    elif secim == "4":
        if sayi2 == 0:
            print("Hata: 0'a bölme yapılamaz.")
        else:
            print("Sonuç:", sayi1 / sayi2)
    def gelismis_islemler():
     while True:
        print("\n--- Gelişmiş İşlemler ---")
        print("1. Yüzde Hesaplama")
        print("2. Ortalama Hesaplama")
        print("3. Ana Menüye Dön")

        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            try:
                sayi = float(input("Sayıyı girin: "))
                yuzde = float(input("Yüzde değerini girin: "))
                sonuc = (sayi * yuzde) / 100
                print(f"Sonuç: {sonuc}")
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")

        elif secim == "2":
            try:
                adet = int(input("Kaç sayı gireceksiniz: "))
                if adet <= 0:
                    print("Sıfır veya negatif sayı adedi girilemez.")
                    continue

                toplam = 0
                for i in range(1, adet + 1):
                    sayi = float(input(f"{i}. sayıyı girin: "))
                    toplam += sayi

                ortalama = toplam / adet
                print(f"Ortalama: {ortalama}")
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")

        elif secim == "3":
            break

        else:
            print("Geçersiz seçim yaptınız.")


def ana_menu():
    while True:
        print("\n=== HESAP MAKİNESİ ===")
        print("1. Basit İşlemler")
        print("2. Gelişmiş İşlemler")
        print("3. Çıkış")

        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            basit_islemler()
        elif secim == "2":
            gelismis_islemler()
        elif secim == "3":
            print("Program kapatılıyor...")
            break
        else:
            print("Geçersiz seçim yaptınız.")