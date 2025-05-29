# Task 1
greet = "Hello, Python World!"
print(greet)

# Task 2
print((lambda x, y: ' '.join(str(f(x, y)) for f in [lambda a, b: a+b, lambda a, b: a-b, lambda a, b: a*b, lambda a, b: a/b]))(*map(int, input().split())))

# Task 3
print((lambda st: ' '.join([st, str(len(st))]))(input()+input()))

# Task 4
print(('Odd', 'Even')[int(input()) % 2 == 0])

# Task 5
print(' '.join([str(i) for i in range(1, 11)]))

# Task 6
print((lambda x: 'Positive' if x > 0 else ('Zero' if x == 0 else 'Negative'))(int(input())))

# Task 7
print(' '.join([str(i) for i in range(1, 11) if i % 2 == 0]))
# print(' '.join([str(i) for i in range(2, 11, 2)]))

# Task 8
print(sum([x for x in range(1, int(input())+1)]))

# Task 9
print(' '.join([str(i) for i in range(10, 0, -1)]))

# Task 10
for i in range(1, 11):
    if i == 5:
        continue
    if i == 7:
        break
    print(i)

