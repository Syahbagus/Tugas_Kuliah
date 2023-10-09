#include <iostream>
using namespace std;

struct Mahasiswa
{
    string nama, npm;
    int usia;
    Mahasiswa *next;
};

Mahasiswa *head, *tail, *cur, *newNode, *del;

void create(string nama, string npm, int usia)
{
    head = new Mahasiswa();
    head->nama = nama;
    head->npm = npm;
    head->usia = usia;
    head->next = NULL;
    tail = head;
}

void addFirst(string nama, string npm, int usia)
{
    newNode = new Mahasiswa();
    newNode->nama = nama;
    newNode->npm = npm;
    newNode->usia = usia;
    newNode->next = head;
    head = newNode;
}

void addLast(string nama, string npm, int usia)
{
    newNode = new Mahasiswa();
    newNode->nama = nama;
    newNode->npm = npm;
    newNode->usia = usia;
    newNode->next = NULL;
    tail->next = newNode;
    tail = newNode;
}

void changeFirst(string nama, string npm, int usia)
{
    head->nama = nama;
    head->npm = npm;
    head->usia = usia;
}

void changeLast(string nama, string npm, int usia)
{
    tail->nama = nama;
    tail->npm = npm;
    tail->usia = usia;
}

void deleteFirst()
{
    del = head;
    head = head->next;
    delete del;
}

void deleteLast()
{
    del = tail;
    cur = head;
    while (cur->next != tail)
    {
        cur = cur->next;
    }
    tail = cur;
    tail->next = NULL;
    delete del;
}

void view()
{
    cur = head;
    while (cur != NULL)
    {
        cout << "Nama   : " << cur->nama << endl;
        cout << "NPM    : " << cur->npm << endl;
        cout << "Usia   : " << cur->usia << endl;
        cur = cur->next;
    }
}

void addMiddle(string nama, string npm, int usia, int position)
{
    if (position == 1)
    {
        newNode = new Mahasiswa();
        newNode->nama = nama;
        newNode->npm = npm;
        newNode->usia = usia;
        newNode->next = head;
        head = newNode;
    }
    else
    {
        cur = head;
        int i = 1;
        while (cur != NULL && i < position - 1)
        {
            cur = cur->next;
            i++;
        }
        if (cur != NULL)
        {
            newNode = new Mahasiswa();
            newNode->nama = nama;
            newNode->npm = npm;
            newNode->usia = usia;
            newNode->next = cur->next;
            cur->next = newNode;
        }
    }
}

void changeMiddle(string nama, string npm, int usia, int position)
{
    cur = head;
    int i = 1;
    while (cur != NULL && i < position)
    {
        cur = cur->next;
        i++;
    }
    if (cur != NULL)
    {
        cur->nama = nama;
        cur->npm = npm;
        cur->usia = usia;
    }
}

void deleteMiddle(int position)
{
    if (position == 1)
    {
        del = head;
        head = head->next;
        delete del;
    }
    else
    {
        cur = head;
        int i = 1;
        while (cur != NULL && i < position - 1)
        {
            cur = cur->next;
            i++;
        }
        if (cur != NULL && cur->next != NULL)
        {
            del = cur->next;
            cur->next = del->next;
            delete del;
        }
    }
}

int main()
{
    create("Radit", "22081010255", 19);
    view();
    cout << endl;
    addFirst("Nopal", "22081010256", 20);
    view();
    cout << endl;
    addLast("Dhika", "22081010257", 21);
    view();
    cout << endl;
    addMiddle("Ghany", "22081010259", 18, 3);
    view();
    cout << endl;
    changeFirst("Winas", "22081010258", 22);
    view();
    cout << endl;
    changeLast("Sandy", "22081010259", 18);
    view();
    cout << endl;
    changeMiddle("Nopan", "22081010260", 17, 3);
    view();
    cout << endl;
    deleteFirst();
    view();
    cout << endl;
    deleteLast();
    view();
    cout << endl;
    deleteMiddle(2);
    view();
    return 0;
}
