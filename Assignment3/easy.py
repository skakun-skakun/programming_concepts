from random import choice
from string import printable

a = list(map(int, input().split()))
print(a)
b = [''.join(choice(printable) for __ in range(20)) for _ in range(10)]
print(b)

# -----------------------------------

# Task 1
print((lambda lst, x: [i for i in lst if i > x])(a, int(input())))

# Task 2
print((lambda lst: sum(lst)/len(lst))([i for i in a if i > 0]))

# Task 3
print(max((lambda lst, x: [i for i in lst if i < x])(a, int(input()))))

# Task 4
print(sum((lambda lst, y: [i for i in lst if i % y == 0])(a, int(input()))))

# Task 5
print([i**2 for i in a])

# Task 6
new_a_lol = [i for i in a if i > 0]

# Task 7
print((lambda lst, pref: [i for i in b if i.startswith(pref)])(b, input()))

# Task 8
print((lambda lst, n: sum(a[:n]))(a, int(input())))

# Task 9
print([i for i in b if i == i[::-1]])

# Task 10
print((lambda lst, n: [i % n == 0 for i in a])(a, int(input())))
