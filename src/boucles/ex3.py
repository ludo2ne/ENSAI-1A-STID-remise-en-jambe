f0 = 0
f1 = 1

print(f0, end=" ")
print(f1, end=" ")


while f1 + f0 < 10000:
    print(f0 + f1, end=" ")
    f1 = f0 + f1
    f0 = f1 - f0

print("\n" + "-" * 50)

# Avec une boucle for

f0 = 0
f1 = 1

print(f0, end=" ")
print(f1, end=" ")


for i in range(50):
    if f0 + f1 > 10000:
        break
    else:
        print(f0 + f1, end=" ")
        f1, f0 = f0 + f1, f1
