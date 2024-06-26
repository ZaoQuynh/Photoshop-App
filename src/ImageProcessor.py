from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance
import cv2
import numpy as np
from PIL import Image, ImageFilter
from Components import *

def selected_image_path():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    return file_path

def get_image(image_path):
    image = Image.open(image_path)
    return image

def rotate_image(image, degrees):
    rotated_image = image.rotate(degrees, expand=True)
    return rotated_image

def resize_image(image: Image,  w, h, type = Image.BICUBIC):
    aspect_ratio = image.width / image.height
    new_width = w if aspect_ratio >= 1 else int(w * aspect_ratio)
    new_height = h if aspect_ratio <= 1 else int(h / aspect_ratio)
    image = image.resize((new_width, new_height), type)

    margin_right = (w - new_width)/2
    margin_top = (h - new_height)/2
    
    return image, margin_right, margin_top

def load_image(parent: Canvas, image, w, h, type_resize = Image.BICUBIC):
    resized_img, x, y = resize_image(image,  w, h, type_resize)
    photo = ImageTk.PhotoImage(resized_img)
    parent.delete("all")
    parent.create_image(x, y, anchor=NW, image=photo)
    parent.image = photo
    return image

def load_gif_into_frame(parent: Canvas, gif , w, background = Colors.BACKGROUND.value):
    gif = Image.open("gifs\_background.gif")

    frames = []
    while True:
        try:
            gif.seek(len(frames))
            frame = gif.copy()
            _w, _h = frame.size
            w_new, h_new = w, int((w * _h)/_w)
            frame = frame.resize((w_new, h_new), Image.BICUBIC)
            frames.append(ImageTk.PhotoImage(frame))
        except EOFError:
            break

    label = Label(parent, width=w, background=background)
    label.pack()

    def update_frame(idx):
        frame = frames[idx]
        label.config(image=frame)
        parent.after(50, update_frame, (idx + 1) % len(frames))
    
    update_frame(0)

# def saturation_feature(image, factor):
#     '''
#     Điều chỉnh độ bảo hòa của ảnh

#     Kỹ thuật: Cân bằng histogram toàn cục

#     Input: 
#     - image: ảnh đang được chọn
#     - factor: chỉ số điều chỉnh bảo hòa.
#             + factor = 0: ảnh gốc
#             + factor > 0: tăng độ bảo hòa
#             + factor < 0: giảm độ bảo hòa

#     Output: hình ảnh sau khi xử lý bảo hòa.
#     '''
#     saturation_factor = 1 + factor/50
#     img_arr = np.array(image)

#     img_cvt = cv2.cvtColor(img_arr, cv2.COLOR_BGR2HSV)
#     img_cvt[:,:,1] = np.clip(img_cvt[:,:,1] * saturation_factor, 0, 255)

#     saturated_array = cv2.cvtColor(img_cvt, cv2.COLOR_HSV2BGR)
#     saturated_image = Image.fromarray(saturated_array)

#     return saturated_image

import numpy as np
import cv2
from PIL import Image

def saturation_feature(image, factor):
    '''
    Điều chỉnh độ bảo hòa của ảnh

    Kỹ thuật: Piecewise-Linear Transformation

    Input: 
    - image: ảnh đang được chọn
    - factor: chỉ số điều chỉnh bảo hòa.
            + factor = 0: ảnh gốc
            + factor > 0: tăng độ bảo hòa
            + factor < 0: giảm độ bảo hòa

    Output: hình ảnh sau khi xử lý bảo hòa.
    '''
    img_arr = np.array(image)

    img_cvt = cv2.cvtColor(img_arr, cv2.COLOR_BGR2HSV)

    factor_saturate = factor/50
    
    def piecewise_linear(x):
        return np.piecewise(x, [x < 128, x >= 128], [lambda x: x * (1 + factor_saturate), lambda x: 255 - (255 - x) * (1 - factor_saturate)])

    img_cvt[:,:,1] = piecewise_linear(img_cvt[:,:,1])

    saturated_array = cv2.cvtColor(img_cvt, cv2.COLOR_HSV2BGR)
    saturated_image = Image.fromarray(saturated_array)

    return saturated_image 

def blur_feature(image, factor):
    '''
    Điều chỉnh độ mờ của ảnh
    
    Kỹ thuật: Sử dụng bộ lọc làm mờ Gaussian

    Input: 
    - image: ảnh đang được chọn
    - factor: chỉ số điều chỉnh độ mờ.
        + factor = 0: ảnh gốc
        + factor > 0: tăng độ mờ (tăng bán kính bộ lọc)
    
    Output: hình ảnh sau khi xử lý độ mờ.
    '''
    blur_factor = 0 + abs(factor)/10
    blur_radius = int(blur_factor * 3)

    img_arr = np.array(image)
    kernel_size = (blur_radius * 2 + 1, blur_radius * 2 + 1)
    blurred_img = cv2.GaussianBlur(img_arr, kernel_size, 0)
    blurred_image = Image.fromarray(blurred_img)
    return blurred_image

def rotate_image(image, angle):
    rotated_image = image.rotate(angle, expand=True)
    return rotated_image

def brightness_feature(image, factor):
    '''
    Điều chỉnh độ sáng của ảnh

    Kỹ thuật: Điều chỉnh kênh L (Lightness) trong không gian màu Lab

    Input: 
    - image: ảnh đang được chọn
    - factor: chỉ số điều chỉnh độ sáng.
            + factor = 0: ảnh gốc
            + factor > 0: tăng độ sáng
            + factor < 0: giảm độ sáng

    Output: hình ảnh sau khi xử lý độ sáng.
    '''
    brightness_factor = factor
    img_arr = np.array(image)

    # Chuyển đổi ảnh sang không gian màu Lab
    lab_img = cv2.cvtColor(img_arr, cv2.COLOR_RGB2LAB)

    # Tách các kênh màu
    L, a, b = cv2.split(lab_img)

    # Điều chỉnh kênh L (độ sáng)
    adjusted_L = np.clip(L.astype(np.int16) + brightness_factor, 0, 255).astype(np.uint8)
    # Kết hợp lại các kênh màu
    adjusted_lab_img = cv2.merge((adjusted_L, a, b))
    # Chuyển đổi ảnh trở lại không gian màu RGB
    adjusted_rgb_img = cv2.cvtColor(adjusted_lab_img, cv2.COLOR_LAB2RGB)
    adjusted_image = Image.fromarray(adjusted_rgb_img)
    return adjusted_image

import cv2
import numpy as np
from PIL import Image

import cv2
import numpy as np
from PIL import Image

def contrast_feature(image, factor):
    '''
    Điều chỉnh độ tương phản của ảnh

    Kỹ thuật: Điều chỉnh kênh L (Lightness) trong không gian màu Lab

    Input: 
    - image: ảnh đang được chọn
    - factor: chỉ số điều chỉnh độ tương phản.
            + factor = 0: ảnh gốc
            + factor > 0: tăng độ tương phản
            + factor < 0: giảm độ tương phản

    Output: hình ảnh sau khi xử lý độ tương phản.
    '''
    factor = 1 +factor/50
    contrast_factor = factor
    img_arr = np.array(image)

    # Chuyển đổi ảnh sang không gian màu Lab
    lab_img = cv2.cvtColor(img_arr, cv2.COLOR_RGB2LAB)

    # Tách các kênh màu
    L, a, b = cv2.split(lab_img)

    # Điều chỉnh kênh L (độ sáng)
    mean_L = np.mean(L)
    adjusted_L = np.clip((L - mean_L) * contrast_factor + mean_L, 0, 255).astype(np.uint8)

    # Kết hợp lại các kênh màu
    adjusted_lab_img = cv2.merge((adjusted_L, a, b))

    # Chuyển đổi ảnh trở lại không gian màu RGB
    adjusted_rgb_img = cv2.cvtColor(adjusted_lab_img, cv2.COLOR_LAB2RGB)

    adjusted_image = Image.fromarray(adjusted_rgb_img)

    return adjusted_image

def sharpen_feature(image, sigma, strength=1.5, median_kernel_size=3):

    '''
    Tăng độ sắc nét cho hình ảnh

    Kỹ thuật: Unsharp Masking

    Input: 
    - image: ảnh đang được chọn
    - factor: chỉ số điều chỉnh độ sắc nét.
            + factor = 0: ảnh gốc
            + factor > 0: tăng độ sắc nét
            + factor < 0: giảm độ sắc nét

    Output: hình ảnh sau khi xử lý tăng độ sắc nét.
    '''

    sharpen_factor = sigma/10
    image_np = np.array(image)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    blurred = cv2.GaussianBlur(image_bgr, (0, 0), sharpen_factor)
    unsharp = cv2.addWeighted(image_bgr, 1.0 + strength, blurred, -strength, 0)
    sharpened = Image.fromarray(cv2.cvtColor(unsharp, cv2.COLOR_BGR2RGB))

    return sharpened

def smoothing_feature(image, factor):
    
    image_np = np.array(image)
    bil_blur = cv2.bilateralFilter(image_np, 13, factor, factor)
    smooth_img = Image.fromarray(bil_blur)

    return smooth_img

def color_filter(image, s1, s2, s3, factor):
    '''
    Lọc màu hình ảnh.

    Nguồn code tham khảo: Duo-Tone - link: https://learnopencv.com/photoshop-filters-in-opencv/

    Input: 
    - image: ảnh đang được chọn
    - s1: chỉ số kênh màu 0-blue, 1-green, 2-red
    - s2: chỉ số kênh màu 0-blue, 1-green, 2-red, 3-none
    - s3: chỉ số 0-dark, 1-light
    - factor: chỉ số điều chỉnh sắc độ.
            + factor = 0: ảnh gốc.
            + factor > 0: tăng sắc độ.

    Output: Hình ảnh sau khi lọc màu.
    '''
    color_filter_factor = 1 + factor/100
    image_np = np.array(image)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    for i in range(3):
        if i in (s1, s2):
            image_bgr[:, :, i] = exponential_function(image_bgr[:, :, i], color_filter_factor)
        else:
            if s3:
                image_bgr[:, :, i] = exponential_function(image_bgr[:, :, i], 2 - color_filter_factor)
            else:
                image_bgr[:, :, i] = 0
    
    filtered_img = Image.fromarray(cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB))
    return filtered_img

def exponential_function(channel, exp):

    table = np.array([min((i**exp), 255) for i in range(256)], dtype=np.uint8) 
    return cv2.LUT(channel, table)