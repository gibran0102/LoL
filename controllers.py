import api as fetch


def summon_info(name):
    request = fetch.summon_info(name)
    return request['accountId']

def matches_ids(accountId):
    request = fetch.matches_ids(accountId)
    return [match['gameId'] for match in request['matches']]

def matches_info(ids, accountId):
    matchs = []
    identities_ids = []
    for id in ids:
        matchs.append(fetch.matches_info(id))
        for game in matchs:
            __indeparticipantIdentities = game['participantIdentities']
            __map_id = game['mapId']
            if __map_check(__map_id):
                for player in __indeparticipantIdentities:
                    if __identities_check(player, accountId):
                        identities_ids.append(player['participantId'])    
    return identities_ids
                        

def timeline(match_ids, identity_player):
    kill_pos = []
    dead_pos = []
    for id in match_ids:
        request = fetch.timeline(id)
        _organized_timeline(request['frames'], identity_player, kill_pos, dead_pos)

    return kill_pos, dead_pos

def _organized_timeline(frames, identity_player, kill_pos, dead_pos):
    for frame in frames:
        _timeline_events(frame['events'], identity_player, kill_pos, dead_pos)


def _timeline_events(events, identity_player, kill_pos, dead_pos):
    for event in events:
        if __event_type_check(event):
            for identity in identity_player:
                if __event_kill_check(event, identity):
                    kill_pos.append([event['position']['x'], event['position']['y']])                    
                if __event_dead_check(event, identity):
                    dead_pos.append([event['position']['x'], event['position']['y']])



def __map_check(map_id):
    if map_id == 11:
        return True
    else: 
        return False

def __event_type_check(event):
    if event['type'] == 'CHAMPION_KILL':
        return True
    else: 
        return False

def __event_kill_check(event, identity):
    if event['killerId'] == identity:
        return True
    else: 
        return False

def __event_dead_check(event, identity):
    if event['victimId'] == identity:
        return True
    else: 
        return False

def __identities_check(player, accountId):
    if player['player']['currentAccountId'] == accountId:
        return True
    else:
        return False
        