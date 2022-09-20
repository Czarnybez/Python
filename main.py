import random
import cowsay
import pyttsx3

def main():
    imie = input("Jak masz na imie? ")
    praca = input("gdzie pracujesz? ")
    wiek = int(input("ile masz lat?. "))
    engine = pyttsx3.init()

    propPraca = ['CIA', 'FBI', 'KGB']


    print('w tym miejscu zacznie sie nowa galaz')
    print('second brench')
    print('no to testujemy pulla')


    odp = [f"co ty jeszcze robisz w wupie!!, w {random.choice(propPraca)} jest wone miejsce",   #odp[0]
           "puk puk zostal jeden roczek do zmiany pracy !! ",                                   #odp[1]
           f"Za {40 - wiek} lat ma Cie tu nie byc",                                             #odp[2]
           "Bravo TY :)",                                                                       #odp[3]
           "Witam panie KIEROWNIKU, co tam u kasi? ",                                           #odp[4]
           "Jak tam juz DYREKTOR ?"                                                             #odp[5]
           ]

    if imie.casefold() == "wojtek":
        if wiek >= 40 and praca.casefold() == "wup":
            odpowiedz(odp[0])

        elif wiek < 40 and praca.casefold() == "wup":
            if wiek == 39:
                odpowiedz(odp[1])
            else:
                odpowiedz(odp[2])
        elif praca.casefold() != "wup":
            odpowiedz(odp[3])
    elif imie.casefold() == "adam":
        cowsay.stegosaurus("Adam, Adaś, Adam, Adam ... \nA nie to Witek")
    elif imie.casefold() == "emil":
        if praca.casefold() == "wup":
            if wiek >= 40:
                cowsay.daemon(odp[5])
                engine.say(odp[5])
                engine.runAndWait()
            else:

                cowsay.cow(odp[4])
                engine.say(odp[4])
                engine.runAndWait()

        else:
            odpowiedz(odp[3])

    else:
        cowsay.ghostbusters(f"SORRY {imie}, ale nie znam CIE !!")

#sprawdza czy string zawiera liczbe
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

#generuje odpowiedz
def odpowiedz(odp):

    print('-'* 80)
    print(odp)
    print('-' * 80)

#chyba trzeba poprawic
while True:

    pytanie = input("Czy chcesz rozpoczac test kompetencji (T/N)  ")
    if pytanie.casefold() == 't':
        main()
    elif pytanie.casefold()== 'n':
        break
    else:
        print("Nie pojemaju !")
