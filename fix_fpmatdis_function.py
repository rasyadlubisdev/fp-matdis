# Fungsi floodfill menggunakan pendekatan algoritma DFS
def floodfill(grid, i, j, old_color, new_color):
    n = len(grid)
    m = len(grid[0])
    if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != old_color:
        return 0
    else:
        # Ini untuk mengubah target tujuan menjadi apa yang ingin diubah, contoh : angka 1 menjadi 2
        grid[i][j] = new_color
        # Count untuk menghitung berapa banyak angka dalam satu kali penjalanan floodfill di program utama (menghitung banyaknya area di setiap pulau)
        count = 1
        count += floodfill(grid, i+1, j, old_color, new_color)
        count += floodfill(grid, i-1, j, old_color, new_color)
        count += floodfill(grid, i, j+1, old_color, new_color)
        count += floodfill(grid, i, j-1, old_color, new_color)
        return count

# Biasa dikenal dengan rumus Manhattan, untuk menghitung berapa banyak langkah dari titik Start ke titik Finish
def heuristic(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])
# Menggunakan looping dan fungsi heuristic untuk menemukan posisi dari target yang paling dekat dari suatu titik tertentu
def cari_terdekat(grid, posisi, target_color):
    jarak_min = float('inf')
    posisi_terdekat = None

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == target_color:
                jarak = heuristic(posisi, [i, j])
                if jarak < jarak_min:
                    jarak_min = jarak
                    posisi_terdekat = [i, j]

    return posisi_terdekat


area = []
pulau_list = []
jarak_list = []
# Input baris (N) dan kolom (M) dari suatu matriks
# Contoh : 5 5
N, M = map(int, input().split())
# Input angka dari setiap baris. 1 untuk pulau, 0 untuk laut
# Contoh :
# 1 1 0 1 0
# 0 1 1 0 0
# 0 1 0 0 1
# 0 0 0 0 1
# 1 1 1 0 1
for i in range(N):
    newInput = list(map(int, input().split()))
    area.append(newInput)
# Input koordinat titik tertentu
# Contoh : 4 2
X, Y = map(int, input().split())
# Melakukan loop untuk menjalankan fungsi floodfill, cari_terdkeat, heuristic dari setiap baris dan kolom (yang memuat angka 1)
for i in range(N):
    for j in range(M):
        if area[i][j] == 1:
            pulau_list.append(floodfill(area, i, j, 1, 2))
            posisi = cari_terdekat(area, [Y, X], 2)
            jarak = heuristic([Y, X], posisi)
            jarak_list.append(jarak)
            floodfill(area, i, j, 2, 3)
# Diurutkan dari jarak yang paling dekat dahulu dari titik terntetu, kemudian dari ukuran area yang terbesar
order_island = [x + 1 for x in range(len(pulau_list))]
island_data = list(zip(order_island, jarak_list, pulau_list))
island_data.sort(key=lambda x: (x[1], -x[2]))
# Print hasil dari sortir tersebut
for i in range(len(island_data)):
    print(f"Island {island_data[i][0]} (Distance: {island_data[i][1]}, Area: {island_data[i][2]})")
