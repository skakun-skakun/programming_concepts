a = list(map(int, input().split()))
print(a)
b = [1, 2, 3, [4, 5], 6, [7, 8]]
# -----------------------------------

# Task 1
print((lambda lst, x, y, *args: [i for i in lst if i % x == 0 and i % y != 0])(a, *map(int, input().split()[:2])))

# Task 2
res = []; [(lambda x: res.append(x), lambda x: res.extend(x))[isinstance(i, list)](i) for i in b]; print(res)

# Task 3
main_str = input()
for i in input().split():
    main_str = main_str.replace(i, i.upper())
print(main_str)

# Task 4
print((lambda lst: sorted(sorted(lst, reverse=True), key=lst.count))(a))

# Task 5
print((lambda lst1, lst2, cond: lst1+lst2 if cond(lst1, lst2) else None)(input().split(), input().split(), lambda lst1, lst2: len(lst1) > len(lst2)))

# Task 6
print((lambda lst, key, vals: {i: {val: sum(j[val] for j in lst if j[key] == i) for val in vals} for i in {j[key] for j in lst}})(
    [{'id': 1, 'a': 10, 'b': 10},
     {'id': 2, 'a': 20, 'b': 20},
     {'id': 1, 'a': 30, 'b': 30},
     {'id': 3, 'a': 40, 'b': 40},
     {'id': 2, 'a': 50, 'b': 50},
     {'id': 1, 'a': 60, 'b': 60},
     {'id': 3, 'a': 70, 'b': 70}], key='id', vals=['a', 'b']
))

# Task 7
print((lambda lst, replacement, cond: [(i, replacement)[cond(i)] for i in lst])(input().split(), "...", lambda s: len(s) > 4))

# Task 8
print((lambda lst, x: len([i for i in lst if len(i)>x]))(input().split(), int(input())))

# Task 9
print((lambda a, b: ''.join([a[i] + b[i] for i in range(min(len(a), len(b)))]) + ''.join([a, b][len(a)<len(b)][min(len(a), len(b)):]))(input().split(), input().split()))

# Task 10
print((lambda lst, x, y, *args: [(i, i*y)[i > x] for i in lst])(a, *map(int, input().split()[:2])))
