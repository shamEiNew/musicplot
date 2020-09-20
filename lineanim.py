import numpy as np
import matplotlib.pyplot as plt
import sys, random, json, os
import matplotlib.animation as animation
from matplotlib.patches import Ellipse, Circle
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
from matplotlib.lines import Line2D
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from matplotlib.font_manager import FontProperties

#fig = plt.figure(figsize=(10, 10), facecolor = 'black'

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

#scattered ellipses
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

#Scattered circles like rain
def scatter_circles(*args):
    N = 40
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = (5 * np.random.rand(N))**2
    return plt.scatter(x, y, s=area, c=colors, alpha= 0.8)

#Rainbow curves
p = ['red', 'orange', 'gold', 'lawngreen', 'lightseagreen', 'royalblue', 'blueviolet',
 'cyan', 'crimson','purple', 'maroon', 'indigo', 'navy', 'darkolivegreen', 'deeppink']
def curve():
    x = np.arange(0, 2*np.pi, 0.1)

    lines = []
    for i in range(0, 7):
        line, = ax.plot(x, np.sin(x), color = p[i])
        lines.append(line,)
    return lines

def curve_anim(i):
    x = np.arange(0, 2*np.pi, 0.1)
    for j in range(0, 7): lines[j].set_ydata(np.sin(x - (j/10) + i / 10))
    return lines

def polar_curve():
    theta = np.arange(0, 6*np.pi, 0.05)
    r = ((1+ np.sqrt(5))/2)**(theta *(2/(np.pi)))
    ax.set_rmax(np.max(r))
    ax.set_rticks([1.0, 2.0, 3.0, 4.0])
    ax.grid(True)
    ax.set_title("Golden Spiral", va = 'bottom')
    return r, theta

def curve_polar_anim(i):
    return ax.plot(r[:i], theta[:i], color = p[2])

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

def music_plot(i):
    return ax.scatter(x_a[:i], y_a[:i], s = area[:i], c = color[:i], alpha = 1)

def save_entity(file_name):
    from matplotlib.animation import FFMpegWriter
    writer = FFMpegWriter(fps=35, metadata=dict(artist='Sham'),  bitrate=1800)
    ani.save(f"videomp4/{file_name}.mp4", writer=writer)

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

    """
    Pass 2-tuple for frame size and color as string in canvas.
    Pass row, column, index as 111, bool value, color, projection.
    """
def artist_anim(i):
    return ax.scatter(artist_tracks_danceability[:i], artist_tracks_speechiness[:i], s= artist_tracks_loudness[:i],
     c = album_color[:i])

figure = canvas((8, 8), 'white') 
fig = figure._frame_()
ax = figure._subplot_(211, True, 'white', None)
#ax = ax = fig.add_subplot(111, projection='3d')


if __name__ =='__main__':

    m = artist_anim
    if m == curve_anim:lines = curve()
    if m == curve_polar_anim: r, theta = polar_curve()
    if m == music_plot: x_a, y_a, area, color = music()
    
    with open('music_data/data_artists.json', 'r', encoding='utf-8' ) as out_file:
        artist_data = json.load(out_file)
    artist_tracks_loudness = []
    artist_tracks_danceability = []
    artist_tracks_speechiness = []
    album_color = []
    color_ = {}
    for i_ in range(1, len(artist_data.keys()) + 1):
        if artist_data[f'artist_{i_}'][0]['artist_name'].encode('utf-8', 'ignore').decode('utf-8').lower() == "lana del rey":
            for j_ in range(0, len(artist_data[f'artist_{i_}'][0]['albums_full'])):
                for k_ in range(0, len(artist_data[f'artist_{i_}'][0]['albums_full'][j_]['tracks'])):
                    item = artist_data[f'artist_{i_}'][0]['albums_full'][j_]['tracks'][k_]['features'][0]
                    if artist_data[f'artist_{i_}'][0]['albums_full'][j_]['album_name'] != 'Ultraviolence - Audio Commentary':
                        artist_tracks_loudness.append(item['loudness'])
                        artist_tracks_danceability.append(item['danceability'])
                        artist_tracks_speechiness.append(item['speechiness'])
                        album_color.append(p[j_])
                        color_[artist_data[f'artist_{i_}'][0]['albums_full'][j_]['album_name']] = p[j_]
    
    #print(color_)
    artist_tracks_loudness = np.abs(np.array(artist_tracks_loudness))
    #save_entity('ldr')

    try:
        if m is not None:
            ani = animation.FuncAnimation(fig, m, frames = 150, interval=2, save_count=100)
    except TypeError as t:
        print('m has no value to animate')
        raise t
    ax.set_xlabel('Danceabiltiy')
    ax.set_ylabel('Speechines')
    ax.set_title("Lana Del Rey's albums")
    legend_el = [Circle((1, 1), 10, facecolor= color_[i], label= i) for i in color_.keys()]
    ax.legend(handles=legend_el, loc='upper center', bbox_to_anchor=(0.5, -0.5),
    fancybox = True, prop = FontProperties().set_size('xx-small'))
    from matplotlib.animation import FFMpegWriter
    writer = FFMpegWriter(fps=35, metadata=dict(artist='Sham'),  bitrate=1800)
    ani.save(f"videomp4/ldr.mp4", writer=writer)
    #ax.scatter(artist_tracks_danceability, artist_tracks_speechiness, s= artist_tracks_loudness,
    # c = album_color)

    #legend_elements1 = [Line2D([0], [0], marker='o', color= color_[i], label= i,
    #                  markerfacecolor=color_[i], markersize=1) for i in color_.keys()]
    
    #ax.scatter(artist_tracks_danceability, artist_tracks_speechiness, s= artist_tracks_loudness,
    #c = album_color)
    #ax.set_xticks(np.arange(0, 1.0))
    #ax.set_yticks(np.arange(0.0, 1.1, 0.1))
    #ax.set_ylim(0.0, 1.0)
    #ax.grid(True)
    #ax.legend()
    #ax.xaxis.set_major_locator(MultipleLocator(0.1))
    #ax.xaxis.set_major_formatter('{x:.0f}')

    # For the minor ticks, use no labels; default NullFormatter.
    #ax.view_init(elev=25., azim=-35)
    #plt.xticks(fontsize = 55)
    #plt.yticks(fontsize = 55)
    #ax.yaxis.set_minor_locator(AutoMinorLocator())
    #ax.xaxis.set_minor_locator(AutoMinorLocator())
    #plt.savefig('temp_ldr.png')
    plt.show()
