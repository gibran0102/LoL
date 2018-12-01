import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random

from controllers import *

IMAGE = mpimg.imread('maps/map1.png')

class Summon():
    def __init__(self, name):
        self.name = name
        self.accountId = summon_info(name)
        self.matches_ids = []
        self.summon_identities = []
        self.timeline_position_Kill = []
        self.timeline_position_dead = []

    
    def matchs_ids(self):
        self.matches_ids = matches_ids(self.accountId)
    
    def match_info_data(self): 
        l = self.matches_ids[:3]
        self.summon_identities.extend(matches_info(l, self.accountId))
        self.timeline_position_Kill, self.timeline_position_dead = timeline(l, self.summon_identities)


    def generate_map(self):
        id = random.randint(1,21)*5
        plt.imshow(IMAGE, aspect='auto', extent=(-120,14820, -120,14881))
        plt.axis([-120, 14820, -120, 14881])
        plt.axis('off')
        plt.plot(*zip(*self.timeline_position_Kill), 'o', color='green', linewidth=5.9, ls='')    
        plt.plot(*zip(*self.timeline_position_dead), '+',  color='blue', linewidth=5.9)
        plt.savefig('test/{}{}_map.png'.format(self.name, id), format='png', transparent= True)
        plt.show()
        