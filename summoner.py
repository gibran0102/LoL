import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from controllers import *
from map import Map

class Summon():
    def __init__(self, name):
        self.name = name
        self.accountId = summon_info(name)
        self.matches_ids = []
        self.summon_identities = []
        self.position_kill = []
        self.position_dead = []
        self.map = Map()

    def matchs_ids(self):
        self.matches_ids = matches_ids(self.accountId)
    
    def match_info_data(self): 
        max_ids = self.matches_ids[:1]
        self.summon_identities.extend(matches_info(max_ids, self.accountId))
        self.position_kill, self.position_dead = timeline(max_ids, self.summon_identities)

    def show_map(self):
        self.map.generate(self.position_kill, self.position_dead)
        self.map.show()
    
    def save_map(self):
        self.map.save(self.name)