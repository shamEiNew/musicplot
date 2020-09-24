import numpy as np
import matplotlib.pyplot as plt
import sys, random, json, os, inspect
import matplotlib.animation as animation
from matplotlib.patches import Ellipse, Circle
#from matplotlib.cbook import cdates
from matplotlib.markers import MarkerStyle
#from matplotlib.lines import Line2D
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from matplotlib.font_manager import FontProperties
import matplotlib.colors as mcolors
import playlists as ply

"""
Class for creating figure and subplots as there are multiple functions.

"""
p = list(mcolors.CSS4_COLORS.keys())
for i in range(len(p)):
    if i in ['black','grey','dimgrey','dimgray','darkslategrey','darkslategray', 'midnightblue',
    'navy', 'darkblue','slategray','darkslateblue']:p.remove(i) 
class canvas:
    def __init__(self, figsize, facecolor):
        self.figsize = figsize
        self.facecolor = facecolor
        
    def _frame_(self):
        return plt.figure(figsize = self.figsize, facecolor = self.facecolor)

    def _subplot_(self, rci, frame_bool, c, proj):
        self.rci =  rci
        self.frame_bool = frame_bool
        self.proj = proj
        self.c = c
        return plt.subplot(self.rci, frameon = self.frame_bool, facecolor = self.c, projection = self.proj)

"""
The following is plot for random scatter ellipse.
"""
def scatter_ellipse(*args):
    NUM = 11
    ells = [Ellipse(xy=np.random.rand(2) * 15,
                width=np.random.rand(), height=np.random.rand(),
                angle=np.random.rand() * 360)
        for i in range(NUM)]

    for e in ells:
        ax.add_artist(e)
        e.set_clip_box(ax.bbox)
        e.set_alpha(np.random.rand())
        e.set_facecolor(np.random.rand(3))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 15)
    return e

"""
The below function is for animating the above plot.
"""
def scatter_circles(*args):
    N = 40
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = (5 * np.random.rand(N))**2
    return plt.scatter(x, y, s=area, c=colors, alpha= 0.8)


"""
The below function is meant for plotting lines in rainbow form
"""
def curve():
    x = np.arange(0, 2*np.pi, 0.1)

    lines = []
    for _ in range(0, 7):
        line, = ax.plot(x, np.sin(x), color = ['red', 'orange', 'gold', 'lawngreen', 'lightseagreen', 'royalblue','blueviolet'])
        lines.append(line,)
    return lines
"""
The below animates the above function.
"""
def curve_anim(i):
    x = np.arange(0, 2*np.pi, 0.1)
    for j in range(0, 7): lines[j].set_ydata(np.sin(x - (j/10) + i / 10))
    return lines
"""
The below is a polar curve while defining subplot change the projection to polar.
"""
def polar_curve():
    theta = np.arange(0, 6*np.pi, 0.05)
    r = ((1+ np.sqrt(5))/2)**(theta *(2/(np.pi)))
    ax.set_rmax(np.max(r))
    ax.set_rticks([1.0, 2.0, 3.0, 4.0])
    ax.grid(True)
    ax.set_title("Golden Spiral", va = 'bottom')
    return r, theta
"""
The below animates the above plot.
"""
def curve_polar_anim(i):
    return ax.plot(r[:i], theta[:i], color = p[2])
"""
This is used for plotting music albums tracks and loudness for 1970s to 2010s.
"""
def music():
    with open('music_data/music.json') as out:
        data = json.load(out)
    x = []
    y = []
    area = []
    color = []
    j = 0
    for k in data.keys():
        for i in range(0,len(data[k])):
            color.append(p[j])
            x.append(data[k][i][f'track_{i}'][0]['features'][0]['year'])
            y.append(data[k][i][f'track_{i}'][0]['features'][0]['properties']['loudness'])
            area.append(data[k][i][f'track_{i}'][0]['features'][0]['properties']['speechiness'])
        j += 1

    x_a = np.array(x)
    y_a = np.array(y)
    area = np.array(area) * 70
    #legend1 = ax.legend(*scatter.legend_elements(),
                    #loc="lower left", title="Classes")
    #ax.add_artist(legend1)
    #textstr = 'dB = {0} to {1}\n Speech = {2} to {3}'.format(-60, 0, 0, 1)
    #plt.text(2000, 2000, textstr, fontsize=14)
    ax.set_xlim(1965, 2020)
    #ax.set_xticks(range(1970, 2020, 4))
    ax.set_xlabel('Year', c = 'white')
    ax.set_ylabel('Loudness in dB (-60 to 0)', c = 'white')
    ax.set_title('Spotify: Music Loudness and Speechines from 1970 to 2019', c = 'lime')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis = 'y', colors = 'floralwhite')
    ax.tick_params(axis='x', colors='floralwhite')

    #print(len(y_a))
    #print(x_a)
    #print(y_a)
    #colors = np.random.rand(
    #area =  # 0 to 15 point radii
    # produce a legend with a cross section of sizes from the scatter
    #handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
    #legend2 = ax.legend(handles, labels, loc="upper right", title="Sizes")
    return x_a, y_a, area, color
"""
This is used for animating plots.
"""
def music_plot(i):
    return ax.scatter(x_a[:i], y_a[:i], s = area[:i], c = color[:i], alpha = 1)

def text_plot():
    plt.text(0.6, 0.7, "banogi \U0001F60D", size=40, rotation=0.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.7, 0.5),
                   fc=(1., 0.9, 0.9),
                   )
         )

    plt.text(0.55, 0.6, "meri dost", size=50, rotation=-10.,
         ha="right", va="top",
         bbox=dict(boxstyle="square",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.9, 0.8),
                   )
         )
    
    ax.grid(False)
    #plt.savefig('dost.png')
    plt.show()

def artist_plot(i_, artist_data):
    
    global artist_tracks_loudness 
    artist_tracks_loudness = []

    global artist_tracks_danceability
    artist_tracks_danceability = []

    global artist_tracks_speechiness
    artist_tracks_speechiness =  []

    global album_color
    album_color = []

    global album_popularity 
    album_popularity = []
    
    global album_names
    album_names = []

    global y_pos

    global color_ 
    color_ = {}

    loudest_track_name = ''
    #sp = ply.configure('user')
    if len(artist_data[f'artist_{i_}'][0]['albums_full']) > 0:

        for j_ in range(0, len(artist_data[f'artist_{i_}'][0]['albums_full'])):

            album_names.append(artist_data[f'artist_{i_}'][0]['albums_full'][j_]['album_name'])
            album_popularity.append(artist_data[f'artist_{i_}'][0]['albums_full'][j_]['album_popularity'])
            loudest_track = -60

            for k_ in range(0, len(artist_data[f'artist_{i_}'][0]['albums_full'][j_]['tracks'])):

                item = artist_data[f'artist_{i_}'][0]['albums_full'][j_]['tracks'][k_]['features'][0]

                if artist_data[f'artist_{i_}'][0]['albums_full'][j_]['album_name'] != 'Ultraviolence - Audio Commentary':

                    if item['loudness'] >= loudest_track:
                        loudest_track = item['loudness']
                        loudest_track_name = artist_data[f'artist_{i_}'][0]['albums_full'][j_]['tracks'][k_]['track_name']
                        loudest_track_id = artist_data[f'artist_{i_}'][0]['albums_full'][j_]['tracks'][k_]['track_id']

                    artist_tracks_loudness.append(item['loudness'])
                    artist_tracks_danceability.append(item['danceability'])
                    artist_tracks_speechiness.append(item['speechiness'])
                    album_color.append(p[j_])
                    color_[artist_data[f'artist_{i_}'][0]['albums_full'][j_]['album_name']] = p[j_]
        
        """
        This part adds songs to the spotify.
        """
        #sp.user_playlist_add_tracks('0hczuz4ovfgx09ch7q216824z','3fpDpJpq2G5zgTURhFxy2W', [loudest_track_id])
        popular_album = (album_names[album_popularity.index(max(album_popularity))].encode('utf-8').decode('utf-8'),
        color_[album_names[album_popularity.index(max(album_popularity))]])

    else:

        popular_album = ["None", "black"]

    y_pos = np.arange(len(album_names))*6
    artist_tracks_loudness = np.abs(np.array(artist_tracks_loudness))

    return color_, loudest_track_name, popular_album, album_popularity

def artist_albums_plot(i_, artist_data):


    color_, loudest_track_name, popular_album,  album_popularity = artist_plot(i_,artist_data)
    #sp = ply.configure()
    #sp.user_playlist_create('0hczuz4ovfgx09ch7q216824z', 'Louddddd', public =True,description= 'loud tracks I guess')
    """
    Scatter plot of Danceability vs Speechiness.
    """
    ax0.spines['bottom'].set_color('w')
    ax0.spines['top'].set_color('w')
    ax0.spines['right'].set_color('w')
    ax0.spines['left'].set_color('w')
    ax0.tick_params(axis = 'y', colors = 'w')
    ax0.tick_params(axis='x', colors='floralwhite')
    ax0.set_xlabel('Danceability', color = 'w')
    ax0.set_ylabel('Speechiness', color ='w')
    ax0.set_title(f"{artist_data[f'artist_{i_}'][0]['artist_name']}", c = 'w')
    
    #ax0.scatter(artist_tracks_danceability, artist_tracks_speechiness, s= artist_tracks_loudness, c = album_color, marker = "+", alpha = 1)

    """
    Horizontal bar plot for album popularity
    """
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(album_names, fontsize = 8, c='r')
    ax1.set_xlabel('Album Popularity', fontsize = 8, c = 'w')
    ax1.spines['bottom'].set_color('w')
    ax1.spines['top'].set_color('w')
    ax1.spines['right'].set_color('w')
    ax1.spines['left'].set_color('r')
    ax1.tick_params(axis = 'y', colors = 'w')
    ax1.tick_params(axis='x', colors='w')
    #ax1.barh(
    #    y_pos,
    #    album_popularity,
    #    height = 0.5,
    #    color = list(color_.values()),
    #    align = 'center'
    #    )

    """
    Adding name of popular album and loudest track on left upper corner.
    """
    plt.subplots_adjust(left = 0.3)
    textstr = "\n".join([f"Popular Album\n{popular_album[0]}",f"Loudest Track\n{loudest_track_name}"])
    plt.text(0.02, 0.9, textstr, fontsize=10, color = 'lime',
    fontname = 'sans-serif',transform=plt.gcf().transFigure)
    #plt.savefig(rf"ims\{artist_data[f'artist_{i_}'][0]['artist_name']}".replace(" ", "_"))
    #plt.show()
    #plt.clf()
    #plt.close()


def artist_anim(i):
    scatter = ax0.scatter(artist_tracks_danceability[:i*20], artist_tracks_speechiness[:i*20], s= artist_tracks_loudness[:i*20],
     c = album_color[:i*20])
    bar = ax1.barh(y_pos[:i], album_popularity[:i], height = 0.5, color = list(color_.values()), align = 'center')
    return bar, scatter

"""
Saving .mp4 files in videomp4

"""
def save_entity(ani, file_name):
    from matplotlib.animation import FFMpegWriter
    writer = FFMpegWriter(fps= 15, metadata=dict(artist='Sham'),  bitrate=1800)
    ani.save(f"videomp4/{file_name}.mp4", writer=writer)

"""
Pass 2-tuple for frame size and color as string in canvas.
Pass row, column, index as 111, bool value, color, projection.
"""
figure1 = figure = canvas((12, 10), 'black')
fig2 = figure._frame_()
ax = figure._subplot_(111, True, 'black', None)

if __name__ =='__main__':

    with open('music_data/data_artists.json', 'r', encoding = 'utf-8' ) as out_file:
        artist_data = json.load(out_file)
    
    m = artist_anim


    for i_ in range(1, len(artist_data.keys())):
        figure = canvas((12, 10), 'black')
        fig1 = figure._frame_()
        ax0 = figure._subplot_(211, True, 'black', None)
        ax1 = figure._subplot_(212, True, 'black', None)
        artist_albums_plot(i_, artist_data)

        """
        Animating part for music data of artists
        """
        ani = animation.FuncAnimation(fig1, m, frames = 60, interval=2, save_count=100)
        #ani = animation.FuncAnimation(fig1, m, frames = 45, interval=2, save_count=100)
        save_entity(ani, f"{artist_data[f'artist_{i_}'][0]['artist_name']}".replace(" ", "_"))
        print(f"Done {artist_data[f'artist_{i_}'][0]['artist_name']}")
        #plt.show()
        plt.clf()
        plt.close()
    
    if m == curve_anim:lines = curve()
    if m == curve_polar_anim: r, theta = polar_curve()
    if m == music_plot: x_a, y_a, area, color = music()
        