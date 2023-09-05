remise_a_niveau = {
    "UE": "Informatique pour la data science",
    "module": "remise_a_niveau",
    "nb_eleve": 20,
    "eleves": ["eleve1", "eleve2", "eleve3"],
}


print(list(remise_a_niveau.keys()))
print(remise_a_niveau.values())

remise_a_niveau["nb_eleve"] = 3
remise_a_niveau["annee"] = 2023

print(remise_a_niveau)
