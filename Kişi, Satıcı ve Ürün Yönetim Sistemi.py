import os

class Kisi:
    def __init__(self, isim, soyisim, tc_kimlik):
        self.isim = isim
        self.soyisim = soyisim
        self.tc_kimlik = tc_kimlik

    @staticmethod
    def bilgileri_listele():
        try:
            with open("kisiler.txt", "r") as dosya:
                kisiler = dosya.readlines()
                if kisiler:
                    for kisi in kisiler:
                        print(kisi.strip())
                else:
                    print("Henüz kişi eklenmedi.")
        except FileNotFoundError:
            print("Henüz kişi eklenmedi.")

    def bilgileri_kaydet(self):
        with open("kisiler.txt", "a") as dosya:
            dosya.write(f"{self.isim},{self.soyisim},{self.tc_kimlik}\n")

class Satici(Kisi):
    def __init__(self, isim, soyisim, tc_kimlik, maas):
        super().__init__(isim, soyisim, tc_kimlik)
        self.maas = maas

    @staticmethod
    def bilgileri_listele():
        try:
            with open("saticilar.txt", "r") as dosya:
                saticilar = dosya.readlines()
                if saticilar:
                    for satici in saticilar:
                        print(satici.strip())
                else:
                    print("Henüz satıcı eklenmedi.")
        except FileNotFoundError:
            print("Henüz satıcı eklenmedi.")

    def bilgileri_kaydet(self):
        with open("saticilar.txt", "a") as dosya:
            dosya.write(f"{self.isim},{self.soyisim},{self.tc_kimlik},{self.maas}\n")

class Urun:
    def __init__(self, urun_id, marka, model):
        self.urun_id = urun_id
        self.marka = marka
        self.model = model

    @staticmethod
    def bilgileri_listele():
        try:
            with open("urunler.txt", "r") as dosya:
                urunler = dosya.readlines()
                if urunler:
                    for urun in urunler:
                        print(urun.strip())
                else:
                    print("Henüz ürün eklenmedi.")
        except FileNotFoundError:
            print("Henüz ürün eklenmedi.")

    def bilgileri_kaydet(self):
        with open("urunler.txt", "a") as dosya:
            dosya.write(f"{self.urun_id},{self.marka},{self.model}\n")

class Menu:
    @staticmethod
    def kisi_ekle():
        isim = input("İsim: ")
        soyisim = input("Soyisim: ")
        tc_kimlik = input("TC Kimlik No: ")
        kisi = Kisi(isim, soyisim, tc_kimlik)
        kisi.bilgileri_kaydet()
        print("Kişi başarıyla eklendi.")

    @staticmethod
    def satici_ekle():
        isim = input("İsim: ")
        soyisim = input("Soyisim: ")
        tc_kimlik = input("TC Kimlik No: ")
        maas = input("Maaş: ")
        satici = Satici(isim, soyisim, tc_kimlik, maas)
        satici.bilgileri_kaydet()
        print("Satıcı başarıyla eklendi.")

    @staticmethod
    def urun_ekle():
        urun_id = input("Ürün ID: ")
        marka = input("Marka: ")
        model = input("Model: ")
        urun = Urun(urun_id, marka, model)
        urun.bilgileri_kaydet()
        print("Ürün başarıyla eklendi.")

    @staticmethod
    def menu_goster():
        while True:
            secim = input("\n1. Kişi Ekle\n2. Satıcı Ekle\n3. Ürün Ekle\n4. Kişileri Listele\n5. Satıcıları Listele\n6. Ürünleri Listele\n7. Çıkış\nSeçiminiz: ")
            if secim == "1":
                Menu.kisi_ekle()
            elif secim == "2":
                Menu.satici_ekle()
            elif secim == "3":
                Menu.urun_ekle()
            elif secim == "4":
                print("\nKayıtlı Kişiler:")
                Kisi.bilgileri_listele()
            elif secim == "5":
                print("\nKayıtlı Satıcılar:")
                Satici.bilgileri_listele()
            elif secim == "6":
                print("\nKayıtlı Ürünler:")
                Urun.bilgileri_listele()
            elif secim == "7":
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz seçim.")

if __name__ == "__main__":
    Menu.menu_goster()
