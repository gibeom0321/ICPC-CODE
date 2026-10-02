def solution(participant, completion):
    counts = {}
    for name in participant:
        counts[name] = counts.get(name, 0) + 1
        
    for name in completion:
        counts[name] -= 1
        
    for name, value in counts.items():
        if value == 1:
            return name