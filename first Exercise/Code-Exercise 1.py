import pandas as pd
import re

def extract_hashtags(text):
    """Extracts hashtags from a string of text"""
    hashtags = re.findall(r'\#\w+', text)
    return hashtags


tweets = {'tweet': ['This is an #example Tweet for the interesting #DataAnalysis course at #BTH in #2023.',
                    'The #AIStudents are taking the course for the second year at the campus in #Karlskrona.']}

df = pd.DataFrame(tweets)


df['hashtags'] = df['tweet'].apply(extract_hashtags)

print(df['hashtags'])
