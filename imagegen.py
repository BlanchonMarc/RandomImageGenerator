import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import random_shapes


def generateRandShapes(min_s, max_s, min_size, overlap, sizes=(1000, 1000)):
    image, _ = random_shapes(sizes, min_shapes=min_s, max_shapes=max_s,
                             min_size=min_size, allow_overlap=overlap, num_trials=100)

    return image
