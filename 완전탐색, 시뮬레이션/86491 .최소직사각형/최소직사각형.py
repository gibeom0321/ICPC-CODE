def solution(sizes):
    maxa = 0
    maxb = 0
    for row in sizes:
        row.sort(reverse=True)
    for a, b in sizes:
        maxa = max(maxa, a)
        maxb = max(maxb, b)
    return maxa*maxb