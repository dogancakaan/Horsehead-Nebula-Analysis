from astropy.io import fits
from astropy.visualization import simple_norm, LogStretch, SqrtStretch
import numpy as np
import matplotlib.pyplot as plt
from astropy.utils.data import download_file

image_url = 'http://data.astropy.org/tutorials/FITS-images/HorseHead.fits'
image_file = download_file(image_url, cache=True)

hdul = fits.open(image_file)
data = hdul[0].data
hdul.close()

print("Goruntu Matris Boyutu:", data.shape)
print("Minimum Piksel Degeri:", np.min(data))
print("Maksimum Piksel Degeri:", np.max(data))
print("Ortalama Piksel Degeri:", np.mean(data))
print("Medyan Piksel Degeri:", np.median(data))
print("Standart Sapma:", np.std(data))
print("Toplam Piksel Sayisi:", data.size)
print("Piksel Yogunluk Dagilimi (Histogram) Hazirlaniyor...")

#2x2 matris subplot
fig, axes = plt.subplots(2, 2, figsize=(12,12))

#1, sol ust, orjinal goruntu
im1 =axes[0, 0].imshow(data, cmap='gray', origin='lower')
axes[0, 0].set_title('Orjinal Atbasi Nebulası')
fig.colorbar(im1, ax=axes[0,0], label='Piksel Yogunlugu')

#2, sag ust, Sqrt Esnetilmis Goruntu
norm_sqrt = simple_norm(data, 'sqrt')
im2 = axes[0,1].imshow(data, cmap='gray', origin='lower', norm=norm_sqrt)
axes[0,1].set_title('Sqrt Esnetilmis Atbasi Nebulası')
fig.colorbar(im2, ax=axes[0,1], label='Esnetilmis Yogunluk')

#3, sol alt, Log Esnetilmis Goruntu
norm_log = simple_norm(data, 'log')
im3 = axes[1,0].imshow(data, cmap='gray', origin='lower', norm=norm_log)
axes[1,0].set_title('Log Esnetilmis Atbasi Nebulası')
fig.colorbar(im3, ax=axes[1,0], label='Logaritmik Yogunluk')

#4, sag alt, Histogram
axes[1,1].hist(data.flatten(), bins=100, color='purple', alpha=0.7)
axes[1,1].set_title('Piksel Yogunluk Dagilimi')
axes[1,1].set_xlabel('Piksel Degeri')
axes[1,1].set_ylabel('Piksel Sayisi')

plt.tight_layout()
plt.show()