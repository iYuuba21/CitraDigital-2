from os import path
import numpy as np
import imageio.v3 as image


path = "C:/Users/Ev/Pictures/suisei.jpg"
image_source = image.imread(path)


if len(image_source.shape) != 3 or image_source.shape[2] != 3:
    print("Gambar harus dalam mode RGB")
    exit()


image_source = image_source.astype(np.float32)


red_ch = image_source[:, :, 0]
green_ch = image_source[:, :, 1]
blue_ch = image_source[:, :, 2]


grey_ch = (red_ch + green_ch + blue_ch) / 3


threshold_value = 128


binary_image = np.where(grey_ch > threshold_value, 255, 0)


image_binary = np.zeros_like(image_source)
image_binary[:, :, 0] = binary_image
image_binary[:, :, 1] = binary_image
image_binary[:, :, 2] = binary_image


image_binary = np.clip(image_binary, 0, 255).astype(np.uint8)
image.imwrite("C:/Users/Ev/Pictures/binary.jpg", image_binary)

print("Proses konversi biner selesai dijalankan")
