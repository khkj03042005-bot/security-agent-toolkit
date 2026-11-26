import csv

# ── 1) 입력 파일 준비 (없으면 만든다) ──
lines = [
    "time,user,ip,action,result",
    "09:01,kim01,10.0.3.21,LOGIN,FAIL",
    "09:03,lee02,10.0.7.5,LOGIN,OK",
    "09:05,kim01,10.0.3.21,LOGIN,FAIL",
    "09:08,park03,10.0.9.8,FILE_OPEN,OK",
    "09:11,kim01,10.0.3.21,LOGIN,FAIL",
    "09:14,park03,10.0.9.8,LOGIN,FAIL",
]

try:
    with open("logs_with_header.csv", encoding="utf-8") as f:
        pass
except FileNotFoundError:
    with open("logs_with_header.csv", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(f"{line}\n")
    print("logs_with_header.csv를 새로 만들었습니다")

# ── 2) csv.reader로 줄마다 출력 + 줄 수 세기 ──
line_count = 0
with open("logs_with_header.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        line_count += 1

print(f"총 {line_count}줄")