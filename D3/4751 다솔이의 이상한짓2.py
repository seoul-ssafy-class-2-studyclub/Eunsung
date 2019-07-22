def decoration(letter):
    deco = []
    deco.append('..#..')
    deco.append('.#.#.')
    deco.append('#.'+letter+'.#')
    deco.append('.#.#.')
    deco.append('..#..')
    
    return deco

for rounds in range(int(input())):
    words = list(input())
    result = []
    for i in range(len(words)):
        if i == 0:
            result.append(decoration(words[i]))
        else:
            words[i] = list(zip(*decoration(words[i])))
            words[i].pop(0)
            words[i] = list(map(list,zip(*words[i])))
            for l in range(5):
                words[i][l] = ''.join(words[i][l])
            result.append(words[i])
    result = list(map(list,zip(*result)))
    for i in range(5):
        result[i] = ''.join(result[i])
        print(result[i])




