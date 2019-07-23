arr = list(input().split())
num = int(input())

def circulation(arr,num,chosen = []):
    
    count = [0 for _ in range(len(arr))]
    
    if len(temp) == num:
        chosen.append(temp)
        return chosen

    
    