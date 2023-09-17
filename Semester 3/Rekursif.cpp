#include <iostream>
using namespace std;

int oper, n;
double x, hasil;

double rekursif(double x, int n)
{
    if (n == 0)
    {
        return 1;
    }
    else if (n > 0)
    {
        return x * rekursif(x, n - 1);
    }
    else if (n < 0)
    {
        return 1 / rekursif(x, -n)
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
        cout << endl;
        cout << "Masukan bilangan pangkat N : ";
        cin >> n;
        cout << endl;
        hasil = rekursif(x, n);
    }
}