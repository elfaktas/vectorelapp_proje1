# vectorelapp_proje1

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

secim = input("Seçiminiz nedir?")
if secim in ["1","2","3"]:
    if secim == "1" : 
        print(secim, "sectiniz")
        print("Hesaplamalar bölümüne yönlendirileceksiniz")
    import moduller1.hesapmakinesi
    if secim == "2" : 
        print(secim, "sectiniz")
        print("Oyunlar bölümüne yönlendirileceksiniz")
else :
        print("Böyle bir seçenek yok.")