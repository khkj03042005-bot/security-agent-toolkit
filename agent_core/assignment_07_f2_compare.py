groups = [[2, 1], [3, 0]]

print("--- 실험 A: total = 0이 바깥 for 안 (원래 F2) ---")
for group in groups:
    total = 0
    for value in group:
        total += value
    print(total)

print("--- 실험 B: total = 0이 맨 위 (리셋 안 함) ---")
total = 0
for group in groups:
    for value in group:
        total += value
    print(total)