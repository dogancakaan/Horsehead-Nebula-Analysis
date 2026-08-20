from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from astropy.utils.data import download_file

image_url = 'http://data.astropy.org/tutorials/FITS-images/HorseHead.fits'
image_file = download_file(image_url, cache=True)

hdul = fits.open(image_file)
data = hdul[0].data
hdul.close()

print("Goruntu Matris Boyutu: ", data.shape)
print("Minimum Piksel Degeri:", np.min(data))
print("Maksimum Piksel Degeri:", np.max(data))
print("Ortalama Piksel Degeri:", np.mean(data))
print("Medyan Piksel Degeri:", np.median(data))
print("Standart Sapma:", np.std(data))
print("Toplam Piksel Sayisi:", data.size)
print("Piksel Yogunluk Dagilimi (Histogram) Hazirlaniyor...")

plt.figure(figsize=(6,6))
plt.imshow(data, cmap='gray', origin='lower')
plt.colorbar(label='Piksel Yogunlugu')
plt.title('Horsehead Nebula')

plt.figure(figsize=(6,4))
plt.hist(data.flatten(), bins=100, color='purple', alpha=0.7)
plt.title('Piksel Yogunluk Dagilimi (Histogram)')
plt.xlabel('Piksel Yogunlugu')
plt.ylabel('Piksel Sayisi')

plt.show()