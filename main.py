# Dronebot
# Plik główny - tutaj program się zaczyna i tutaj kończy działanie

import pytania as p


def main():
    # Powitanie
    odp = p.powitaj()

    if odp == 'tak':
        # Przechodzimy do pierwszego pytania
        p.pytaj()
    elif odp == 'nie':
        # Upewniamy się czy użytkownik chce kontynuować
        odp = p.potwierdzenie()

        if odp == 'tak':
            # Przechodzimy do pierwszego pytania
            p.pytaj()
        elif odp == 'nie':
            # Koniec programu
            p.odmowa()

    p.zakoncz()


if __name__ == '__main__':
    main()
