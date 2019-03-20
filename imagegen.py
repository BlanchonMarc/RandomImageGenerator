import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import random_shapes
import noise
import random


def generateRandShapes(min_s, max_s, min_size, overlap, sizes=(1000, 1000)):
    image, _ = random_shapes(sizes, min_shapes=min_s, max_shapes=max_s,
                             min_size=min_size, allow_overlap=overlap, num_trials=100)

    return image


def GeneratePerlin(scale=100, octaves=6, persistence=0.5, lacunarity=2.0):
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

    color1 = [random.randint(0, 256),
              random.randint(0, 256),
              random.randint(0, 256)]
    color2 = [random.randint(0, 256),
              random.randint(0, 256),
              random.randint(0, 256)]
    color3 = [random.randint(0, 256),
              random.randint(0, 256),
              random.randint(0, 256)]
    color4 = [random.randint(0, 256),
              random.randint(0, 256),
              random.randint(0, 256)]
    color5 = [random.randint(0, 256),
              random.randint(0, 256),
              random.randint(0, 256)]
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
