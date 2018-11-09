import requests as rq
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from time import sleep
import pandas as pd
import scipy.stats as ss
 
import random


#Local Files
from Global import api_key, entry_point


entry_point = entry_point
api_key = api_key


class Summon():

    def __init__(self, name): 
        self.name = name 
        self.account = None
        self.id = None
        self.ids = []
        self._data = []
        self.games = []
        self.killX = []
        self.killY = []
        self.deadX = []
        self.deadY = []
        self.img = mpimg.imread('maps/map1.png')

        self.init_fetch()    
        self.fetch_matches()
        

    def init_fetch(self): 
        request = rq.get('{}/lol/summoner/v4/summoners/by-name/{}?{}'.format(entry_point, self.name, api_key)).json()
        
        self.id = request['id']
        self.name = request['name']
        self.account = request['accountId']
    


    def fetch_matches(self):
        request = rq.get('{}/lol/match/v4/matchlists/by-account/{}?{}'.format(entry_point, self.account, api_key)).json()
        self.ids = [match['gameId'] for match in request['matches']]
        
    
    def info_match(self): 
        ids = self.ids[0:5]
        print(ids)
    
        for id in ids:
            requests = rq.get('{}/lol/match/v4/matches/{}?{}'.format(entry_point, id, api_key)).json()    
            self._data.append(requests)
            
        for games in self._data:
            _indeparticipantIdentities = games['participantIdentities']
            _mapId = games['mapId']
            if _mapId == 11:
                for player in _indeparticipantIdentities:
                    if player['player']['currentAccountId'] == self.account:
                        _id = player['participantId']
                        for id in ids: 
                            self.timeline(id, _id)

        
        self.draw_point()
                        
    def timeline(self, match, _id):
        request = rq.get('{}/lol/match/v3/timelines/by-match/{}?{}'.format(entry_point, match, api_key)).json()

        for frame in request['frames']:
            for event in frame['events']:
                if event['type'] == 'CHAMPION_KILL':
                    if event['killerId'] == _id:
                        self.killX.append(event['position']['x'])
                        self.killY.append(event['position']['y'])
                    if event['victimId'] == _id:
                        self.deadX.append(event['position']['x'])
                        self.deadY.append(event['position']['y'])


    def draw_point(self):

        plt.imshow(self.img, aspect='auto', extent=(-1000,14800,-570,14800))
        plt.axis([-1000, 14800,-570, 14800])
        plt.axis('off')
        plt.plot(self.killX,self.killY, '*', color='green', alpha=1.0, linewidth=.9, pickradius=0.9)
        plt.plot(self.deadX,self.deadY, 'X',  color='blue', alpha=.8, linewidth=3.9, pickradius=9.9)
        plt.savefig('test/{}_map.png'.format(self.name), format='png', transparent= True)
        plt.show()
    
    
                        

        
                            
                        
            
                    


            





    
        
    
