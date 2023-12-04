import random
import pandas as pd
import string
from faker import Faker
from faker_airtravel import AirTravelProvider

# Inisialisasi objek Faker
fake = Faker('id_ID')
fake.add_provider(AirTravelProvider)

# Data untuk Tabel DEPARTEMEN
# Daftar nama departemen pesawat
departemen_pesawat_nama = [
    "Departemen Perancangan Pesawat (Aircraft Design Department)",
    "Departemen Produksi Pesawat (Aircraft Production Department)",
    "Departemen Pengujian Pesawat (Aircraft Testing Department)",
    "Departemen Perawatan dan Perbaikan Pesawat (Aircraft Maintenance and Repair Department)",
    "Departemen Operasi Pesawat (Aircraft Operations Department)",
    "Departemen Sumber Daya Manusia (Human Resources Department)",
    "Departemen Keamanan Pesawat (Aircraft Security Department)",
    "Departemen Pemasaran dan Penjualan Pesawat (Aircraft Marketing and Sales Department)",
    "Departemen Administrasi dan Keuangan (Administration and Finance Department)",
    "Departemen Teknologi Informasi (Information Technology Department)",
    "Departemen Pelayanan Pelanggan (Customer Service Department)",
    "Departemen Penanganan Bagasi (Baggage Handling Department)",
    "Departemen Pemadam Kebakaran (Fire Department)",
    "Departemen Manajemen Terminal (Terminal Management Department)",
    "Departemen Administrasi Bandara (Airport Administration Department)",
    "Departemen Operasi Darat (Ground Operations Department)",
    "Departemen Keselamatan Bandara (Airport Safety Department)",
    "Departemen Layanan Perawatan Pesawat (Aircraft Maintenance Services Department)",
]

departemen_data = []
for _ in range(500):
    departemen_data.append((
        f"{random.choice(string.ascii_uppercase)}{fake.unique.random_int(min=1, max=9999)}",
        random.choice(departemen_pesawat_nama),
        fake.unique.address(),
        fake.random_int(min=10, max=100)
    ))

# Data untuk Tabel MASKAPAI
maskapai_data = []
for _ in range(500):
    maskapai_data.append((
        fake.unique.random_int(min=1000, max=9999),
        fake.airline(),
        fake.random_int(min=10000000, max=99999999),
        fake.company_suffix()
    ))

# Data untuk Tabel PENUMPANG
jenis_kelamin = ["Laki-laki", "Perempuan"]
penumpang_data = []
for _ in range(500):
    penumpang_data.append((
        fake.unique.random_int(min=1, max=9999),
        fake.name(),
        fake.address(),
        f"{random.choice(string.ascii_uppercase)}{fake.unique.random_int(min=1, max=9999)}",
        fake.date_time_between(
            start_date='-65y', end_date='-17y').strftime('%Y-%m-%d'),
        fake.phone_number(),
        random.choice(jenis_kelamin),
    ))

# Data untuk Tabel PEGAWAI
# Daftar nama jabatan pegawai
jabatan_pegawai_nama = [
    "Manajer Bandara (Airport Manager)",
    "Petugas Keamanan Bandara (Airport Security Officer)",
    "Petugas Ground Handling (Ground Handling Staff)",
    "Petugas Pemberangkatan (Departure Agent)",
    "Petugas Kepabeanan dan Bea Cukai (Customs and Customs Officer)",
    "Petugas Informasi Bandara (Airport Information Officer)",
    "Petugas Pelayanan Pelanggan (Customer Service Agent)",
    "Petugas Pengaturan Lalu Lintas Udara (Air Traffic Controller)",
    "Petugas Pemadam Kebakaran (Firefighter)",
    "Petugas Teknik (Maintenance Technician)",
    "Petugas Penanganan Bagasi (Baggage Handler)",
    "Petugas Fasilitas (Facility Maintenance Staff)",
    "Petugas Perawatan Lanskap (Landscape Maintenance Worker)",
    "Petugas Manajemen Terminal (Terminal Manager)",
    "Petugas Administrasi Bandara (Airport Administration Officer)"
]

pegawai_data = []
for _ in range(500):
    pegawai_data.append((
        fake.unique.random_int(min=1000, max=9999),
        fake.name(),
        random.choice(jabatan_pegawai_nama),
        fake.date_time_between(
            start_date='-5y', end_date='now').strftime('%H:%M:%S'),
        fake.random_int(min=4000000, max=9000000),
        f"{random.choice(string.ascii_uppercase)}{fake.unique.random_int(min=1, max=9999)}",
    ))

# Data untuk Tabel PESAWAT
# Daftar tipe pesawat
tipe_pesawat = [
    "Boeing 737",
    "Airbus A320",
    "ATR 72",
    "Embraer E-Jet",
    "Bombardier CRJ",
    "Boeing 777",
    "Airbus A330",
    "Boeing 747",
    "Airbus A350",
    "ATR 42",
    "Embraer ERJ",
    "Airbus A380",
    "Boeing 787",
    "Boeing 757",
    "Airbus A340",
    "Airbus A319",
    "Boeing 767",
    "Bombardier Q400",
    "Fokker 100",
    "Sukhoi Superjet 100",
]

pesawat_data = []
for _ in range(500):
    pesawat_data.append((
        fake.unique.random_int(min=1, max=9999),
        fake.airline(),
        fake.random_int(min=1990, max=2023),
        random.choice(['Operasional', 'Perbaikan', 'Tidak Aktif']),
        fake.random_int(min=100, max=500),
        random.choice(tipe_pesawat),
    ))

penerbangan_data = []
for _ in range(500):
    penerbangan_data.append((
        f"{random.choice(string.ascii_uppercase)}{fake.unique.random_int(min=1, max=9999)}",
        fake.city_name(),
        fake.city_name(),
        fake.date_time_between(
            start_date='-1y', end_date='-1m').strftime('%y-%m-%d %H:%M:%S'),
        fake.date_time_between(
            start_date='-1m', end_date='now').strftime('%y-%m-%d %H:%M:%S'),
    ))

cargo_data = []
for _ in range(500):
    cargo_data.append((
        f"{random.choice(string.ascii_uppercase)}{fake.unique.random_int(min=1, max=9999)}",
        fake.unique.random_int(min=1, max=9999),
        f"{random.choice(string.ascii_uppercase)}{fake.unique.random_int(min=1, max=9999)}",
        fake.city_name(),
        fake.random_int(min=1, max=40),
        fake.random_element(elements=(
            'Umum', 'Berbahaya', 'Cair', 'Padat(Solid)', 'Refrigerasi', 'Hewan Hidup')),
    ))

# DataFrames
df_departemen = pd.DataFrame(departemen_data, columns=[
    'IDDEPARTEMEN', 'NAMADEPARTEMEN', 'LOKASIDEPARTEMEN', 'JUMLAHPEKERJA'])
df_maskapai = pd.DataFrame(maskapai_data, columns=[
    'KODEMASKAPAI', 'NAMAMASKAPAI', 'KONTAKMASKAPAI', 'BASISOPERASI'])
df_pegawai = pd.DataFrame(pegawai_data, columns=[
    'NOMORPEGAWAI', 'NAMA', 'PEKERJAAN', 'JADWALKERJA', 'GAJI', 'IDDEPARTEMEN'])
df_pesawat = pd.DataFrame(pesawat_data, columns=[
    'NOMORREGISTRASI', 'MASKAPAIOPERASIONAL', 'TAHUNPEMBUATAN', 'STATUSOPERASIONAL', 'KAPASITASPENUMPANG', 'TIPEPESAWAT'])
df_penumpang = pd.DataFrame(penumpang_data, columns=[
    'NOMORTIKET', 'NAMAPENUMPANG', 'ALAMAT', 'NOMORPASPOR', 'TANGGALLAHIR', 'KONTAK', 'JENIS KELAMIN'])
df_penerbangan = pd.DataFrame(penerbangan_data, columns=[
    'NOMORPENERBANGAN', 'KOTAASAL', 'KOTATUJUAN', 'WAKTUKEBERANGKATAN', 'WAKTUKEDATANGAN'])
df_cargo = pd.DataFrame(cargo_data, columns=[
    'NOCARGO', 'NOMORTIKET', 'NOMORPENERBANGAN', 'TUJUANCARGO', 'BERATCARGO', 'JENISCARGO'])

# Pengurutan DataFrame berdasarkan kolom dari terkecil ke terbesar
df_departemen = df_departemen.sort_values(by='IDDEPARTEMEN', ascending=True)
df_maskapai = df_maskapai.sort_values(by='KODEMASKAPAI', ascending=True)
df_pegawai = df_pegawai.sort_values(by='NOMORPEGAWAI', ascending=True)
df_pesawat = df_pesawat.sort_values(by='NOMORREGISTRASI', ascending=True)
df_penumpang = df_penumpang.sort_values(by='NOMORTIKET', ascending=True)
df_penerbangan = df_penerbangan.sort_values(by='NOMORPENERBANGAN', ascending=True)
df_cargo = df_cargo.sort_values(by='NOCARGO', ascending=True)

# Membuat file Excel dan menyimpan tiap DataFrame
# df_departemen.to_excel('departemen_data.xlsx', index=False)
# df_maskapai.to_excel('maskapai_data.xlsx', index=False)
# df_pegawai.to_excel('pegawai_data.xlsx', index=False)
# df_pesawat.to_excel('pesawat_data.xlsx', index=False)
# df_penumpang.to_excel('penumpang_data.xlsx', index=False)
df_penerbangan.to_excel('penerbangan_data.xlsx', index=False)
# df_cargo.to_excel('cargo_data.xlsx', index=False)

print("Data untuk Tabel DEPARTEMEN:")
print(df_departemen)

print("\nData untuk Tabel MASKAPAI:")
print(df_maskapai)

print("\nData untuk Tabel PEGAWAI:")
print(df_pegawai)

print("\nData untuk Tabel PESAWAT:")
print(df_pesawat)

print("\nData untuk Tabel PENUMPANG:")
print(df_penumpang)

print("\nData untuk Tabel PENUMPANG:")
print(df_penerbangan)

print("\nData untuk Tabel CARGO:")
print(df_cargo)

# Tampilkan pesan konfirmasi
print("Data telah disimpan berbentuk file Excel dengan tiap DataFrame sebagai file yang berbeda.")
