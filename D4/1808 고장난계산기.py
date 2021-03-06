primenumbers = [True, True, False] + [False] * 999999
for num in range(2, 500002):
    if primenumbers[num]:
        continue

    for bae in range(2 * num, 1000002, num):
        primenumbers[bae] = True

def counting(num):
    if cache.get(num) != None:
        return cache[num]

    for letter in str(num):
        if not nums[int(letter)]:
            if not primenumbers[num]:
                cache[num] = False
                return False
            else:
                min_count = 999
                temp = findyaksu(num)
                for su1, su2 in temp:
                    su1_result = counting(su1)
                    su2_result = counting(su2)

                    if not su1_result:
                        cache[su1] = False
                        continue
                    if not su2_result:
                        cache[su2] = False
                        continue
                    else:
                        min_count = min(min_count, su1_result + su2_result + 1)
                return min_count
    
    res = len(str(num))
    cache[num] = res
    return res
    
def findyaksu(num):
    result = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            result.append((i, num // i))

    return result

for ro in range(int(input())):
    nums = list(map(int,input().split()))
    gaol_num = int(input())
    cache = dict()
    res = counting(gaol_num) + 1
    if res == 1000:
        res = -1
    print('#%d %d' %(ro + 1, res))
