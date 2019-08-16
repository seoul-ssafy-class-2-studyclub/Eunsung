row, col = map(int,input().split())
N = int(input())
square = row * col

row_points = []
col_points = []
for i in range(N):
    A, B = map(int,input().split())
    if A:
        row_points.append(B)
    else:
        col_points.append(B)
col_points.sort()
row_points.sort()
col_points.insert(0, 0)
col_points.append(col)
row_points.insert(0, 0)
row_points.append(row)

max_row = 0
max_col = 0
for i in range(1, len(col_points)):
    temp = col_points[i] - col_points[i - 1]
    if max_col < temp:
        max_col = temp

for i in range(1, len(row_points)):
    temp = row_points[i] - row_points[i - 1]
    if max_row < temp:
        max_row = temp
print(max_col * max_row)