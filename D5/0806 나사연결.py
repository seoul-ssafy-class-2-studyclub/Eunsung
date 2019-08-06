# import sys
# from pprint import pprint
# sys.stdin = open('input.txt', 'r')

def ambasubasa(result_list, su, am):
    #이미 들어와있으므로 False로 들어왔다는 표시를 해준다
    graph[su][am] = False

    #현재 나사를 조합에 추가해줘야하지만, 만약 체크포인트상태로 들어온거라면 두번입력되므로 그 상황에 대해서 걸러주고
    if not (su, am) in result_list:
        result_list.append((su, am))
    
    #길이를 저장해준다(할필요없다.)
    length = len(result_list)

    #길이가 전체와 같다면 굳이 더할필요가 없으므로 반환
    if length == N:
        return result_list
    
    #암나사와 같은 지름의 숫나사가 있다면 그리로 간다. 이때 다시 돌아올 수 있도록 체크포인트 가장 끝에 저장해준다.
    for i in range(max_length + 2):
        if graph[am][i]:
            graph[am][i] = False
            checkpoint.append((su, am))
            return ambasubasa(result_list, am, i)
    
    #만약 같은 지름의 숫나사가 없다면 체크포인트로 돌아가야하는데

    #체크포인트가 없다면 결과 반환
    if not checkpoint:
        return result_list

    #체크포인트가 있다면 그곳으로 최신 체크포인트로 돌아가기위하여 삭제하고 체크포인트를 저장해둔다
    x = checkpoint.pop()

    #그리고 체크포인트로 돌아간 후와 현재 무엇이 더 긴지 판단해야 하므로 현재 상태를 저장해두고
    temp = result_list[:]

    #체크포인트로 돌아가면 지금 들어온 곳은 필요없으니 삭제. 2,3개의 체크포인트를 되돌아가는경우에도 마찬가지로 삭제된다.
    result_list.pop()
    #그리고 직전 체크포인트로 돌아가 다시 한번 돈다.
    result_list = ambasubasa(result_list, x[0], x[1])

    #체크포인트로 돌아간 상태와 현재를 비교해서 더 긴쪽을 반환한다
    if len(result_list) > len(temp):
        return result_list

    return temp


result_list = []
for round in range(int(input())):
    N = int(input())
    bolt_list = list(map(int,input().split()))
    bolts = []

    #가장 넓은 암나사와 숫나사를 저장해주면서 볼트의 암나사 숫나사를 튜플형식으로 저장한다
    max_ambasa = bolt_list[1]
    max_subasa = bolt_list[0]
    
    if max_subasa > max_ambasa:
        max_length = max_subasa
    for i in range(N):
        bolts.append((bolt_list[i * 2], bolt_list[i * 2 + 1]))
        if max_ambasa < bolt_list[i * 2 + 1]:
            max_ambasa = bolt_list[i * 2 + 1]
        if max_subasa < bolt_list[i * 2]:
            max_subasa = bolt_list[i * 2]

    #그래프를 만들기위하여 암나사와 숫나사중 가장 긴 것을 저장한다.
    max_length = max(max_ambasa, max_subasa)
    
    #그리고 최대 길이를 정사각형으로 갖는 그래프를 만든다(인덱스가 지름이 되도록 0줄을 추가한다/)
    graph = [[False] * (max_length + 2) for _ in range(max_length + 2)]
    max_result = []

    #시작나사를 무얼하느냐에따라 길이가 달라지므로 모든 시작나사에 대해서 조사한다.
    for i in range(N):

        #함수가 한번돌면 그래프가 바뀌므로 초기화하여주고
        for j in range(N):
            graph[bolts[j][0]][bolts[j][1]] = True
        
        #체크포인트도 초기화해준다.
        checkpoint = []

        #해당 나사를 시작으로 하였을때 나사조합을 구하고 저장해둔다.
        temp_result = ambasubasa([],bolts[i][0],bolts[i][1])

        #가장 긴것을 구한다.
        if len(max_result) < len(temp_result):
            max_result = temp_result

    #가장 긴 조합을 추출한다
    result = []
    for i in range(len(max_result)):
        max_result[i] = list(map(str,max_result[i]))
        result.append(' '.join(max_result[i]))

    result_list.append('#%d %s' %(round + 1, ' '.join(result)))


for value in result_list:
    print(value)