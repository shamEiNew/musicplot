import numpy as np
import matplotlib.pyplot as plt
import sys, random, json, os
import matplotlib.animation as animation
from matplotlib.patches import Ellipse
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

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
p = ['red', 'orange', 'gold', 'lawngreen', 'lightseagreen', 'royalblue', 'blueviolet']
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


figure = canvas((8, 8), 'black') #Pass 2-tuple for frame size and color as string
fig = figure._frame_()
ax = figure._subplot_(111, True, 'red', 'polar') #Pass row, column, index as 111, bool value, color, projection

if __name__ =='__main__':
    m = curve_polar_anim
    if m == curve_anim:lines = curve()
    if m == curve_polar_anim: r, theta = polar_curve()
    if m == music_plot: x_a, y_a, area, color = music()
    ani = animation.FuncAnimation(fig, m, frames = 600, interval=2, save_count=100) #blit false
    plt.show()