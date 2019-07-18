def decoding(encoded):
    for k in range(len(encoded)):
        encoded[k] = format(encoding_table[encoded[k]],'b').zfill(6)

    encoded = ''.join(encoded)
    new_encoded = []
    bi_num = 0
    bi_y = -1

    while bi_num < len(encoded):
        if bi_num % 8 == 0:
            bi_y += 1
            new_encoded.append([])
            new_encoded[bi_y].append(encoded[bi_num])
        else:
            new_encoded[bi_y].append(encoded[bi_num])
        bi_num += 1

    for i in range(bi_y+1):
        new_encoded[i] = ''.join(new_encoded[i])
        new_encoded[i] = chr(int(new_encoded[i], base=2))
    
    return new_encoded


encoding_table = dict()
num = 0

for i in range(ord('A'), ord('Z')+1):
    encoding_table[chr(i)] = num
    num += 1
for i in range(ord('a'), ord('z')+1):
    encoding_table[chr(i)] = num
    num += 1
for i in range(ord('0'), ord('9')+1):
    encoding_table[chr(i)] = num
    num += 1
encoding_table['+'] = num
encoding_table['/'] = num +1

for rounds in range(int(input())):
    
    encoded = list(input())
    decoded = decoding(encoded)

    print(f'#{rounds + 1} '+''.join(decoded))

