from astropy.io import fits
from astropy.visualization import simple_norm, LogStretch, SqrtStretch
import numpy as np
import matplotlib.pyplot as plt

orion_red = "m42_40min_red.fits"
orion_ir = "m42_40min_ir.fits"

hdul_red = fits.open(orion_red)
data_red = hdul_red[0].data
hdul_red.close()

hdul_ir = fits.open(orion_ir)
data_ir = hdul_ir[0].data
hdul_ir.close()

#Orion bulutsusunun merkezine odaklanacak şekilde piksel aralığını kesiyoruz
y_min, y_max = 950, 1500
x_min, x_max = 1000, 1550

crop_red = data_red[y_min:y_max, x_min:x_max]
crop_ir = data_ir[y_min:y_max, x_min:x_max]


print("Goruntu Matris Boyutu (Red):", data_red.shape)
print("Goruntu Matris Boyutu (IR):", data_ir.shape)
print("Minimum Piksel Degeri (Red):", np.min(data_red))
print("Minimum Piksel Degeri (IR):", np.min(data_ir))
print("Maksimum Piksel Degeri (Red):", np.max(data_red))
print("Maksimum Piksel Degeri (IR):", np.max(data_ir))
print("Ortalama Piksel Degeri (Red):", np.mean(data_red))
print("Ortalama Piksel Degeri (IR):", np.mean(data_ir))
print("Medyan Piksel Degeri (Red):", np.median(data_red))
print("Medyan Piksel Degeri (IR):", np.median(data_ir))
print("Standart Sapma (Red):", np.std(data_red))
print("Standart Sapma (IR):", np.std(data_ir))
print("Toplam Piksel Sayisi (Red):", data_red.size)
print("Toplam Piksel Sayisi (IR):", data_ir.size)
print("Piksel Yogunluk Dagilimi (Histogram) Hazirlaniyor...")

#3x4 matris subplot
fig, axes = plt.subplots(3,4, figsize=(16,12))

#1, sol ust, orjinal goruntu (red)
img1 = axes[0,0].imshow(data_red, cmap='gray', origin='lower')
axes[0,0].set_title('Orjinal Orion Nebulasi (Red)')
fig.colorbar(img1, ax=axes[0,0], label= "Piksel Yogunlugu (Red)")

#2, orta ust, Sqrt Esnetilmis Goruntu (red)
norm_sqrt_red = simple_norm(data_red, 'sqrt')
img2 = axes [0,1].imshow(data_red, cmap= 'gray', origin='lower', norm=norm_sqrt_red)
axes[0,1].set_title('Sqrt Esnetilmis Orion Nebulasi (Red)')
fig.colorbar(img2, ax=axes[0,1], label= "Esnetilmis Yogunluk (Red)")

#3, sag ust, log Esnetilmis Goruntu (red)
norm_log_red = simple_norm(data_red, 'log')
img3 = axes[0,2].imshow(data_red, cmap='gray', origin='lower', norm=norm_log_red)
axes[0,2].set_title('Log Esnetilmis Orion Nebulasi (Red)')
fig.colorbar(img3, ax=axes[0,2], label= "Logaritmik Yogunluk (Red)")

#cropped, red
img7 = axes[0,3].imshow(crop_red, cmap='gray', origin='lower')
axes[0,3].set_title('Odaklanmis Orion Nebula (Red)')
fig.colorbar(img7, ax=axes[0,3], label='Piksel Yogunlugu (Red)')

#4, sol orta, orjinal goruntu (IR)
img4 = axes[1,0].imshow(data_ir, cmap='inferno', origin='lower')
axes[1,0].set_title('Orjinal Orion Nebulasi (IR)')
fig.colorbar(img4, ax=axes[1,0], label= "Piksel Yogunlugu (IR)")

#5, orta orta, Sqrt Esnetilmis Goruntu (IR)
norm_sqrt_ir = simple_norm(data_ir, 'sqrt')
img5 = axes[1,1].imshow(data_ir, cmap='inferno', origin='lower', norm=norm_sqrt_ir)
axes[1,1].set_title('Sqrt Esnetilmis Orion Nebulasi (IR)')
fig.colorbar(img5, ax=axes[1,1], label= "Esnetilmis Yogunluk (IR)")

#6, sag orta, log Esnetilmis Goruntu (IR)
norm_log_ir = simple_norm(data_ir, 'log')
img6 = axes[1,2].imshow(data_ir, cmap='inferno', origin='lower', norm=norm_log_ir)
axes[1,2].set_title('Log Esnetilmis Orion Nebulasi (IR)')
fig.colorbar(img6, ax=axes[1,2], label= "Logaritmik Yogunluk (IR)")

#cropped, IR
img8 = axes[1,3].imshow(crop_ir, cmap='inferno', origin='lower')
axes[1,3].set_title('Odaklanmis Orion Nebula (IR)')
fig.colorbar(img7, ax=axes[1,3], label='Piksel Yogunlugu (IR)')

#7, sol alt, Histogram (Red)
axes[2,0].hist(data_red.flatten(), bins=100, color='blue', alpha=0.7)
axes[2,0].set_title('Piksel Yogunluk Dagilimi (Red)')
axes[2,0].set_xlabel('Piksel Degeri (Red)')
axes[2,0].set_ylabel('Piksel Sayisi (Red)')

#8, orta alt, Histogram (IR)
axes[2,1].hist(data_ir.flatten(), bins=100, color='purple', alpha=0.7)
axes[2,1].set_title('Piksel Yogunluk Dagilimi (IR)')
axes[2,1].set_xlabel('Piksel Degeri (IR)')
axes[2,1].set_ylabel('Piksel Sayisi (IR)')

#9, sag alt, Histogram (Red ve IR)
axes[2,2].hist(data_red.flatten(), bins=100, color='blue', alpha=0.7)
axes[2,2].hist(data_ir.flatten(), bins=100, color='purple', alpha=0.7)
axes[2,2].set_title('Piksel Yogunluk Dagilimi Karsilastirma')

#cropped, histogram (Red ve IR)
axes[2,3].hist([crop_red.flatten(), crop_ir.flatten()], bins=100, color=['blue', 'purple'], alpha=0.7)
axes[2,3].set_title('Odaklanmis Piksel Yogunluk Dagilimi Karsilastirma')

plt.tight_layout()
plt.show()