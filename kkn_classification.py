import math

A = [(7, 8, 200), (8, 9, 220), (6, 6, 180), (7.5, 8.5, 210), (6.5, 7, 190)]
B = [(5, 5, 100), (5.5, 4.5, 120), (6, 5, 130), (5, 6, 110), (5.5, 5, 115)]
C = [(2, 2, 50), (2.5, 2.5, 55), (1.5, 2, 45), (2, 2.5, 52), (3, 2, 58)]
D= [(10, 3, 120), (12, 3.1, 110), (11, 2.9, 130), (14, 3, 120), (15, 2.6, 110)]

coords = A+B+C+D

x = (8,9,111)
k=5 #3 or 5
"""
x와 가장 가까운 k개를 알아내고 그들 간의 거리를 계산해주는 함수 + 어떤 class에 속할 지 알려주는 함수 (제일 많이 든 class가 inference class)
"""

def get_distance(a,b):
    distance = math.sqrt(math.pow(a[0]-b[0],2) + math.pow(a[1]-b[1],2) + math.pow(a[2]-b[2],2))
    return distance

def get_class(coord):
    if coord in A:
        return 'A'
    elif coord in B:
        return 'B'
    elif coord in C:
        return 'C'
    else:
        return 'D'

def l2_closest():
    distances = []
    for coord in coords:
        distances.append((get_distance(coord, x),get_class(coord), coord))
    
    distances.sort(key = lambda x: x[0])

    return distances[:k], distances

def normal_knn(closests):
    dict = {}
    for closest in closests:
        if closest[1] not in dict:
            dict[closest[1]] = 1
        else:
            dict[closest[1]] += 1
    
    max_val = max(dict.values())
    majority = [k for k,v in dict.items() if v==max_val]
    print(f"X is one of {majority}")
    print(f"closest coordinates were {closests}")

closests, all_distances = l2_closest()

print("Normal KNN")
normal_knn(closests)


"""
x와 가장 가까운 k개 들에서 weight을 사용하여 어떤 class에 속할 지 알려주는 함수
"""


def weight_function(a,b):
    return math.exp(-get_distance(a,b))

def weighted_knn(closests):
    #각 class에 맞는 weight을 계산해야 한다
    dict = {}
    for closest in closests:
        if closest[1] not in dict:
            dict[closest[1]] = 1 / closest[0]
        else:
            dict[closest[1]] += 1 / closest[0]

    max_val = max(dict.values())
    majority = [k for k,v in dict.items() if v==max_val]
    print(f"X is one of {majority}")
    for k,v in dict.items():
        print(f"class {k}'s weight was {v}")




print("Weighted KNN")
weighted_knn(closests)