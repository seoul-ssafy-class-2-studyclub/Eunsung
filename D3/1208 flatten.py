for rounds in range(1,11):
    N = int(input())
    boxes = list(map(int,input().split()))

    for dump in range(N):
        max_index = boxes.index(max(boxes))
        min_index = boxes.index(min(boxes))

        boxes[max_index] -= 1
        boxes[min_index] += 1

    print(f'#{rounds} {max(boxes) - min(boxes)}')