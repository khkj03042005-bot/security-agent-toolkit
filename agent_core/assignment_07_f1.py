groups = [[2, 1], [3, 0]]

for group in groups:        # 바깥: 묶음을 꺼냄
    for value in group:     # 안쪽: 묶음 안의 숫자를 꺼냄
        print(value)