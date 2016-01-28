#!/usr/bin/python

from matplotlib.pyplot import figure, clf, axis, plot, draw
from pylab import ion
from random import uniform
from time import sleep
from math import hypot, atan2, sin, cos, floor


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class RRT:
    def __init__(self):
        # init plot
        self.fig = figure(num=None, figsize=(6, 6), dpi=80, facecolor='w', edgecolor='k')
        ion()
        self.axis_size = 5
        self.step_size = 1
        self.config_list = []

    def updatePlot(self):
        #clf()

        # Set axis
        axis([-self.axis_size,self.axis_size,-self.axis_size,self.axis_size])

        # Plot bob position as dot and string as line
        #plot(self.L1*sin(theta),self.L1*cos(theta), 'ro')
        #plot([self.L1*sin(theta),0],[self.L1*cos(theta),0], '-')

        # Update the plot
        draw()

    def add_tree(self, tree):
        self.plot_config(tree)
        self.config_list.append(tree)

    def get_free_config(self):
        x = uniform(-self.axis_size, self.axis_size)
        y = uniform(-self.axis_size, self.axis_size)
        config = Point(x,y)
        return config

    def plot_config(self, config):
        plot(config.x, config.y,'o')

    def dot_line(self, from_config, shortest_config):

        dots_num = floor(hypot(from_config.x-shortest_config.x, from_config.y-shortest_config.y)/self.step_size)
        angle = atan2(from_config.y-shortest_config.y, from_config.x-shortest_config.x )

        #from_line = shortest_config
        for dot in range( int( dots_num ) + 1 ):
            x = from_config.x - dot*self.step_size*cos(angle)
            y = from_config.y - dot*self.step_size*sin(angle)
            #plot([from_line.x, x],[from_line.y,y],'-')
            plot(x,y,'o')
            config = Point(x,y)
            self.config_list.append(config)
            #from_line = Point(x,y)

    def get_shortest_config(self, from_config):
        self.config_list.sort(key=lambda tmp: hypot(from_config.x - tmp.x,from_config.y - tmp.y), reverse=False)
        shortest_config = self.config_list[0]

        self.dot_line(shortest_config, from_config)

        plot([shortest_config.x,from_config.x],[shortest_config.y,from_config.y],'-')

    def sample(self, tree):
        free_config = self.get_free_config()

        shortest_config = self.get_shortest_config(free_config)

        self.plot_config(free_config)
        self.config_list.append(free_config)
        self.updatePlot()

rrt = RRT()
T1 = Point(0,0)

rrt.add_tree(T1)
for i in range(1000):
    rrt.sample(T1)

sleep(100)