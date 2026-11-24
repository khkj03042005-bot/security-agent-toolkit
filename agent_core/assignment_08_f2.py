import json

logs = [
    {"time": "09:01", "user": "kim01", "event": "LOGIN_OK", "ip": "10.0.3.21"},
    {"time": "09:05", "user": "admin", "event": "LOGIN_FAIL", "ip": "10.0.9.8"},
    {"time": "09:12", "user": "admin", "event": "LOGIN_FAIL", "ip": "10.0.9.8"},
    {"time": "09:18", "user": "lee02", "event": "LOGIN_FAIL", "ip": "10.0.7.5"},
    {"time": "09:21", "user": "admin", "event": "LOGIN_FAIL", "ip": "10.0.9.8"},
]

# 1) 저장: 파이썬 값 → 파일
with open("logs.json", "w", encoding="utf-8") as f:
    json.dump(logs, f, ensure_ascii=False)

# 2) 복원: 파일 → 파이썬 값
with open("logs.json", encoding="utf-8") as f:
    back = json.load(f)

# 3) 첫 번째 기록의 user 칸
print(back[0]["user"])