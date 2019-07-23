for rounds in range(int(input())):
    word = list(input())
    number = int(input())
    locations = list(map(int,input().split()))
    witch = []
    for i in range(0,len(word)+1):
        witch.append(locations.count(i))
    for l in range(len(word), -1, -1):
        word.insert(l,'-'*witch[l])
    print(f'#{rounds + 1} {"".join(word)}')
