N  = int(input())
papers = []
for _ in range(N):
    w, h = map(int,input().split())
    
    if h > w:
        w, h = h, w
    
    papers.append((w, h))
print(papers)