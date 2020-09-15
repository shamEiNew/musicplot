import numpy as np
import matplotlib.pyplot as plt
import sys, random
import matplotlib.animation as animation
from matplotlib.patches import Ellipse

fig = plt.figure(figsize=(8, 8), facecolor = 'black')
ax = plt.subplot(111, frameon=False)

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
def curve():
    x = np.arange(0, 2*np.pi, 0.1)
    p = ['red', 'orange', 'gold', 'lawngreen', 'lightseagreen', 'royalblue', 'blueviolet']

    lines = []
    for i in range(0, 7):
        line, = ax.plot(x, np.sin(x), color = p[i])
        lines.append(line,)
    return lines

lines = curve()
def curve_anim(i):
    x = np.arange(0, 2*np.pi, 0.1)
    print(i)
    for j in range(0, 7): lines[j].set_ydata(np.sin(x - (j/10) + i / 10))
    return lines

if __name__ =='__main__':
    ani = animation.FuncAnimation(fig, curve_anim, frames = 150, interval=2, save_count=100) #blit false

    #from matplotlib.animation import FFMpegWriter
    #writer = FFMpegWriter(fps=20, metadata=dict(artist='Sham'),  bitrate=1800)
    #ani.save("gifs/sines.mp4", writer=writer)

    plt.show()