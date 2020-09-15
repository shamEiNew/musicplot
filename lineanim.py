import numpy as np
import matplotlib.pyplot as plt
import sys, random
import matplotlib.animation as animation
from matplotlib.patches import Ellipse

fig = plt.figure(figsize=(8, 8), facecolor = 'black')
ax = plt.subplot(111, frameon=True, projection = 'polar')

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

if __name__ =='__main__':
    m = curve_polar_anim
    if m == curve_anim:lines = curve()
    if m == curve_polar_anim: r, theta = polar_curve()

    ani = animation.FuncAnimation(fig, m, frames = 180, interval=2, save_count=100) #blit false

    from matplotlib.animation import FFMpegWriter
    writer = FFMpegWriter(fps=24, metadata=dict(artist='Sham'),  bitrate=1800)
    ani.save("videomp4/golden_spiral_grid.mp4", writer=writer)
    #plt.show()