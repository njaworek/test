baza = {"volvo": 1.8,
        "kia": 2.0,
        "BMW": 5.6}


marka = raw_input("Podaj marke: ")
podaj_km = 15
cena_za_litr = 5.2

if marka in baza:
    spalanie= baza[marka]
    print(podaj_km * spalanie * cena_za_litr)

# in python3 baza.items()
for key, value in baza.iteritems():
    print("{0}:{1}".format(key, value))


for key in baza:
    print("{0}:{1}".format(key, baza[key]))



def calculate_vat(netto):
    vat = float(netto * 23)/100
    return vat


if __name__ == "__main__":
    vat = calculate_vat(1000)
    print("{0}".format(vat))
