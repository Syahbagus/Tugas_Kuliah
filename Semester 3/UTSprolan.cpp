#include <iostream>
using namespace std;

string konversi, idTerendah, idTertinggi;
int x;

struct Responden
{
    string idResponden;
    int skorPengetahuan;
};

string konversiNilai(int skor)
{
    if (skor > 79)
    {
        return "tinggi";
    }
    else if (skor >= 65 && skor <= 79)
    {
        return "Sedang";
    }
    else
    {
        return "Rendah";
    }
}

string cariTerendah(Responden data[])
{
    int skorTerendah = data[0].skorPengetahuan;
    idTerendah = data[0].idResponden;

    for (int i = 1; i < 10; i++)
    {
        if (data[i].skorPengetahuan < skorTerendah)
        {
            skorTerendah = data[i].skorPengetahuan;
            idTerendah = data[i].idResponden;
        }
    }
    return idTerendah;
}

string cariTertinggi(Responden data[])
{
    int skorTertinggi = data[0].skorPengetahuan;
    idTertinggi = data[0].idResponden;

    for (int i = 1; i < 10; i++)
    {
        if (data[i].skorPengetahuan > skorTertinggi)
        {
            skorTertinggi = data[i].skorPengetahuan;
            idTertinggi = data[i].idResponden;
        }
    }

    return idTertinggi;
}

void kategoriTinggi(Responden data[])
{
    cout << "Responden dengan kategori pengetahuan tinggi :" << endl;
    for (int i = 0; i < 10; i++)
    {
        if (konversiNilai(data[i].skorPengetahuan) == "tinggi")
        {
            cout << data[i].idResponden << endl;
        }
    }
}

void rekursifX(Responden data[], int index)
{
    // Base case
    if (index == 10)
    {
        return;
    }

    if (data[index].skorPengetahuan > x)
    {
        cout << data[index].idResponden << " dengan skor : " << data[index].skorPengetahuan << endl;
    }

    rekursifX(data, index + 1);
}

int main()
{
    system("cls");
    cout << "----UTS Pemrograman Lanjut----" << endl;
    cout << "idResponden\t"
         << " skorPengetahuan\t"
         << "Kategori" << endl
         << endl;

    Responden dataResponden[10]{
        {"Aminah", 80},
        {"Badu", 34},
        {"Culun", 56},
        {"Dedi", 78},
        {"Endah", 59},
        {"Fuji", 69},
        {"Genta", 47},
        {"Hamidah", 75},
        {"Indie", 40},
        {"Jony", 90},
    };

    for (int i = 0; i < 10; i++)
    {
        konversi = konversiNilai(dataResponden[i].skorPengetahuan);
        cout << dataResponden[i].idResponden << "\t\t\t" << dataResponden[i].skorPengetahuan << "\t\t" << konversi << endl;
    }

    cout << endl;
    idTerendah = cariTerendah(dataResponden);
    cout << "Responden dengan skor terendah  : " << idTerendah << endl;

    idTertinggi = cariTertinggi(dataResponden);
    cout << "Responden dengan skor tertinggi : " << idTertinggi << endl
         << endl;

    kategoriTinggi(dataResponden);
    cout << endl;

    cout << "Masukkan nilai X : ";
    cin >> x;
    cout << "Responden dengan skor lebih dari " << x << " : " << endl;
    rekursifX(dataResponden, 0);

    return 0;
}
