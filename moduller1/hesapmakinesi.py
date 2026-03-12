def menu():
    print("\n==============================")
    print("     HESAP MAKİNESİ APP")
    print("==============================")
    print("1 -> Toplama")
    print("2 -> Çıkarma")
    print("3 -> Çarpma")
    print("4 -> Bölme")
    print("5 -> Çıkış")
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