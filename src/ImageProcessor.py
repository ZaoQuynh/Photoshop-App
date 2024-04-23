from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance
import cv2
import numpy as np

def selected_image_path():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    return file_path

def get_image(image_path):
    image = Image.open(image_path)
    return image

def resize_image(image: Image, size):
    aspect_ratio = image.width / image.height
    new_width = size if aspect_ratio >= 1 else int(size * aspect_ratio)
    new_height = size if aspect_ratio <= 1 else int(size / aspect_ratio)
    image = image.resize((new_width, new_height), Image.BICUBIC)

    margin_right = (size - new_width)/2
    margin_top = (size - new_height)/2
    
    return image, margin_right, margin_top

def load_image(parent: Canvas, image, size):
    resized_img, x, y = resize_image(image, size)
    photo = ImageTk.PhotoImage(resized_img)
    parent.delete("all")
    parent.create_image(x, y, anchor=NW, image=photo)
    parent.image = photo
    return image

def saturation_feature(image, factor):
    '''
    Điều chỉnh độ bảo hòa của ảnh

    Kỹ thuật: Cân bằng histogram toàn cục

    Input: 
    - selected_image: ảnh đang được chọn
    - factor: chỉ số điều chỉnh bảo hòa.
            + factor = 0: ảnh gốc
            + factor > 0: tăng độ bảo hòa
            + factor < 0: giảm độ bảo hòa

    Output: hình ảnh sau khi xử lý bảo hòa.
    '''
    saturation_factor = 1 + factor/50
    img_arr = np.array(image)

    img_cvt = cv2.cvtColor(img_arr, cv2.COLOR_BGR2HSV)
    img_cvt[:,:,1] = np.clip(img_cvt[:,:,1] * saturation_factor, 0, 255)

    saturated_array = cv2.cvtColor(img_cvt, cv2.COLOR_HSV2BGR)
    saturated_image = Image.fromarray(saturated_array)

    return saturated_image

def brightness_feature(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    brightened_image = enhancer.enhance(1 + factor/50)
    return brightened_image

def contrast_feature(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    contrasted_image = enhancer.enhance(1 + factor/50)
    return contrasted_image

def sharpen_feature(image, sigma, strength=1.5, median_kernel_size=3):
    sigma_ = 1 + sigma/10
    
    # Apply Unsharp Mask
    image_np = np.array(image)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    blurred = cv2.GaussianBlur(image_bgr, (0, 0), sigma_)
    unsharp = cv2.addWeighted(image_bgr, 1.0 + strength, blurred, -strength, 0)
    sharpened = Image.fromarray(cv2.cvtColor(unsharp, cv2.COLOR_BGR2RGB))

    return sharpened

