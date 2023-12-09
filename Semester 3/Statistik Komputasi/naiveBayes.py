import pandas as pd
import os

# Fungsi clear screen
def clear_screen():
    os.system('cls')

dataFrame = pd.read_excel('Data_Mahasiswa.xlsx')
dataFrame

# Mengambil data kolom
jenisKelamin = dataFrame['JENIS KELAMIN']
asalDaerah = dataFrame['ASAL DAERAH']
cuti = dataFrame['CUTI']
asalSMA = dataFrame['ASAL SMA']
nikah = dataFrame['NIKAH']
program = dataFrame['PROGRAM']
kelas = dataFrame['KELAS']


# Distribusi data
# Memisahkan data menjadi data training dan data testing dengan perbandingan 80:20
# Data kelas "Tepat"
kelas_tepat = dataFrame[kelas == 'Tepat']
print(len(kelas_tepat))
kelas_tepat

# Memisahkan 70% data dari kelas yang bernilai "Tepat" sebagai data training. 30% sisanya akan menjadi data testing.
# Menenentukan index ke berapa data akan dipotong
index_potong_tepat = int(len(kelas_tepat) * 0.7)
index_potong_tepat


data_training_tepat = kelas_tepat.iloc[:index_potong_tepat]
data_testing_tepat = kelas_tepat.iloc[index_potong_tepat:]
print(len(data_training_tepat))
print(len(data_testing_tepat))
print(data_training_tepat)
print()
print(data_testing_tepat)


# Data kelas "Terlambat"
kelas_terlambat = dataFrame[kelas == 'Terlambat']
print(len(kelas_terlambat))
kelas_terlambat

# Memisahkan 70% data dari kelas yang bernilai "Terlambat" sebagai data training. 30% sisanya akan menjadi data testing.
# Menenentukan index ke berapa data akan dipotong
index_potong_terlambat = int(len(kelas_terlambat) * 0.71) #Ini hanya agar mendapat hasil 45
index_potong_terlambat


data_training_terlambat = kelas_terlambat.iloc[:index_potong_terlambat]
data_testing_terlambat = kelas_terlambat.iloc[index_potong_terlambat:]
print(len(data_training_terlambat))
print(len(data_testing_terlambat))
print(data_training_terlambat)
print()
print(data_testing_terlambat)

# Menggabungkan data training
join_training = pd.concat([data_training_tepat, data_training_terlambat])
data_training = join_training.sample(frac=1) #fungsi acak baris
print(len(data_training))
data_training


#  Menggabungkan data testing
join_testing = pd.concat([data_testing_tepat,data_testing_terlambat])
data_testing = join_testing.sample(frac=1) #fungsi acak baris
print(len(data_testing))
data_testing


# Hitung Probabilitas
# Probabilitas kelas
print('Banyak data tepat : ', len(data_training_tepat))
print('Banyak data terlambat :', len(data_training_terlambat))
persen_tepat = len(data_training_tepat)/len(data_training)
persen_terlambat = len(data_training_terlambat)/len(data_training)

print(f"{persen_tepat:.2%}")
print(f"{persen_terlambat:.2%}")


# Kolom jenis kelamin
# Jumlah Tepat
jumlah_laki_tepat = len(data_training[(data_training['JENIS KELAMIN'] == 'Laki-laki') & (data_training['KELAS'] == 'Tepat')])
jumlah_perempuan_tepat = len(data_training[(data_training['JENIS KELAMIN'] == 'Perempuan') & (data_training['KELAS'] == 'Tepat')])

# Jumlah Terlambat
jumlah_laki_terlambat = len(data_training[(data_training['JENIS KELAMIN'] == 'Laki-laki') & (data_training['KELAS'] == 'Terlambat')])
jumlah_perempuan_terlambat = len(data_training[(data_training['JENIS KELAMIN'] == 'Perempuan') & (data_training['KELAS'] == 'Terlambat')])

# Probabilitas
persen_laki_tepat = jumlah_laki_tepat/len(data_training_tepat)
persen_perempuan_tepat = jumlah_perempuan_tepat/len(data_training_tepat)
persen_laki_terlambat = jumlah_laki_terlambat/len(data_training_terlambat)
persen_perempuan_terlambat = jumlah_perempuan_terlambat/len(data_training_terlambat)

data = {
    'Jenis Kelamin': ['Laki-laki', 'Perempuan'],
    'Jumlah Tepat': [jumlah_laki_tepat, jumlah_perempuan_tepat],
    'Jumlah Terlambat': [jumlah_laki_terlambat, jumlah_perempuan_terlambat],
    'Persentase Tepat': [persen_laki_tepat, persen_perempuan_tepat],
    'Persentase Terlambat': [persen_laki_terlambat, persen_perempuan_terlambat]
}

df_jenisKelamin= pd.DataFrame(data)


# Kolom Asal Daerah
# Jumlah Tepat
jumlah_dk_tepat = len(data_training[(data_training['ASAL DAERAH'] == 'Dalam Kabupaten') & (data_training['KELAS'] == 'Tepat')]) # Dalam Kabupaten
jumlah_dp_tepat = len(data_training[(data_training['ASAL DAERAH'] == 'Dalam Provinsi') & (data_training['KELAS'] == 'Tepat')] )
jumlah_lp_tepat = len(data_training[(data_training['ASAL DAERAH'] == 'Luar Pulau') & (data_training['KELAS'] == 'Tepat')])

# Jumlah Terlambat
jumlah_dk_terlambat = len(data_training[(data_training['ASAL DAERAH'] == 'Dalam Kabupaten') & (data_training['KELAS'] == 'Terlambat')])
jumlah_dp_terlambat = len(data_training[(data_training['ASAL DAERAH'] == 'Dalam Provinsi') & (data_training['KELAS'] == 'Terlambat')])
jumlah_lp_terlambat = len(data_training[(data_training['ASAL DAERAH'] == 'Luar Pulau') & (data_training['KELAS'] == 'Terlambat')])

# Probabilitas
persen_dk_tepat = jumlah_dk_tepat/len(data_training_tepat)
persen_dp_tepat = jumlah_dp_tepat/len(data_training_tepat)
persen_lp_tepat = jumlah_lp_tepat/len(data_training_tepat)
persen_dk_terlambat = jumlah_dk_terlambat/len(data_training_terlambat)
persen_dp_terlambat = jumlah_dp_terlambat/len(data_training_terlambat)
persen_lp_terlambat = jumlah_lp_terlambat/len(data_training_terlambat)

data_asal_daerah = {
    'Asal Daerah': ['Dalam Kabupaten', 'Dalam Provinsi', 'Luar Pulau'],
    'Jumlah Tepat': [jumlah_dk_tepat, jumlah_dp_tepat, jumlah_lp_tepat],
    'Jumlah Terlambat': [jumlah_dk_terlambat, jumlah_dp_terlambat, jumlah_lp_terlambat],
    'Persentase Tepat': [persen_dk_tepat, persen_dp_tepat, persen_lp_tepat],
    'Persentase Terlambat': [persen_dk_terlambat, persen_dp_terlambat, persen_lp_terlambat]
}

df_asalDaerah = pd.DataFrame(data_asal_daerah)


# Kolom Cuti
# Jumlah Tepat
jumlah_cutiYa_tepat = len(data_training[(data_training['CUTI'] == 'Ya') & (data_training['KELAS'] == 'Tepat')])
jumlah_cutiTidak_tepat = len(data_training[(data_training['CUTI'] == 'Tidak') & (data_training['KELAS'] == 'Tepat')])

# Jumlah Terlambat
jumlah_cutiYa_terlambat = len(data_training[(data_training['CUTI'] == 'Ya') & (data_training['KELAS'] == 'Terlambat')])
jumlah_cutiTidak_terlambat = len(data_training[(data_training['CUTI'] == 'Tidak') & (data_training['KELAS'] == 'Terlambat')])

# Probabilitas
persen_cutiYa_tepat = jumlah_cutiYa_tepat/len(data_training_tepat)
persen_cutiTidak_tepat = jumlah_cutiTidak_tepat/len(data_training_tepat)
persen_cutiYa_terlambat = jumlah_cutiYa_terlambat/len(data_training_terlambat)
persen_cutiTidak_terlambat = jumlah_cutiTidak_terlambat/len(data_training_terlambat)

data_cuti = {
    'CUTI': ['Ya', 'Tidak'],
    'Jumlah Tepat': [jumlah_cutiYa_tepat, jumlah_cutiTidak_tepat],
    'Jumlah Terlambat': [jumlah_cutiYa_terlambat, jumlah_cutiTidak_terlambat],
    'Persentase Tepat': [persen_cutiYa_tepat, persen_cutiTidak_tepat],
    'Persentase Terlambat': [persen_cutiYa_terlambat, persen_cutiTidak_terlambat]
}

df_cuti = pd.DataFrame(data_cuti)


# Kolom Asal SMA
# Jumlah Tepat
jumlah_SMA_tepat = len(data_training[(data_training['ASAL SMA'] == 'SMA') & (data_training['KELAS'] == 'Tepat')])
jumlah_SMK_tepat = len(data_training[(data_training['ASAL SMA'] == 'SMK') & (data_training['KELAS'] == 'Tepat')])
jumlah_MA_tepat = len(data_training[(data_training['ASAL SMA'] == 'MA') & (data_training['KELAS'] == 'Tepat')])

# Jumlah Terlambat
jumlah_SMA_terlambat = len(data_training[(data_training['ASAL SMA'] == 'SMA') & (data_training['KELAS'] == 'Terlambat')])
jumlah_SMK_terlambat = len(data_training[(data_training['ASAL SMA'] == 'SMK') & (data_training['KELAS'] == 'Terlambat')])
jumlah_MA_terlambat = len(data_training[(data_training['ASAL SMA'] == 'MA') & (data_training['KELAS'] == 'Terlambat')])

# Probabilitas
persen_SMA_tepat = jumlah_SMA_tepat/len(data_training_tepat)
persen_SMK_tepat = jumlah_SMK_tepat/len(data_training_tepat)
persen_MA_tepat = jumlah_MA_tepat/len(data_training_tepat)
persen_SMA_terlambat = jumlah_SMA_terlambat/len(data_training_terlambat)
persen_SMK_terlambat = jumlah_SMK_terlambat/len(data_training_terlambat)
persen_MA_terlambat = jumlah_MA_terlambat/len(data_training_terlambat)

# Buat DataFrame
data_asal_sma = {
    'ASAL SMA': ['SMA', 'SMK', 'MA'],
    'Jumlah Tepat': [jumlah_SMA_tepat, jumlah_SMK_tepat, jumlah_MA_tepat],
    'Jumlah Terlambat': [jumlah_SMA_terlambat, jumlah_SMK_terlambat, jumlah_MA_terlambat],
    'Persentase Tepat': [persen_SMA_tepat, persen_SMK_tepat, persen_MA_tepat],
    'Persentase Terlambat': [persen_SMA_terlambat, persen_SMK_terlambat, persen_MA_terlambat]
}

df_asal_sma = pd.DataFrame(data_asal_sma)


# Kolom Nikah
# Jumlah Tepat
jumlah_nikahYa_tepat = len(data_training[(data_training['NIKAH'] == 'Sudah') & (data_training['KELAS'] == 'Tepat')])
jumlah_nikahTidak_tepat = len(data_training[(data_training['NIKAH'] == 'Belum') & (data_training['KELAS'] == 'Tepat')])

# Jumlah Terlambat
jumlah_nikahYa_terlambat = len(data_training[(data_training['NIKAH'] == 'Sudah') & (data_training['KELAS'] == 'Terlambat')])
jumlah_nikahTidak_terlambat = len(data_training[(data_training['NIKAH'] == 'Belum') & (data_training['KELAS'] == 'Terlambat')])

# Probabilitas
persen_nikahYa_tepat = jumlah_nikahYa_tepat/len(data_training_tepat)
persen_nikahTidak_tepat = jumlah_nikahTidak_tepat/len(data_training_tepat)
persen_nikahYa_terlambat = jumlah_nikahYa_terlambat/len(data_training_terlambat)
persen_nikahTidak_terlambat = jumlah_nikahTidak_terlambat/len(data_training_terlambat)

# Buat DataFrame
data_nikah = {
    'NIKAH': ['Sudah', 'Belum'],
    'Jumlah Tepat': [jumlah_nikahYa_tepat, jumlah_nikahTidak_tepat],
    'Jumlah Terlambat': [jumlah_nikahYa_terlambat, jumlah_nikahTidak_terlambat],
    'Persentase Tepat': [persen_nikahYa_tepat, persen_nikahTidak_tepat],
    'Persentase Terlambat': [persen_nikahYa_terlambat, persen_nikahTidak_terlambat]
}

df_nikah = pd.DataFrame(data_nikah)


# Kolom Program
# Jumlah Tepat
jumlah_karyawan_tepat = len(data_training[(data_training['PROGRAM'] == 'Karyawan') & (data_training['KELAS'] == 'Tepat')])
jumlah_reguler_tepat = len(data_training[(data_training['PROGRAM'] == 'Reguler') & (data_training['KELAS'] == 'Tepat')])

# Jumlah Terlambat
jumlah_karyawan_terlambat = len(data_training[(data_training['PROGRAM'] == 'Karyawan') & (data_training['KELAS'] == 'Terlambat')])
jumlah_reguler_terlambat = len(data_training[(data_training['PROGRAM'] == 'Reguler') & (data_training['KELAS'] == 'Terlambat')])

# Probabilitas
persen_karyawan_tepat = jumlah_karyawan_tepat/len(data_training_tepat)
persen_reguler_tepat = jumlah_reguler_tepat/len(data_training_tepat)
persen_karyawan_terlambat = jumlah_karyawan_terlambat/len(data_training_terlambat)
persen_reguler_terlambat = jumlah_reguler_terlambat/len(data_training_terlambat)

# Buat DataFrame
data_program = {
    'PROGRAM': ['Karyawan', 'Reguler'],
    'Jumlah Tepat': [jumlah_karyawan_tepat, jumlah_reguler_tepat],
    'Jumlah Terlambat': [jumlah_karyawan_terlambat, jumlah_reguler_terlambat],
    'Persentase Tepat': [persen_karyawan_tepat, persen_reguler_tepat],
    'Persentase Terlambat': [persen_karyawan_terlambat, persen_reguler_terlambat]
}

df_program = pd.DataFrame(data_program)

# Fungsi Naive Bayes
def naive_bayes_prediction(jenisKelamin, asalDaerah, cuti, asalSMA ,nikah, program ):
    persentase_jenisKelamin = {'Laki-laki': {'Tepat': persen_laki_tepat, 'Terlambat': persen_terlambat},
                            'Perempuan': {'Tepat': persen_perempuan_tepat, 'Terlambat': persen_perempuan_terlambat}}

    persentase_asalDaerah = {'Dalam Kabupaten': {'Tepat': persen_dk_tepat, 'Terlambat': persen_dk_terlambat},
                            'Dalam Provinsi': {'Tepat': persen_dp_tepat, 'Terlambat': persen_dp_terlambat},
                                'Luar Pulau': {'Tepat': persen_lp_tepat, 'Terlambat': persen_lp_terlambat}}
    
    persentase_cuti = {'Ya': {'Tepat': persen_cutiYa_tepat, 'Terlambat': persen_cutiYa_terlambat},
                            'Tidak': {'Tepat': persen_cutiTidak_tepat, 'Terlambat': persen_cutiTidak_terlambat}}
    
    persentase_asalSMA = {'SMA': {'Tepat': persen_SMA_tepat, 'Terlambat': persen_SMA_terlambat},
                            'SMK': {'Tepat': persen_SMK_tepat, 'Terlambat': persen_SMK_terlambat},
                                'MA': {'Tepat': persen_MA_tepat, 'Terlambat': persen_MA_terlambat}}
    
    persentase_nikah = {'Sudah': {'Tepat': persen_nikahYa_tepat, 'Terlambat': persen_nikahYa_terlambat},
                            'Belum': {'Tepat': persen_nikahTidak_tepat, 'Terlambat': persen_nikahTidak_terlambat}}
    
    persentase_golongan = {'Karyawan': {'Tepat': persen_karyawan_tepat, 'Terlambat': persen_karyawan_terlambat},
                            'Reguler': {'Tepat': persen_reguler_tepat, 'Terlambat': persen_reguler_terlambat}}
    
    # Menghitung prediksi untuk kelas 'Tepat'
    prediksi_tepat = (
        persen_tepat *
        persentase_jenisKelamin.get(jenisKelamin, 0).get('Tepat', 0) *
        persentase_asalDaerah.get(asalDaerah, 0).get('Tepat', 0) *
        persentase_cuti.get(cuti, 0).get('Tepat', 0) *
        persentase_asalSMA.get(asalSMA, 0).get('Tepat', 0) *
        persentase_nikah.get(nikah, 0).get('Tepat', 0) *
        persentase_golongan.get(program, 0).get('Tepat', 0)
    )

    # Menghitung prediksi untuk kelas 'Terlambat'
    prediksi_terlambat = (
        persen_terlambat *
        persentase_jenisKelamin.get(jenisKelamin, 0).get('Terlambat', 0) *
        persentase_asalDaerah.get(asalDaerah, 0).get('Terlambat', 0) *
        persentase_cuti.get(cuti, 0).get('Terlambat', 0) *
        persentase_asalSMA.get(asalSMA, 0).get('Terlambat', 0) *
        persentase_nikah.get(nikah, 0).get('Terlambat', 0) *
        persentase_golongan.get(program, 0).get('Terlambat', 0)
    )

    print(f'Persentase tepat: {prediksi_tepat}')
    print(f'Persentase terlambat: {prediksi_terlambat}')

    prediksi = max(prediksi_tepat, prediksi_terlambat)
    if prediksi == prediksi_tepat:
        return 'Tepat'
    else:
        return 'Terlambat'

clear_screen()
jenisKelamin = input('Masukkan jenis kelamin anda? (Laki-laki/Perempuan): ')
asalDaerah = input('Dari mana asal anda? (Dalam Kabupaten/Dalam Provinsi/Luar Pulau: ')
cuti = input('Pernahkah anda cuti? (Ya/Tidak): ')
asalSMA = input('Masukkan asal SMA anda (SMA/SMK/MA): ')
nikah = input('Sudahkah anda menikah? (Sudah/Belum): ')
program = input('Program yang anda ikuti (Karyawan/Reguler): ')

kelas_prediksi = naive_bayes_prediction(jenisKelamin, asalDaerah, cuti, asalSMA, nikah, program)
print("Prediksi Kelas: ", kelas_prediksi)