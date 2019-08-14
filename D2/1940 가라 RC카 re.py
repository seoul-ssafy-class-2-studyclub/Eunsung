for rounds in range(int(input())):
    velocity = 0
    vector = 0
    seconds = int(input())
    for second in range(seconds):
        status_given = list(map(int,input().split()))
        status = status_given[0]
        
        if status == 0:
            vector += velocity

        elif status == 1:
            accelerate = status_given[1]
            velocity += accelerate
            vector += velocity

        elif status == 2:
            accelerate = status_given[1]
            if accelerate >= velocity:
                velocity = 0
            else:
                velocity -= accelerate

            vector += velocity
            
    
    print(f'#{rounds + 1} {vector}')
    

        