import tweepy
import botometer

def authenticateOnTwitter(consumer_key, consumer_secret, token_key, token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token_key, token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    try:
        api.verify_credentials()
        print("Authentication ok!")
    except:
        print("Error during authentication")
        exit()

    return api

def authenticateOnBotometer(rapidapi_key, twitter_app_auth):
    return botometer.Botometer(wait_on_ratelimit=True, rapidapi_key=rapidapi_key, **twitter_app_auth)
