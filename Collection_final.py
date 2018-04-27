import tweepy
import csv
import os
import time
import json
#import time
from pymongo import MongoClient
import mysql.connector
MONGO_HOST= 'mongodb://localhost/twitterdb'

ckey = "p1T0Z0T2dLZb9w27SeFZObHmV"
csecret = "xFg4Vx5XtRVskJwxG8ClQFcmUXVDQnB8Z1FF2KiRHet1EMeFMz"
atoken = "930697484611084289-xB9QEioVC8ffKEt78F0v2lqDyPDJ4Wl"
asecret = "5j21028VYCxCXFhLRGe6818RXEp4MsdtOpvTaIlEHk2dV"

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,
    'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)

db=mysql.connector.connect(user ='root', password= 'root', host = 'localhost', database='twitter_data')
cur=db.cursor();


file_exists = os.path.isfile('D:\work\Parsing\data1.csv')
csvFile = open('data1.csv', 'ab')
fields = ('Tweet_Id', 'Tweet_Text','Tweet_authorscreen_name','Tweet_author_id','Tweet_created_at','Tweet_coordinates','Tweet_source','Tweet_user_verified','Tweet_retweet_count','Tweet_lang','Tweet_favcount','Tweet_username','Tweet_userid','Tweet_location') #field names
csvWriter = csv.DictWriter(csvFile, fieldnames=fields)
if not file_exists:
    csvWriter.writeheader()
    
c = tweepy.Cursor(api.search, q="#Airtel",since="2018-04-12", until="2018-04-18", lang="en", tweet_mode="extended").items()

count=0;
while True:
    try:
        tweet = c.next()
        for tweet in tweepy.Cursor(api.search, q="#Airtel",since="2018-04-12", until="2018-04-18", tweet_mode="extended").items():
            tw_id=str(tweet.id_str)+str("L")
            tw_text=tweet.full_text.replace('\n', '').replace('\r', ' ').strip()
            tw_uscreen_name=tweet.author.screen_name
            tw_uid=str(tweet.author.id)+str("L")
            tw_crdate=tweet.created_at
            tw_source=tweet.source
            tw_rtcount=tweet.retweet_count
            tw_lang=tweet.lang
            tw_favcount=tweet.user.favourites_count
            tw_uname=tweet.user.name
            tw_uid=tweet.user.id_str

            if tweet.user.verified==True:
                tw_isver=1
            else:
                tw_isver=0
            print tw_id
            print tw_text
            print tw_uscreen_name
            print "tw_isver===", tw_isver
            print tw_uid
            print tw_crdate
            print tw_uname

            print "\n\n"
            time.sleep(2)
            
            #print (tweet.id_str, (tweet.full_text.encode('utf-8').replace('\n', '').replace('\r', ' ').strip()), tweet.author.screen_name, tweet.author.id, tweet.created_at,tweet.source,tweet.user.verified,tweet.retweet_count,tweet.lang,tweet.user.favourites_count,tweet.user.name,tweet.user.id_str,tweet.user.location)
    
            try:
                cur.execute("insert into tw_data(Tid, Tweet, Auth_name, Auth_id, cr_date, Source, verified, rt_count, lang, fav_count, username, userid) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (tw_id, tw_text, tw_uscreen_name, tw_uid, tw_crdate, tw_source, tw_isver, tw_rtcount, tw_lang, tw_favcount, tw_uname, tw_uid))
                db.commit()
            except(mysql.connector.OperationalError, mysql.connector.ProgrammingError, mysql.connector.DatabaseError), e:
                print e
            #csvWriter.writerow({'Tweet_Id': str(tweet.id_str)+str("L"), 'Tweet_Text': (tweet.full_text.encode('utf-8').replace('\n', '').replace('\r', ' ').decode('unicode_escape').encode('ascii','ignore').strip()),'Tweet_authorscreen_name':tweet.author.screen_name.encode('utf-8').strip(),'Tweet_author_id':str(tweet.author.id)+str("L"),'Tweet_created_at':tweet.created_at,'Tweet_source':tweet.source.encode('utf-8').strip(),'Tweet_user_verified':tweet.user.verified,'Tweet_retweet_count':tweet.retweet_count,'Tweet_lang':tweet.lang.encode('utf-8').strip(),'Tweet_favcount':tweet.user.favourites_count,'Tweet_username':tweet.user.name.encode('utf8').strip(),'Tweet_userid':tweet.user.id_str,'Tweet_location':tweet.user.location.encode('utf-8').strip()})
            count +=1
            if count==10000:
                break
        
    except tweepy.TweepError:
        print("Whoops, could not fetch more! just wait for 15 minutes :")
        time.sleep(900)
        continue
    except StopIteration:
        break
csvFile.close()

