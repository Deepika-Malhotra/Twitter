# Twitter
This project is on fetching data from twitter and applying some operations on the collected dataset. 
The programming part is done in Python and used MySQL to store the database from twitter API.
First of all, the whole dataset is collected from twitter API in Collection_final.py and a table (tw_data) in mysql database (twitter_data) is created in which all tweets as well as the metadata related to each tweet is stored in dfferent fields. This step basically covers the Step-1 and Step-5 of the given task.  (Step-1 - Collect a random sample of 10K tweets using the Twitter API, Step-5 - Who posted the data, What was it about, When was it posted, from Where was it posted etc.)
Then, fequency.py is created to parse the 5 most frequently occurring named-entities. This code will make a dictionary in which all the entities and their corresponding counter is stored. In this, TextBlob extracter is used to parse the named-entities and the concept of data-dictionary is maintained to stored the named entities as key and their counter value as value.
Now, the keys in resultant dictionary are sorted in ascending order according to their values and then get the most frequentoy occuring 5 entities in the dictionary.
The above two steps covers the Step-2 of the task in frequency.py.
Now, Sentimental Analysis (Step-4) is performed in Sentiment_Analysis.py by using Sentiment Analysis in TextBlob.
