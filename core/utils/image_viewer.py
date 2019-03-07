import matplotlib.pyplot as plt
from skimage import exposure


def display_image(img):
    # viewing protocol for a 16 bit image Dicom
    LO = 1031
    HI = 1091
    min_val = 0
    max_val = 255
    better_contrast = exposure.rescale_intensity(img,
                                                 in_range=(LO, HI),
                                                 out_range=(min_val, max_val))
    plt.imshow(better_contrast, cmap=plt.cm.gray)
