a = list(map(int, input().split()))
print(a)

# -----------------------------------

# Task 1
print(sum(a))

# Task 2
print(min(a))

# Task 3
print(a[::-1])

# Task 4
print([i for i in a if i % 2 == 0])

# Task 5
print((lambda lst,n: [i*n for i in lst])(a, int(input())))
