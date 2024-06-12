import os
from tabulate import tabulate

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
    while left_list:
        sorted_list.append(left_list[0])
        left_list.pop(0)
    while right_list:
        sorted_list.append(right_list[0])
        right_list.pop(0)
    return sorted_list

priority = [0]
order = ['desc']
# data = [[90000000], [9000000000], [79120000], [40000000], [8000000], [0], [7200000], [2976000]]
data = [[90000000], [40000000], [79120000], [40000000], [8000000], [0], [7200000], [2976000]]
disortir = merge_sort(data, order, priority)
print(disortir)
disortir_lagi = merge_sort(disortir, order, priority)
print(disortir_lagi)

# menu = [['fried_calamari', 5000, 10], ['fried_rice_seafood', 10000, 10], ['shrimp_platter', 7500, 9], ['roasted_tuna_mackerel', 8000, 10], ['roasted_shrimp', 8000, 8]]
# order = ['asc', 'desc', 'desc']
# priority = [2, 0, 1]  # Prioritas pengurutan: harga, kualitas, nama makanan
# head = [f"nama ikan ({order[0]})", f"harga satuan ({order[1]})", f"stok ({order[2]})"]
# sorted = merge_sort(menu, order, priority)
# # print(merge_sort(menu, order, priority))
# print(tabulate(sorted, headers=head, tablefmt="grid"))
# # os.system('cls' if os.name == 'nt' else 'clear')

# menu = [['h8130431', 'salmon', 'ikan', 'air laut', 1000, 950, 900, 100000, 900, 90000000], ['h13412', 'udang mutiara', 'udang', 'air tawar', 993, 993, 990, 80000, 989, 79120000], ['h942390', 'lele', 'ikan', 'air tawar', 1500, 1500, 2000, 20000, 2000, 40000000], ['h9234', 'mujair', 'ikan', 'air tawar', 900, 500, '400', 20000, 400, 8000000]]
# order = ['asc', 'asc', 'asc', 'asc', 'asc', 'asc', 'asc', 'asc', 'asc', 'asc']
# priority = [6, 0, 1, 2, 3, 4, 5, 7, 8, 9]

# open = True
# while open:
#     sorted = merge_sort(menu, order, priority)
#     print("=====================")
#     print("1. Tampilkan data")
#     print("2. Input data baru")
#     print("3. Exit")
#     print("=====================")

#     select_menu = int(input("Pilih : "))
#     os.system('cls' if os.name == 'nt' else 'clear')

#     if select_menu == 1:
#         print(tabulate(sorted, headers=head, tablefmt="grid"))

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
    

