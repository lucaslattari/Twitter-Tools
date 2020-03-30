from argparse import ArgumentParser
import sys
import json
from authentication import *

'''
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
'''

def searchAndBlock(twitterApi, botometerObject, userSearched, filename, bot_threshold):
    tweetCount = 0
    maxTweets = 10000000
    max_id = -1
    sinceId = None
    searchQuery = userSearched
    tweetsPerQry = 100
    print("Searching max {0} tweets".format(maxTweets))

    while tweetCount < maxTweets:
        if (max_id <= 0):
            if (not sinceId):
                new_tweets = twitterApi.search(q=searchQuery, count=tweetsPerQry)
            else:
                new_tweets = twitterApi.search(q=searchQuery, count=tweetsPerQry,
                                        since_id=sinceId)
        else:
            if (not sinceId):
                new_tweets = twitterApi.search(q=searchQuery, count=tweetsPerQry,
                                        max_id=str(max_id - 1))
            else:
                new_tweets = twitterApi.search(q=searchQuery, count=tweetsPerQry,
                                        max_id=str(max_id - 1),
                                        since_id=sinceId)
        if not new_tweets:
            print("No more tweets found")
            break
        for tweet in new_tweets:
            response = botometerObject.check_account('@' + tweet.user.screen_name)
            #nota de 0 a 5 (5 é bot, 0 é humano)
            probOfBeingBot = response["display_scores"]["universal"]

            print(tweet.user.screen_name, probOfBeingBot, tweet.text)
            wasBlocked = False
            if probOfBeingBot > bot_threshold:
                wasBlocked = True
                twitterApi.create_block(tweet.user.screen_name)

            d = {}
            d["username"] = tweet.user.screen_name
            d["score"] = probOfBeingBot
            d["tweet"] = tweet._json
            d["wasBlocked"] = wasBlocked

            f = open(filename, 'a+')
            f.write(json.dumps(d))
            f.write("\n\n")
            f.close()

        tweetCount += len(new_tweets)
        print("Searched {0} tweets".format(tweetCount))
        max_id = new_tweets[-1].id

    print ("Searched {0} tweets, Saved to {1}".format(tweetCount, filename))

def init(args):
    if(args.token_secret is None and args.token_key is None):
        api, token_key, token_secret = authenticateOnTwitterWithoutToken(args.consumer_key, args.secret_key)
    else:
        api = authenticateOnTwitterWithToken(args.consumer_key, args.secret_key, args.token_key, args.token_secret)
        token_key = args.token_key
        token_secret = args.token_secret

    rapidapi_key = args.rapid_key
    twitter_app_auth = {
        'consumer_key': args.consumer_key,
        'consumer_secret': args.secret_key,
        'access_token': token_key,
        'access_token_secret': token_secret,
    }
    botometerObj = authenticateOnBotometer(rapidapi_key, twitter_app_auth)

    searchAndBlock(twitterApi, botometerObj, args.username, args.block_file, args.bot_threshold)

if __name__ == "__main__":
    parser = ArgumentParser(description = 'Gera um relatório a partir de algum termo buscado no Twitter / Generates a report from terms searched on Twitter')
    parser.add_argument('consumer_key', help = 'Chave consumidora / Consumer key')
    parser.add_argument('secret_key', help = 'Chave secreta / Secret key')
    parser.add_argument('rapid_key', help = 'Chave Rapid API / Key rapid API')
    parser.add_argument('username', help = 'Usuário buscado / Searched usename')
    parser.add_argument('-tk', dest='token_key', default = None, help = 'Chave de token / Token key')
    parser.add_argument('-ts', dest='token_secret', default = None, help = 'Token secreto / Token secret')
    parser.add_argument('-f', dest='block_file', default = 'block.json', help="Nome do arquivo de saída contendo o relatório em formato json / Name of the output file containing the report in json format")
    parser.add_argument('-b', action = 'store', dest = 'bot_threshold', type = float, default = 2.5, required = False,
                        help = 'Limiar que define quando um usuário será bloqueado / Threshold that defines when a user will be blocked')

    if len(sys.argv) < 4:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    init(args)
