from collections import deque

def solution(priorities, location):
    queue = deque()
    cnt = 0
    for i, p in enumerate(priorities):
        queue.append((i, p))
    while queue:
        check = queue.popleft()
        if not queue or check[1] >= max([q for i, q in queue]): 
            cnt += 1
            if check[0] == location:
                return cnt
        else: 
            queue.append(check)