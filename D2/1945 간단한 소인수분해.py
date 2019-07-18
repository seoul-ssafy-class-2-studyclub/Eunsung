T = int(input())

for i in range(T):
    
    num = int(input())
    dem = [2, 3, 5, 7, 11]
    dem_in = [0, 0, 0, 0, 0]

    for de in range(len(dem)):
        while num % (dem[de]**(dem_in[de]+1)) == 0:
            dem_in[de] += 1


    print(f'#{i+1} ', end = '')
    print(''.join(dem_in))
    print('')