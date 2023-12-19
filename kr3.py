import numpy
import numpy as np
from scipy import ndimage
from PIL import Image
import numpy as np

file_path = input()

img = Image.open(file_path)
data = np.array(img)
result = ndimage.generic_filter(a, np.nanmean, size=3, mode='constant', cval=np.NaN)

print(np.min(data), np.max(data))