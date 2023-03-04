## Poly-A
print("Poly-A")
print("A" * 20)

## Poly-A et poly-GC
print("Poly-A et poly-GC")
print("A" * 20 + "GC"*40)

## Écriture formatée
print("Écriture formatée")
a="Salut"
b=102
c=10.318

print(f"{a} {b} {c:.2f}")

## Écriture formatée 2
print("Écriture formatée 2")
perc_GC = ((4500 + 2575)/14800)*100

print(f"Le pourcentage de GC est {perc_GC:<10.0f} %")
print(f"Le pourcentage de GC est {perc_GC:<10.1f} %")
print(f"Le pourcentage de GC est {perc_GC:<10.2f} %")
print(f"Le pourcentage de GC est {perc_GC:<10.3f} %")