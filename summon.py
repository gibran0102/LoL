import requests as rq
import numpy as np
from time import sleep

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
        ids = self.ids[:3]
        print(ids)
        playerIdentitie = []
        
        for id in ids:
            requests = rq.get('{}/lol/match/v4/matches/{}?{}'.format(entry_point, id, api_key)).json()    
            self._data.append(requests)
            
        for games in self._data:
            _indeparticipantIdentities = games['participantIdentities']
            for player in _indeparticipantIdentities:
                if player['player']['currentAccountId'] == self.account:
                    _id = player['participantId']
                    for game in games['participants']:    
                        if game['participantId'] == _id: 
                            self.games.append(game)


        for history in self.games:
            print(history['stats']['kills'])
                            
                        
            
                    


            





    
        
    
