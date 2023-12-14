#include <iostream>
using namespace std;
float a, b, tinggi, luas;

int main()
{
    system("cls");
    cout << "Program hitung luas trapesium\n";
    cout << "=============================\n";
    cout << "Masukkan panjang sisi sejajar 1: ";
    cin >> a;
    cout << "Masukkan panjang sisi sejajar 2: ";
    cin >> b;
    cout << "Masukkan tinggi: ";
    cin >> tinggi;
    luas = ((a + b) * tinggi) / 2;
    cout << "Luas trapesiumnya adalah : " << luas;
    return 0;
}