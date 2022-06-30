s = "one4sevenzero"
def solution(s):
    data = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in data:
      if i in s: s = s.replace(i, str(data.index(i)))
    return int(s)

print(solution(s))
