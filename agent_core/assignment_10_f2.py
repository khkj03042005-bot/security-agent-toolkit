def summarize(values):
    total = sum(values)
    return f"합계 {total}"

text = summarize([2, 3])
with open("report.txt", "w", encoding="utf-8") as f:
    f.write(text)
print(text)