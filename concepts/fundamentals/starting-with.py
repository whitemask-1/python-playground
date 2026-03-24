countries = ["America", "Canada", "India", "Austrailia", "China", "California", "Chile"]

for c in countries.copy():
    if c.startswith("C"):
        print(c)
        countries.remove(c)

print(countries)
