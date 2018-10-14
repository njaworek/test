import json

file_object = open("test2.csv", 'r')
print("XXXXX")

total_cena = 0.0
total_ilosc = 0.0

for l in file_object:
    poz = l.strip().split(',')
    print(poz)
    total_cena += float(poz[2])
    total_ilosc += float(poz[1])

print(total_cena)
print(total_ilosc)

json.dumps({'price': total_cena}, ensure_ascii=False)
json.dumps({'price': total_ilosc}, ensure_ascii=False)
