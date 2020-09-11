def solution(nodeinfo):

    levels = {} 
    max_y = 0
    cnt_node = len(nodeinfo)
    for i in range(cnt_node):
        node = nodeinfo[i]
        x, y = node
        if y > max_y:
            max_y = y
        if levels.get(y) == None:
            levels[y] = [(x, i + 1)]
        else:
            levels[y].append((x, i + 1))
    print(levels)
    class Node:
        def __init__(self, x, y, p, number):
            self.p = p
            self.x = x
            self.y = y
            self.left = None
            self.right = None
            self.number = number

    start_node = Node(levels[max_y][0][0], max_y, None, levels[max_y][0][1])
    now_y = max_y
    def make_tree(now_node):
        for ty in range(now_node.y - 1, -1, -1):
            if ty <= 0:
                return 0

            if levels.get(ty) == None:
                continue
            else:
                break
        levels[ty].sort()

        for tx, number in levels[ty]:
            if is_ok(tx, now_node, now_node.p, True):
                now_node.left = Node(tx, ty, now_node, number)
            if is_ok(tx, now_node, now_node.p, False):
                now_node.right = Node(tx, ty, now_node, number)

        make_tree(now_node.left)
        make_tree(now_node.right)
    def is_ok(x, now_node, parent_node, left):
        if not parent_node:
            print(now_node.number, 7, left)
            
            if left:
                if x < now_node.x:
                    return True
                else:
                    return False
            else:
                if x > now_node.x:
                    return True
                else:
                    return False
        print(now_node.number, parent_node.number, left)
        if parent_node.left and parent_node.left == now_node.x:
            if x < parent_node.x and x < now_node.x:
                return True
            else: return False  
        else:
            if x > parent_node.x and x > now_node.x:
                return True
            else: return False

        pass
    make_tree(start_node)
    res_pre = [0] * cnt_node
    cnt_pre = [0]

    res_post = [0] * cnt_node
    cnt_post = [0]
    def preorder_traverse(now_node):
        
        res_pre[cnt_pre[0]] = now_node.number
        cnt_pre[0] += 1
        print(now_node.number)

        if now_node.left:
            preorder_traverse(now_node.left)
        if now_node.right:
            preorder_traverse(now_node.right)
    
    def postorder_traverse(now_node):
        
        if now_node.left:
            postorder_traverse(now_node.left)
        if now_node.right:
            postorder_traverse(now_node.right)
        
        res_post[cnt_post[0]] = now_node.number
        cnt_post[0] += 1
    
    preorder_traverse(start_node)
    postorder_traverse(start_node)

    answer = [res_pre, res_post]
    print(res_pre)
    return answer

solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])