result = []
for rounds in range(int(input())):
    horn, animal = map(int,input().split())

    twinhorn = horn - animal
    unicorn = animal - twinhorn
    

    result.append(f'#{rounds + 1} {unicorn} {twinhorn}')

for value in result:
    print(value)