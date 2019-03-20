import argparse
import os
import numpy as np
import random
import imagegen
import matplotlib.pyplot as plt
#import cv2
#from PIL import Image
import matplotlib.colors as color
#import matplotlib.image as mpimg

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", help="number of images",
                        type=str)
    parser.add_argument("-o", "--output", help="output path")
    args = parser.parse_args()
    print(f"number of generated images: {args.number}")
    print(f"ouput path is: {args.output}")

    if not os.path.exists(args.output):
        os.makedirs(args.output[:-1])
    # set the display level to none.
    display = False

    min_shape = random.randint(1, 101)
    max_shape = random.randint(min_shape+1, 201)

    min_size = random.randint(1, 10)

    boolOverlap = bool(random.getrandbits(1))
    try:
        generated_Image = imagegen.generateRandShapes(
            min_s=min_shape, max_s=max_shape, min_size=min_size, overlap=boolOverlap)
    except Exception:
        print(f"Error In the Shape Creation")
    #cv2.cvtColor(generated_Image, cv2.COLOR_RGB2HSV)
    generated_Image = color.rgb_to_hsv(generated_Image)
    if diplay:
        print(f"shape is {generated_Image.shape}")
        print(f"max val is {np.amax(generated_Image[:,:,1])}")
        plt.imshow(generated_Image)
        plt.show()

    np.save(f"{args.output}osef.npy", generated_Image)

    if display:
        loaded = np.load(f"{args.output}osef.npy")
        plt.imshow(loaded)
        plt.show()
