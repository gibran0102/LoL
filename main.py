from summoner import Summon


def main(): 
    input_name = input('name of the summoner (only LAN): ')

    summon = Summon(input_name)   
    summon.matchs_ids()
    summon.match_info_data()



if __name__ == '__main__': main()