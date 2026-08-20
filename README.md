# Astrofizik Veri Analizi: Atbaşı Bulutsusu (Horsehead Nebula) FITS Görüntü İşleme

Bu proje, Astropy ve Matplotlib kütüphanelerini kullanarak uzaydan gelen ham FITS (Flexible Image Transport System) formatındaki astronomik verilerin nasıl okunacağını, temel istatistiksel analizlerinin nasıl yapılacağını ve görselleştirme için hangi matematiksel esnetme (stretching) tekniklerinin kullanıldığını gösteren başlangıç düzeyinde bir veri bilimi ve astrofizik çalışmasıdır.

## 🚀 Projede Neler Yapıldı?
1. **Veri Çekme:** AstroPy veri tabanından Atbaşı Bulutsusu'na ait ham FITS dosyası otomatik olarak indirildi.
2. **Matris Analizi & İstatistikler:** 
   - Görüntü matris boyutu (`shape`) çıkarıldı.
   - Piksel değerlerinin minimum, maksimum, ortalama, medyan ve standart sapma değerleri hesaplandı.
3. **Piksel Dağılımı (Histogram):** Görüntüdeki ışık yoğunluklarının dağılımını incelemek için 100 binli (bins=100) histogram grafiği çizildi.
4. **Görüntü Esnetme (Image Stretching):** 
   - İnsan gözünün ve ekranların sönük detayları seçebilmesi için **Karekök (`sqrt`)** ve **Logaritmik (`log`)** esnetme algoritmaları uygulandı.
5. **Çoklu Görselleştirme (Subplots):** Tüm analizler ve esnetilmiş halleri Matplotlib kullanılarak tek bir 2x2'lik şık tuval üzerinde birleştirildi.

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler
* **Python** 
* **NumPy** (Matris işlemleri ve matematiksel hesaplamalar)
* **Astropy** (FITS dosya okuma ve esnetme araçları)
* **Matplotlib** (Görselleştirme ve histogram çizimi)

## 📊 Örnek Çıktı Özeti
* **Matris Boyutu:** 893 x 891 piksel
* **Piksel Değer Aralığı:** 3759 (Min) - 22918 (Maks)

---
*Bu proje, astronomi ve uzay bilimleri alanındaki veri analizi yetkinliklerini geliştirmek amacıyla oluşturulmuştur.*