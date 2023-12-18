#!/bin/bash

while true; do
    clear

    case $pilihan in
        1)
            read -p "Masukkan nama folder: " nama_folder
            mkdir "$nama_folder"
            echo "Folder $nama_folder berhasil dibuat"
            ;;
        2)
            echo "1. Buat file dan ganti hak akses"
            echo "2. Ganti hak akses dengan file yang sudah ada"
            read -p "Pilih menu (1-2)" menu
            
            case $menu in
            1)
            read -p "Masukkan nama file " nama_file_pil1
            touch "$nama_file_pil1"
            read -p "Masukkan kode hak aksesnya (user): (read = 4, write = 2, execute = 1): " code_akses1
            read -p "Masukkan kode hak aksesnya (group): (read = 4, write = 2, execute = 1): " code_akses2
            read -p "Masukkan kode hak aksesnya (another user): (read = 4, write = 2, execute = 1): " code_akses3
            chmod "$code_akses1$code_akses2$code_akses3" "$nama_file_pil1"
            echo "File dengan nama $nama_file_pil berhasil dibuat dengan kode akses $code_akses1$code_akses2$code_akses3"
            ;;
            2)
            echo "Berikut adalah file - file yang ada di folder UAS : "
            ls
            read -p "Masukkan nama file yang sudah ada di folder UAS yang ingin diganti hak aksesnya : " nama_file_pil2
            read -p "Masukkan kode hak aksesnya (user): (read = 4, write = 2, execute = 1): " code_akses1
            read -p "Masukkan kode hak aksesnya (group): (read = 4, write = 2, execute = 1): " code_akses2
            read -p "Masukkan kode hak aksesnya (another user): (read = 4, write = 2, execute = 1): " code_akses3
            chmod "$code_akses1$code_akses2$code_akses3" "$nama_file_pil2"
            echo "File dengan nama $nama_file_pil2 berhasil diubah hak aksesnya dengan kode akses $code_akses1$code_akses2$code_akses3 "
            ;;
            esac
            ;;
        3) 
            read -p "Masukkan jari-jarinya: " jari
            luas_lingkaran() {
            luas=$(echo "scale=2; $jari * $jari * 3.14" | bc)
            echo $luas
	    }
            echo "Luas Lingkaran dengan jari-jari $jari adalah " $(luas_lingkaran)
            ;;
	4)
            read -p "Masukkan acuannya: " n
            a=0
            b=1

	    echo -n "Deret Fibonacci dengan acuan $n: "
            while [ $a -le $n ]; do
            echo -n "$a "
            temp=$a
            a=$b
            b=$((temp + b))
            done
            echo ""
            ;;
        5) 
            echo "1. Calculator"
            echo "2. Cheese"
            echo "3. Calendar"
            echo "4. Videos"
            echo "5. Mines"
            echo "6. Mahjongg"
            echo "7. Shotwell"
            echo "8. Sudoku"
            read -p "Pilih aplikasi (1/8): " aplikasi
            
            case $aplikasi in
                1) 
                gnome-calculator
                ;;
                2) 
                cheese
                ;;
                3) 
                gnome-calendar
                ;;
                4) 
                totem
                ;;
                5) 
                gnome-mines
                ;;
                6) 
                gnome-mahjongg
                ;;
                7) 
                gnome-shotwell
                ;;
                8) 
                gnome-sudoku
                ;;
                *)
                echo "Pilihan aplikasi tidak valid"
                ;;
            esac
            clear
            ;;
        6) 
            read -p "Masukkan jari-jarinya: " jari
            read -p "Masukkan tingginya: " tinggi
            volume_tabung() {
            volume=$(echo "scale=2; $jari * $jari * 3.14 * $tinggi" |bc)
            echo $volume
            }
            
            echo "Volume Tabung dengan jari-jari $jari dan tinggi $tinggi adalah " $(volume_tabung)
            ;;
            
        7)
           read -p "Masukkan acuan untuk angka ganjil : " n
           for((i=0; i<=n ; i++))
           do
           if [ $((i % 2)) != 0 ]; then
           echo $i
           fi
           done
           ;;
        8)
           read -p "Masukkan angka faktorialnya : " n
           hasil=1
           for((i=1; i<=n ; i++))
           do
           hasil=$((hasil * i))
           if [ $i -ne $n ]; then
           echo -n "$i * "
           else
           echo $i
           fi
           done
           echo "Hasil faktorialnya adalah : $hasil"
           ;;
        9)
          read -p "Masukkan nama anda: " nama
          read -p "Masukkan berat benda anda: " bb
          read -p "Masukkan tinggi badan anda: " tb
          bmi=$(echo "scale=2; $bb / (($tb / 100) * ($tb / 100))" | bc)

          if (( $(echo "$bmi >= 1 && $bmi <= 18.5" | bc) )); then
          category=kurang
          echo "Hallo $nama, dengan berat $bb, dan tinggi $tb maka BMI anda adalah $bmi dengan kategori $category"
          elif (( $(echo "$bmi >= 18.6 && $bmi <= 24.9" | bc) )); then
          category=sedang
          echo "Hallo $nama, dengan berat $bb, dan tinggi $tb maka BMI anda adalah $bmi dengan kategori $category"
	  elif (( $(echo "$bmi >= 25 && $bmi <= 29.9" | bc) )); then
          category=berat
          echo "Hallo $nama, dengan berat $bb, dan tinggi $tb maka BMI anda adalah $bmi dengan kategori $category"
          elif (( $(echo "$bmi >= 29.9" | bc) )); then
          category=obesitas
          echo "Hallo $nama, dengan berat $bb, dan tinggi $tb maka BMI anda adalah $bmi dengan kategori $category"
          else
          echo "Error silahkan coba lagi!"
          fi
          ;;
        10)
           exit 0
           ;;
        *)
           echo "Silakan pilih 1-10."
           ;;
    esac
    
    echo "Tugas Proyek Akhir Sistem Operasi! (1-10)"
    echo "Kelompok 17"
    echo " "
    echo "Nama : Syahbagus Radithya H.S"
    echo "NPM : 22081010255"
    echo " "
    echo "Nama : M. Naufal Rafy Ghaly"
    echo "NPM : 22081010295"
    echo " "
    echo "1. Buat Folder Baru"
    echo "2. Manipulasi hak akses berkas"
    echo "3. Menghitung Luas Lingkaran"
    echo "4. Menampilkan Angka Fibonachi"
    echo "5. Membuka Aplikasi"
    echo "6. Menghitung Volume Tabung"
    echo "7. Menampilkan Angkan Ganjil Menurut Acuan"
    echo "8. Menghitung Faktorial"
    echo "9. Menghitung BMI"
    echo "10. Keluar Program"
    read -p "Pilih aksi (1/10) : " pilihan
    
done
