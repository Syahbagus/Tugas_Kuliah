import pandas as pd
import matplotlib.pyplot as plt

# Baca data excel
file_name = "Kickstart Project (Tugas)(1).xlsx"
excel = pd.ExcelFile(file_name)

# Baca sheet 2 dan hitung jumlah data
sheet1 = excel.parse("New1")
banyakData = len(sheet1)
print('Jumlah Data: ', banyakData, "\n")

kolom1 = "usd_pledged_real"
kolom2 = "usd_goal_real"
kolom3 = "pledged"
kolom4 = "goal"

# Menghitung mean, median, dan modus untuk masing-masing kolom
mean1 = sheet1[kolom1].mean()
median1 = sheet1[kolom1].median()
# Mengambil data pertama jika ada yang kembar
modus1 = sheet1[kolom1].mode().iloc[0]
dev1 = sheet1[kolom1].std()
varian1 = sheet1[kolom1].var()

mean2 = sheet1[kolom2].mean()
median2 = sheet1[kolom2].median()
modus2 = sheet1[kolom2].mode().iloc[0]
dev2 = sheet1[kolom2].std()
varian2 = sheet1[kolom2].var()

mean3 = sheet1[kolom3].mean()
median3 = sheet1[kolom3].median()
modus3 = sheet1[kolom3].mode().iloc[0]
dev3 = sheet1[kolom3].std()
varian3 = sheet1[kolom3].var()

mean4 = sheet1[kolom4].mean()
median4 = sheet1[kolom4].median()
modus4 = sheet1[kolom4].mode().iloc[0]
dev4 = sheet1[kolom4].std()
varian4 = sheet1[kolom4].var()

# Tampilkan data
print("Data kolom ", kolom1)
print("Mean             : ", mean1)
print("Median           : ", median1)
print("Modus            : ", modus1)
print("Standar Deviasi  : ", dev1)
print("Varian           : ", varian1)
print("")
print("Data kolom ", kolom2)
print("Mean             : ", mean2)
print("Median           : ", median2)
print("Modus            : ", modus2)
print("Standar Deviasi  : ", dev2)
print("Varian           : ", varian2)
print("")
print("Data kolom ", kolom3)
print("Mean             : ", mean3)
print("Median           : ", median3)
print("Modus            : ", modus3)
print("Standar Deviasi  : ", dev3)
print("Varian           : ", varian3)
print("")
print("Data kolom ", kolom4)
print("Mean             : ", mean4)
print("Median           : ", median4)
print("Modus            : ", modus4)
print("Standar Deviasi  : ", dev4)
print("Varian           : ", varian4)

# ---- Tabel Normalisasi Data ----
print("")
print("")
min_value1 = sheet1[kolom1].min()
max_value1 = sheet1[kolom1].max()
min_value2 = sheet1[kolom2].min()
max_value2 = sheet1[kolom2].max()
min_value3 = sheet1[kolom3].min()
max_value3 = sheet1[kolom3].max()
min_value4 = sheet1[kolom4].min()
max_value4 = sheet1[kolom4].max()

normalisasi1 = (sheet1[kolom1] - min_value1)/(max_value1 - min_value1)
normalisasi2 = (sheet1[kolom2] - min_value2)/(max_value2 - min_value2)
normalisasi3 = (sheet1[kolom3] - min_value3)/(max_value3 - min_value3)
normalisasi4 = (sheet1[kolom4] - min_value4)/(max_value4 - min_value4)

# Tabel frekuensi
print("=====================")
print("== Tabel Frekuensi ==")
print("=====================")
batas_kelompok = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
frekuensi1 = pd.cut(normalisasi1, bins=batas_kelompok,
                    include_lowest=True).value_counts()
print("Frekuensi untuk usd_pledged_real: ")
print(frekuensi1, "\n")

frekuensi2 = pd.cut(normalisasi2, bins=batas_kelompok,
                    include_lowest=True).value_counts()
print("Frekuensi untuk usd_goal_real: ")
print(frekuensi2, "\n")

frekuensi3 = pd.cut(normalisasi3, bins=batas_kelompok,
                    include_lowest=True).value_counts()
print("Frekuensi untuk pledged: ")
print(frekuensi3, "\n")
frekuensi4 = pd.cut(normalisasi4, bins=batas_kelompok,
                    include_lowest=True).value_counts()
print("Frekuensi untuk goal: ")
print(frekuensi4, "\n")

# Tabel Frekuensi Kumulatif Kurang Dari
# KK = Kumulatif kurang dari
KK1 = frekuensi1.cumsum()
KK2 = frekuensi2.cumsum()
KK3 = frekuensi3.cumsum()
KK4 = frekuensi4.cumsum()

print("=====================================")
print("== Frekuensi Kumulatif Kurang dari ==")
print("=====================================")
print("usd_pledged_real: ")
print(KK1, "\n")

print("usd_goal_real: ")
print(KK2, "\n")

print("pledged: ")
print(KK3, "\n")

print("goal: ")
print(KK4, "\n")

# Tabel Frekuensi Kumulatif Lebih Dari
KL1 = frekuensi1.iloc[::-1].cumsum().iloc[::-1]
KL2 = frekuensi2.iloc[::-1].cumsum().iloc[::-1]
KL3 = frekuensi3.iloc[::-1].cumsum().iloc[::-1]
KL4 = frekuensi4.iloc[::-1].cumsum().iloc[::-1]
print("====================================")
print("== Frekuensi Kumulatif Lebih dari ==")
print("====================================")
print("usd_pledged_real: ")
print(KL1, "\n")

print("usd_goal_real: ")
print(KL2, "\n")

print("pledged: ")
print(KL3, "\n")

print("goal: ")
print(KL4, "\n")

# Tabel Frekuensi relatif
frekuensi_relatif1 = (frekuensi1 / banyakData) * 100
frekuensi_relatif2 = (frekuensi2 / banyakData) * 100
frekuensi_relatif3 = (frekuensi3 / banyakData) * 100
frekuensi_relatif4 = (frekuensi4 / banyakData) * 100
print("=======================")
print("== Frekuensi Relatif ==")
print("=======================")
print("usd_pledged_real:")
print(frekuensi_relatif1, "\n")

print("usd_goal_real:")
print(frekuensi_relatif2, "\n")

print("pledged:")
print(frekuensi_relatif3, "\n")

print("goal:")
print(frekuensi_relatif4, "\n")

# Tabel Frekuensi relatif Kumulatif Kurang dari
RKK1 = (KK1 / banyakData) * 100
RKK2 = (KK2 / banyakData) * 100
RKK3 = (KK3 / banyakData) * 100
RKK4 = (KK4 / banyakData) * 100
print("=============================================")
print("== Frekuensi Relatif Kumulatif Kurang dari ==")
print("=============================================")
print("usd_pledged_real: ")
print(RKK1, "\n")

print("usd_goal_real: ")
print(RKK2, "\n")

print("pledged: ")
print(RKK3, "\n")

print("goal: ")
print(RKK4, "\n")

# Tabel Frekuensi relatif Kumulatif Lebih dari
RKL1 = (KL1 / banyakData) * 100
RKL2 = (KL2 / banyakData) * 100
RKL3 = (KL3 / banyakData) * 100
RKL4 = (KL4 / banyakData) * 100
print("============================================")
print("== Frekuensi Relatif Kumulatif Lebih dari ==")
print("============================================")
print("usd_pledged_real: ")
print(RKL1, "\n")

print("usd_goal_real: ")
print(RKL2, "\n")

print("pledged: ")
print(RKL3, "\n")

print("goal: ")
print(RKL4, "\n")

"""
# Grafik
# Data frekuensi dan kelompok labels
kelompok_labels = [
    f"{kelompok.left:.1f} - {kelompok.right:.1f}" for kelompok in frekuensi1.index]

# Membuat grafik batang frekuensi
plt.bar(kelompok_labels, frekuensi1.values, color='skyblue')
plt.xlabel('Kelompok Data')
plt.ylabel('Frekuensi')
plt.title('Grafik Frekuensi usd_pledged_real')
plt.show()

plt.bar(kelompok_labels, frekuensi2.values, color='skyblue')
plt.xlabel('Kelompok Data')
plt.ylabel('Frekuensi')
plt.title('Grafik Frekuensi usd_goal_real')
plt.show()

plt.bar(kelompok_labels, frekuensi3.values, color='skyblue')
plt.xlabel('Kelompok Data')
plt.ylabel('Frekuensi')
plt.title('Grafik Frekuensi pledged')
plt.show()

plt.bar(kelompok_labels, frekuensi4.values, color='skyblue')
plt.xlabel('Kelompok Data')
plt.ylabel('Frekuensi')
plt.title('Grafik Frekuensi goal')
plt.show()

# Grafik Frekuensi Kumulatif
plt.plot(kelompok_labels, KK1, label='Kurang Dari')
plt.plot(kelompok_labels, KL1, label='Lebih dari')
plt.xlabel('Kelompok Data')
plt.ylabel('Frekuensi Kumulatif')
plt.title('Grafik Frekuensi Kumulatif usd_pledged_real')
plt.legend()
plt.grid(True)
plt.show()

plt.plot(kelompok_labels, KK2, label='Kurang Dari')
plt.plot(kelompok_labels, KL2, label='Lebih dari')
plt.xlabel('Kelompok Data')
plt.ylabel('Frekuensi Kumulatif')
plt.title('Grafik Frekuensi Kumulatif usd_goal_real')
plt.legend()
plt.grid(True)
plt.show()

plt.plot(kelompok_labels, KK3, label='Kurang Dari')
plt.plot(kelompok_labels, KL3, label='Lebih dari')
plt.xlabel('Kelompok Data')
plt.ylabel('Frekuensi Kumulatif')
plt.title('Grafik Frekuensi Kumulatif pledged')
plt.legend()
plt.grid(True)
plt.show()

plt.plot(kelompok_labels, KK4, label='Kurang Dari')
plt.plot(kelompok_labels, KL4, label='Lebih dari')
plt.xlabel('Kelompok Data')
plt.ylabel('Frekuensi Kumulatif')
plt.title('Grafik Frekuensi Kumulatif goal')
plt.legend()
plt.grid(True)
plt.show()

# Grafik Frekuensi relatif
plt.bar(kelompok_labels, frekuensi_relatif1, color='skyblue')
plt.xlabel('Kelompok Data')
plt.ylabel('Frekuensi Relatif (%)')
plt.title('Grafik Frekuensi Relatif usd_pledged_real')
plt.show()

plt.bar(kelompok_labels, frekuensi_relatif2, color='skyblue')
plt.xlabel('Kelompok Data')
plt.ylabel('Frekuensi Relatif (%)')
plt.title('Grafik Frekuensi Relatif usd_goal_real')
plt.show()

plt.bar(kelompok_labels, frekuensi_relatif3, color='skyblue')
plt.xlabel('Kelompok Data')
plt.ylabel('Frekuensi Relatif (%)')
plt.title('Grafik Frekuensi Relatif pledged')
plt.show()

plt.bar(kelompok_labels, frekuensi_relatif4, color='skyblue')
plt.xlabel('Kelompok Data')
plt.ylabel('Frekuensi Relatif (%)')
plt.title('Grafik Frekuensi Relatif goal')
plt.show()

# Grafik Frekuensi Relatif Kumulatif
plt.plot(kelompok_labels, RKK1, label='Kurang dari')
plt.plot(kelompok_labels, RKL1, label='Lebih dari')
plt.xlabel('Kelompok Data')
plt.ylabel('Frekuensi Relatif Kumulatif')
plt.title('Grafik Frekuensi Relatif Kumulatif usd_pledged_real')
plt.legend()
plt.grid(True)
plt.show()

plt.plot(kelompok_labels, RKK2, label='Kurang dari')
plt.plot(kelompok_labels, RKL2, label='Lebih dari')
plt.xlabel('Kelompok Data')
plt.ylabel('Frekuensi Relatif Kumulatif')
plt.title('Grafik Frekuensi Relatif Kumulatif usd_goal_real')
plt.legend()
plt.grid(True)
plt.show()

plt.plot(kelompok_labels, RKK3, label='Kurang dari')
plt.plot(kelompok_labels, RKL3, label='Lebih dari')
plt.xlabel('Kelompok Data')
plt.ylabel('Frekuensi RelatifKumulatif')
plt.title('Grafik Frekuensi RelatifKumulatif pledged')
plt.legend()
plt.grid(True)
plt.show()

plt.plot(kelompok_labels, RKK4, label='Kurang dari')
plt.plot(kelompok_labels, RKL4, label='Lebih dari')
plt.xlabel('Kelompok Data')
plt.ylabel('Frekuensi RelatifKumulatif')
plt.title('Grafik Frekuensi RelatifKumulatif goal')
plt.legend()
plt.grid(True)
plt.show()
"""
