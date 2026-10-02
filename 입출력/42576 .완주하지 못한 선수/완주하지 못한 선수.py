from collections import Counter
def solution(participant, completion):
    remaining = Counter(participant) - Counter(completion)
    return list(remaining.keys())[0]