
def calculate_vat(netto, rate):
    return float(netto * rate)/100

def prepare_report(pozycje, wybory):
    for poz in pozycje:
        if poz['produkt'] in wybory:
            total_brutto = total_brutto + poz['cena']
            total_netto = total_brutto + calculate_vat(poz['cena'], poz[vat_procent])
def main():
    pozycje = [
        {'produkt': 'wyklady', 'cena':1.10,  'vat_procent' : 50},
        {'produkt': 'wyklady', 'cena':199,  'vat_procent' : 33},
        {'produkt': 'samochod', 'cena':100,  'vat_procent' : 8.5},
        {'produkt': 'masaz', 'cena':200,  'vat_procent' : 25}

    ]

    wybory = [ 'wyklady', 'samochod']

    total_netto = 0
    total_brutto = 0



    for poz in pozycje:
        if poz['produkt'] in wybory:
            total_brutto = total_brutto + poz['cena']
            total_netto = total_brutto + calculate_vat(poz['cena'], poz[vat_procent])

            print(total_netto)
            print(total_brutto)

if __name__=="__main__":
    main()
