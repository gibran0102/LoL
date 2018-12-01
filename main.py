#!/usr/bin/python3
from summoner import Summon
import time 

def main(): 
    input_name = input('name of the summoner (only LAN): ')
    new_summon = Summon(input_name)   
    new_summon.matchs_ids()
    new_summon.match_info_data()
    new_summon.generate_map()

if __name__ == '__main__': main()