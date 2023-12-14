#include <iostream>
using namespace std;

int binarySearch(int sortedArr[], int size, int key)
{
    int left = 0;
    int right = size - 1;

    while (left <= right)
    {
        int mid = (right + left) / 2;

        if (sortedArr[mid] == key)
        {
            return mid; // Elemen ditemukan
        }
        else if (key > sortedArr[mid])
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }

    return -1; // Elemen tidak ditemukan
}

int main()
{
    int arr[] = {1, 9, 8, 2, 0, 2, 1, 1, 2, 0, 2, 1, 2, 1, 2, 0, 0, 5};
    int sortedArr[] = {0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 5, 8, 9};
    int size = 18;
    int key;

    cout << "Masukkan angka yang ingin dicari : ";
    cin >> key;

    int result = binarySearch(sortedArr, size, key);

    if (result != -1)
    {
        cout << "Elemen " << key << " ditemukan pada indeks ke-" << result << endl;
    }
    else
    {
        cout << "Elemen " << key << " tidak ditemukan dalam array." << endl;
    }

    return 0;
}
