## Jours de la semaine
print("Jours de la semaine")

jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']

semaine = jours[:5]
week_end = jours[5:]
print(f"Semaine : {semaine}")
print(f"Week-end: {week_end}")

## Avec indices négatifs
semaine = jours[:-2]
week_end = jours[-2:]
print(f"Semaine : {semaine}")
print(f"Week-end: {week_end}")

## Dernier jours de la semaine
print("Dernier jour de la semaine : " + jours[-1])
print("Dernier jour de la semaine : " + jours[len(jours) - 1])

# Inverser la liste
print(f"Semaine inversée : {jours[::-1]}")

print(f"Semaine inversée : {list(reversed(jours))}")

## Saisons 
print("Saisons")
saisons = ['hiver', 'printemps', 'ete', 'automne']
print(saisons[2])
print(saisons[1][0])
print(saisons[1:2])
print(saisons[:][1])

## Table de multiplication par 9
print(list(range(0,91,9)))