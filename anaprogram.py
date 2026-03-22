# vectorelapp_proje1
#main_menu
import moduller1.hesap_makinesi
import moduller1.çizimler2
import moduller1.oyunlar3


print ()
print ("\033[1;32;40m Renkli yazı\n")
print (" ╔═════════════════════╗ ")
print (" ║    VEKTOREL APP     ║ ")
print (" ╠═════════════════════╣ ")
print (" ║  1-Hesaplamalar     ║ ")
print (" ║  2-Oyunlar          ║ ")
print (" ║  3-Çizimler         ║ ")
print (" ║  C-Çıkış            ║ ")
print (" ║                     ║ ")
print (" ╚═════════════════════╝ ")

try:
        a = int(input("Lütfen bir işlem seçiniz:\t"))
        if a == 1:
            print(f"{a}'e bastınız; Hesaplamalar bölümüne yönlendiriliyorsunuz.\n\n")
            moduller1.hesap_makinesi.calistir()
        elif a == 2:
            print(f"{a}'ye bastınız; Şekil Çizdirme bölümüne yönlendiriliyorsunuz.\n\n")
            moduller1.sekil_cizdirme2.calistir()
        elif a == 3:
            print(f"{a}'e bastınız; Oyunlar bölümüne yönlendiriliyorsunuz.\n\n")
            moduller1.oyunlar3.calistir()
        elif a == 0:
            print('Programdan çıkılıyor...')
            break
        else:
            print("Lütfen Hesap Makinesinde belirtilen işlemlerden birini seçiniz!\n"*3)
    except ValueError:
        print("Hata: Lütfen sayı giriniz!")