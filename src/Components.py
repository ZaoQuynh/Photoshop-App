from tkinter import *
from Constraint import *
from PIL import Image, ImageTk
from customtkinter import *


class ScrollHorizontalFrame(CTkScrollableFrame):
    def __init__(self, master, width=Sizes.WIDTH_BOTTOM.value, height=Sizes.HEIGHT_BOTTOM.value, color=Colors.BACKGROUND_V2.value):
        super().__init__(master,  width=width, height=height, fg_color=color, orientation="horizontal")


class MultilFeature(CTkFrame):
    def __init__(self, parent, background_color = Colors.BACKGROUND_V2.value ,width = None, height = None):
        super().__init__(master=parent, fg_color=background_color)
        self.btns = []

        self.selected_button = None

        if width is not None:
            self.configure(width = width)
        if height is not None:
            self.configure(height = height)

    def set_selected_btn(self, btn):
        self.selected_button = btn

    def get_selected_btn(self):
        return self.selected_button
    
    def set_btns(self, btns):
        self.btns = btns

        for btn in self.btns:
            btn.set_container(self)
            btn.pack(side = LEFT, padx = 10, pady = 5)

    def get_btns(self):
        return self.btns

    def draw(self):
        self.selected_button = None
        self.pack()

    def destroy(self):
        if self.winfo_exists() and self.winfo_ismapped():
            if self.selected_button is not None:
                self.selected_button.config(background=Colors.BTN_COLOR.value)
            for btn in self.btns:
                btn.hide_frame()
            self.pack_forget()

   

class FeatureScaleFrame(CTkFrame):
    def __init__(self, parent: Frame, variable_name, cmd = None, arrange = [0,100], w = Sizes.FEATURE_FRAME_WIDTH.value , h = Sizes.FEATURE_FRAME_HEIGHT.value, background = Colors.BACKGROUND_V3.value):
        super().__init__(master=parent)
        self.pack_propagate(FALSE)
        self.parent = parent
        self.width = w
        self.height = h
        self.background = background
        self.variable_value = 0
        self.command = cmd

        self.label_frame = Frame(self, width=self.width, height=30, background=self.background)
        self.label_frame.pack_propagate(FALSE)
        self.label_frame.pack(pady=5)

        self.label = Label(self.label_frame, text=variable_name, background=self.background)
        self.label_value = Label(self.label_frame, background=self.background)

        step = arrange[1] - arrange[0]
        self.scale = CTkSlider(self, from_=arrange[0], to=arrange[1], command=self.set_value, number_of_steps=step)

        self.update_button = CTkButton(self, width=100, height=20, text=Strings.UPDATE_BTN.value)

        if cmd is not None:
            self.update_button.configure(command = cmd)

        self.configure(width=self.width, height = self.height, fg_color = self.background)
        self.label.pack(side=LEFT, padx=20)
        self.scale.pack(pady=5)
        self.update_button.pack()
        
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
        if self.winfo_exists() and self.winfo_ismapped():
            self.pack_forget()


class FeatureButton(Button):
    def __init__(self, parent: Frame, text: str, img_path = None,
                 background = Colors.BTN_COLOR.value, 
                 color_border = Colors.BORDER_COLOR.value,
                 width_size = Sizes.WIDTH_FEATURE_BUTTON.value):
        
        super().__init__(parent, text = text, 
                         width = width_size)
        
        self.container = None
        self.frame = None

        if img_path != None:
            self.image =Image.open(img_path)
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

    def get_frame(self):
        return self.frame

    def set_container(self, container):
        self.container = container

    def get_container(self):
        return self.container

    def show_frame(self):
        if self.frame is not None:
            self.frame.draw() 

    def hide_frame(self):
        if self.frame is not None:
            self.frame.destroy()

    def select_button(self):
        temp_btn = self.container.get_selected_btn()
        if self.container is not None:
            if self != temp_btn:
                self.container.set_selected_btn(self)
            else:
                self.container.set_selected_btn(None)

            self.update_selected_btn_color()
    
    def update_selected_btn_color(self):
        temp_btn = self.container.get_selected_btn()
        for btn in self.container.btns:
            if btn is temp_btn:
                btn.config(bg = Colors.BTN_HIGHTLIGHT_COLOR.value)
                btn.show_frame()
            else:
                btn.config(bg = Colors.BTN_COLOR.value)
                btn.hide_frame()

