import requests as rq
from Global import KEY, ENTRY_POINT



def summon_info(name):
    return rq.get('{}/lol/summoner/v3/summoners/by-name/{}?{}'.format(ENTRY_POINT, name, KEY)).json()

def matches_ids(accountId):
    return rq.get('{}/lol/match/v3/matchlists/by-account/{}?{}'.format(ENTRY_POINT, accountId, KEY)).json()

def matches_info(id):
    return rq.get('{}/lol/match/v3/matches/{}?{}'.format(ENTRY_POINT, id, KEY)).json()

def timeline(id):
    return rq.get('{}/lol/match/v4/timelines/by-match/{}?{}'.format(ENTRY_POINT, id, KEY)).json()