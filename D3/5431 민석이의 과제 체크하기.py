for rounds in range(int(input())):
    n, k = input().split()
    
    students = list(map(str,range(1,int(n)+1)))
    
    submited = list(input().split())

    for i in range(int(k)):
        students.pop(students.index(submited[i]))

    print(f'#{rounds + 1}', ' '.join(students))