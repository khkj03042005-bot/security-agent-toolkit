import csv

failed_users = []

with open("logs_with_header.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["result"] == "FAIL":          # 결과가 FAIL이면
            failed_users.append(row["user"]) # 계정을 목록에 추가

print(failed_users)