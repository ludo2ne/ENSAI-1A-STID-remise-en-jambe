f0 = 0
f1 = 1

print(f0, end=" ")
print(f1, end=" ")

for i in range(29):
    print(f0 + f1, end=" ")
    f1 = f0 + f1
    f0 = f1 - f0


print("\n" + "-" * 50)

# Avec une boucle While
i = 2
f0 = 0
f1 = 1
print(f0, end=" ")
print(f1, end=" ")


while i <= 30:
    print(f0 + f1, end=" ")
    f1 = f0 + f1
    f0 = f1 - f0
    i += 1
