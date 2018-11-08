from summon import Summon


def main(): 
    input_name = input('Nombre del invocador (solo LAN): ')
    search = Summon(input_name)
    print(search.fetch_matches())
        


if __name__ == '__main__': main()