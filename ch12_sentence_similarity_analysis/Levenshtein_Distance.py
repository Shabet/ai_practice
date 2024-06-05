import numpy as np
import random

# 레벤슈타인 거리 구하기
def calc_distance(a, b):
    ''' 레벤슈타인 거리 계산하기 '''
    if a == b: return 0 # 같으면 0을 반환
    a_len = len(a) # a 길이
    b_len = len(b) # b 길이
    if a == "": return b_len
    if b == "": return a_len
    # 2차원 표 (a_len+1, b_len+1) 준비하기 --- (※1)
    # matrix 초기화의 예 : [[0, 1, 2, 3], [1, 0, 0, 0, 0], [2, 0, 0, 0, 0], [3, 0, 0, 0, 0], [4, 0, 0, 0, 0]]
    #
    # ex)
    #        서 울 시
    #    [0, 1, 2, 3]
    # 서 [1, 0, 1, 2]
    # 울 [2, 1, 0, 1]
    # 시 [3, 2, 1, 0] 
    matrix = [[] for i in range(a_len+1)] # 리스트 컴프리헨션을 사용하여 1차원 초기화
    for i in range(a_len+1): # 0으로 초기화
        matrix[i] = [0 for j in range(b_len+1)]  # 리스트 컴프리헨션을 사용하여 2차원 초기화
    # 0일 때 초깃값을 설정
    for i in range(a_len+1):
        matrix[i][0] = i
    for j in range(b_len+1):
        matrix[0][j] = j
    # 표 채우기 --- (※2)
    # print(matrix,'----------')
    for i in range(1, a_len+1):
        ac = a[i-1]
        # print(ac,'=============')
        for j in range(1, b_len+1):
            bc = b[j-1] 
            # print(bc)
            cost = 0 if (ac == bc) else 1  #  파이썬 조건 표현식 예:) result = value1 if condition else value2
            matrix[i][j] = min([
                matrix[i-1][j] + 1,     # 문자 제거: 위쪽에서 +1
                matrix[i][j-1] + 1,     # 문자 삽입: 왼쪽 수에서 +1   
                matrix[i-1][j-1] + cost # 문자 변경: 대각선에서 +1, 문자가 동일하면 대각선 숫자 복사
            ])
            # print(matrix)
        # print(matrix,'----------끝')
    # print(np.array(matrix))
    return matrix[a_len][b_len]


def get_shortest_distance_index(input_sentence, questions):
    '''입력된 질문과 미리준비된 질문 리스트를 calc_distance() 함수를 호출하여 레벤슈타인 거리를 계산하고, 이를 기준으로 가장 유사한 질문에 해당하는 인덱스를 리턴'''
    shortest_distances = [] # (index, distance, question) 튜플 형식으로 저장
    for idx, question in enumerate(questions):
        distance = calc_distance(input_sentence, question)

        if not shortest_distances:                 #최초 수행시
            shortest_distances = [(idx, distance, question)]
        elif distance < shortest_distances[0][1]:  #거리가 짧은 것을 저장
            shortest_distances = [(idx, distance, question)]
        elif distance == shortest_distances[0][1]: #거리가 같을때는 append
            shortest_distances.append((idx, distance, question))

    # print(shortest_distances) # 테스트시 주석 해제

    # 같은 거리로 계산된 것중에 random하게 인덱스 리턴
    random_num_idx = random.randint(0,len(shortest_distances)-1)
    return shortest_distances[random_num_idx][0]

def get_shortest_distance_index_old(input_sentence, questions):
    shortest_distances = [] # (index, distance, question) 튜플 형식으로 저장
    distances = []
    for idx, question in enumerate(questions):
        distance = calc_distance(input_sentence, question)

        if not shortest_distances:                #최초 수행시
            shortest_distances = [(idx, distance, question)]
        elif distance < shortest_distances[0][1]:  #거리가 짧은 것을 저장
            shortest_distances = [(idx, distance, question)]
        elif distance == shortest_distances[0][1]: #거리가 같을때는 append
            shortest_distances.append((idx, distance, question))
        
        print(idx, calc_distance(input_sentence, question), question)
        distances.append(calc_distance(input_sentence, question))

    print("@@@")
    for key, value in enumerate(distances):
        print(key, value)

    print("@@@")
    print(shortest_distances)
    #print(len(shortest_distances))
    print("@@@")

    random_num_idx = random.randint(0,len(shortest_distances)-1)
    print(random_num_idx)
    print(shortest_distances[random_num_idx])
    print("###")

    return shortest_distances[random_num_idx][0]


# "얼마나 분석이 될까요"와 "유사도나 분석 할까요"의 거리 --- (※3)
print("Levenshtein_Distance:", calc_distance("얼마나 분석이 될까요","유사도나 분석 할까요"))


# 실행 예
samples = ["신촌역","신천군","신천역","신발","마곡역"]
base = samples[0]
r = sorted(samples, key = lambda n: calc_distance(base, n))  # samples 리스트의 각 요소에 대해 calc_distance(base, n) 함수를 호출하여 레벤슈타인 거리를 계산하고, 이를 기준으로 리스트를 정렬
for n in r:
    print(calc_distance(base, n), n)

shortest_distance_index = get_shortest_distance_index(base, samples[1:])
#shortest_distance_index = get_shortest_distance_index_old(base, samples[1:])
print(shortest_distance_index)




