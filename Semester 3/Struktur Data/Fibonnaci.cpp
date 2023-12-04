#include <iostream>
using namespace std;

int main()
{
    system("cls");
    int n;

    cout << "Masukkan panjang deret Fibonacci: ";
    cin >> n;

    int fibo[n];

    fibo[0] = 1;
    fibo[1] = 1;

    for (int i = 2; i < n; i++)
    {
        fibo[i] = fibo[i - 1] + fibo[i - 2];   //Rumus Fibonacci
    }

    // Menuliskan Output
    cout << "Deret Fibonacci dengan panjang " << n << " adalah: ";
    for (int i = 0; i < n; i++)
    {
        cout << fibo[i];
        if (i < n - 1)
        {
            cout << ", ";
        }
    }

    cout << endl;

    return 0;
}
