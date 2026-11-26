import csv
from collections import Counter

THRESHOLD = 2

# ── ① logs_with_header.csv 를 DictReader 로 읽어 실패 계정 모으기 ──
failed_users = []
with open("logs_with_header.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["result"] == "FAIL":
            failed_users.append(row["user"])

# ── ② Counter 로 세기 ──
counts = Counter(failed_users)

# ── ③ THRESHOLD 이상인 계정을 "확인 필요: kim01 · 3회" 모양으로 출력 ──
for user, count in counts.items():
    if count >= THRESHOLD:
        print(f"확인 필요: {user} · {count}회")