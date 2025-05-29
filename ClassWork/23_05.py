# 1
# print((lambda value, percentage: value*percentage/100)(*map(float, input().split())))

# 2
# print((lambda price, rate=0.2: price*(1+rate))(*map(float, input().split())))

# 3
# print((lambda *args: sum(args)/len(args))(*map(float, input().split())))

# 4


# 5
# print((lambda amount, rate: amount / rate)(*map(float, input().split())))

# 6
# from math import ceil; print((lambda x: ceil(x))(float(input())))

# 7
# print((lambda x, y: max([x, y]))(*map(float, input().split())))

# 8
# print((lambda price, discount: price * (1 - discount))(*map(float, input().split())))

# 9
# print((lambda name, *expenses: f"{name}: {str(sum(expenses))}")('Nill Kiggers', 1, 2, 3, 4, 5, 6, 7, 8, 9))

a = {}
while True:
    b = input()
    if not b:
        break
    c, d = b.split()
    a[c] = float(d)

print(sum(a.values()), len(a), sum(a.values())/len(a), max(a.keys(), key=lambda i: a[i]))
