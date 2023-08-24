import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    output = tweets[tweets['content'].str.len() > 15][['tweet_id']]
    return output

data = [[1, 'Vote for Biden'], [2, 'Let us make America great again!']]
Tweets = pd.DataFrame(data, 
                      columns=['tweet_id', 'content']).astype(
                              {'tweet_id':'Int64', 'content':'object'})

print("Invalid Tweets (Char_length over 15):\n", invalid_tweets(Tweets))
