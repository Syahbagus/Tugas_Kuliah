#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

double x, y, h, batasBawah, batasAtas, xSebelum, hasil, batasBawahBaru, batasAtasBaru, eror;
double tolerance = 1e-7;

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

    do
    {
        h = (batasAtas - batasBawah) / n;
        cout << h << endl;
        cout << endl;
        for (int i = 0; i <= n; i++)
        {
            x = batasBawah + i * h;
            xSebelum = batasBawah + (i - 1) * h;
            y = f(x);
            cout << x << setprecision(8) << "\t\t" << y << "\t";
            if (f(x) == 0)
            {
                cout << "Akar penyelesaiannya adalah : " << x;
            }
            else if (f(x) * f(xSebelum) < 0)
            {
                if (abs(f(x)) < abs(f(xSebelum)))
                {
                    hasil = x;
                    batasAtasBaru = x;
                    batasBawahBaru = xSebelum;
                    eror = abs(y);
                    cout << " <---Akar";
                }
                else
                {
                    hasil = xSebelum;
                    batasAtasBaru = x;
                    batasBawahBaru = xSebelum;
                    eror = abs(y);
                    cout << "<---Akar";
                }
            }
            cout << endl;
        }
        cout << "Akarnya adalah : " << hasil << endl;
        batasAtas = batasAtasBaru;
        batasBawah = batasBawahBaru;
    } while (eror >= tolerance);
}

void regulaFalsi()
{
    system("cls");
    cout << "----Metode Regula Falsi----" << endl;
    cout << "Masukkan batas bawah : ";
    cin >> batasBawah; // a
    cout << "Masukkan batas atas  : ";
    cin >> batasAtas; // b
    cout << "a\t"
         << "b\t"
         << "fa\t\t"
         << "fb\t\t"
         << "c\t\t"
         << "fc";
    cout << endl;
    do
    {
        double fa = f(batasBawah);
        double fb = f(batasAtas);
        x = (((batasBawah * fb) - (batasAtas * fa)) / (fb - fa));
        eror = f(x);
        if (eror * fa < 0)
        {
            batasAtasBaru = x;
            batasBawahBaru = batasBawah;
        }
        else
        {
            batasBawahBaru = x;
            batasAtasBaru = batasAtas;
        }
        cout << batasBawah << "\t" << batasAtas << "\t" << fa << "\t" << fb << "\t" << x << "\t" << eror << endl;
        batasAtas = batasAtasBaru;
        batasBawah = batasBawahBaru;
    } while (eror >= tolerance);
}

int main()
{
    bool repeat = true, keluar = false;
    int metode;
    char pilihan;
    do
    {
        system("cls");
        cout << "----Program Metode Tertutup----" << endl;
        cout << "1. Metode Tabel" << endl;
        cout << "2. Metode Regula Falsi" << endl;
        cout << "3. Keluar" << endl;
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
        case 3:
            keluar = true;
            break;
        default:
            cout << "Metode tidak ditemukan.";
        }
    } while (keluar == false);

    return 0;
}