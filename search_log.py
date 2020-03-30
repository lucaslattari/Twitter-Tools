from argparse import ArgumentParser
import sys
import json
from authentication import *

def generateLog(api, query, filename, twitter_app_auth):
    tweetCount = 0
    maxTweets = 10000000
    max_id = -1
    sinceId = None
    searchQuery = userSearched
    tweetsPerQry = 100
    print("Downloading max {0} tweets".format(maxTweets))

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
            f = open(filename, 'a+')
            f.write(json.dumps(tweet._json))
            f.write("\n\n")
            f.close()

        tweetCount += len(new_tweets)
        print("Downloaded {0} tweets".format(tweetCount))
        max_id = new_tweets[-1].id

    print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, filename))

def init(args):
    if(args.token_secret is None and args.token_key is None):
        api, token_key, token_secret = authenticateOnTwitterWithoutToken(args.consumer_key, args.secret_key)
    else:
        api = authenticateOnTwitterWithToken(args.consumer_key, args.secret_key, args.token_key, args.token_secret)
        token_key = args.token_key
        token_secret = args.token_secret

    twitter_app_auth = {
        'consumer_key': args.consumer_key,
        'consumer_secret': args.secret_key,
        'access_token': token_key,
        'access_token_secret': token_secret,
    }

    generateLog(api, args.query, args.log_file, twitter_app_auth)

if __name__ == "__main__":
    parser = ArgumentParser(description = 'Gera um relatório a partir de algum termo buscado no Twitter / Generates a report from terms searched on Twitter')
    parser.add_argument('consumer_key', help = 'Chave consumidora / Consumer key')
    parser.add_argument('secret_key', help = 'Chave secreta / Secret key')
    parser.add_argument('query', help = 'Termos buscados / Searched terms')
    parser.add_argument('-tk', dest='token_key', default = None, help = 'Chave de token / Token key')
    parser.add_argument('-ts', dest='token_secret', default = None, help = 'Token secreto / Token secret')
    parser.add_argument('-f', dest='log_file', default = 'report.json', help="Nome do arquivo de saída contendo o relatório em formato json / Name of the output file containing the report in json format")

    if len(sys.argv) < 3:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    init(args)
