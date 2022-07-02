import collections

# 예제 input
a = ["mislav", "stanko", "mislav", "ana"]
b = 	["stanko", "ana", "mislav"]
# 내가 푼 코드
# def solution(participant, completion):
#   for i in completion: 
#     if i in participant: participant.remove(i)

#   return participant

# collections Counter 클래스 활용
def solution(participant, completion):
  answer = collections.Counter(participant) - collections.Counter(completion)
  return list(answer.keys())[0]

print(solution(a, b))
