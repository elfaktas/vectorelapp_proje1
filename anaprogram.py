import moduller1.hesapmakinesi
import moduller1.oyunlar
import moduller1.cizimler


def ana_menu():
    while True:
        print("\033[1;32;40m Renkli yazi\n")
        print(" ┌──────────────────────┐ ")
        print(" │    VEKTOREL APP      │ ")
        print(" ├──────────────────────┤ ")
        print(" │   1-Hesaplamalar     │ ")
        print(" │   2-Oyunlar          │ ")
        print(" │   3-Cizimler         │ ")
        print(" │   C-Cikis            │ ")
        print(" └──────────────────────┘ ")

        secim = input("Seçiminiz nedir? ").strip().upper()

        if secim == "1":
            moduller1.hesapmakinesi.ana_menuyu_goster()

        elif secim == "2":
            moduller1.oyunlar.oyun_menusu()

        elif secim == "3":
            moduller1.cizimler.cizim_menusu()

        elif secim == "C":
            print("Programdan çıkılıyor...")
            break

        else:
            print("Böyle bir seçenek yok. Tekrar deneyin.")


if __name__ == "__main__":
    ana_menu()