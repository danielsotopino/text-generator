import operator
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# trends = twitter.get_available_trends()

# Chile 23424782

# Chile Stgo 349859

trends = twitter.get_place_trends(id=23424782)

# trends[0]["trends"].sort(key=operator.itemgetter('tweet_volume'), reverse=True)

filtered_trends = trends[0]["trends"][0:4]

for trend in filtered_trends:

    print(trend["name"].encode("utf-8") + ' -filter:retweets AND -filter:replies AND -filter:links')
    
    results = twitter.search(q=trend["name"].encode("utf-8") + ' -filter:retweets AND -filter:replies AND -filter:links', count=1000, lang="es", include_entities=False, result_type="recent", tweet_mode="extended")

    f = open("/home/pi/projects/text-generator/results.txt", "a+")

    for status in results["statuses"]:
        f.write(status["full_text"].encode("utf-8"))
        f.write("\r\n")


f.close()