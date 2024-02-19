class Library:
    def __init__(self):
        self.dosya = open("books.txt", "a+")

    def close(self):
        self.dosya.close()

    def kitapları_listele(self):
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        for kitap in kitaplar:
            kitap_bilgisi = kitap.strip().split(',')
            print(f"Kitap Adı: {kitap_bilgisi[0]}, Yazar: {kitap_bilgisi[1]}")

    def kitap_ekle(self):
        ad = input("Kitap adını girin: ")
        yazar = input("Yazar adını girin: ")
        yayın_yılı = input("İlk yayın yılını girin: ")
        sayfa_sayısı = input("Sayfa sayısını girin: ")
        kitap_bilgisi = f"{ad},{yazar},{yayın_yılı},{sayfa_sayısı}\n"
        self.dosya.write(kitap_bilgisi)
        print("Kitap başarıyla eklendi.")

    def kitap_sil(self):
        ad = input("Silmek istediğiniz kitabın adını girin: ")
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        güncellenmiş_kitaplar = []
        silindi = False
        for kitap in kitaplar:
            if ad not in kitap:
                güncellenmiş_kitaplar.append(kitap)
            else:
                silindi = True
        if silindi:
            self.dosya.seek(0)
            self.dosya.truncate()
            self.dosya.writelines(güncellenmiş_kitaplar)
            print(f"'{ad}' kitabı başarıyla silindi.")
        else:
            print(f"'{ad}' kitabı bulunamadı.")


kütüphane = Library()

while True:
    print(" MENÜ ")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Sil")

    seçim = input("Seçiminizi girin (1/2/3): ")

    if seçim == '1':
        kütüphane.kitapları_listele()
    elif seçim == '2':
        kütüphane.kitap_ekle()
    elif seçim == '3':
        kütüphane.kitap_sil()
    else:
        print("Geçersiz seçim. Lütfen tekrar seçin.")