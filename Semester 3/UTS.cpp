#include <iostream>
#include <cmath>
using namespace std;

double x, y, h, batasBawah, batasAtas;

// Fungsi X
double f(double x)
{
    return x * x - exp(x) + 5;
}

void tabel()
{
    int n = 10;
    system("cls");
    cout << "----Metode Tabel----" << endl;
    cout << "Masukkan batas bawah : ";
    cin >> batasBawah;
    cout << "Masukkan batas atas  : ";
    cin >> batasAtas;
    h = (batasAtas - batasBawah) / n;
    cout << h << endl;
    cout << endl;
    for (int i = 0; i <= n; i++)
    {
        x = batasBawah + i * h;
        y = f(x);
        cout << x << "\t" << y << endl;
    }
    cout << endl;
}

void regulaFalsi()
{
    system("cls");
    cout << "----Metode Regula Falsi----";
    cout << "Masukkan batas bawah : ";
    cin >> batasBawah;
    cout << "Masukkan batas atas  : ";
    cin >> batasAtas;
}

int main()
{
    bool repeat = false;
    int metode;
    char pilihan;
    system("cls");
    cout << "----Program Metode Tertutup----" << endl;
    cout << "1. Metode Tabel" << endl;
    cout << "2. Metode Regula Falsi" << endl;
    cout << endl;
    cout << "Pilih metode : ";
    cin >> metode;
    switch (metode)
    {
    case 1:
        do
        {
            tabel();
            cout << "Apakah ingin menghitung lagi? (y/n) : ";
            cin >> pilihan;
            if (pilihan == 'y' || pilihan == 'Y')
            {
                repeat = true;
            }
            else
            {
                repeat = false;
            }
        } while (repeat == true);
        break;
    case 2:
        do
        {
            regulaFalsi();
            cout << "Apakah ingin menghitung lagi? (y/n) : ";
            cin >> pilihan;
            if (pilihan == 'y' || pilihan == 'Y')
            {
                repeat = true;
            }
            else
            {
                repeat = false;
            }
        } while (repeat == true);
        break;
    default:
        cout << "Metode tidak ditemukan.";
    }

    return 0;
}