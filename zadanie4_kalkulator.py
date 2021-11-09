import logging
logging.basicConfig(level=logging.DEBUG)


def kalkulator():
    dzialanie = pobierz_dzialanie()
    a,b = pobierz_liczbe()
    wynik = przeprowadz_dzialanie(dzialanie, a, b)
    print(wynik)

def dodawanie(a,b):
    return a + b

def odejmowanie(a,b):
    return a - b

def mnozenie(a,b):
    return a * b

def dzielenie(a,b):
    return a / b

def pobierz_dzialanie():
    print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie")
    odp = input()
    if odp != "1" and odp != "2" and odp != "3" and odp != "4":
        print("podano zly numer")
        odp = "-1"
    return odp

def pobierz_liczbe():
    print("podaj skladnik 1")
    a= int(input())
    print("podaj skladnik 2")
    b= int(input())
    return a, b

def przeprowadz_dzialanie(dzialanie, a, b):
    wynik = -1
    if dzialanie == "1":
        wynik = dodawanie(a, b)
        logging.info("Dodaję "+  str(a) + " i " + str(b) )
    if dzialanie =="2":
        wynik = odejmowanie(a, b)
        logging.info("Odejmuję " + str(a) + " i " + str(b) )
    if dzialanie == "3":
        wynik = mnozenie(a, b)
        logging.info("Mnożę " + str(a) + " i " + str(b))
    if dzialanie == "4":
        wynik = dzielenie(a, b)
        logging.info("Dzielę " + str(a) + " i " + str(b))
    return wynik


kalkulator()


