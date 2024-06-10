# 입력값 초기화
n, k = map(int, input().split())
# 원형 리스트
people = list(range(1, n + 1))
# 현재 위치
k_index = 0
result = []

for i in range(n): 
	k_index = (k_index + k - 1) % len(people)
	result.append(people.pop(k_index))
    
print('<' + str(result)[1:-1] + '>')