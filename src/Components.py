from tkinter import *
from Constraint import *
from PIL import Image, ImageTk
from customtkinter import *

class ScrollHorizontalFrame(CTkScrollableFrame):
    def __init__(self, master, width=Sizes.WIDTH_BOTTOM.value, height=Sizes.HEIGHT_BOTTOM.value, corner_radius=0, fg_color="transparent"):
        super().__init__(master,  width=width, height=height, corner_radius=corner_radius, fg_color=fg_color, orientation="horizontal")

class FeatureScaleFrame(Frame):
    def __init__(self, parent: Frame, variable_name,   arrange = [0,100], w = Sizes.FEATURE_FRAME_WIDTH.value , h = Sizes.FEATURE_FRAME_HEIGHT.value, background = Colors.BACKGROUND_V3.value):
        super().__init__(parent)
        self.pack_propagate(FALSE)
        self.parent = parent
        self.width = w
        self.height = h
        self.background = background
        self.variable_value = 0

        self.label_frame = Frame(self, width=self.width, height=30, background=self.background)
        self.label_frame.pack_propagate(FALSE)
        self.label_frame.pack(pady=5)

        self.label = Label(self.label_frame, text=variable_name, background=self.background)
        self.label_value = Label(self.label_frame, background=self.background)

        step = arrange[1] - arrange[0]
        self.scale = CTkSlider(self, from_=arrange[0], to=arrange[1], command=self.set_value, number_of_steps=step)

        self.save_btn = CTkButton(self, width=100, height=20, text="Save")

        self.config(width=self.width, height = self.height, bg = self.background)
        self.label.pack(side=LEFT, padx=20)
        self.scale.pack(pady=5)
        self.save_btn.pack()
        
    def get_value(self):
        return self.variable_value

    def set_value(self, value):
        self.variable_value = int(value)
        self.label_value.config(text=f"{self.variable_value}")
        self.label_value.pack(side=RIGHT)

    def draw(self):
        self.variable_value = 0
        self.label_value.config(text = self.variable_value)
        self.label_value.pack(side=RIGHT, padx=20)
        self.scale.set(self.variable_value)
        self.pack()

    def destroy(self):
        self.pack_forget()

class FeatureButton(Button):
    def __init__(self, parent: Frame, text: str, img_path = None,
                 background = Colors.BTN_COLOR.value, 
                 color_border = Colors.BORDER_COLOR.value,
                 width_size = Sizes.WIDTH_FEATURE_BUTTON.value):
        
        super().__init__(parent, text = text, 
                         width = width_size)
        
        self.frame = None

        if img_path != None:
            self.image = Image.open(img_path)
            self.image = self.image.resize((Sizes.ICON_BUTTON.value, Sizes.ICON_BUTTON.value), Image.BICUBIC)
            self.photo = ImageTk.PhotoImage(self.image)

            self.config(image=self.photo, compound="top", padx=10, pady=10)

        self.config(bg = background)
        self.config(relief="ridge", borderwidth=2, highlightbackground=color_border)

    def set_text(self, text):
        self.text = text
        self.config(text = self.text)

    def set_frame(self, frame):
        self.frame = frame

    def show_frame(self):
        if self.frame is not None:
            self.frame.draw() 

    def hide_frame(self):
        if self.frame is not None:
            self.frame.destroy()
