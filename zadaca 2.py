import random

imena = ['Ivan', 'Antonio', 'Antonija', 'Anto', 'Marijan', 'Zvjezdan', 'Ivan', 'Mihaela', 'Ružica', 'Dorijan', 'Petra', 'Matej', 'Filip', 'Magdalena', 'Mate', 'Iva', 'Danis', 'Josip', 'Nebojša', 'Ante', 'Luka', 'Ante', 'Lorena', 'Ivan', 'Nikola', 'Ivan', 'Helena', 'Ivan', 'Gabrijela', 'Andrija', 'Regina', 'Petar', 'Dino', 'Marija', 'Semir', 'Gabriela', 'Borna', 'Filip', 'Krešimir', 'Ivana', 'Gabrijel', 'Vinko', 'Vinko', 'Romana', 'Viktorija', 'Mija', 'Matej', 'Vinko', 'Luka', 'Antea', 'Ivan', 'Ivan', 'Luka', 'Daniel', 'Nikola', 'Marko']

ocjene = []

for ime in imena:
    ocjene.append(random.randint(1, 5))

rjecnik = {}

for ocjena in ocjene:
    if ocjena in rjecnik:
        rjecnik[ocjena] += 1
    else:
        rjecnik[ocjena] = 1

print(rjecnik)

ukupno = len(ocjene)
polozili = sum(1 for o in ocjene if o > 1)
postotak = round(polozili / ukupno * 100, 2)

print("Postotak prolaznosti:", postotak, "%")
