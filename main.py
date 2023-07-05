modern_sozluk = {"LOL":"Sesli gülmek", "CRINGE":"Garip ya da utandırıcı bir şeye verilen cevap"}

cevap = input("Öğrenmek istediğin kelimeyi yaz (hepsini büyük harflerle yazın!)")


if cevap in modern_sozluk.keys():
    print(modern_sozluk[cevap])
    
else:
    print("Doğru yazıp yazmadığınızdan emin olun.")
