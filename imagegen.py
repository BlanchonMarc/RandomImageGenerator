import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import random_shapes
import noise
import random
from math import *


def generateRandShapes(min_s, max_s, min_size, overlap, sizes=(1000, 1000)):
    image, _ = random_shapes(sizes, min_shapes=min_s, max_shapes=max_s,
                             min_size=min_size, allow_overlap=overlap, num_trials=100)

    return image


def GeneratePerlin(scale=100, octaves=6, persistence=0.5, lacunarity=2.0):

    scale = int(random.uniform(40, 140))
    octaves = int(random.uniform(1, 25))
    persistence = random.uniform(0, 1.5)
    lacunarity = random.uniform(0, 2.0)

    verbose = False

    if verbose:
        print(scale)
        print(octaves)
        print(persistence)
        print(lacunarity)

    shape = (1000, 1000)
    seed = np.random.randint(0, 100)

    world = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            world[i][j] = noise.pnoise2(i/scale,
                                        j/scale,
                                        octaves=octaves,
                                        persistence=persistence,
                                        lacunarity=lacunarity,
                                        repeatx=1024,
                                        repeaty=1024,
                                        base=seed)
    color_world = np.zeros(world.shape+(3,))

    color1 = [int(random.uniform(0, 255)),
              int(random.uniform(0, 255)),
              int(random.uniform(0, 255))]
    color2 = [int(random.uniform(0, 255)),
              int(random.uniform(0, 255)),
              int(random.uniform(0, 255))]
    color3 = [int(random.uniform(0, 255)),
              int(random.uniform(0, 255)),
              int(random.uniform(0, 255))]
    color4 = [int(random.uniform(0, 255)),
              int(random.uniform(0, 255)),
              int(random.uniform(0, 255))]
    color5 = [int(random.uniform(0, 255)),
              int(random.uniform(0, 255)),
              int(random.uniform(0, 255))]
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.05:
                color_world[i][j] = color1
            elif world[i][j] < 0:
                color_world[i][j] = color2
            elif world[i][j] < .20:
                color_world[i][j] = color3
            elif world[i][j] < 0.35:
                color_world[i][j] = color4
            elif world[i][j] < 1.0:
                color_world[i][j] = color5

    return color_world
