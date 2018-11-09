from summon import Summon

def main(): 
    input_name = input('name of the summoner (only LAN):  ')
    search = Summon(input_name)

if __name__ == '__main__': main()