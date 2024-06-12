import json

with open('data.json') as f:
    data = json.load(f)
# print(data["manajemen_stok"])
array = data["transaksi"]

print(array)

# array = [{'id': 1, 'nama': "Budi"}, {'id': 2, 'nama': "Rama"}]
# nested_array = [[d['id'], d['nama'], d['jenis'], d['habitat'], d['bayi'], d['remaja'], d['dewasa'], d['harga_kg'], d['terjual']] for d in array]
# nested_array = [[d['id'], d['nama'], d['terjual']] for d in array]

# print("awal", nested_array)

# # memodifikasi data JSON
# for d in array:
#     if d['id'] == 'h8130431':
#         d['terjual'] = 950

# # menulis kembali ke file JSON
# with open('data.json', 'w') as f:
#     json.dump(array, f)