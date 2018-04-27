# This code shows the sentimental analysis
#performed on the data collected in Step 1 of the task


import os
import time
import operator
import json
import textblob
from textblob import TextBlob
#import time

import mysql.connector


db=mysql.connector.connect(user ='root', password= 'root', host = 'localhost', database='twitter_data')
cur=db.cursor();
cur.execute ("select Tweet from tw_data")
data = cur.fetchall ()

for r in data:
    text=TextBlob(r[0])
    analysis=text.sentiment
    print analysis
    polarity=text.sentiment.polarity
    print polarity
 
