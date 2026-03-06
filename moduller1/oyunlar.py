print()
print("\033[1;32;40m Renkli yazı  \n")
print(" ╔═════════════════════╗")
print(" ║    OYUNLAR MENÜSÜ   ║")
print(" ╠═════════════════════╣")
print(" ║  1-Yılan            ║")
print(" ║  2-Tetris           ║")
print(" ║  3-Adam asmaca      ║")
print(" ║  4-                 ║")
print(" ║   Seçiminiz?        ║")
print(" ╚═════════════════════╝")

secim = input("Seciminiz nedir?")
if secim in ["1","2","3"]:
    if secim =="1" : pass
    print(secim,"sectiniz")
    print("Hesaplamalar bölümüne yönlendirileceksiniz")
    import moduller1.oyunlar  