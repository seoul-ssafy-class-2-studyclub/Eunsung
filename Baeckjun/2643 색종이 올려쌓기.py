N  = int(input())
papers = []
for _ in range(N):
    w, h = map(int,input().split())
    
    if h > w:
        w, h = h, w
    
    papers.append((w, h))
papers.sort(key=lambda x: x[1], reverse=True)
papers.sort(key=lambda x: x[0], reverse=True)
count = [1 for _ in range(N)]

for i in range(1, N):
    temp = 0
    for j in range(i):
        # print(papers[i], papers[j])
        if papers[i][1] <= papers[j][1]:
            if count[j] > temp:
                temp = count[j]
    count[i] = temp + 1
print(max(count))


