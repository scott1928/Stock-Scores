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


def main_function():
    search = ["TLRY","PANW","APH","ATRS","TNDM","$VOD","$MU","$SQ","$OGI"]
    numberOfTweets = 200
    scores_list = []
    tweet_count = 0
    for phrase in search:
        filterd = phrase + " -filter:retweets"
        for tweet in tweepy.Cursor(api.search,q=filterd,result_type="recent",tweet_mode='extended',lang="en").items(numberOfTweets):
            try:
                tweet_count = tweet_count + 1              
                text = tweet.full_text
                qualified = analysis.qualify(text)
                if qualified == True:
                    split = analysis.tweet_splitter(text)
                    score = analysis.total_score(split)
                    scores_list.append(score)
                    print("Checked Tweet #" + str(tweet_count))
                    print('Tweet by: @'+tweet.user.screen_name)
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
        message = phrase + ":" + str(scores_list) + " Average: " + str(average) + " length: " + str(len(scores_list))
        api.update_status(status=message)
        print("Tweeted: {}".format(message))
        scores_list = []  
    sys.stdout.close()

main_function()

                