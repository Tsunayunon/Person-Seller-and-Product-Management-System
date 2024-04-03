

---

# Kişi, Satıcı ve Ürün Yönetim Sistemi

Bu Python programı, kişileri, satıcıları ve ürünleri yönetmek için bir arayüz sağlar. Kullanıcılar, yeni kişileri, satıcıları ve ürünleri ekleyebilir, mevcut kişileri, satıcıları ve ürünleri listeleyebilir.

## Kullanım

1. `main.py` dosyasını çalıştırın.
2. Ana menüden bir seçenek seçin:
   - Yeni kişi eklemek için "Kişi Ekle"
   - Yeni satıcı eklemek için "Satıcı Ekle"
   - Yeni ürün eklemek için "Ürün Ekle"
   - Mevcut kişileri listelemek için "Kişileri Listele"
   - Mevcut satıcıları listelemek için "Satıcıları Listele"
   - Mevcut ürünleri listelemek için "Ürünleri Listele"
   - Programdan çıkmak için "Çıkış"
3. İlgili seçeneği seçtikten sonra, ekrandaki talimatları izleyin.

## Sınıflar ve Metodlar

- `Kisi`: İsim, soyisim ve TC kimlik numarası bilgilerini içerir.
- `Satici`: `Kisi` sınıfından miras alır. Ayrıca maaş bilgisini de içerir.
- `Urun`: Ürün ID, marka ve model bilgilerini içerir.
- `Menu`: Kullanıcı arayüzünü sağlar ve kullanıcının seçimlerini işler.

## Dosyalar

- `kisiler.txt`: Kişi bilgilerini içeren dosya.
- `saticilar.txt`: Satıcı bilgilerini içeren dosya.
- `urunler.txt`: Ürün bilgilerini içeren dosya.

## Geliştirme

Bu program, temel bir kişi, satıcı ve ürün yönetim sistemi örneğidir. Geliştirmek için şunları düşünebilirsiniz:

- Mevcut kişileri, satıcıları ve ürünleri güncelleme veya silme seçenekleri ekleyin.
- Kullanıcı arayüzünü iyileştirin ve daha etkileşimli hale getirin.
- Veri tabanı desteği ekleyerek verileri daha kalıcı bir şekilde saklayın.

## Lisans

Bu program MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.

---
