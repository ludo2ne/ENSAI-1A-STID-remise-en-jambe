jour = "lundi"
heure = 5
minute = 23


jour_semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]


if jour in jour_semaine:
    print("1. Jour de la semaine")

if jour not in jour_semaine or heure < 8 or heure >= 18:
    print("2. En dehors des heures de travail")

if jour == "vendredi":
    if heure == 18 and minute >= 30:
        print("3. vendredi soir")
    if heure >= 19:
        print("3. vendredi soir")


if heure == 12 and minute >= 30:
    print("4. N'importe quel jour entre 12h30 et 13h45 inclus")
elif heure == 13 and minute <= 45:
    print("4. N'importe quel jour entre 12h30 et 13h45 inclus")


if jour == "jeudi":
    print("5. ok")
else:
    if heure in (15, 16, 17) or (heure == 18 and minute <= 15):
        print("5. ok")
