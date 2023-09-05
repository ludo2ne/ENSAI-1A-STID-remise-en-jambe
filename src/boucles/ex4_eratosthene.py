def crible_eratosthene(n):
    """Crible d'Eratosthene par ChatGPT"""

    # Initialisation de la liste des booléen de 0 à n-1
    liste_nombres_premiers = [True] * (n + 1)
    liste_nombres_premiers[0] = liste_nombres_premiers[1] = False

    # On parcourt la liste et on élimine au fur et à mesure les multiples
    for i in range(2, int(n**0.5) + 1):
        if liste_nombres_premiers[i]:
            for j in range(i * i, n + 1, i):
                liste_nombres_premiers[j] = False

    primes = [i for i, is_prime in enumerate(liste_nombres_premiers) if is_prime]

    # La ligne ci dessus est équivalente à :
    # primes2 = []
    # for i in range(len(liste_nombres_premiers)):
    #     if liste_nombres_premiers[i]:
    #         primes2.append(i)

    return primes


if __name__ == "__main__":
    print(crible_eratosthene(1000))
