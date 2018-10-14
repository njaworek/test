def prepare_report(pozycje):
    total_ilosc = 0.0
    total_KG = 0.0
    total_cena = 0.0

    for poz in pozycje:
        total_ilosc = total_ilosc + poz['Ilosc']
        total_KG = total_KG + poz['KG']
        total_cena = total_cena + poz['cena']
    #return [str(total_ilosc), str(total_cena), str(total_KG)]
    iwp = ('Ile sztuk:' +',' + str(total_ilosc) + ',' + ' Jaka cena: ' +','+str(total_cena) + ',' + ' ile kilogramow: ' +','+str(total_KG))
    return iwp






def retrieve_data():
    pozycje = [
        {'nazwa':'jablka', 'ID': 1, 'KG': 19, 'Ilosc': 15, 'cena': 2.50, 'is_toxic': True},
        {'nazwa':'kiwi', 'ID':2, 'KG':0.5, 'Ilosc':1, 'cena':3},
        {'nazwa':'pomarancze', 'ID':3, 'KG':2, 'Ilosc':4, 'cena':4.50, 'is_toxic': True},
        {'nazwa':'ziemniaki', 'ID':4, 'KG':10, 'Ilosc':25, 'cena':1.25, 'is_toxic': False},
        {'nazwa':'banany', 'ID':5, 'KG':3, 'Ilosc':8, 'cena':3.25},
        {'nazwa':'sliwki', 'ID':6, 'KG':6, 'Ilosc':30, 'cena':4.80, 'is_toxic': True},
        {'nazwa':'brzoskwinie', 'ID':7, 'KG':8, 'Ilosc':15, 'cena':2.50, 'is_toxic': False},
        {'nazwa':'mandarynka', 'ID':8, 'KG':5, 'Ilosc':10, 'cena':3.50, 'is_toxic': True}
    ]
    return pozycje


def main():
    pozycje = retrieve_data()
    poz = retrieve_data()
    raport = prepare_report(pozycje)
    toksyk = toxic(poz)
    #csv_raport = ",".join(str(raport))
    file_object = open("test.txt", "w")
    #file_object.write(str(csv_raport))
    file_object.write(raport)
    file_object.close()


    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx")
    total_toxic = 0
    total_nottoxic = 0

    for poz in pozycje:
        if 'is_toxic' in poz:
            if poz['is_toxic'] == True:
                total_toxic = total_toxic+1
            else:
                total_nottoxic = total_nottoxic+1
        else:
            total_nottoxic = total_nottoxic+1
    return total_toxic, total_nottoxic




    #export_to_file(raport)


if __name__ == '__main__':
    main()
