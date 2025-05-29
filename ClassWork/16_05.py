# 1
# print((lambda lst: sum(lst)/len(lst))([3, 7, 2, 9, 5]))

# 2
# print((lambda lst: sorted([i for i in set(lst) if i % 2 == 0])[::-1])([4, 7, 2, 4, 8, 9, 2, 10, 3, 8]))

# 3
# print((lambda grades: (lambda student: f"{grades.index(student)}\n{sum(student)/len(student)}\n{student}")(max(grades, key=lambda x: sum(x)/len(x))))([[90, 85, 88], [75, 80, 79], [95, 92, 96], [88, 85, 84]]))

# 4
print(sum({"apple": 12, "banana": 8, "milk": 25, "bread": 20}.values()))

print()

# 5
print((lambda sl: {city: [name for name in sl.keys() if sl[name] == city] for city in set(sl.values())})({"Anna": "Kyiv", "Bohdan": "Lviv", "Oksana": "Kyiv", "Dmytro": "Odesa"}))
