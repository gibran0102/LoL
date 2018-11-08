import requests as rq
import numpy as np

#Local Files
from Global import api_key, entry_point


class Summon():

    def __init__(self, name): 
        self.entry_point = entry_point
        self.api_key = api_key
        self.name = name 
        self.account = None
        self.id = None
        self.list_matches_ids = []
        self.champions_used = []
        self.lanes = []


        self.init_fetch()    
        self.fetch_matches()

    def init_fetch(self): 
        request = rq.get('{}/lol/summoner/v4/summoners/by-name/{}?{}'.format(self.entry_point, self.name, self.api_key)).json()
        
        self.id = request['id']
        self.name = request['name']
        self.account = request['accountId']
    


    def fetch_matches(self):
        request = rq.get('{}/lol/match/v4/matchlists/by-account/{}?{}'.format(self.entry_point, self.account, self.api_key)).json()

        self.list_matches_ids = [match['gameId'] for match in request['matches']]
        self.champions_used =  [match['champion'] for match in request['matches']]
        self.lanes = [match['lane'] for match in request['matches']]

        return { 'ids': self.list_matches_ids, 'champions': self.champions_used, 'lanes': self.lanes }

    
        
    
