#Deklarasi Fungsi
hitungLuas(){
  panjang=$1
  lebar=$2

  # Ganti koma dengan titik
  panjang=$(echo $panjang | tr "," ".")
  lebar=$(echo $lebar | tr "," ".")

  luas=$(echo "$panjang * $lebar" | bc)
  printf "Luas persegi yang memiliki panjang $panjang dan lebar $lebar\nAdalah : $luas\n"  
}

#input parameter
echo "Masukkan panjang : "
read panjang

echo "Masukkan Lebar : "
read lebar

#Panggil fungsi
hitungLuas $panjang $lebar
