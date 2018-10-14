import json
with open("test2.csv", 'r') as outfile:
    print("XXXXX")

    total_cena = 0.0
    total_ilosc = 0.0

    for l in outfile:
        poz = l.strip().split(',')
        print(poz)
        total_cena += float(poz[2])
        total_ilosc += float(poz[1])

    print(total_cena)
    print(total_ilosc)

    json.dumps({'suma': total_cena}, outfile)
    json.dumps({'ilosc': total_ilosc}, outfile)
