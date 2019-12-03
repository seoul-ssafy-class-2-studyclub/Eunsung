N, P = map(int,input().split())

knows = list(map(int,input().split()))

# parties = [0] * (P + 1)
parties = [[] for _ in range(P + 1)]
checked = [False] * (N + 1)
people = [[] for _ in range(N + 1)]
max_cnt = P
cant_party = [False] * (P + 1)

for party in range(P):
    party_info = list(map(int,input().split()))
    party_length = party_info[0]
    for idx in range(1, party_length + 1):
        parties[party].append(party_info[idx])
        people[party_info[idx]].append(party)

queue = []
if len(knows) != 1:
    queue = knows[1:]

while queue:
    person = queue.pop(0)
    for party in people[person]:
        if cant_party[party]:
            continue
        cant_party[party] = True
        max_cnt -= 1
        for comed in parties[party]:
            if checked[comed]:
                continue
            checked[comed] = True
            queue.append(comed)

print(max_cnt)