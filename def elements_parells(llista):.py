def elements_parells(llista):
    """Retorna una llista amb les paraules en posicions parelles."""
    return [llista[i] for i in range(len(llista)) if i % 2 == 0]

# Proves de la funció
llista_paraules = ["maca", "tardor", "flor", "estiu", "nadal", "primavera"]
resultat = elements_parells(llista_paraules)

print("Paraules en posicions parelles:", resultat)