import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random

from controllers import *
from map import Map


IMAGE = mpimg.imread('maps/map1.png')

class Summon():
    def __init__(self, name):
        self.name = name
        self.accountId = summon_info(name)
        self.matches_ids = []
        self.summon_identities = []
        self.timeline_position_kill = []
        self.timeline_position_dead = []
        self.map = Map()

    def matchs_ids(self):
        self.matches_ids = matches_ids(self.accountId)
    
    def match_info_data(self): 
        max_ids = self.matches_ids[:3]
        self.summon_identities.extend(matches_info(max_ids, self.accountId))
        self.timeline_position_kill, self.timeline_position_dead = timeline(max_ids, self.summon_identities)

    def show_map(self):
        self.map.generate(self.timeline_position_kill, self.timeline_position_dead)
        self.map.show()
    
    def save_map(self):
        self.map.save(self.name)