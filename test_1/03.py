def solution(info, query):
    answer = []
    
    info_list = [0] * 100001

    key_list = {
    'cpp' : 0,
    'java' : 1,
    'python' : 2,
    
    'backend' : 0,
    'frontend' : 1,

    'junior' : 0,
    'senior' : 1,

    'chicken' : 0,
    'pizza' : 1,

    '-' : None
    }

    LANG = 3
    END = 2
    AGE = 1
    FOOD = 0

    class Info:

        def __init__(self, point):
            self.point = point
            self.cnt = 0
            self.info = {}
            info_list[point] = self
        
        def append_info(self,lang, end, age, food):
            key = (lang * (3 ** LANG)) + (end * (3 ** END)) + (age * (3 ** AGE))  + (food * (3 ** FOOD)) 
            if self.info.get(key):
                self.info[key] += 1
            else:
                self.info[key] = 1
            self.cnt += 1

    for i in info:
        i = i.split()
        lang, end, age, food, point = i
        point = int(point)
        lang = key_list[lang]
        end = key_list[end]
        age = key_list[age]
        food = key_list[food]

        if info_list[point] == 0:
            info_list[point] = Info(point)
            info_list[point].append_info(lang, end, age, food)
            
        else:
            info_list[point].append_info(lang, end, age, food)

    def check_point(point, lang, end, age, food):

        cnt = 0

        for k, v in info_list[point].info.items():
            
            if lang !=None and (k // (3 ** LANG)) != (lang):
                continue
            if end !=None and ((k % (3 ** (END + 1))) // (3 ** END)) != (end):
                continue
            if age !=None and ((k % (3 ** (AGE + 1))) // (3 ** AGE)) != (age):
                continue
            if food !=None and ((k % (3 ** (FOOD + 1))) // (3 ** FOOD)) != (food):
                continue
            
            cnt += v
    
        return cnt

    len_q = len(query)
    answer = [0] * len_q
    for i in range(len_q):
        q = query[i].split()
        lang = key_list[q[0]]
        end = key_list[q[2]]
        age = key_list[q[4]]
        food = key_list[q[6]]
        point = int(q[7])
        t_cnt = 0

        flag = False
        if lang == None and end == None and age == None and food == None :
            flag = True
        
        for p in range(point, 100001):
            if info_list[p] == 0:
                continue
            
            else:
                if flag:
                    t_cnt += info_list[p].cnt
                else:
                    t_cnt += check_point(p, lang, end, age, food)
        answer[i] = t_cnt




    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))