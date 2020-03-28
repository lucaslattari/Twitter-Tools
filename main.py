from argparse import ArgumentParser
import sys
import tweepy
import botometer
from tqdm import tqdm
import json

def oauth_login(consumer_key, consumer_secret, token_key, token_secret):
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

def replyProbBotOfMentions(api, rapidapi_key, twitter_app_auth):
    bom = botometer.Botometer(wait_on_ratelimit=True, rapidapi_key=rapidapi_key, **twitter_app_auth)

    tweets = api.mentions_timeline()
    for tweet in tweets:
        #print(tweet.id)

        result = bom.check_account('@' + tweet.user.screen_name)
        percent = result["cap"]["universal"] * 100.0

        print(tweet.user.screen_name, percent)

        msg = "Oi @" + tweet.user.screen_name + ", você tem " + str(percent) + "% de chance de ser bot. Bjomeliga!"
        api.update_status(
                        msg,
                        in_reply_to_status_id=tweet.id,
                        auto_populate_reply_metadata=True
                    )
        print(msg, tweet.user.screen_name)

def searchForBots(api, userSearched, rapidapi_key, twitter_app_auth):
    fName = "tweetsJson.txt"
    tweetCount = 0
    maxTweets = 10000000
    max_id = -1
    sinceId = None
    searchQuery = userSearched
    tweetsPerQry = 100
    print("Downloading max {0} tweets".format(maxTweets))

    bom = botometer.Botometer(wait_on_ratelimit=True, rapidapi_key=rapidapi_key, **twitter_app_auth)

    while tweetCount < maxTweets:
        if (max_id <= 0):
            if (not sinceId):
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
            else:
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        since_id=sinceId)
        else:
            if (not sinceId):
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        max_id=str(max_id - 1))
            else:
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        max_id=str(max_id - 1),
                                        since_id=sinceId)
        if not new_tweets:
            print("No more tweets found")
            break
        for tweet in new_tweets:
            response = bom.check_account('@' + tweet.user.screen_name)
            #nota de 0 a 5 (5 é bot, 0 é humano)
            probOfBeingBot = response["display_scores"]["universal"]

            print(tweet.user.screen_name, probOfBeingBot, tweet.text)
            if probOfBeingBot > 2.5:
                print("BLOCK!")
                api.create_block(tweet.user.screen_name)
            f = open(fName, 'a+')
            f.write(json.dumps(tweet._json))
            f.write("\n\n")
            f.close()

        tweetCount += len(new_tweets)
        print("Downloaded {0} tweets".format(tweetCount))
        max_id = new_tweets[-1].id

    print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))

def init(args):
    api = oauth_login(args.consumer_key, args.secret_key, args.token_key, args.token_secret)
    #api.update_status("Esse tweet foi feito por um bot. Respondam aqui pra eu testar! #OBrasilTemQuePararBolsonaro")

    rapidapi_key = args.rapid_key
    twitter_app_auth = {
        'consumer_key': args.consumer_key,
        'consumer_secret': args.secret_key,
        'access_token': args.token_key,
        'access_token_secret': args.token_secret,
    }

    #replyProbBotOfMentions(api, rapidapi_key, twitter_app_auth)
    searchForBots(api, '@oatila', rapidapi_key, twitter_app_auth)


if __name__ == "__main__":
    parser = ArgumentParser(description = 'Silencia ou bloqueia contas automaticamente / Automatically blocks or mutes accounts')
    parser.add_argument('consumer_key', help = 'Chave consumidora / Consumer key')
    parser.add_argument('secret_key', help = 'Chave secreta / Secret key')
    parser.add_argument('token_key', help = 'Chave de token / Token key')
    parser.add_argument('token_secret', help = 'Token secreto / Token secret')
    parser.add_argument('rapid_key', help = 'Chave Rapid API / Key rapid API')

    if len(sys.argv) < 6:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    init(args)
