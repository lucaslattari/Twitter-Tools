from argparse import ArgumentParser
import sys
import json
from authentication import *

def log_tweep_error(tweep_error):
    if tweep_error.api_code:
        if tweep_error.api_code == 32:
            print("\nError: invalid API authentication tokens")
        elif tweep_error.api_code == 34:
            print("\nError: requested object (user, Tweet, etc) not found")
        elif tweep_error.api_code == 64:
            print("\nError: your account is suspended and is not permitted")
        elif tweep_error.api_code == 130:
            print("\nError: Twitter is currently in over capacity")
        elif tweep_error.api_code == 131:
            print("\nError: internal Twitter error occurred")
        elif tweep_error.api_code == 135:
            print("\nError: could not authenticate your API tokens")
        elif tweep_error.api_code == 136:
            print("\nError: you have been blocked to perform this action")
        elif tweep_error.api_code == 179:
            print("\nError: you are not authorized to see this Tweet")
        elif tweep_error.api_code == 404:
            print("\nError: The URI requested is invalid or the resource requested, such as a user, does not exist. ")
        elif tweep_error.api_code == 429:
            print("\nError: request cannot be served due to the app rate limit having been exhausted for the resource.")
        else:
            print("\nError while using the REST API:", tweep_error)
    else:
        print("\nError with Twitter:", tweep_error)

def downloadTweets(api, filename):
    for tweet in tweepy.Cursor(api.user_timeline).items():
        try:
            f = open(filename, 'a+')
            f.write(json.dumps(tweet._json))
            f.write("\n\n")
            f.close()
        except tweepy.TweepError as e:
            log_tweep_error(e)

def init(args):
    if(args.token_secret is None and args.token_key is None):
        twitterApi, token_key, token_secret = authenticateOnTwitterWithoutToken(args.consumer_key, args.secret_key)
    else:
        twitterApi = authenticateOnTwitterWithToken(args.consumer_key, args.secret_key, args.token_key, args.token_secret)
        token_key = args.token_key
        token_secret = args.token_secret

    downloadTweets(twitterApi, args.log_file)

if __name__ == "__main__":
    parser = ArgumentParser(description = 'Realiza o download de seus tweets / Download your tweets')
    parser.add_argument('consumer_key', help = 'Chave consumidora / Consumer key')
    parser.add_argument('secret_key', help = 'Chave secreta / Secret key')
    parser.add_argument('-tk', dest='token_key', default = None, help = 'Chave de token / Token key')
    parser.add_argument('-ts', dest='token_secret', default = None, help = 'Token secreto / Token secret')
    parser.add_argument('-f', dest='log_file', default = 'download.json', help="Nome do arquivo de saída contendo o relatório em formato json / Name of the output file containing the report in json format")

    if len(sys.argv) < 2:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    init(args)
