echo "Masukkan jumlah data"
read jumlahData

declare -a arrayAngka 

for ((i=1; i<=jumlahData; i++)); do
  echo "Masukkan angka ke $i"
  read nilaiIPS

  # Ganti koma dengan titik
  nilaiIPS=$(echo $nilaiIPS | tr "," ".")

  arrayAngka[$i]=$nilaiIPS
done

total_ips=0

# Gunakan ekspresi aritmatika untuk penjumlahan
for ips in "${arrayAngka[@]}"; do
  total_ips=$(echo "$total_ips + $ips" | bc)
done

# Hitung IPK dengan menggunakan jumlahData sebagai pembagi
ipk=$(echo "scale=2; $total_ips / $jumlahData" | bc)

echo "$total_ips / $jumlahData"
echo "IPK : $ipk"

