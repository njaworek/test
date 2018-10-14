imie= 'Ala'
zwierze = 'kot'
zwierzeta = ['psy', 'wilki', 'pandy' , 'niedzwiedzie']
print("{0} ma {1}a".format(imie, zwierze))

print(zwierzeta[0])
print(zwierzeta[1])
print(zwierzeta[2])


for z in zwierzeta:
    print(z)

for idx in range(len(zwierzeta) ) :
    print("idx: " + str(idx) + " : " + zwierzeta[idx])

print("Tylko psowatwe")
# w tablicy mozemy wywolywac elementy poprzez 2 np
#2: range wieksze od 2 :2 range mniejsze od 2 albo przedzial
for z in zwierzeta[2:3]:
    print[z]
#wypisze pandy


for z in zwierzeta:
    print(z)


nazwa_samochodu = "Honda"

#wyciaganie ostatniej litery
if len(nazwa_samochodu)>0:
    ostatnia_litera = nazwa_samochodu[-1]
    print(ostatnia_litera)
else:
    print('pusty string')

#uzytkownik wypisuje swoje zwierzeta dopisuje do ciagu 
li=['pies', 'kot', 'kon', 'owca']
for i in li:
    nazwa_zwierzeta=raw_input("Podaj nazwe zwierzecia: ")
    if nazwa_zwierzeta in li:
        print("to znam")
    else:
        li.append(nazwa_zwierzeta)
        print ("tego nie znam, ale przy kolejnej probie bede znac")
