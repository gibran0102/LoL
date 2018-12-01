import requests as rq
from Global import KEY, ENTRY_POINT



def fetch_summon(name):
    return rq.get('{}/lol/summoner/v3/summoners/by-name/{}?{}'.format(ENTRY_POINT, name, KEY)).json()

def fetch_matches_ids(accountId):
    return rq.get('{}/lol/match/v3/matchlists/by-account/{}?{}'.format(ENTRY_POINT, accountId, KEY)).json()

def fetch_matches_info(id):
    return rq.get('{}/lol/match/v3/matches/{}?{}'.format(ENTRY_POINT, id, KEY)).json()

def fetch_timeline(id):
    return rq.get('{}/lol/match/v4/timelines/by-match/{}?{}'.format(ENTRY_POINT, id, KEY)).json()