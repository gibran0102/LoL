import sys
from summoner import Summon

def main(): 
    
    if sys.argv[1]:
        input_name = sys.argv[1]
    else:
        input_name = input('name of the summoner (only LAN): ')

    summon = Summon(input_name)   
    summon.matchs_ids()
    summon.match_info_data()
    summon.show_map()
    summon.save_map()
    
    

if __name__ == '__main__': 
    main()


