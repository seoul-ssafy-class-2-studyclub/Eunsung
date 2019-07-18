T = int(input())

for i in range(T):
    count = 0 #패턴의글자수
    words = list(input()) 
    for l in range(1,len(words)):
        if words[0] == words[l] and words[0:l-1] == words[l:2*l-1]: #처음글자가 다시 나오면서, 그 사이의 글자와 앞으로 나올 글자들이 같다면
            count = l #패턴의 글자수 확정
            break

    print(f&apos;#{i+1} {count}&apos;)