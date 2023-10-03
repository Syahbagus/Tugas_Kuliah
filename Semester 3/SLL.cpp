#include <iostream>
using namespace std;

struct Mahasiswa{
    string nama, npm;
    int usia;
    Mahasiswa *next;
};

Mahasiswa *head, *tail, *cur, *newNode;

void create(string nama, string npm, int usia){
    head = new Mahasiswa();
    head->nama = nama;
    head->npm = npm;
    head->usia = usia;
    head->next=NULL;
    tail = head;
}
void addFirst(string nama, string npm, int usia){
    newNode = new Mahasiswa();
    newNode->nama = nama;
    newNode->npm = npm;
    newNode->usia = usia;
    newNode->next=head;
    head = newNode;
}
void addLast(string nama, string npm, int usia){
    newNode = new Mahasiswa();
    newNode->nama = nama;
    newNode->npm = npm;
    newNode->usia = usia;
    newNode->next=NULL;
    tail->next = newNode;
    tail = newNode;
}

void view(){
    cur = head;
    while(cur != NULL){
        cout << "Nama Mahasiswa : " << cur->nama << endl;
        cout << "NPM Mahasiswa  : " << cur->npm << endl;
        cout << "Usia Mahasiswa : " << cur->usia << endl;
        cur = cur->next;
    }
}


int main() {
    create("Yusron", "22081010255", 19);
    cout << "\n";
    view();
    addFirst("Hana", "22081010256", 20);
    cout << "\n";
    view();
    addLast("Yuna", "22081010257", 18);
    cout << "\n";
    view();

    return 0;
}




