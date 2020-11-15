# 홍길동 씨의 과목별 점수는 다음과 같다.
# 홍길동 씨의 평균 점수를 구해 보자.

# 과목	점수
# 국어	80
# 영어	75
# 수학	55

score_list = [80, 75, 55]
score_tuple = (80, 75, 55)
score_dict = {
    'kor': 80,
    'eng': 75,
    'math': 55
}

avg_list = avg_tuple = avg_dict = 0

for i in score_list:
    avg_list += i
print('avg : ', avg_list/len(score_list))

for t in score_tuple:
    avg_tuple += t
print('avg : ', avg_tuple/len(score_tuple))

for d in score_dict.values():
    avg_dict += d
print('avg : ', avg_dict/len(score_dict.keys()))
