from PIL import Image
import numpy as np

file_path = 'lunar03_raw.jpg'
new_file_path = 'lunar03_out.jpg'
# считаем картинку в numpy array
img = Image.open(file_path)
data = np.array(img)

min_el = np.min(data)
max_el = np.max(data)
k = 255 / (max_el - min_el)
b = -255 * min_el / (max_el - min_el)
updated_data = np.round(k * data + b).astype(np.uint8)

# запись картинки после обработки
res_img = Image.fromarray(updated_data)
res_img.save(new_file_path)
