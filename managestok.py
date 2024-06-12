import os
import json
from tabulate import tabulate
import uuid

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
                if left_list[0][i] < right_list[0][i]:
                    sorted_list.append(left_list[0])
                    left_list.pop(0)
                    break
                elif left_list[0][i] > right_list[0][i]:
                    sorted_list.append(right_list[0])
                    right_list.pop(0)
                    break
            elif order[i] == 'desc':
                if left_list[0][i] > right_list[0][i]:
                    sorted_list.append(left_list[0])
                    left_list.pop(0)
                    break
                elif left_list[0][i] < right_list[0][i]:
                    sorted_list.append(right_list[0])
                    right_list.pop(0)
                    break
        if len(sorted_list) == len(left_list) + len(right_list):
            break
    while left_list:
        sorted_list.append(left_list[0])
        left_list.pop(0)
    while right_list:
        sorted_list.append(right_list[0])
        right_list.pop(0)
    return sorted_list

# with open('data.json') as f:
#     data = json.load(f)
# # print(data["manajemen_stok"])
# manage_list = data["manajemen_stok"]
# menu_keys = [key for key in manage_list[0].keys()]
# # print(menu_keys)
# newDict = {}
# newDict["id"] = "123214"
# print(type(newDict))
# angka = [0, 1, 2, 3, 4, 5]
# for i in range(len(angka)-1, -1, -1):
#     print(angka[i])

# apakek = input("Masukkan inputan : ").split()
print(str(uuid.uuid4())[:10])



# manage_items = [[d['id'], d['nama'], d['jenis'], d['habitat'], d['bayi'], d['remaja'], d['dewasa'], d['harga_kg'], d['terjual']] for d in manage_list]
# # print(manage_items)
# head = [f"id", f"nama", f"jenis", f"habitat", f"bayi", f"remaja", f"dewasa", f"harga kg", f"terjual"]
# print(tabulate(manage_items, headers=head, tablefmt="grid"))

# order = []
# priority = []
# for i in range(len(manage_items[0])):
#     order.append('asc')
# for i in range(len(manage_items[0])):
#     priority.append(i)

# manage_sort = merge_sort(manage_items, order, priority)
# print(tabulate(manage_sort, headers=head, tablefmt="grid"))

# open = True
# while open:
#     # sorted = merge_sort(menu, order, priority)
#     print("=====================")
#     print("========[Menu]=======")
#     print("1. Tampilkan data")
#     print("2. Input data baru")
#     print("3. Ubah nilai tententu")
#     print("4. Lihat transaksi")
#     print("5. Catat transaksi baru")
#     print("x. Keluar")
#     print("=====================")
#     print("=====================")

#     select_menu = int(input("Pilih : "))
#     os.system('cls' if os.name == 'nt' else 'clear')

#     if select_menu == 1:
#         # print(tabulate(sorted, headers=head, tablefmt="grid"))
#         print("=====================")
#         print("=======[Pilih]=======")
#         for i in range(len(menu_keys)):
#             print(f"{i}. {menu_keys[i]}")
#         print("x. Keluar")
#         print("=====================")
#         print("=====================")


#         select_back = input("Back? (y/n) > ")
#         if select_back == 'y':
#             os.system('cls' if os.name == 'nt' else 'clear')
#             continue
#         else:
#             open = False
#     elif select_menu == 2:
#         print("[ input baru ]")
#         nama = input("Nama ikan : ")
#         harga = int(input("Harga : "))
#         stok = int(input("Stok : "))
#         newInput = [nama, harga, stok]
#         menu.append(newInput)
#         # print(menu)

#         select_back = input("Back? (y/n) > ")
#         if select_back == 'y':
#             os.system('cls' if os.name == 'nt' else 'clear')
#             continue
#         else:
#             open = False
#     else:
#         open = False
