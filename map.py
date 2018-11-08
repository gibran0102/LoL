import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random
#'x': 6346, 'y': 8123

x = np.array([192])
y = np.array([383])

class Map():
    def __init__(self,x ,y ):
        self.img = mpimg.imread('map1.png')
        self.x = x
        self.y = y


    def draw(self):     
        plt.imshow(self.img, aspect='auto', extent=(-1000,14800,-570,14800))
        plt.axis([-1000, 14800,-570, 14800])
        plt.plot(self.x,self.y, 'ro')
        #plt.savefig('books_rea{}.png'.format(random.random()))
        plt.show()




