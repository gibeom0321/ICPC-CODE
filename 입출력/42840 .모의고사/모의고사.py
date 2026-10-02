def solution(answers):
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    counts = {1: 0, 2:0, 3:0}
    
    for i in range(len(answers)):
        if answers[i] == a1[i % 5]:
            counts[1] += 1
        if answers[i] == a2[i % 8]:
            counts[2] += 1
        if answers[i] == a3[i % 10]:
            counts[3] += 1    
    max_score = max(counts.values())
    
    result = []
    for k, v in counts.items():
        if v == max_score:
            result.append(k)
    return result