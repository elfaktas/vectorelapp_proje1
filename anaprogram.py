import moduller1.hesapmakinesi
import moduller1.oyunlar
import moduller1.çizimler

def ana_menu():
    while True:
        print("\033[1;32;40m Renkli yazi\n")
        print(" ┌──────────────────────┐ ")
        print(" │    VEKTOREL APP      │ ")
        print(" ├──────────────────────┤ ")
        print(" │   1-Hesaplamalar     │ ")
        print(" │   2-Oyunlar          │ ")
        print(" │   3-Çizimler         │ ")
        print(" │   C-Çıkış            │ ")
        print(" └──────────────────────┘ ")

        secim = input("Seçiminiz nedir? ").strip().upper()

        if secim == "1":
            print("Hesaplamalar bölümüne yönlendiriliyorsunuz...")
            break
        elif secim == "2":
            print("Oyunlar bölümüne yönlendiriliyorsunuz...")
            break
        elif secim == "3":
            print("Çizimler bölümüne yönlendiriliyorsunuz...")
            break
        elif secim == "C":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Böyle bir seçenek yok. Tekrar deneyin.")

if _name_ == "_main_":
    ana_menu()