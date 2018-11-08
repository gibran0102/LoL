from summon import Summon


def main(): 
    input_name = input('Nombre del invocador (solo LAN): ')
    search = Summon(input_name)

    matches = search.fetch_matches()

    print(len(matches))
        


if __name__ == '__main__': main()