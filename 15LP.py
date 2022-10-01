g = [[1 for i in range(21)] for i in range(21)]

for i in range(1, 21):
    for j in range(1, 21):
        g[i][j] = g[i-1][j] + g[i][j-1]
print(g)