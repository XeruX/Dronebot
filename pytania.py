# Plik ten zawiera funkcje obsługujące wczytywanie oraz wyświetlanie pytań w konsoli

# Zmienne przechowujące zawartość plików z pytaniami
powitanie = open('pytania/powitanie.txt', encoding='UTF-8')
powitanie_odmowa = open('pytania/powitanie_odmowa.txt', encoding='UTF-8')
powitanie_potwierdzenie = open('pytania/powitanie_potwierdzenie.txt', encoding='UTF-8')
pytanie_1 = open('pytania/pytanie_1.txt', encoding='UTF-8')
pytanie_2 = open('pytania/pytanie_2.txt', encoding='UTF-8')
pytanie_3 = open('pytania/pytanie_3.txt', encoding='UTF-8')
pytanie_4 = open('pytania/pytanie_4.txt', encoding='UTF-8')
pytanie_4a = open('pytania/pytanie_4a.txt', encoding='UTF-8')
pytanie_4b = open('pytania/pytanie_4b.txt', encoding='UTF-8')
pytanie_4c = open('pytania/pytanie_4c.txt', encoding='UTF-8')
pytanie_4d = open('pytania/pytanie_4d.txt', encoding='UTF-8')
pytanie_4e = open('pytania/pytanie_4e.txt', encoding='UTF-8')
pytanie_4f = open('pytania/pytanie_4f.txt', encoding='UTF-8')
pytanie_4g = open('pytania/pytanie_4g.txt', encoding='UTF-8')
pytanie_4h = open('pytania/pytanie_4h.txt', encoding='UTF-8')
pytanie_4i = open('pytania/pytanie_4i.txt', encoding='UTF-8')
pytanie_4j = open('pytania/pytanie_4j.txt', encoding='UTF-8')
pytanie_4k = open('pytania/pytanie_4k.txt', encoding='UTF-8')
pytanie_4l = open('pytania/pytanie_4l.txt', encoding='UTF-8')
pytanie_4m = open('pytania/pytanie_4m.txt', encoding='UTF-8')
pytanie_4n = open('pytania/pytanie_4n.txt', encoding='UTF-8')
pytanie_4o = open('pytania/pytanie_4o.txt', encoding='UTF-8')
pytanie_5 = open('pytania/pytanie_5.txt', encoding='UTF-8')
pytanie_6 = open('pytania/pytanie_6.txt', encoding='UTF-8')
pytanie_7 = open('pytania/pytanie_7.txt', encoding='UTF-8')
pytanie_8 = open('pytania/pytanie_8.txt', encoding='UTF-8')
pytanie_8x = open('pytania/pytanie_8x.txt', encoding='UTF-8')
pytanie_9 = open('pytania/pytanie_9.txt', encoding='UTF-8')
pytanie_9x = open('pytania/pytanie_9x.txt', encoding='UTF-8')
pytanie_10 = open('pytania/pytanie_10.txt', encoding='UTF-8')
pytanie_10x = open('pytania/pytanie_10x.txt', encoding='UTF-8')
pytanie_11 = open('pytania/pytanie_11.txt', encoding='UTF-8')
pytanie_11x = open('pytania/pytanie_11x.txt', encoding='UTF-8')
pytanie_12 = open('pytania/pytanie_12.txt', encoding='UTF-8')
pytanie_12x = open('pytania/pytanie_12x.txt', encoding='UTF-8')
pytanie_13 = open('pytania/pytanie_13.txt', encoding='UTF-8')
pytanie_13x = open('pytania/pytanie_13x.txt', encoding='UTF-8')
pytanie_14 = open('pytania/pytanie_14.txt', encoding='UTF-8')
pytanie_14x = open('pytania/pytanie_14x.txt', encoding='UTF-8')
pytanie_15 = open('pytania/pytanie_15.txt', encoding='UTF-8')
pytanie_15x = open('pytania/pytanie_15x.txt', encoding='UTF-8')
pytanie_16 = open('pytania/pytanie_16.txt', encoding='UTF-8')
pytanie_16x = open('pytania/pytanie_16x.txt', encoding='UTF-8')
pytanie_17 = open('pytania/pytanie_17.txt', encoding='UTF-8')
pytanie_18 = open('pytania/pytanie_18.txt', encoding='UTF-8')
pytanie_19 = open('pytania/pytanie_19.txt', encoding='UTF-8')
pytanie_20 = open('pytania/pytanie_20.txt', encoding='UTF-8')
pytanie_21 = open('pytania/pytanie_21.txt', encoding='UTF-8')
pytanie_22 = open('pytania/pytanie_22.txt', encoding='UTF-8')
pytanie_23 = open('pytania/pytanie_23.txt', encoding='UTF-8')
pytanie_23_nie = open('pytania/pytanie_23_nie.txt', encoding='UTF-8')
pytanie_24 = open('pytania/pytanie_24.txt', encoding='UTF-8')
pytanie_24_nie = open('pytania/pytanie_24_nie.txt', encoding='UTF-8')
pytanie_25 = open('pytania/pytanie_25.txt', encoding='UTF-8')
pytanie_26 = open('pytania/pytanie_26.txt', encoding='UTF-8')
pytanie_27 = open('pytania/pytanie_27.txt', encoding='UTF-8')
pytanie_27_nie = open('pytania/pytanie_27_nie.txt', encoding='UTF-8')
pytanie_28 = open('pytania/pytanie_28.txt', encoding='UTF-8')
pytanie_28_nie = open('pytania/pytanie_28_nie.txt', encoding='UTF-8')
pytanie_29 = open('pytania/pytanie_29.txt', encoding='UTF-8')
schemat_1_nie = open('pytania/schemat_1_nie.txt', encoding='UTF-8')
schemat_1_nie_nie = open('pytania/schemat_1_nie_nie.txt', encoding='UTF-8')
schemat_1_tak = open('pytania/schemat_1_tak.txt', encoding='UTF-8')
schemat_2_nie = open('pytania/schemat_2_nie.txt', encoding='UTF-8')
schemat_2_nie_nie = open('pytania/schemat_2_nie_nie.txt', encoding='UTF-8')
schemat_2_nie_tak = open('pytania/schemat_2_nie_tak.txt', encoding='UTF-8')
schemat_2_tak = open('pytania/schemat_2_tak.txt', encoding='UTF-8')
schemat_3_nie = open('pytania/schemat_3_nie.txt', encoding='UTF-8')
schemat_3_tak = open('pytania/schemat_3_tak.txt', encoding='UTF-8')
schemat_4_nie = open('pytania/schemat_4_nie.txt', encoding='UTF-8')
schemat_4_tak = open('pytania/schemat_4_tak.txt', encoding='UTF-8')
schemat_5_1 = open('pytania/schemat_5_1.txt', encoding='UTF-8')
schemat_5_2 = open('pytania/schemat_5_2.txt', encoding='UTF-8')
schemat_5_3 = open('pytania/schemat_5_3.txt', encoding='UTF-8')
schemat_5_4 = open('pytania/schemat_5_4.txt', encoding='UTF-8')
schemat_5_5 = open('pytania/schemat_5_5.txt', encoding='UTF-8')
schemat_5_5_tak = open('pytania/schemat_5_5_tak.txt', encoding='UTF-8')
schemat_5_5_nie = open('pytania/schemat_5_5_nie.txt', encoding='UTF-8')
schemat_5_6 = open('pytania/schemat_5_6.txt', encoding='UTF-8')
schemat_6_nie = open('pytania/schemat_6_nie.txt', encoding='UTF-8')
schemat_6_nie_nie = open('pytania/schemat_6_nie_nie.txt', encoding='UTF-8')
schemat_7_tak = open('pytania/schemat_7_tak.txt', encoding='UTF-8')
schemat_7_nie = open('pytania/schemat_7_nie.txt', encoding='UTF-8')

zla_odpowiedz = '\nNie rozumiem. Potwórzę jeszcze raz:'
zly_zakres = '\nOdpowiedź musi być liczbą z zakresu od 1 do 5. Potwórzę jeszcze raz:'

lista_pytan = [pytanie_1, pytanie_2, pytanie_3, pytanie_4, pytanie_4a, pytanie_4b, pytanie_4c, pytanie_4d, pytanie_4e,
               pytanie_4f, pytanie_4g, pytanie_4h, pytanie_4i, pytanie_4j, pytanie_4k, pytanie_4l, pytanie_4m,
               pytanie_4n, pytanie_4o, pytanie_5, pytanie_6, pytanie_7, pytanie_8, pytanie_8x, pytanie_9, pytanie_9x,
               pytanie_10, pytanie_10x, pytanie_11, pytanie_11x, pytanie_12, pytanie_12x, pytanie_13, pytanie_13x,
               pytanie_14, pytanie_14x, pytanie_15, pytanie_15x, pytanie_16, pytanie_16x, pytanie_17, pytanie_18,
               pytanie_19, pytanie_20, pytanie_21, pytanie_22, pytanie_23, pytanie_24, pytanie_25, pytanie_26,
               pytanie_27, pytanie_28, pytanie_29]

# Słownik, który definiuje jaki schemat należy uruchomić do danego pytania
schematy = {
    pytanie_1: 'schemat_1',
    pytanie_2: 'schemat_1',
    pytanie_3: 'schemat_1',
    pytanie_4: 'schemat_2',
    pytanie_4a: 'schemat_2',
    pytanie_4b: 'schemat_2',
    pytanie_4c: 'schemat_2',
    pytanie_4d: 'schemat_2',
    pytanie_4e: 'schemat_2',
    pytanie_4f: 'schemat_2',
    pytanie_4g: 'schemat_2',
    pytanie_4h: 'schemat_2',
    pytanie_4i: 'schemat_2',
    pytanie_4j: 'schemat_2',
    pytanie_4k: 'schemat_2',
    pytanie_4l: 'schemat_2',
    pytanie_4m: 'schemat_2',
    pytanie_4n: 'schemat_2',
    pytanie_4o: 'schemat_2',
    pytanie_5: 'schemat_1',
    pytanie_6: 'schemat_3',
    pytanie_7: 'schemat_4',
    pytanie_8: 'schemat_5',
    pytanie_8x: 'schemat_5',
    pytanie_9: 'schemat_5',
    pytanie_9x: 'schemat_5',
    pytanie_10: 'schemat_5',
    pytanie_10x: 'schemat_5',
    pytanie_11: 'schemat_5',
    pytanie_11x: 'schemat_5',
    pytanie_12: 'schemat_5',
    pytanie_12x: 'schemat_5',
    pytanie_13: 'schemat_5',
    pytanie_13x: 'schemat_5',
    pytanie_14: 'schemat_5',
    pytanie_14x: 'schemat_5',
    pytanie_15: 'schemat_5',
    pytanie_15x: 'schemat_5',
    pytanie_16: 'schemat_5',
    pytanie_16x: 'schemat_5',
    pytanie_17: 'schemat_6',
    pytanie_18: 'schemat_6',
    pytanie_19: 'schemat_6',
    pytanie_20: 'schemat_6',
    pytanie_21: 'schemat_6',
    pytanie_22: 'schemat_6',
    pytanie_23: 'schemat_pytanie_23',
    pytanie_24: 'schemat_pytanie_24',
    pytanie_25: 'schemat_6',
    pytanie_26: 'schemat_6',
    pytanie_27: 'schemat_pytanie_27',
    pytanie_28: 'schemat_pytanie_28',
    pytanie_29: 'schemat_7'
}


def powitaj():
    while True:
        print()

        for line in powitanie:
            print(line.strip())

        powitanie.seek(0)

        odp = pobierz_odp()
        if odp == 'tak' or odp == 'nie':
            break
        else:
            print(zla_odpowiedz)

    return odp


def potwierdzenie():
    while True:
        print()
        for line in powitanie_potwierdzenie:
            print(line.strip())

        powitanie_potwierdzenie.seek(0)

        odp = pobierz_odp()
        if odp == 'tak' or odp == 'nie':
            break
        else:
            print(zla_odpowiedz)

    return odp


def odmowa():
    print()
    for line in powitanie_odmowa:
        print(line.strip())


def pytaj():
    # Zmienna przechowująca poziom danego ryzyka
    global ryzyko
    ryzyko = 1

    # Pętla główna wyświetlająca kolejne pytania
    for pytanie in lista_pytan:
        # Pętla wewnętrzna - weryfikuje poprawność podanej odpowiedzi
        while True:
            print()

            # Wyświetlenie pytania
            for line in pytanie:
                print(line.strip())

            # Przesunięcie kursora na początek pliku
            pytanie.seek(0)
            odp = pobierz_odp()

            if odp.isdecimal():
                try:
                    ryzyko *= int(eval(schematy.get(pytanie))(odp))
                    if pytanie.name.endswith('x.txt'):
                        schemat_5a(ryzyko)
                        ryzyko = 1
                    break
                except TypeError:
                    print(zla_odpowiedz)
                except ValueError:
                    print(zly_zakres)

            else:
                try:
                    if eval(schematy.get(pytanie))(odp):
                        break
                    else:
                        return
                except TypeError:
                    print(zla_odpowiedz)
                except ValueError:
                    print(zly_zakres)


# ------- Schematy -------
def schemat_1(answer: str):
    if answer == 'tak':
        return True
    elif answer == 'nie':
        while True:
            print()
            for line in schemat_1_nie:
                print(line.strip())
            schemat_1_nie.seek(0)

            answer = pobierz_odp()

            if answer == 'tak':
                while True:
                    print()
                    for line in schemat_1_tak:
                        print(line.strip())
                    schemat_1_tak.seek(0)

                    answer = pobierz_odp()

                    if answer == 'tak':
                        return True
                    elif answer == 'nie':
                        print('\nSzkoda. Mimo to, mam nadzieję, że jeszcze się usłyszymy ;)')
                        return False
                    else:
                        print(zla_odpowiedz)
            elif answer == 'nie':
                print()
                for line in schemat_1_nie_nie:
                    print(line.strip())
                return False
            else:
                print(zla_odpowiedz)
    else:
        raise TypeError


def schemat_2(answer: str):
    if answer == 'tak':
        print()
        for line in schemat_2_tak:
            print(line.strip())
        schemat_2_tak.seek(0)
        return True
    elif answer == 'nie':
        while True:
            print()
            for line in schemat_2_nie:
                print(line.strip())
            schemat_2_nie.seek(0)

            answer = pobierz_odp()

            if answer == 'tak':
                while True:
                    print()
                    for line in schemat_2_nie_tak:
                        print(line.strip())
                    schemat_2_nie_tak.seek(0)

                    answer = pobierz_odp()

                    if answer == 'tak':
                        return True
                    elif answer == 'nie':
                        print()
                        for line in schemat_2_nie_nie:
                            print(line.strip())
                        return False
                    else:
                        print(zla_odpowiedz)

            elif answer == 'nie':
                print()
                for line in schemat_2_nie_nie:
                    print(line.strip())
                return False
            else:
                print(zla_odpowiedz)
    else:
        raise TypeError


def schemat_3(answer: str):
    if answer == 'tak':
        print()
        for line in schemat_3_tak:
            print(line.strip())
        return True

    elif answer == 'nie':
        print()
        for line in schemat_3_nie:
            print(line.strip())
        return True

    else:
        raise TypeError


def schemat_4(answer: str):
    if answer == 'tak':
        print()
        for line in schemat_4_tak:
            print(line.strip())
        return True

    elif answer == 'nie':
        print()
        for line in schemat_4_nie:
            print(line.strip())

        print()
        for line in schemat_4_tak:
            print(line.strip())
        return True

    else:
        raise TypeError


def schemat_5(answer: int):
    if 1 <= int(answer) <= 5:
        return answer
    else:
        raise ValueError


def schemat_5a(risk: int):
    if 1 <= int(risk) <= 2:
        print()
        for line in schemat_5_1:
            print(line.strip())
        schemat_5_1.seek(0)

    elif 3 <= int(risk) <= 4:
        print()
        for line in schemat_5_2:
            print(line.strip())
        schemat_5_2.seek(0)

    elif 5 <= int(risk) <= 9:
        print()
        for line in schemat_5_3:
            print(line.strip())
        schemat_5_3.seek(0)

    elif 10 <= int(risk) <= 12:
        print()
        for line in schemat_5_4:
            print(line.strip())
        schemat_5_4.seek(0)

    elif int(risk) == 15:
        while True:
            print()
            for line in schemat_5_5:
                print(line.strip())

            schemat_5_5.seek(0)
            odp = pobierz_odp()

            if odp == 'tak':
                while True:
                    print()
                    for line in schemat_5_5_tak:
                        print(line.strip())

                    schemat_5_5_tak.seek(0)
                    odp = pobierz_odp()

                    if odp == 'tak':
                        return
                    elif odp == 'nie':
                        print('\nW takim razie kończę. Do usłyszenia!')
                        eval('zakoncz()')
                        exit()

                    else:
                        print(zla_odpowiedz)

            elif odp == 'nie':
                print()
                for line in schemat_5_5_nie:
                    print(line.strip())
                eval('zakoncz()')
                exit()

            else:
                print(zla_odpowiedz)

    elif 16 <= int(risk) <= 25:
        print()
        for line in schemat_5_6:
            print(line.strip())
        eval('zakoncz()')
        exit()

    else:
        print('\nNieprawidłowa wartość!')


def schemat_6(answer: str):
    if answer == 'tak':
        return True

    elif answer == 'nie':
        while True:
            print()
            for line in schemat_6_nie:
                print(line.strip())

            schemat_6_nie.seek(0)
            odp = pobierz_odp()

            if odp == 'tak':
                print('\nPrzejdźmy dalej.')
                return True

            elif odp == 'nie':
                print()
                for line in schemat_6_nie_nie:
                    print(line.strip())
                return False

            else:
                print(zla_odpowiedz)
    else:
        raise TypeError


def schemat_7(answer: str):
    if answer == 'tak':
        print()
        for line in schemat_7_tak:
            print(line.strip())
        return True

    elif answer == 'nie':
        print()
        for line in schemat_7_nie:
            print(line.strip())
        return True

    else:
        raise TypeError


def schemat_pytanie_23(answer: str):
    if answer == 'tak':
        return True

    elif answer == 'nie':
        print()
        for line in pytanie_23_nie:
            print(line.strip())
        return False

    else:
        raise TypeError


def schemat_pytanie_24(answer: str):
    if answer == 'tak':
        return True

    elif answer == 'nie':
        print()
        for line in pytanie_24_nie:
            print(line.strip())
        return False

    else:
        raise TypeError


def schemat_pytanie_27(answer: str):
    if answer == 'tak':
        return True

    elif answer == 'nie':
        print()
        for line in pytanie_27_nie:
            print(line.strip())
        return True

    else:
        raise TypeError


def schemat_pytanie_28(answer: str):
    if answer == 'tak':
        return True

    elif answer == 'nie':
        print()
        for line in pytanie_28_nie:
            print(line.strip())
        return True

    else:
        raise TypeError


def pobierz_odp():
    odpowiedz = input('[Odpowiedź]: ')
    odpowiedz = odpowiedz.lower()
    return odpowiedz


# Funkcja zamykająca wszystkie otwarte wcześniej pliki
def zakoncz():
    powitanie.close()
    powitanie_odmowa.close()
    powitanie_potwierdzenie.close()
    pytanie_1.close()
    pytanie_2.close()
    pytanie_3.close()
    pytanie_4.close()
    pytanie_4a.close()
    pytanie_4b.close()
    pytanie_4c.close()
    pytanie_4d.close()
    pytanie_4e.close()
    pytanie_4f.close()
    pytanie_4g.close()
    pytanie_4h.close()
    pytanie_4i.close()
    pytanie_4j.close()
    pytanie_4k.close()
    pytanie_4l.close()
    pytanie_4m.close()
    pytanie_4n.close()
    pytanie_4o.close()
    pytanie_5.close()
    pytanie_6.close()
    pytanie_7.close()
    pytanie_8.close()
    pytanie_8x.close()
    pytanie_9.close()
    pytanie_9x.close()
    pytanie_10.close()
    pytanie_10x.close()
    pytanie_11.close()
    pytanie_11x.close()
    pytanie_12.close()
    pytanie_12x.close()
    pytanie_13.close()
    pytanie_13x.close()
    pytanie_14.close()
    pytanie_14x.close()
    pytanie_15.close()
    pytanie_15x.close()
    pytanie_16.close()
    pytanie_16x.close()
    pytanie_17.close()
    pytanie_18.close()
    pytanie_19.close()
    pytanie_20.close()
    pytanie_21.close()
    pytanie_22.close()
    pytanie_23.close()
    pytanie_23_nie.close()
    pytanie_24.close()
    pytanie_24_nie.close()
    pytanie_25.close()
    pytanie_26.close()
    pytanie_27.close()
    pytanie_27_nie.close()
    pytanie_28.close()
    pytanie_28_nie.close()
    pytanie_29.close()
    schemat_1_nie.close()
    schemat_1_nie_nie.close()
    schemat_1_tak.close()
    schemat_2_nie.close()
    schemat_2_nie_nie.close()
    schemat_2_nie_tak.close()
    schemat_2_tak.close()
    schemat_3_nie.close()
    schemat_3_tak.close()
    schemat_4_nie.close()
    schemat_4_tak.close()
    schemat_5_1.close()
    schemat_5_2.close()
    schemat_5_3.close()
    schemat_5_4.close()
    schemat_5_5.close()
    schemat_5_5_tak.close()
    schemat_5_5_nie.close()
    schemat_5_6.close()
    schemat_6_nie.close()
    schemat_6_nie_nie.close()
    schemat_7_tak.close()
    schemat_7_nie.close()
