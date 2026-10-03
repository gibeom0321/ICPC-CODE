def solution(brown, yellow):
    area = brown + yellow
    for height in range(1, area+1):
        if area % height == 0:
            width = area // height
            if ((height-2) * (width - 2) == yellow):
                return [width, height]              