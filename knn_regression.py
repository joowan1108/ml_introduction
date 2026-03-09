import math


Car1 = (2, 200, 4, 27)
Car2 = (5, 150, 3, 35)
Car3 = (3, 180, 4, 25)
Car4 = (1, 230, 2, 10)
Car5 = (5, 180, 5, 40)
Car6 = (4, 210, 3, 30)
cars = [Car1, Car2, Car3, Car4, Car5, Car6]
prices = [0,30000,20000, 25000, 21000, 38000, 31000]

k = 5
x = (6,200,5,30)

def get_distance(a,b):
    distance = math.sqrt(math.pow(a[0]-b[0],2) + math.pow(a[1]-b[1],2) + math.pow(a[2]-b[2],2) + + math.pow(a[3]-b[3],2))
    return distance

"""
가장 가까운 k개을 구한 뒤에 이 k개의 price의 평균을 내서 최종 얘측값 계산
"""

def which_car(car):
    if car == Car1:
        return 1
    elif car == Car2:
        return 2
    elif car == Car3:
        return 3
    elif car == Car4:
        return 4
    elif car == Car5:
        return 5
    else:
        return 6
    
def l2_closest():
    distances = []
    for car in cars:
        distances.append((get_distance(car, x), which_car(car)))
    
    distances.sort(key = lambda x: x[0])

    return distances[:k], distances


closests, all_distances = l2_closest()

#average predicition: 가장 가까운 k개 입력받음
def average(closests):
    sum = 0
    for closest in closests:
        sum += prices[closest[1]]
    k_average = sum / k
    print(f"average price of {k} neighbors: {k_average}")

average(closests)

def get_weight(dist):
    return math.exp(-dist)

#weighted prediction: 각 car의 weight을 계산한 다음 price 예측
def weighted_average(closests):

    denumerator = 0
    numerator = 0

    for closest in closests:
        weight = get_weight(closest[0])
        numerator += weight * prices[closest[1]]
        denumerator += weight
    
    print(f"weighted average price of {k} neighbors: {numerator/denumerator}")

weighted_average(closests)



