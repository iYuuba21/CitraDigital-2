from os import path
import numpy as np
import imageio.v3 as image

path= "C:/Users/Ev/Pictures/suisei.jpg"

image_source = image.imread (path)

if len(image_source.shape) > 3:
    print("Gambar harus dalam mode RGB")
    exit()


image_source= image_source.astype(np.float32)

red_ch = image_source[:,:,0]
green_ch = image_source[:,:,1]
blue_ch = image_source[:,:,2]
grey_ch = red_ch + green_ch + blue_ch / 3

image_grey = np.zeros_like (image_source)

image_grey[:,:,0] = grey_ch
image_grey[:,:,1] = grey_ch
image_grey[:,:,2] = grey_ch

image_grey=np.clip(image_grey,0,255).astype(np.uint8)

image.imwrite("C:/Users/Ev/Pictures/greyscale.jpg",image_grey)

print("Proses selesai dijalankan")