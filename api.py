import requests as rq
from keys import KEY, ENTRY_POINT

def summon_info(name):
    return rq.get('{}/lol/summoner/v4/summoners/by-name/{}?api_key={}'.format(ENTRY_POINT, name, KEY)).json()

def matches_ids(accountId):
    return rq.get('{}/lol/match/v4/matchlists/by-account/{}?api_key={}'.format(ENTRY_POINT, accountId, KEY)).json()

def matches_info(id):
    return rq.get('{}/lol/match/v4/matches/{}?api_key={}'.format(ENTRY_POINT, id, KEY)).json()

def timeline(id):
    return rq.get('{}/lol/match/v4/timelines/by-match/{}?api_key={}'.format(ENTRY_POINT, id, KEY)).json()