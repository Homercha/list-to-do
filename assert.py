tasks = []

tasks.append("Купити молоко")
assert len(tasks) == 1

tasks.append("Вивчити Python")
assert len(tasks) == 2

tasks.pop(0)
assert len(tasks) == 1

print("Усі assert-тести пройдено успішно")
