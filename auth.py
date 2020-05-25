from dotenv import load_dotenv
import os
load_dotenv()

consumer_key = os.getenv('twitter_text_generator_consumer_key')
consumer_secret = os.getenv('twitter_text_generator_consumer_secret')
access_token = os.getenv('twitter_text_generator_access_token')
access_token_secret = os.getenv('twitter_text_generator_access_token_secret')