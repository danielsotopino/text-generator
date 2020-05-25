import markovify
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def get_text_model(filename):
    # Get raw text as string.
    with open(filename) as f:
        text = f.read()
    open(filename, 'w').close()
    # print(text)
    # Build the model.
    return markovify.Text(text)

def post_tweet(text, twitter):
    print('tweeting: {}'.format(tweet))
    twitter.update_status(status=tweet)

def main():

    twitter_credentials = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    for x in range(0, 4):
        filename = "/home/pi/projects/text-generator/results_{}.txt".format(x)
        text_model = get_text_model(filename)
        tweet = text_model.make_short_sentence(280)
        post_tweet(tweet, twitter_credentials)

# Print five randomly-generated sentences
# for i in range(1):
#     print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
# for i in range(1):
#     print(text_model.make_short_sentence(280))


if __name__ == '__main__':
   main()