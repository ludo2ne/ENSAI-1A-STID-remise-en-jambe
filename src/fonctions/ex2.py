def fizz_buzz(n) -> str:
    res = ""
    if n % 3 == 0:
        res += "FIZZ"
    if n % 5 == 0:
        res += " BUZZ"

    return res.strip()  # strip supprime les espaces superflus au début et à la fin


if __name__ == "__main__":
    print(fizz_buzz(15))
    print(fizz_buzz(21))
