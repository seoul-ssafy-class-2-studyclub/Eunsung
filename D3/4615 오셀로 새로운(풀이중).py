

size, rounds = map(int,input().split())

white = {(size // 2 - 1, size //2 - 1),(size // 2, size //2)}
black = {(size // 2, size //2 - 1), (size // 2 - 1, size //2)}

for round in range(rounds):
    y, x, color = map(int,input().split())
    y -= 1
    x -= 1

    if color == 2:
        white.add((x,y))
        white = check_around(white,black,x,y)

        
        
    
    elif color == 1:
        black.add((x,y))

print(white)