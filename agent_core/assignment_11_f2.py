import json

# ── 1) 입력 파일이 없으면 직접 만든다 ──
sample_rows = [
    {"user": "kim01", "result": "FAIL"},
    {"user": "lee02", "result": "OK"},
    {"user": "kim01", "result": "FAIL"},
]

try:
    with open("gichan_input.json", encoding="utf-8") as f:
        rows = json.load(f)
except FileNotFoundError:
    with open("gichan_input.json", "w", encoding="utf-8") as f:
        json.dump(sample_rows, f, ensure_ascii=False, indent=2)
    print("gichan_input.json를 새로 만들었습니다")
    rows = sample_rows

# ── 2) 전체 건수, 실패 건수 계산 ──
total = len(rows)
fail = 0
for row in rows:
    if row["result"] == "FAIL":
        fail += 1

# (한 줄로 쓰고 싶다면)
# fail = sum(1 for row in rows if row["result"] == "FAIL")

# ── 3) summary.txt 에 결과 저장 ──
with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(f"전체 {total}건, 실패 {fail}건")

# ── 4) 확인용 화면 출력 ──
print(f"전체 {total}건, 실패 {fail}건")
print("summary.txt 에 저장했습니다")