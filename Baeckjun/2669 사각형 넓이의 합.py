import sys
sys.stdin = open('input.txt', 'r')

rectangles = []
for i in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    rectangles.append([(x1, y1), (x2, y2)])

print(rectangles)

