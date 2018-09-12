import tweepy	
import random
import time
import sys
import auth
import time
import datetime
import analysis
used = open("scores.txt","r")

consumer_key        = auth.consumer_key
consumer_secret     = auth.consumer_secret
access_token        = auth.access_token
access_token_secret = auth.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def tweet_downloader():
    search_query = "TLRY"
    max_tweets = 10000
    tweets_per_qry = 100
    fname = 'tweets.txt'
    sinceID = None
    max_id = -1
    tweetCount = 0
    print("Downloading max {0} tweets".format(max_tweets))
    with open(fname,'w') as f:
        while tweetCount < max_tweets:
            try:
                if (max_id <= 0):
                    if (not sinceID):
                        new_tweets = api.search(q=search_query, count=tweets_per_qry)
                    else:
                        new_tweets = api.search(q=search_query,count=tweets_per_qry,sinceID=sinceID)
                else:
                    if (not sinceID):
                        new_tweets = api.search(q=search_query, count=tweets_per_qry,max_id=str(max_id -1))
                    else:
                        new_tweets = api.search(q=search_query, count=tweets_per_qry,max_id=str(max_id -1),sinceID=sinceID)
                if not new_tweets:
                    print("no new tweets found")
                    break
                for tweet in new_tweets:
                    f.write(tweet.full_text)
#                    f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
#                            '\n')
                tweetCount += len(new_tweets)
                print("Downloaded {0} tweets".format(tweetCount))
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                break
    print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))

#tweet_downloader()

def main_function():
    search = ["TLRY","PANW"]
    numberOfTweets = 100
    scores_list = []
    tweet_count = 0
    for phrase in search:
        for tweet in tweepy.Cursor(api.search,q=phrase,result_type="recent",tweet_mode='extended',lang="en").items(numberOfTweets):
            try:
                tweet_count = tweet_count + 1
                print(tweet_count)
#                print('Tweet by: @'+tweet.user.screen_name)
                text = tweet.full_text
#                print(text)
                qualified = analysis.qualify(text)
#                print(qualified)
                if qualified == True:
                    split = analysis.tweet_splitter(text)
                    score = analysis.total_score(split)
                    scores_list.append(score)
                    print(text)
                    print(score)
            except tweepy.TweepError as e:
            	print(e.reason)
            except StopIteration:
            	break
#        else:
#        	break
        print("scores list for : ",phrase, scores_list)
        used = open("scores.txt","a")
        now = datetime.datetime.now()
        used.write(str(now.strftime("%Y-%m-%d %H:%M")))
        used.write(" ")
        used.write("Tracking: "+ phrase)
        used.write(str(scores_list))
        used.write("\n")
        total_score = 0
        for num in scores_list:
            total_score = total_score + num
        if len(scores_list) != 0:
            average = total_score / len(scores_list)
        else:
            average = 0
        used.write("average: " + str(average) + " ")
        used.write("\n")
        used.write("Score list len: " + str(len(scores_list)))
        used.write("\n")
        scores_list = []
    sys.stdout.close()

main_function()

                