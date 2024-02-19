import tkinter as tk
from tkinter import messagebox


class library:
    def __init__(self):
        self.lib = open("books.txt", "a+")

    def close(self):
        self.lib.close()

    def kitap_listele(self):
        self.lib.seek(0)
        kitaplar = self.lib.readlines()
        kitap_listesi = ""

        for kitap in kitaplar:
            kitap_bilgisi = kitap.split(',')
            kitap_listesi += f"Kitap Adı: {kitap_bilgisi[0]}, Yazar: {kitap_bilgisi[1]}, Yayın Yılı: {kitap_bilgisi[2]}, Sayfa Sayısı: {kitap_bilgisi[3]}\n\n"
        return kitap_listesi



    def kitap_ekle(self, ad, yazar, yayin_yili, sayfa_sayisi):
        kitap_bilgisi = f"{ad},{yazar},{yayin_yili},{sayfa_sayisi}\n"
        self.lib.write(kitap_bilgisi)

    def kitap_sil(self, ad, yazar):
        self.lib.seek(0)
        kitaplar = self.lib.readlines()
        güncellenmis_kitaplar = []
        silindi = False

        for kitap in kitaplar:
            kitap_bilgisi = kitap.strip().split(',')
            if ad == kitap_bilgisi[0] and yazar == kitap_bilgisi[1]:
                silindi = True
            else:
                güncellenmis_kitaplar.append(kitap)

        if silindi:
            self.lib.close()
            self.lib = open("books.txt", "w")
            self.lib.writelines(güncellenmis_kitaplar)
            self.lib.close()
            self.lib = open("books.txt", "a+")
            return True
        else:
            return False


class Kütüp_uyg:
    def __init__(self, root):
        self.root = root
        self.root.title("Kütüphane ")

        self.kütüphanem = library()

        self.menu_frame = tk.Frame(root, bg="orange")
        self.menu_frame.pack(pady=20)

        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(pady=20)

        self.menu_label = tk.Label(self.menu_frame, text="ANA MENÜ", bg="orange")
        self.menu_label.grid(row=0, column=1, pady=10)

        self.list_button = tk.Button(self.menu_frame, text="Kitapları Listele", command=self.kitap_listele,bg="light blue")
        self.list_button.grid(row=1, column=0)

        self.add_button = tk.Button(self.menu_frame, text="Kitap Ekle", command=self.kitap_ekle, bg="light blue")
        self.add_button.grid(row=1, column=1)

        self.delete_button = tk.Button(self.menu_frame, text="Kitap Sil", command=self.kitap_sil, bg="light blue")
        self.delete_button.grid(row=1, column=2)

        labels = ["Kitap Adı:", "Yazar:", "Yayın Yılı:", "Sayfa Sayısı:"]
        entries = [tk.Entry(self.entry_frame) for _ in range(4)]

        tk.Label(self.entry_frame, text=labels[0]).grid(row=0, column=0)
        entries[0].grid(row=0, column=1)

        tk.Label(self.entry_frame, text=labels[1]).grid(row=1, column=0)
        entries[1].grid(row=1, column=1)

        tk.Label(self.entry_frame, text=labels[2]).grid(row=2, column=0)
        entries[2].grid(row=2, column=1)

        tk.Label(self.entry_frame, text=labels[3]).grid(row=3, column=0)
        entries[3].grid(row=3, column=1)

        self.ad_entry, self.yazar_entry, self.yayin_yili_entry, self.sayfa_sayisi_entry = entries

    def kitap_listele(self):
        book_list = self.kütüphanem.kitap_listele()
        messagebox.showinfo("Kitap Listesi", book_list)

    def kitap_ekle(self):
        ad = self.ad_entry.get()
        yazar = self.yazar_entry.get()
        yayin_yili = self.yayin_yili_entry.get()
        sayfa_sayisi = self.sayfa_sayisi_entry.get()
        if ad and yazar and yayin_yili and sayfa_sayisi:
            self.kütüphanem.kitap_ekle(ad, yazar, yayin_yili, sayfa_sayisi)
            messagebox.showinfo("Başarılı", "Kitap başarıyla eklendi.")
        else:
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")

    def kitap_sil(self):
        ad = self.ad_entry.get()
        yazar = self.yazar_entry.get()
        if ad and yazar:
            success = self.kütüphanem.kitap_sil(ad, yazar)
            if success:
                messagebox.showinfo("Başarılı", f"'{ad}' kitabı başarıyla silindi.")
            else:
                messagebox.showinfo("Hata", f"'{ad}' kitabı bulunamadı.")
        else:
            messagebox.showerror("Hata", "Lütfen kitap adı ve yazar adını girin.")

    def close_app(self):
        self.kütüphanem.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = Kütüp_uyg(root)
    root.geometry("250x250")
    root.mainloop()
