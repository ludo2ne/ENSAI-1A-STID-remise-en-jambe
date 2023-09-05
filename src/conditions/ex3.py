def sup_et_affiche(liste):
    if liste == []:
        print("La liste est vide")
    else:
        print("dernier élément : " + str(liste[-1]))
        liste.pop()
    return liste


if __name__ == "__main__":
    ma_liste = [1, 2, 3, 4]
    sup_et_affiche(ma_liste)
    print(ma_liste)
