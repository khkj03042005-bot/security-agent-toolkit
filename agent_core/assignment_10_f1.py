def collect_high(values):
    high = []
    for v in values:
        if v >= 3:
            high.append(v)
    return high          # ← for와 같은 들여쓰기 (for 밖)

print(collect_high([1, 4, 2, 5]))
print(collect_high([]))