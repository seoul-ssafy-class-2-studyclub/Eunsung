w, h = map(int,input().split())
x, y = map(int,input().split())
t = int(input())

# t = t % (w * h)
x += t
y += t

x %= 2 * w
y %= 2 * h

if x > w:
    x = 2 * w - x
if y > h:
    y = 2 * h - y


# while not (0 <= x <= w) or not (0 <= y <= h):
#     if y > (-1) * x + h and y >= x + w - h:
#         y = 2 * h - y
    
#     elif y > x and y <= (-1) * x + h:
#         x *= -1
        
#     elif y < (-1) * x + w and y <= x:
#         y *= -1
        
#     else:
#         x = 2 * w - x
        

print(x, y)
