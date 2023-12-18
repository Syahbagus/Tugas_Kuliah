echo "Masukkan bilangan : "
read input

echo "Bilangan kelipatan ganjil hingga $input adalah : "

for (( i=$input; i>=1; i-=2))
  do 
   echo $i
done
