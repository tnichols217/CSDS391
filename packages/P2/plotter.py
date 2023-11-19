import matplotlib
import numpy as np
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
import kMeans
import solver

def plot(hist: kMeans.HistoricalData, x=2, y=3):
    fig, axis = plt.subplots(nrows=2)
    [ax, err] = axis
    COLORS = ["r", "g", "b", "c", "m", "y", "k", "w"]

    def drawPlots(t):
        return [
            ax.plot(set.transpose()[x], set.transpose()[y], COLORS[i%len(COLORS)]+"^", markersize=4)
            for i,set
            in enumerate(hist.subsets[t])
        ]

    def drawMeans(t):
        return [
            ax.plot(mean.transpose()[x], mean.transpose()[y], COLORS[i%len(COLORS)]+"x", markersize=12)
            for i,mean
            in enumerate(hist.means[t])
        ]

    def drawVoronoi(t):
        h = hist.means[t].copy()
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        s = solver.Solver(xlim, ylim, x, y, ax, h)

    drawPlots(hist.iterations)
    drawMeans(hist.iterations)
    drawVoronoi(hist.iterations)

    fig.subplots_adjust(bottom=0.25)

    axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
    step_slider = Slider(
        ax=axfreq,
        label='Step',
        valmin=0,
        valmax=hist.iterations,
        valstep=1,
        valinit=hist.iterations,
    )

    def update(val):
        ax.cla()
        drawPlots(val)
        drawMeans(val)
        drawVoronoi(val)
        fig.canvas.draw_idle()

    step_slider.on_changed(update)

    err.plot(hist.error)

    # for a bug in matplotlib (need to maintain a reference to sliders for them to be interactive)
    return step_slider, fig, ax, err

def show():
    plt.show()