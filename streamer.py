import os, tweepy, trends, time
import matplotlib.pyplot as plt
import numpy as np

class streamer(tweepy.StreamListener):

    screen_names_dict= {}
    val = None
    start_time = time.time()
    def on_status(self, status):
        if (time.time()-self.start_time) <= 60:
            self.val = status.user.screen_name
            if self.val not in self.screen_names_dict.keys():
                self.screen_names_dict[self.val] = 0
            else:
                self.screen_names_dict[self.val] += 1
        else:
            return False

def big_values(user_data, f, g):
    user_names = []
    user_count = []
    
    if f == 1 and g == 0:
        for key in user_data.keys():
            if user_data[key] > 0:
                user_names.append(key)
        return user_names
    
    if g == 1 and f == 0:
        for count in user_data.values():
            if count > 0:
                user_count.append(count)
        return user_count
        
def final_plot(user_data):
    #x = big_values(1, 0)
    y = big_values(user_data, 0, 1)
    fig, ax = plt.subplots()
    width = 0.2
    ind = np.arange(len(y))
    ax.barh(ind, y, width, color="blue")
    #ax.set_yticks(ind)
    #ax.set_yticklabels(x, minor=False)
    plt.title(trends.trends_finder())
    plt.xlabel('Number of tweets')
    plt.ylabel('Users')
    #plt.show()
    plt.savefig(os.path.join('twitter_data2.png'), dpi=300, format='png', bbox_inches='tight')

def stream_generator():
    listener = streamer()
    stream = tweepy.Stream(auth = trends.api.auth, listener = listener)
    stream.filter(track = [trends.trends_finder()]) 
    user_data = streamer.screen_names_dict
    final_plot(user_data)

