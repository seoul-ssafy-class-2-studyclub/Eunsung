import math
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for test_round in range((int(input()))):
    students, goal_student = map(int,input().split())

    scores = []
    
    for i in range(students):
        students_scores = list(map(int,input().split()))
        scores.append(0.35*students_scores[0]+0.45*students_scores[1]+0.2*students_scores[2])
        if i == goal_student - 1:
            goal_score = scores[i]
    
    scores = sorted(scores, reverse = True)
        
    deung = scores.index(goal_score) + 1
    each_grade = students / 10
    grade = grades[math.ceil(deung / each_grade)-1]

    
            
    print(f'#{test_round + 1} {grade}')