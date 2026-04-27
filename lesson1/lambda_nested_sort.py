people = [
    ("Alice", 25, 160),
    ("Bob", 30, 175),
    ("Charlie", 25, 170),
    ("David", 30, 168),
    ("Eve", 22, 158)
]

sorted_people = sorted(people, key=lambda x: (x[1], -x[2]))

print(sorted_people)
# 出力: [('Eve', 22, 158), ('Charlie', 25, 170), ('Alice', 25, 160), ('Bob', 30, 175), ('David', 30, 168)]