import re
# test input
# new_id = 	"...!@BaT#*..y.abcdefghijklm"
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for char in new_id:
        if char.isalnum() or char in '-_.':
            answer += char
    while '..' in answer: answer = answer.replace('..', '.')
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    answer = 'a' if answer == '' else answer
    if len(answer) >= 16 : 
        answer = answer[:15]
        if answer[-1] == '.': answer = answer[:-1] 
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3-len(answer))
    
    return answer

print(solution(new_id))