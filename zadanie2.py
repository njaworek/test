samochody=['honda', 'BMW', 'opel', 'toyota']
spalanie=[6, 9, 5, 4]




while True:
    haslo=raw_input("Podaj haslo: ")
    if len(haslo) < 4:
       print("Haslo za krotkie wprowadz dluzsze haslo")
    else:
       srodek = '*' *(len(haslo)-2)
       haslo2 = haslo[0] + srodek + haslo[-1]
       file_object = open("test.txt", "w")
       file_object.write(haslo2)
       file_object.close()
       break
