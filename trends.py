import sys, random
sys.path.insert(1, 'C:/Users/Sham/OneDrive/Desktop/projects')
from crushbot import config
api = config.create_api()

def trends_finder():
    trends_temp = api.trends_place(2282863)[0]['trends']
    trends_itr = iter(trends_temp)
    trend_name = []
    trend_volume = []
    for trend in trends_itr:
        trend_name.append(trend['name'].encode('utf-8').decode('utf-8'))
        trend_volume.append(trend['tweet_volume'])
    
    return trend_name[0]

if __name__ == '__main__':

    for tweet in api.user_timeline(screen_name = 'the_meursault_', count = 5):
        if ('RT' not in tweet.text):
            print(tweet.text)