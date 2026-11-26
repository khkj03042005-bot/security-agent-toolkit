import csv

# ── 1) 입력 파일이 없으면 직접 만든다 (8.1 방식) ──
lines = [
    "time,user,ip,action,result",
    "09:01,kim01,10.0.3.21,LOGIN,FAIL",
    "09:03,lee02,10.0.7.5,LOGIN,OK",
    "09:05,kim01,10.0.3.21,LOGIN,FAIL",
]

try:
    with open("gichan_input.csv", encoding="utf-8") as f:
        pass  # 파일이 이미 있으면 그대로 사용
except FileNotFoundError:
    with open("gichan_input.csv", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(f"{line}\n")
    print("gichan_input.csv를 새로 만들었습니다")

# ── 2) DictReader로 읽어서 FAIL 개수 세기 ──
count = 0
with open("gichan_input.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if row["result"] == "FAIL":
            count += 1

# ── 3) 결과 출력 ──
print(count)