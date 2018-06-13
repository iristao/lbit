try:
    import json
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream                                                                                                                
from twitter import OAuth             

#CONSUMER_KEY = 'M0nXx9qhVD6LioMfGDAHUnpsz'                                                                                                                                            
#CONSUMER_SECRET = 'fOgwzeQnxt5JwwIouH9g6vpwjCNORdv16vPCJiH9FxPTpvJcG9'
#ACCESS_KEY = '713426597060222976-sFHTL2QG6Y2dBM7go96v5koc4VyZaj2'
#ACCESS_SECRET = 'Xh1lo49s1viG5sjbAz8l3BbIjAIsog4GahYz7MKhyuIvN'

CONSUMER_KEY = 'R3iCiAD1k64u5sFMQMvXhD8Aw'
CONSUMER_SECRET = 'Vy1PmgU56iKQqg1FRbvre6Ejb35JZKQLGA8dhWCwJvtK3QSFZs'
ACCESS_KEY = '1005478089420410880-Sqd5aNafKjbCUqtENgLRpP6V5iycp0'
ACCESS_SECRET = 'grwWZNG4XnyUib3NGCPdPGDLYsh4EAv9pRAwGPak0kGmw'
#import twitter
t = Twitter(auth = OAuth(ACCESS_KEY, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

#t.direct_messages.new(user="dimitriy_l21", text="I sent this from the command line")

def recent():
    collect = t.search.tweets(q="#escalator", count=5, result_type="recent")
#t = api.GetSearch(term="#escalator", result_type="recent", return_json=True, include_entities=True, count="1")
    collect_id = collect["statuses"][0]["id"]
#print collect_id
    collect_handle = collect["statuses"][0]["user"]["screen_name"]

    collect_url = "https://twitter.com/" + collect_handle + "/status/" + str(collect_id)
#print collect_url
    t_embed = t.statuses.oembed(url=collect_url)
    fin_prod = t_embed["html"]
#print fin_prod
    return fin_prod


def update():
    timeline = t.search.tweets(q="StuyTracker", count=5, result_type="recent")
    print timeline

    
    timeline_id = timeline["statuses"][0]["id"]
    print timeline_id


    timeline_url = "https://twitter.com/StuyTracker/status/" + str(timeline_id)
    print timeline_url

    
    time_embed = t.statuses.oembed(url=timeline_url)
    time_prod = time_embed["html"]
    print time_prod
    return time_prod

def tweet_out(textual):
    t.statuses.update(status=textual)




