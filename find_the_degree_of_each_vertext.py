matrix = [[0,1,1],[1,0,1],[1,1,0]]
degree = []
for i in matrix:
    degree.append(sum(i))

print(degree)