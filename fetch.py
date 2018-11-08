import requests as rq 

from key import key

class Fetch():
    def __init__(self, name):
        self._name = name
        self.entry_point = 'https://la1.api.riotgames.com'
        self.api_key = 'api_key={}'.format(key)
    
    def get_user_info(self):
        request = rq.get('{}/lol/summoner/v4/summoners/by-name/{}?{}'.format(self.entry_point, self._name, self.api_key))
        
        return request.json()
