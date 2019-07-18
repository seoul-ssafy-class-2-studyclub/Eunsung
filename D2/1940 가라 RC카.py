
def plus_v_vector(accelerate,velocity):
    return velocity + accelerate
def minus_v_vector(accelerate,velocity):
    if accelerate >= velocity:
        return 0
    else:
        return velocity - accelerate

for rounds in range(int(input())):
    velocity = 0
    vector = 0
    seconds = int(input())
    for second in range(seconds):
        status_given = list(map(int,input().split()))
        status = status_given[0]
        try:
            accelerate = status_given[1]
        except:
            accelerate = 0

        if status == 0:
            vector += velocity
        elif status == 1:
            vector += plus_v_vector(accelerate, velocity)
            velocity += accelerate
        elif status == 2:
            vector += minus_v_vector(accelerate, velocity)
            if accelerate >= velocity:
                velocity = 0
            else:
                velocity -= accelerate
    
    print(f'#{rounds + 1} {vector}')
    

        