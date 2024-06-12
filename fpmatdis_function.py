# def flood_fill(matrix, i, j):
#     if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0:
#         return 0
#     matrix[i][j] = 0
#     size = 1

#     size += flood_fill(matrix, i+1, j)
#     size += flood_fill(matrix, i-1, j)
#     size += flood_fill(matrix, i, j+1)
#     size += flood_fill(matrix, i, j-1)

#     return size

def dfs(grid, i, j, old_color, new_color):
    n = len(grid)
    m = len(grid[0])
    if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != old_color:
        return
    else:
        grid[i][j] = new_color
        dfs(grid, i+1, j, old_color, new_color)
        dfs(grid, i-1, j, old_color, new_color)
        dfs(grid, i, j+1, old_color, new_color)
        dfs(grid, i, j-1, old_color, new_color)

def flood_fill(grid, i, j, new_color):
    old_color = grid[i][j]
    if old_color == new_color:
        return
    dfs(grid, i, j, old_color, new_color)

def cari_terdekat(matriks, posisi):
    jarak_min = float('inf')
    posisi_terdekat = None

    for i in range(len(matriks)):
        for j in range(len(matriks[i])):
            if matriks[i][j] == 1:
                jarak = abs(posisi[0] - i) + abs(posisi[1] - j)
                if jarak < jarak_min:
                    jarak_min = jarak
                    posisi_terdekat = [i, j]

    return posisi_terdekat

def heuristic(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

jumlahPulau = []
pulau = []

# Input
N, M = map(int, input().split())

for i in range(N):
    newInput = list(map(int, input().split()))
    pulau.append(newInput)

X, Y = map(int, input().split())

# jarak = []
# print("p", heuristic([4, 2], [2, 1]))
# print(pulau)

# posisi = cari_terdekat(pulau, [4, 2])
# print("l", posisi)
# print("k", heuristic([4, 2], posisi))
    
# posisi = cari_terdekat(pulau, [Y, X])
# for i in range(len(pulau)):
#     for j in range(len(pulau[0])):
#         print(pulau[i][j], end=" ")
#     print()
# print()
# flood_fill(pulau, posisi[0], posisi[1], 0)
# for i in range(len(pulau)):
#     for j in range(len(pulau[0])):
#         print(pulau[i][j], end=" ")
#     print()
# print()

jarak_list = []


for i in range(len(pulau)):
    for j in range(len(pulau[0])):
        if pulau[i][j] == 1:
            posisi = cari_terdekat(pulau, [Y, X])
            jarak = heuristic([Y, X], posisi)
            jarak_list.append(jarak)
            flood_fill(pulau, posisi[0], posisi[1], 0)

print(jarak_list)


# for i in range(len(pulau)):
#     for j in range(len(pulau[i])):
#         if pulau[i][j] == 1:
#             jumlahPulau.append(flood_fill(pulau, i, j))

# print(f"Banyak Pulau: {len(jumlahPulau)}")
# print(f"Luas Pulau: {' '.join(str(x) for x in jumlahPulau)}")

