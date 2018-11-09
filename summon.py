import requests as rq
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import random

#Local Files

#entryPoint = https://la1.api.riotgames.com
#key = Riot developer api key
from Global import key, entryPoint 


class Summon():

    def __init__(self, name): 
        self.name = name 
        self.accountId = None
        self.ids = []
        self._data = []
        self.killX = []
        self.killY = []
        self.deadX = []
        self.deadY = []
        self.img = mpimg.imread('maps/map1.png')


        self.init_fetch()    
        self.fetch_matches()
        self.info_match()
        
    def init_fetch(self): 
        request = rq.get('{}/lol/summoner/v4/summoners/by-name/{}?{}'.format(entryPoint, self.name, key)).json()
        self.accountId = request['accountId']

    def fetch_matches(self):
        request = rq.get('{}/lol/match/v4/matchlists/by-account/{}?{}'.format(entryPoint, self.accountId, key)).json()
        self.ids = [match['gameId'] for match in request['matches']]
        
    
    def info_match(self): 
        ids = self.ids[0:1]

        for id in ids:
            self._data.append(rq.get('{}/lol/match/v4/matches/{}?{}'.format(entryPoint, id, key)).json())
            for games in self._data:
                _indeparticipantIdentities = games['participantIdentities']
                _mapId = games['mapId']
                if _mapId == 11:
                    for player in _indeparticipantIdentities:
                        if player['player']['currentAccountId'] == self.accountId:
                            _id = player['participantId']
                            self.timeline(id, _id)
        self.draw_point()
                        
    def timeline(self, match, _id):
        request = rq.get('{}/lol/match/v3/timelines/by-match/{}?{}'.format(entryPoint, match, key)).json()

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
        id = random.randint(1,21)*5
        print(id)
        
        plt.imshow(self.img, aspect='auto', extent=(-1000,14800,-570,14800))
        plt.axis([-1000, 14800,-570, 14800])
        
        plt.axis('off')
        
        plt.plot(self.killX,self.killY, 'o', color='green', linewidth=5.9)
        plt.plot(self.deadX,self.deadY, '+',  color='blue', linewidth=5.9)

        plt.savefig('test/{}{}_map.png'.format(self.name, id), format='png', transparent= True)
        plt.show()
    
    
                        

        
                            
                        
            
                    


            





    
        
    
