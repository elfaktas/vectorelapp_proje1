
print(" ╔═════════════════════╗")
print(" ║    HESAP MAKİNESİ   ║")
print(" ╠═════════════════════╣")
print(" ║  1-Toplama          ║")
print(" ║  2-Çarpma           ║")
print(" ║  3-                 ║")
print(" ║  4-Çıkış            ║")
print(" ║   Seciminiz?        ║")
print(" ╚═════════════════════╝")

secim = input("Seciminiz nedir?")
if secim in ["1","2","3"]:
    if secim =="1" : pass
    print(secim,"sectiniz")
    print("Hesaplamalar bölümüne yönlendirileceksiniz")
    import moduller1.hesapmakinesi  