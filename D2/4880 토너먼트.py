def jjangambo(a, b):
    if {ga_list[a], ga_list[b]} == {1, 3}:
        return a if ga_list[a] == 1 else b
    elif ga_list[a] == ga_list[b]:
        return a if a < b else b
    else:
        return a if ga_list[a] > ga_list[b] else b

def tonur(arr):
    length = len(arr)
    if length % 2:
        for _ in range(length // 2):
            rounds[-1].append(jjangambo(arr.pop(0), arr.pop(0)))
        rounds[-1].append(arr.pop())
    else:
        for _ in range(length // 2):
            rounds[-1].append(jjangambo(arr.pop(0), arr.pop(0)))


for ro in range(int(input())):
    N = int(input())
    ga_list = list(map(int,input().split()))
    ga_list.insert(0,0)
    players = list(range(1, N + 1))
    rounds = []

    left_queue = players[:(N + 1) // 2]
    right_queue = players[(N + 1) // 2:]

    while True:
        rounds.append([])

        tonur(left_queue)
        tonur(right_queue)

        if len(rounds[-1]) == 2:
            left_queue = rounds[-1]
            right_queue = []
 
        elif len(rounds[-1]) == 1:
            break
        
        else:
            left_queue = list(filter(lambda x: x <= (rounds[-1][0] + rounds[-1][-1]) // 2, rounds[-1]))
            right_queue = list(filter(lambda x: x > (rounds[-1][0] + rounds[-1][-1]) // 2, rounds[-1]))
        print('l', left_queue)
        print('r', right_queue)

    print('#%d %d' %(ro + 1, rounds[-1][0]))


