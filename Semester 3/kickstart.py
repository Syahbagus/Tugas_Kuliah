import pandas as pd

# Baca data excel
file_name = "Kickstart Project (Tugas).xlsx"
excel = pd.ExcelFile(file_name)

# Baca sheet 2 dan hitung jumlah data
sheet2 = excel.parse("Sheet 2")
print('Jumlah Data: ', len(sheet2), "\n")

kolom1 = "usd_pledged_real"
kolom2 = "usd_goal_real"
kolom3 = "pledged"
kolom4 = "goal"

# Menghitung mean, median, dan modus untuk masing-masing kolom
mean1 = sheet2[kolom1].mean()
median1 = sheet2[kolom1].median()
modus1 = sheet2[kolom1].mode().iloc[0]

mean2 = sheet2[kolom2].mean()
median2 = sheet2[kolom2].median()
modus2 = sheet2[kolom2].mode().iloc[0]

mean3 = sheet2[kolom3].mean()
median3 = sheet2[kolom3].median()
modus3 = sheet2[kolom3].mode().iloc[0]

mean4 = sheet2[kolom4].mean()
median4 = sheet2[kolom4].median()
modus4 = sheet2[kolom4].mode().iloc[0]

# Tampilkan data
print("Data kolom ", kolom1)
print("Mean     : ", mean1)
print("Median   : ", median1)
print("Modus    : ", modus1)
print("")
print("Data kolom ", kolom2)
print("Mean     : ", mean2)
print("Median   : ", median2)
print("Modus    : ", modus2)
print("")
print("Data kolom ", kolom3)
print("Mean     : ", mean3)
print("Median   : ", median3)
print("Modus    : ", modus3)
print("")
print("Data kolom ", kolom4)
print("Mean     : ", mean4)
print("Median   : ", median4)
print("Modus    : ", modus4)
