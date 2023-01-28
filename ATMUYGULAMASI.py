print("""**************************** 
HELAL FAİZSİZ BANKAYA HOŞGELDİNİZ.....
1- PARA ÇEKME
2- PARA YATIRMA
3- PARA GÖNDERME
****************************""")

bakiye=1000
hak=3

while True:
    try:
        islem=int(input("LÜTFEN YAPMAK İSTEDİĞİNİZ İŞLEMİ GİRİNİZ: \n"))
        if islem==1:
            print("--------- PARA ÇEKME İŞLEMİ SEÇİLDİ ---------")
            print(f"ŞUAN Kİ GÜNCEL BAKİYENİZ {bakiye} TL")
            paraCekme=int(input("HESABINIZDAN ÇEKMEK İSTEDİĞİNİZ TUTARI GİRİN: "))
            if paraCekme<=bakiye:
                bakiye=bakiye-paraCekme
                print(f"İŞLEM BAŞARILI BİR ŞEKİLDE GERÇEKLEŞTİ. GÜNCEL BAKİYENİZ: {bakiye} TL")
                if bakiye==0:
                    print(f"ÜZGÜNÜZ ÇEKECEK PARANIZ  KALMADI ARTIK...GÜNCEL BAKİYENİZ: {bakiye} TL :( ")
            else:
                print(f"ÜZGÜNÜZ HESABINIZDA O KADAR PARA YOK. GÜNCEL BAKİYENİZ {bakiye} TL DİR.")

        if islem==2:
            print("--------- PARA YATIRMA İŞLEMİ SEÇİLDİ ---------")
            print(f"ŞUAN Kİ GÜNCEL BAKİYENİZ {bakiye} TL")
            paraYatirma = int(input("HESABINIZA YATIRMAK İSTEDİĞİNİZ TUTARI GİRİN: "))
            bakiye = bakiye + paraYatirma
            print(f"İŞLEM BAŞARILI BİR ŞEKİLDE GERÇEKLEŞTİ. GÜNCEL BAKİYENİZ: {bakiye} TL")

        if islem==3:
            print("--------- PARA GÖNDERME İŞLEMİ SEÇİLDİ HEMİ DE İŞLEM ÜCRETİ YOK :) ---------")
            print(f"ŞUAN Kİ GÜNCEL BAKİYENİZ {bakiye} TL")
            paraGonderilenHesap=int(input("KİMİN HESABINA GÖNDERMEK İSTİYORSAN ONUN TC SİNİ GİR: "))
            gonderilenBakiye=int(input("NE KADAR PARA GÖNDERMEK İSTİYORSUN: "))
            if gonderilenBakiye<=bakiye:
                bakiye=bakiye-gonderilenBakiye
                print(f"İŞLEM BAŞARILI BİR ŞEKİLDE GERÇEKLEŞTİ. GÜNCEL BAKİYENİZ: {bakiye} TL")
                if bakiye==0:
                    print(f"GÜNCEL BAKİYENİZ: {bakiye} TL :( ")
            else:
                print(f"ÜZGÜNÜZ HESABINIZDA O KADAR PARA YOK. GÜNCEL BAKİYENİZ {bakiye} TL DİR.")


    except:
        hak -= 1
        print(f"LüTFEN LİSTEYE GÖRE İŞLEM YAPINIZ.\n İşlem için kalan hakkınız {hak} !!!")
        if hak==0:
            print(f"işlem yapmak için destek alınız... üzgünüz işlem yapamadınız..")
            break
