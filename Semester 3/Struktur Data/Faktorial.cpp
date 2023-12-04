#include <iostream>
using namespace std;

int main()
{
    int angka;

    cout << "Masukkan angka yang ingin difaktorialkan: ";
    cin >> angka;

    if (angka < 0)
    {
        cout << "Masukkan angka non-negatif." << endl;
    }
    else
    {
        int hasil = 1;
        for (int i = 1; i <= angka; i++)
        {
            hasil *= i;
        }

        cout << "Faktorial dari " << angka << " adalah " << hasil << endl;
    }

    return 0;
}
