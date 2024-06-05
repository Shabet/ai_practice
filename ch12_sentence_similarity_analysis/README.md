# 문장 유사도 분석

## 레벤슈타인 거리를 이용한 문장 유사도 분석


- Levenshtein_Distance.py

```
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
    # [0, 1, 2, 3]
    # [1, 0, 0, 0]
    # [2, 0, 0, 0]
    # [3, 0, 0, 0] 
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
    return matrix[a_len][b_len]
# "가나다라"와 "가마바라"의 거리 --- (※3)
print(calc_distance("얼마나 분석이 될까요","유사도나 분석 할까요"))
# 실행 예
samples = ["신촌역","신천군","신천역","신발","마곡역"]
base = samples[0]
r = sorted(samples, key = lambda n: calc_distance(base, n))  # samples 리스트의 각 요소에 대해 calc_distance(base, n) 함수를 호출하여 레벤슈타인 거리를 계산하고, 이를 기준으로 리스트를 정렬
for n in r:
    print(calc_distance(base, n), n)
```


## n-gram을 이용한 문장 유사도 분석

```
# 문자열 s를 num-gram으로 나누는 함수
def ngram(s, num):  
    res = []
    slen = len(s) - num + 1
    for i in range(slen):
        ss = s[i:i+num]
        res.append(ss)
    return res

# 두 문자열 sa와 sb를 각각 num-gram으로 나눈 후, sa와 sb에서 공통으로 나타난 num-gram의 개수와 리스트를 반환하는 함수
def diff_ngram(sa, sb, num):
    a = ngram(sa, num)
    b = ngram(sb, num)
    r = []
    cnt = 0
    for i in a:
        for j in b:
            if i == j:
                cnt += 1
                r.append(i)
    return cnt / len(a), r
a = "오늘 강남에서 맛있는 스파게티를 먹었다."
b = "강남에서 먹었던 오늘의 스파게티는 맛있었다."
# 2-gram
r2, word2 = diff_ngram(a, b, 2)
print("2-gram:", r2, word2)
# 3-gram
r3, word3  = diff_ngram(a, b, 3)
print("3-gram:", r3, word3)
```