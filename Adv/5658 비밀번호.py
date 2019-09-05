class Node():

    def __init__(self, value, nxt):
        self.value = value
        self.nxt = nxt
        return

for ro in range(int(input())):
    N, K = map(int,input().split())
    hexas = input()

    temp = Node(hexas[-1], None)
    last = temp

    for i in range(N - 2, -1, -1):
        temp = Node(hexas[i], temp)
    head = temp
    last.nxt = head

    results = []

    for _ in range(N // 4):
        head = head.nxt

        p = head
        temp = []
        for i in range(N):
            if i % (N // 4) == (N // 4) - 1:
                temp.append(p.value)
                results.append(temp)
                temp = []

            else:
                temp.append(p.value)
            p = p.nxt
    tens = []
    for arr in results:
        temp = ''.join(arr)
        num = int(temp, 16)
        if not num in tens:
            tens.append(num)

    tens.sort(reverse=True)
    print('#%d %d' %(ro + 1, tens[K - 1]))

