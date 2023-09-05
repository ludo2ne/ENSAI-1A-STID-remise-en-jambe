res = ""
a = 15


if a % 3 == 0:
    res += "FIZZ"
if a % 5 == 0:
    res += " BUZZ"


print(res.strip())
