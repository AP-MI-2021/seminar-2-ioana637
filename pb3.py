from copy import deepcopy, copy

a = [1, [1, 2, [3, 5]], 3]
b = deepcopy(a)
a[1][0] = 100
print(a)
print(b)

a = [1, [1, 2, [3, 5]], 3]
b = copy(a)
a[1][0] = 100
print(a)
print(b)
