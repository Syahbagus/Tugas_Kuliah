#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int menu()
{
    int input;

    system("cls");
    cout << "\nProgram Data Mahasiswa" << endl;
    cout << "========================" << endl;
    cout << "1. Tambah data Mahasiswa" << endl;
    cout << "2. Tampilkan data Mahasiswa" << endl;
    cout << "3. Cari data Mahasiswa" << endl;
    cout << "4. Keluar" << endl;
    cout << "========================" << endl;
    cout << "Pilihan (1/2/3/4) : ";
    cin >> input;
    return input;
}

int main()
{
    char is_continue;
    int pilihan = menu();

    // Menandai switch case agar mudah dibaca
    enum option
    {
        ADD = 1,
        SHOW,
        FIND,
        FINISH
    };
    while (pilihan != FINISH)
    {
        switch (pilihan)
        {
        case ADD:
            cout << "Menambah data Mahasiswa" << endl;
            break;
        case SHOW:
            cout << "Menampilkan data Mahasiswa" << endl;
            break;
        case FIND:
            cout << "Mencari data Mahasiswa" << endl;
            break;
        default:
            cout << "Pilihan tidak valid" << endl;
            break;
        }

        // Sistem untuk melanjutkan program atau tidak
    label_continue:
        cout << "Lanjutkan?(y/n) : ";
        cin >> is_continue;
        if (is_continue == 'y' || is_continue == 'Y')
        {
            pilihan = menu();
        }
        else if (is_continue == 'N' || is_continue == 'n')
            break;
        else
        {
            goto label_continue; // Agar user menginput kembali (y/n)
        }
    }
    cout << "Akhir dari program";

    return 0;
}
