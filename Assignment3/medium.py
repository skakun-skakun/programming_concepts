# a = list(map(int, input().split()))
# print(a)
a = [1, 2, 3, [4, 5], 6, [7, 8]]
# -----------------------------------

# Task 1
# print((lambda lst, x, y, *args: [i for i in lst if i % x == 0 and i % y != 0])(a, *map(int, input().split())))

# Task 2
# res = []; [(lambda x: res.append(x), lambda x: res.extend(x))[isinstance(i, list)](i) for i in a]; print(res)

# Task 3
main_str = input()
for i in input().split():
    main_str = main_str.replace(i, i.upper())
print(main_str)

# Task 4


# Task 5


# Task 6


# Task 7


# Task 8


# Task 9


# Task 10
# print((lambda lst, x, y, *args: [(i, i*y)[i > x] for i in lst])(a, *map(int, input().split())))
