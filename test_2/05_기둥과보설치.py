def solution(n, build_frame):
    answer = []
    building = [[0] * (n + 1) for _ in range(n + 1)]
    기둥 = 0
    보 = 1

    def make_floor_ok(x, y, tmp_building):
        flag = False

        if tmp_building[y - 1][x] & (1 << 기둥):
            flag = True
        if x < n and tmp_building[y - 1][x + 1] & (1 << 기둥):
            flag = True
        if x + 1 < n and x > 0 and tmp_building[y][x - 1] & (1 << 보) and tmp_building[y][x + 1] & (1 << 보):
            flag = True

        return flag

    def make_pillar_ok(x, y, tmp_building):
        flag = False
        if y == 0:
            flag = True
        if tmp_building[y][x] & (1 << 보):
            flag = True
        if x > 0 and tmp_building[y][x - 1] & (1 << 보):
            flag = True
        if y > 0 and tmp_building[y - 1][x] & (1 << 기둥):
            flag = True
        return flag

    def detroy_floor_ok(n, x, y, tmp_building):

        for dx in [-1, 0, 1]:
            if not 0 <= x + dx <= n:
                continue

            # 보가있을경우
            if tmp_building[y][x + dx] & (1 << 보):
                if not make_floor_ok(x + dx, y, tmp_building):
                    return False
            
            if tmp_building[y][x + dx] & (1 << 기둥):
                if not make_pillar_ok(x + dx, y, tmp_building):
                    return False
        
        return True

    def detroy_pillar_ok(n, x, y ,tmp_building):
        if y == n:
            return True

        if tmp_building[y + 1][x] & (1 << 보):
            if not make_floor_ok(x, y + 1, tmp_building):
                return False
        if tmp_building[y + 1][x] & (1 << 기둥):
            if not make_pillar_ok(x, y + 1, tmp_building):
                return False
        if x > 0 and tmp_building[y + 1][x - 1] & (1 << 보):
            if not make_floor_ok(x - 1, y + 1, tmp_building):
                return False

        return True

    def copy_building(n, building):
        copied_building = []

        for idx in range(n + 1):
            copied_building.append(building[idx][:])

        return copied_building
    
    for frame in build_frame:
        tx, ty, tw, th = frame
        
        if th == 1:
            if tw == 기둥:
                if make_pillar_ok(tx, ty, building):
                    building[ty][tx] += (1 << 기둥)
            if tw == 보:
                if make_floor_ok(tx, ty, building):
                    building[ty][tx] += (1 << 보)
        else:
            if tw == 기둥:
                tmp_building = copy_building(n, building)
                tmp_building[ty][tx] -= (1 << 기둥)    
                if detroy_pillar_ok(n, tx, ty, tmp_building):
                    building[ty][tx] -= (1 << 기둥)
            if tw == 보:
                tmp_building = copy_building(n, building)
                tmp_building[ty][tx] -= (1 << 보)    
                if detroy_floor_ok(n, tx, ty, tmp_building):
                    building[ty][tx] -= (1 << 보)
    for rx in range(n + 1):
        for ry in range(n + 1):
            if building[ry][rx] & (1 << 기둥):
                answer.append([rx, ry, 기둥])
            if building[ry][rx] & (1 << 보):
                answer.append([rx, ry, 보])

    return answer


print(solution(5,	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))