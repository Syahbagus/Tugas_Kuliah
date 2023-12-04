#include <iostream>
using namespace std;

struct Kampus
{
    string namaKampus;
    int TB;
};

struct Mahasiswa
{
    string npm, nama, jurusan;
    int usia;
    string hobi[2];
    Kampus kps;
} mhs1, mhs2;

// Cara Global
Mahasiswa mhs4[2];

int main()
{
    system("cls");

    // Cara lokal
    Mahasiswa mhs5[2];

    // Cara 1
    mhs1.npm = "22081010001";
    mhs1.nama = "Andi";
    mhs1.jurusan = "Informatika";
    mhs1.usia = 20;
    mhs1.hobi[0] = "Bermain bola";
    mhs1.hobi[1] = "Bermain layangan";
    // Nested Structure
    mhs1.kps.namaKampus = "Institut Sepuluh Nopember";
    mhs1.kps.TB = 1980;

    // Cara 2
    Mahasiswa mhs2;
    mhs2 = {"22082010002", "Suheb", "Sistem Informasi", 19, "Bersepeda", "Membaca buku", "Airlangga", 1990};

    // Cara 3
    Mahasiswa mhs3 = {"22083010003", "Ratna", "Sains Data", 19};
    mhs3.hobi[0] = "Bermain game";
    mhs3.hobi[1] = "Traveling";
    mhs3.kps = {"UPN Jatim", 1959};

    // Inisisasi
    mhs4[0].hobi[0] = "Ngoding";
    mhs4[1].hobi[0] = "Menonton TV";
    mhs5[0].hobi[0] = "Bermain catur";
    mhs5[1].hobi[0] = "Mendengarkan lagu";

    cout << "NPM Mahasiswa : " << mhs1.npm << endl;
    cout << "Nama Mahasiswa: " << mhs1.nama << endl;
    cout << "Jurusan       : " << mhs1.jurusan << endl;
    cout << "Usia          : " << mhs1.usia << endl;
    cout << "Hobi 1        : " << mhs1.hobi[0] << endl;
    cout << "Hobi 2        : " << mhs1.hobi[1] << endl;
    cout << "Nama Kampus   : " << mhs1.kps.namaKampus << endl;
    cout << "Tahun Berdiri : " << mhs1.kps.TB << endl;
    cout << endl;
    cout << "NPM Mahasiswa : " << mhs2.npm << endl;
    cout << "Nama Mahasiswa: " << mhs2.nama << endl;
    cout << "Jurusan       : " << mhs2.jurusan << endl;
    cout << "Usia          : " << mhs2.usia << endl;
    cout << "Hobi 1        : " << mhs2.hobi[0] << endl;
    cout << "Hobi 2        : " << mhs2.hobi[1] << endl;
    cout << "Nama Kampus   : " << mhs2.kps.namaKampus << endl;
    cout << "Tahun Berdiri : " << mhs2.kps.TB << endl;
    cout << endl;
    cout << "NPM Mahasiswa : " << mhs3.npm << endl;
    cout << "Nama Mahasiswa: " << mhs3.nama << endl;
    cout << "Jurusan       : " << mhs3.jurusan << endl;
    cout << "Usia          : " << mhs3.usia << endl;
    cout << "Hobi 1        : " << mhs3.hobi[0] << endl;
    cout << "Hobi 2        : " << mhs3.hobi[1] << endl;
    cout << "Nama Kampus   : " << mhs3.kps.namaKampus << endl;
    cout << "Tahun Berdiri : " << mhs3.kps.TB << endl;
    cout << endl;
    cout << "Hobi 1        : " << mhs4[0].hobi[0] << endl;
    cout << "Hobi 2        : " << mhs4[1].hobi[0] << endl;
    cout << endl;
    cout << "Hobi 1        : " << mhs5[0].hobi[0] << endl;
    cout << "Hobi 2        : " << mhs5[1].hobi[0] << endl;
    return 0;
}
