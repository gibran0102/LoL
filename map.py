import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

IMAGE = mpimg.imread('maps/map1.png')

class Map():

    def __init__(self):
        self.id = random.randint(1,21)*5
        plt.imshow(IMAGE, aspect='auto', extent=(-120,14820, -120,14881))
        plt.axis([-120, 14820, -120, 14881])
        plt.axis('off')

    def generate(self, x, y):
        plt.plot(*zip(*x), 'o', color='green', linewidth=5.9)    
        plt.plot(*zip(*y), '+',  color='blue', linewidth=5.9)
    
    def save(self, name):
        plt.savefig('test/{}{}_map.png'.format(name, self.id), format='png', transparent= True)
        
    def show(self):
        plt.show()