import settings
import tweepy
import dataset
from textblob import TextBlob

db = dataset.connect(settings.CONNECTION_STRING)

result = db[settings.TABLE_NAME].all()

good = 0
bad = 0
neutral = 0

users = db['election'].all()
print("polarity value 1 is good and -1 is bad")
print("subjectivity value 0 is factual information and  1 is public opinion", end="\n\n")
for user in db['election']:
   if str(user['polarity']) != "0.0" and str(user['subjectivity']) !="0.0":
      print("polarity : "+str(user['polarity']) + "\nsubjectivity : " + str(user['subjectivity']) + " \ntweet text : " + str(user['text']) + " \n---------------------------------------------------------------------------------------------\n")

for user in db['election']:
   if float(user['polarity']) > 0:
      good = good + 1
   elif float(user['polarity']) < 0:
      bad = bad +1
   else:
      neutral = neutral + 1

print(f" Good tweets : {good} \n Bad tweets : {bad} \n Neutral tweets : {neutral}\n\n The following information can also be extracted : \n")

for i in user:
        print(" "+str(i))