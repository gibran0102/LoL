import sys
from summoner import Summon

def main(): 
    
    if sys.argv[1]:
        input_name = sys.argv[1]
        
    summon = Summon(input_name)   
    summon.matchs_ids()
    summon.match_info_data()
    summon.show_map()
    summon.save_map()


    
    

if __name__ == '__main__': 
    main()


