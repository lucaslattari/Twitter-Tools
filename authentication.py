import tweepy
import botometer
import webbrowser

def authenticateOnTwitterWithToken(consumer_key, consumer_secret, token_key, token_secret):
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

def authenticateOnTwitterWithoutToken(consumer_key, consumer_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()

    print("Vou abrir uma janela do seu navegador. Logue-se por ela no Twitter, autorize o uso desse app.")
    webbrowser.open(auth_url)
    verify_code = input("Digite o código de verificação informado pelo Twitter > ")
    auth.get_access_token(verify_code)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    try:
        api.verify_credentials()
        print("Authentication ok!")
    except:
        print("Error during authentication")
        exit()

    return api, auth.access_token, auth.access_token_secret

def authenticateOnBotometer(rapidapi_key, twitter_app_auth):
    return botometer.Botometer(wait_on_ratelimit=True, rapidapi_key=rapidapi_key, **twitter_app_auth)
