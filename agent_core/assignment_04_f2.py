counts = [0, 4, 2, 5]
selected = 0   # 조건에 맞는 값의 '개수'
total = 0      # 조건에 맞는 값의 '합계'
for count in counts:
    if count >= 3:
        selected += 1       # 개수는 하나 찾을 때마다 1씩
        total += count      # 합계는 찾은 값만큼
print(selected, total)      # 반복이 다 끝난 뒤 한 번만 출력