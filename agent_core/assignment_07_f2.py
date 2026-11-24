groups = [[2, 1], [3, 0]]

for group in groups:
    total = 0               # 묶음마다 0에서 다시 시작
    for value in group:
        total += value
    print(total)            # 안쪽 for가 끝난 뒤 출력