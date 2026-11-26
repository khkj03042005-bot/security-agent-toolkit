# ── 상수: 한 번 정하고 안 바꾸는 값 → 전부 대문자 ──
THRESHOLD = 2

# ── 변수: 실패 계정 목록 → snake_case, 알아보는 이름 ──
failed_users = ["kim01", "kim01", "lee02"]

# ── 함수: 소문자와 밑줄 → count_fail ──
def count_fail(users, name):
    count = 0
    for user in users:
        if user == name:
            count = count + 1
    return count

if count_fail(failed_users, "kim01") >= THRESHOLD:
    print("확인 필요: kim01")