import pandas as pd
import numpy as np

# Baca data excel
file_name = "Kickstart Project (Tugas).xlsx"
excel = pd.ExcelFile(file_name)

sheet_name = excel.sheet_names
print(sheet_name)
