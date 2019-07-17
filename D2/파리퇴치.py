for test_case in range(int(input())):
    
    #파리의 마리수를 보드로 만들자!
    board = []
    size, parichae = list(map(int,input().split())) #size = 보드의크기, parichae 파리채의크기
    for o in range(size):
        board.append(list(map(int,input().split())))

    catch = [] #파리채로 친 구간들의 결과 모음 ex [[13마리 12마리 11마리 11마리], [11마리 12마리 11마리 10마리] ...]

    setting = [] #파리채 왼쪽 위(시작부분)의 좌표모음ex [(0,0),(0,1),(1,0),(1,1)]
    for i in range(size - parichae + 1): # 파리채 시작부분의 y좌표모음
        for j in range(size - parichae + 1): #파리채 시작부분의 x좌표모음
            setting.append((i,j)) #파리채 시작부분의 좌표모음

    parichae_size = [] #파리채가 닿는 범위 ex [(0,0),(0,1),(1,0),(1,1)]
    for i in range(parichae): #파리채가 닿는 범위의 y좌표모음
        for j in range(parichae):
            parichae_size.append((i,j))

    #각 시작부분에서 파리채를 휘둘러 잡은 갯수를 세어 catch에 넣어보자
    catch_rounds = 0 #파리채를 휘두른 경우의수
    for y, x in setting:
        catch.append([])#한번 휘둘러서 잡은 파리의 개수를 적을 공간을 만들고
        
        for parichae_y, parichae_x in parichae_size:
            catch[catch_rounds].append(board[y + parichae_y][x + parichae_x]) #파리채가 닿은 구간에서의 파리마리수를 전부 넣어주자

        catch_rounds += 1  #파리채 휘두른 횟수증가
    

    max_pari = max(list(map(sum,catch))) #잡은 파리수를 다 더하고, 더한값을 모은 리스트에서 최대값을 구하여 가장 많이 잡은 파리수를 찾자
    
    print(f'#{test_case+1} {max_pari}')