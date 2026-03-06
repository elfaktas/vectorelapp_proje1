# vectorelapp_proje1
app.py
print ()
print ("\033[1;32;40m Renkli yazı\n")
print (" ╔═════════════════════╗ ")
print (" ║    VEKTOREL APP     ║ ")
print (" ╠═════════════════════╣ ")
print (" ║  1-Hesaplamalar     ║ ")
print (" ║  2-Oyunlar          ║ ")
print (" ║  3-Çizimler         ║ ")
print (" ║  4-                 ║ ")
print (" ║  5-                 ║ ")
print (" ║  6-                 ║ ")
print (" ║  7-                 ║ ")
print (" ║  8-                 ║ ")
print (" ║  9-                 ║ ")
print (" ║  C-Çıkış            ║ ")
print (" ║                     ║ ")
print (" ╚═════════════════════╝ ")

secim = input("Seçiminiz nedir?")
if secim in ["1","2","3"]:
    if secim == "1" : 
        print(secim, "sectiniz")
        print("Hesaplamalar bölümüne yönlendirileceksiniz")
    import moduller.hesapmakinesi
    if secim == "2" : 
        print(secim, "sectiniz")
        print("Oyunlar bölümüne yönlendirileceksiniz")
else :
        print("Böyle bir seçenek yok.")