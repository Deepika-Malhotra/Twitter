# -*- coding: utf-8 -*-

# In this code, 5 most occuring entites  in the dataset obtained in Step 1.
#Here, data dictionary is maintained to store the words and their corresponding counter. 

import csv
import os
import time
import collections
import operator
import re
import json
import textblob
from textblob import TextBlob
#import time

import mysql.connector


db=mysql.connector.connect(user ='root', password= 'root', host = 'localhost', database='twitter_data')
cur=db.cursor();
cur.execute ("select Tid, Tweet from tw_data")
data = cur.fetchall ()

noun_counter={}
for r in data:
    nouns=[]
    text=TextBlob(r[1])
    nouns=text.noun_phrases
    for eachnoun in nouns:
        if eachnoun not in noun_counter.keys():
            noun_counter[eachnoun]=1
        else:
            print "\n\n"
            noun_counter[eachnoun]=noun_counter[eachnoun]+1
            print "noun_counter[eachnoun]===",eachnoun,"====", noun_counter[eachnoun]
    
sorted_x = sorted(noun_counter.items(), key=operator.itemgetter(1))
sorted_list= [x[0] for x in sorted_x]
print sorted_list[-5:]
import pdb;pdb.set_trace()
    
    


