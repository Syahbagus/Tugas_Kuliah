import pandas as pd
import numpy as np

# Baca data excel
file_name = "Kickstart Project (Tugas).xlsx"
excel = pd.ExcelFile(file_name)

# Baca sheet 2 dan hitung jumlah data
sheet2 = excel.parse("Sheet 2")
print('Jumlah Data: ', len(sheet2))

kolom1 = "usd_pledged_real"
kolom2 = "usd_goal_real"
kolom3 = "pledged"
kolom4 = "goal"

notnull1 = len(sheet2[sheet2[kolom1] != 0])
print("Jumlah data tidak nol 1 : ", notnull1)
