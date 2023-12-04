#include <iostream>
using namespace std;

int oper, n;
double x, hasil;

double rekursif1(double x, int n)
{
    if (n == 0)
    {
        return 1;
    }
    else if (n > 0)
    {
        return x * rekursif1(x, n - 1);
    }
    else if (n < 0)
    {
        return 1 / rekursif1(x, -n);
    }
    else
    {
        cout << "Input tidak valid";
        return 0;
    }
}

double rekursif2(double x, int n)
{
    if (n == 0)
    {
        return 1;
    }
    else if (n % 2 == 0) // Untuk pangkat genap
    {
        double setengah = rekursif2(x, n / 2);
        return setengah * setengah;
    }
    else if (n % 2 != 0) // Untuk pangkat ganjil
    {
        double setengah = rekursif2(x, (n - 1) / 2);
        return x * setengah * setengah;
    }
    else
    {
        cout << "Input tidak valid";
        return 0;
    }
}

int main()
{
    cout << "Tugas 2 Struktur Data\n";
    cout << "......................\n";
    cout << "1. X^n" << endl;
    cout << "2. X^n/2" << endl;
    cout << "Pilih Operasi (1/2) : ";
    cin >> oper;
    cout << endl;

    if (oper == 1)
    {
        cout << "Masukkan nilai pokok X : ";
        cin >> x;
        cout << "Masukan bilangan pangkat N : ";
        cin >> n;
        cout << endl;
        hasil = rekursif1(x, n);
        cout << "Hasil dari " << x << " pangkat " << n << " adalah : " << hasil << endl;
    }
    else if (oper == 2)
    {
        cout << "Masukkan nilai pokok X : ";
        cin >> x;
        cout << "Masukan bilangan pangkat N : ";
        cin >> n;
        cout << endl;
        hasil = rekursif2(x, n);
        cout << "Hasil dari " << x << " pangkat " << n << " adalah : " << hasil << endl;
    }
    else
    {
        cout << "Operasi yang anda masukkan salah!";
    }
    return 0;
}
