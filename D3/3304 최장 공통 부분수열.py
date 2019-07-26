def count(arr1, arr2):
    result = []
    for i in range(len(arr1) + 1):

        result.append([])

        for l in range(len(arr2) + 1):

            if i == 0 or l == 0:
                result[i].append(0)
            elif arr1[i - 1] == arr2[l - 1]:
                result[i].append(result[i - 1][l - 1] + 1)
            else:
                result[i].append(max(result[i][l - 1], result[i - 1][l]))
    
    return result[i][l]

for rounds in range(int(input())):
    arr1, arr2 = input().split()

    print(f'#{rounds + 1} {count(arr1, arr2)}')

