#include <iostream>

using namespace std;

// Fungsi rekursi untuk memindahkan piringan dari tiang awal ke tiang akhir
void menaraHanoi(int n, char tiangAwal, char tiangTengah, char tiangAkhir)
{
    if (n == 1)
    {
        cout << "Piringan 1 dari " << tiangAwal << " ke " << tiangAkhir << endl;
        return;
    }

    // Memindahkan (n-1) piringan dari tiang awal ke tiang tengah
    menaraHanoi(n - 1, tiangAwal, tiangAkhir, tiangTengah);

    // Memindahkan piringan terbesar dari tiang awal ke tiang akhir
    cout << "Piringan " << n << " dari " << tiangAwal << " ke " << tiangAkhir << endl;

    // Memindahkan (n-1) piringan dari tiang tengah ke tiang akhir
    menaraHanoi(n - 1, tiangTengah, tiangAwal, tiangAkhir);
}

int main()
{
    int jumlahPiringan;

    cout << "Masukkan jumlah piringan: ";
    cin >> jumlahPiringan;

    // Memanggil fungsi Menara Hanoi
    menaraHanoi(jumlahPiringan, 'A', 'B', 'C');

    return 0;
}
