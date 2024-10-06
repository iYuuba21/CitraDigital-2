from os import path
import numpy as np
import imageio.v3 as image

path= "C:/Users/Ev/Pictures/suisei.jpg"

image_source = image.imread (path)

if len(image_source.shape) > 3:
    print("Gambar harus dalam mode RGB")
    exit()


red_ch = image_source[:,:,0]
green_ch = image_source[:,:,1]
blue_ch = image_source[:,:,2]
grey_ch = red_ch + green_ch + blue_ch / 3

image_red = np.zeros_like (image_source)

image_red[:,:,0] = red_ch

image.imwrite("C:/Users/Ev/Pictures/red.jpg",image_red)

print("Proses selesai dijalankan")