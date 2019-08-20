fact = [1 for _ in range(31)]
for i in range(1, 31):
    fact[i] = fact[i - 1] * i

for ro in range(int(input())):
    N = int(input())
    case = N // 20

    casenumber = 0

    for twenty in range(case + 1):
        ten = (N - 20 * twenty) // 10

        casenumber += (2 ** twenty) * fact[ten + twenty] // (fact[twenty] * fact[ten]) 
    
    print('#%d %d' %(ro + 1, casenumber))
