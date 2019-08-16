N = int(input())
side_list = []

temp_down = 0
temp_up = 0
side_sums = []
dices = []

for i in range(N):
    A, B, C, D, E, F = map(int,input().split())
    dices.append([A, B, C, F, D, E])

for first in range(6):
    side_list = []
    dice_rel = {
            dices[0][0]: dices[0][3],
            dices[0][1]: dices[0][4],
            dices[0][2]: dices[0][5],
            dices[0][3]: dices[0][0],
            dices[0][4]: dices[0][1],
            dices[0][5]: dices[0][2],
        }
    temp_dice = list(range(1,7))
    temp_up = dices[0][first]
    temp_down = dice_rel[temp_up]
    temp_dice.remove(temp_up)
    temp_dice.remove(temp_down)
    side_list.append(max(temp_dice))

    for i in range(1, N):
        temp_dice = list(range(1,7))
        dice_rel = {
            dices[i][0]: dices[i][3],
            dices[i][1]: dices[i][4],
            dices[i][2]: dices[i][5],
            dices[i][3]: dices[i][0],
            dices[i][4]: dices[i][1],
            dices[i][5]: dices[i][2],
        }
        temp_down = temp_up
        temp_up = dice_rel[temp_down]
        temp_dice.remove(temp_up)
        temp_dice.remove(temp_down)
        side_list.append(max(temp_dice))
    
    side_sums.append(sum(side_list))
print(max(side_sums))