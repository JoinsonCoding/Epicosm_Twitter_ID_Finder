import pandas as pd
import tweepy

consumer_key = " "
consumer_secret = " "
access_token = " "
access_token_secret = " "
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

my_file = open("user_list.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
user_list = data.replace('\n', ' ').split()
  
# printing the data
print(user_list)
my_file.close()

ids = []

for u in user_list:
    user = api.get_user(screen_name = u)
    ids.append(user.id)
    
df = pd.DataFrame(columns = ['User Names', 'Author ID'])

df['User Names'] = user_list
df['Author ID'] = ids

print(df)

df.to_csv("id_username.csv")
