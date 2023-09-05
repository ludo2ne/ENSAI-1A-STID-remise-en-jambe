from copy import copy

initiale = [1, 2, "test", True, 4, 5]

second = initiale
my_copy = copy(initiale)

initiale[0] = 42
initiale[5] = "another"
print(initiale)
print(second)
print(my_copy)
