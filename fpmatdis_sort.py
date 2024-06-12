# MOHON MAAF BU, BATAS UPLOAD FILE MAKSIMAL 2
# UNTUK FILE JSON BISA DI AKSES LEWAT : https://drive.google.com/drive/folders/1kIx3Nir_sdjDN8z4yL6uSrUEr_BQOSCR?usp=sharing
# TERIMA KASIH BU DINI ^^

import os
import json
from tabulate import tabulate
import uuid

# Fungsi merge sort dan merge dengan parameter list, order, priority
# List adalah datanya
# Order memakai tipe data list, untuk menentukan kolom akan diurutkan secara 'asc' atau 'desc'
# Priority memakai tipe data list, untuk menentukan kolom mana yang akan diprioritaskan dalam sortir
def merge_sort(lst, order, priority):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_list = merge_sort(lst[:mid], order, priority)
    right_list = merge_sort(lst[mid:], order, priority)
    return merge(left_list, right_list, order, priority)

def merge(left_list, right_list, order, priority):
    sorted_list = []
    while left_list and right_list:
        for i in priority:
            if order[i] == 'asc':
                if left_list[0][i] <= right_list[0][i]:
                    sorted_list.append(left_list[0])
                    left_list.pop(0)
                    break
                elif left_list[0][i] >= right_list[0][i]:
                    sorted_list.append(right_list[0])
                    right_list.pop(0)
                    break
            elif order[i] == 'desc':
                if left_list[0][i] >= right_list[0][i]:
                    sorted_list.append(left_list[0])
                    left_list.pop(0)
                    break
                elif left_list[0][i] <= right_list[0][i]:
                    sorted_list.append(right_list[0])
                    right_list.pop(0)
                    break
        if not left_list or not right_list:
            break
    sorted_list += left_list + right_list
    return sorted_list

# Membuat dictionary in list menjadi list in list
with open('data.json') as f:
    manage_list = json.load(f)
manage_keys = [key for key in manage_list[0].keys()]

# Membuat looping untuk program agar berjalan layaknya aplikasi sederhana
running = True
while running:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=====================")
    print("========[Menu]=======")
    print("1. Tampilkan data")
    print("2. Input data baru")
    print("3. Ubah nilai tententu")
    print("x. Close")
    print("=====================")
    print("=====================")

    select_menu = input("Pilih : ")
    os.system('cls' if os.name == 'nt' else 'clear')

    # Mengakses fitur utama (lihat dan sortir data)
    if select_menu == '1':
        print("=====================")
        print("========[View]=======")
        print("1. Tampilkan semua")
        for key in manage_keys:
            print(f"> {key}")
        print("x. Back")
        print("=====================")
        print("=====================")
        select_view = input("Pilih > ").split()

        # Update data dibagian kolom "pendapatan"
        for data in manage_list:
            data['pendapatan'] = data['harga_satuan'] * data['banyak_terjual']
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(manage_list, f, ensure_ascii=False, indent=4)

        # Tampilkan semua kolom
        if select_view[0] == '1':
            head = [key for key in manage_keys]
            select_view = head
            manage_items = [[d[key] for key in manage_keys] for d in manage_list]
        # Kembali ke menu utama
        elif select_view[0] == 'x':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        # Tampilkan kolom terpilih
        else:
            head = select_view
            manage_items = [[d[key] for key in select_view] for d in manage_list]
        order = []
        priority = []
        # Membuat order dan priority secara default
        for i in range(len(manage_items[0])):
            order.append('asc')
            priority.append(i)
        
        # Menentukan kolom mana yang mau diprioritaskan (priority)
        select_priority = input("Order by > ").split()
        for i in range(len(select_priority)-1, -1, -1):
            get_index_item = select_view.index(select_priority[i])
            priority.remove(get_index_item)
            priority.insert(0, get_index_item)

        # Menentukan kolom mana yang diorder secara 'desc'
        select_order = input("Descendent > ").split()
        for i in range(len(select_order)):
            get_index_item = select_view.index(select_order[i])
            order[get_index_item] = 'desc'
        # Melakukan merge sort dan diprint berbentuk tabel
        manage_sort = merge_sort(manage_items, order, priority)
        print(tabulate(manage_sort, headers=head, tablefmt="grid"))
        # Apakah akan kembali ke menu utama atau ingin keluar dari program
        select_back = input("Back/Close? (y/n) > ")
        if select_back == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            running = False

    # Fitur kedua (input data)
    elif select_menu == '2':
        print("=====================")
        print("=====[Input Baru]====")
        newInput = {}
        # ID akan dibuat secara otomatis dan memiliki value yang unik
        newInput["id"] = str(uuid.uuid4())[:10]
        # Input setiap key atau kolom
        newInput["nama"] = input("Input nama : ")
        newInput["jenis"] = input("Input jenis : ")
        newInput["habitat"] = input("Input habitat : ")
        newInput["bayi"] = int(input("Input bayi : "))
        newInput["remaja"] = int(input("Input remaja : "))
        newInput["dewasa"] = int(input("Input dewasa : "))
        newInput["harga_satuan"] = int(input("Input harga per satuan : "))
        newInput["banyak_terjual"] = int(input("Input banyak_terjual : "))
        # Konfirmasi, jika input data sudah yakin maka akan dilanjutkan ke proses write JSON file
        select_confirm = input("Apakah anda sudah yakin? (y/n) > ")
        if select_confirm == 'y':
            manage_list.append(newInput)
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(manage_list, f, ensure_ascii=False, indent=4)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        # Ingin kembali ke menu utama atau langsung keluar dari programnya
        select_back = input("Back/Close? (y/n) > ")
        if select_back == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            running = False
    # Fitur ketiga (ubah data)
    elif select_menu == '3':
        print("=====================")
        print("========[Ubah]=======")
        # Select id yang ada dari database (JSON file)
        select_id = input("Input id : ")
        # Melakukan looping untuk mencari data dengan ID tersebut, lalu mengubah kolom tertentu dengan value yang dimasukkan
        for i in manage_list:
            if i['id'] == select_id:
                want_change = True
                while True:
                    key_change = input("Ubah kolom : ")
                    if (key_change == 'bayi' or key_change == 'remaja' or key_change == 'dewasa' or key_change == 'harga_satuan' or key_change == 'banyak_terjual') and not key_change == 'pendapatan':
                        i[key_change] = int(input("Masukkan nilai : "))
                    else:
                        i[key_change] = input("Masukkan nilai : ")
                    with open('data.json', 'w', encoding='utf-8') as f:
                        json.dump(manage_list, f, ensure_ascii=False, indent=4)
                    # Jika masih ingin mengubah data di ID yang sama, maka masih berlanjut di while loop. Jika tidak, maka bisa kembagi ke menu utama
                    select_confirm = input("Ingin mengubah lagi? (y/n) ")
                    if select_confirm == 'y':
                        continue
                    else:
                        break
        # Apakah ingin kembali ke menu utama atau keluar dari program
        select_back = input("Back/Close? (y/n) > ")
        if select_back == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            running = False
    else:
        running = False
