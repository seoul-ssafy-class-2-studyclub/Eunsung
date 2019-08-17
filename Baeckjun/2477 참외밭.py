cham = int(input())

bat = {
    1:0,
    2:0,
    3:0,
    4:0,
    }
bang = []
le = []

for i in range(6):
    see, length = map(int,input().split())
    bat[see] += length
    bang.append(see)
    le.append(length)


# if bang[0]==bang[2]:
#     minus = le[1]*le[2]
# elif bang[0]==bang[4]:
#     minus = le[0]*le[5]
# else:
#     minus = le[3]*le[4]
print(bat)
print(cham*(bat[1]*bat[3] - minus))

