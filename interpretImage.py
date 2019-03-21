import numpy as np
import glob
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.colors as color
import math


def ParamToInten(AoP, DoP, Inten, angle):
    return ((Inten/2.0) * (1 + DoP*np.cos(math.radians(2*AoP) - 2*math.radians(angle))))


if __name__ == "__main__":
    imagedir = "output/image/"
    listimage = glob.glob(f"{imagedir}*.tiff")

    for pth in listimage:
        img = color.rgb_to_hsv(mpimg.imread(pth))
        #array = np.zeros_like(img)
        AoP = img[:, :, 0] * 360.0
        DoP = img[:, :, 1] * 100.0
        Inten = img[:, :, 2] / 255.0

        print(np.amax(AoP))

        # plt.imshow(img)
        # plt.show()
