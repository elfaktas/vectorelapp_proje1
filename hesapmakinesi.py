print()
print("\033[1;32;40m Renkli yazı  \n")
print(" ╔═════════════════════╗")
print(" ║    HESAP MAKİNESİ   ║")
print(" ╠═════════════════════╣")
print(" ║  1-Toplama          ║")
print(" ║  2-Çarpma           ║")
print(" ║  3-                 ║")
print(" ║  4-Çıkış            ║")
print(" ║   Seçiminiz?        ║")
print(" ╚═════════════════════╝")

 secim=input("Seçiminiz nedir?")
if seçim in ["1","2","3"]:
     print(secim,"sectiniz")
     print("Hesaplamalar bölümüne yönlendirileceksiniz")
     import moduller1.hesapmakinesi  