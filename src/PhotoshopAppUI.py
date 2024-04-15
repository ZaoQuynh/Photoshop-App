from tkinter import *
from customtkinter import *
from Constraint import *
from Components import *
from ImageProcessor import *

"""
Lớp giao diện chính của phần mềm
"""

class PhotoshopAppUI(Tk):
    def __init__(self):
        super().__init__()
        self.title(Strings.APP_TITLE.value)
        self.geometry(f"{Sizes.WIDTH.value}x{Sizes.HEIGHT.value}")
        self.resizable(False, False)
        self.bg = Colors.BACKGROUND.value
        self.selected_img = None
        self.selected_img_path = None
        self.edit_step = []
        self.feature_btns = []
        self.selected_button:Button = None

        self.main_view()

    def main_view(self):
        """
        Vẽ nền cho giao diện
        control_panel: phần giao diện chứa các button: Load, Export, Undo, Reset
        processing_panel: phần giao diện hiển thị ảnh và các chức năng xử lý
        """
        control_panel = Frame(self, 
                              width=Sizes.WIDTH_LEFT.value, 
                              borderwidth=1, 
                              relief=SOLID,
                              bg=Colors.BACKGROUND.value)
        control_panel.pack(side="left", fill="both", expand=True)
        control_panel.pack_propagate(False)
        self.draw_control_panel(control_panel)

        processing_panel = Frame(self, 
                                 width=Sizes.WIDTH_RIGHT.value,  
                                 borderwidth=1, 
                                 relief=SOLID,
                                 bg=Colors.BACKGROUND.value)
        processing_panel.pack(side="right", fill="both", expand=True)
        processing_panel.pack_propagate(False)
        self.draw_processing_panel(processing_panel)
        
    def draw_control_panel(self, parent):
        load_btn = CTkButton(parent, 
                          width=Sizes.WIDTH_BTN.value, 
                          text = Strings.LOAD_BTN.value,
                          command=self.select_image)
        load_btn.pack(side=TOP, 
                      padx=10,
                      pady=5)
        
        export_btn = CTkButton(parent, 
                          width=Sizes.WIDTH_BTN.value, 
                          text = Strings.EXPORT_BTN.value,
                          command = self.export_image)
        export_btn.pack(side=TOP, 
                      padx=10,
                      pady=5)
        
        
        undo_btn = CTkButton(parent, 
                          width=Sizes.WIDTH_BTN.value,  
                          text = Strings.UNDO_BTN.value,
                          command=self.undo)
        undo_btn.pack(side=TOP, 
                      padx=10,
                      pady=5)
        
        
        restart_btn = CTkButton(parent, 
                          width=Sizes.WIDTH_BTN.value,  
                          text = Strings.RESTART_BTN.value,
                          command=self.restart)
        restart_btn.pack(side=TOP, 
                      padx=10,
                      pady=5)

    def draw_processing_panel(self, parent):
        main_panel = Frame(parent, 
                              height=Sizes.HEIGHT_TOP.value,  
                              borderwidth=1, 
                              relief=SOLID,
                              bg=Colors.BACKGROUND.value)
        main_panel.pack(side=TOP, fill=X)
        main_panel.pack_propagate(False)
        self.draw_main_panel(main_panel)
        
        feature_panel = Frame(parent, 
                              height=Sizes.HEIGHT_BOTTOM.value, 
                              borderwidth=1, 
                              relief=SOLID,
                              bg=Colors.BACKGROUND.value)
        feature_panel.pack(side=BOTTOM, fill=X)
        feature_panel.pack_propagate(False)
        self.draw_feature_panel(feature_panel)

    def draw_main_panel(self, parent):
        top_frame = Frame(parent, width=950, height=510,
                              bg=Colors.BACKGROUND.value)
        top_frame.pack(side=TOP)
        top_frame.pack_propagate(False)

        left_frame = Frame(top_frame, width=400, height=510,
                              bg=Colors.BACKGROUND.value)
        left_frame.pack(side=LEFT)
        left_frame.pack_propagate(False)

        self.original_container = Canvas(left_frame, width=Sizes.ORIGINAL_FRAME.value, height=Sizes.ORIGINAL_FRAME.value,
                              bg=Colors.BACKGROUND_V2.value)
        self.original_container.pack(side=TOP, padx=15, pady=10)

        self.custom_container = Canvas(left_frame, width=Sizes.FEATURE_FRAME_WIDTH.value, height=Sizes.FEATURE_FRAME_HEIGHT.value,
                              bg=Colors.BACKGROUND.value)
        self.custom_container.pack(side=TOP, padx=15, pady=25)

        right_frame = Frame(top_frame, width=550, height=510,
                              bg=Colors.BACKGROUND.value)
        right_frame.pack(side=RIGHT)
        right_frame.pack_propagate(False)

        self.edit_container = Canvas(right_frame, width=Sizes.EDIT_FRAME.value, height=Sizes.EDIT_FRAME.value,
                              bg=Colors.BACKGROUND_V2.value)
        self.edit_container.pack(padx=10, pady=10)

        self.choice_frame = Frame(parent, width=950, height=100,
                              bg=Colors.BACKGROUND.value)
        self.choice_frame.pack(side=BOTTOM)
        self.choice_frame.pack_propagate(False)

    def draw_feature_panel(self, parent):
        inner_frame = ScrollHorizontalFrame(parent)

        self.create_feature_button(inner_frame)
        
        inner_frame.pack()


    def create_feature_button(self, parent):
        cut_btn = FeatureButton(parent, Strings.CUT_BTN.value, "images\ic_cut_btn.png")
        cut_btn.config(command = lambda button=cut_btn: self.on_click_cut_btn(button))
        cut_btn.pack(side=LEFT, padx=10, pady=5)
        cut_btn.pack_propagate(FALSE)
        
        rotation_btn = FeatureButton(parent, Strings.ROTATION_BTN.value, "images\icon_rotate_btn.png")
        rotation_btn.config(command = lambda button=rotation_btn: self.on_click_rotate_btn(button))
        rotation_btn.pack(side=LEFT, padx=10, pady=5)
        rotation_btn.pack_propagate(FALSE)

        resize_btn = FeatureButton(parent, Strings.SCALING_BTN.value, "images\icon_resize_btn.png")
        resize_btn.config(command = lambda button=resize_btn: self.on_click_resize_btn(button))
        resize_btn.pack(side=LEFT, padx=10, pady=5)
        resize_btn.pack_propagate(FALSE)

        brightness_btn = FeatureButton(parent, Strings.BRIGHTNESS_BTN.value, "images\ic_brightness_btn.png")
        brightness_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.BRIGHTNESS_BTN.value))
        brightness_btn.config(command = lambda button=brightness_btn: self.on_click_brightness_btn(button))
        brightness_btn.pack(side=LEFT, padx=10, pady=5)
        brightness_btn.pack_propagate(FALSE)

        contrast_btn = FeatureButton(parent, Strings.CONTRAST_BTN.value, "images\ic_contrast_btn.png")
        contrast_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.CONTRAST_BTN.value))
        contrast_btn.config(command = lambda button=contrast_btn: self.on_click_contrast_btn(button))
        contrast_btn.pack(side=LEFT, padx=10, pady=5)
        contrast_btn.pack_propagate(FALSE)

        saturation_btn = FeatureButton(parent, Strings.SATURATION_BTN.value, "images\ic_saturation_btn.png")
        saturation_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.SATURATION_BTN.value))
        saturation_btn.config(command = lambda button=saturation_btn: self.on_click_saturation_btn(button))
        saturation_btn.pack(side=LEFT, padx=10, pady=5)
        saturation_btn.pack_propagate(FALSE)

        blur_btn = FeatureButton(parent, Strings.BLUR_BTN.value, "images\ic_blur_btn.png")
        blur_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.BLUR_BTN.value))
        blur_btn.config(command = lambda button=blur_btn: self.on_click_blur__btn(button))
        blur_btn.pack(side=LEFT, padx=10, pady=5)
        blur_btn.pack_propagate(FALSE)

        sharpen_btn = FeatureButton(parent, Strings.SHARPEN_BTN.value, "images\ic_sharpen_btn.png")
        sharpen_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.SHARPEN_BTN.value))
        sharpen_btn.config(command = lambda button=sharpen_btn: self.on_click_sharpen_btn(button))
        sharpen_btn.pack(side=LEFT, padx=10, pady=5)
        sharpen_btn.pack_propagate(FALSE)

        color_filter_btn = FeatureButton(parent, Strings.COLOR_FILTER_BTN.value, "images\ic_color_filter_btn.png")
        color_filter_btn.pack(side=LEFT, padx=10, pady=5)
        color_filter_btn.pack_propagate(FALSE)

        draw_btn = FeatureButton(parent, Strings.DRAW_BTN.value, "images\ic_draw_btn.png")
        draw_btn.pack(side=LEFT, padx=10, pady=5)
        draw_btn.pack_propagate(FALSE)

        smoothing_btn = FeatureButton(parent, Strings.SMOOTHING_BTN.value, "images\ic_smoothing_btn.png")
        smoothing_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.SMOOTHING_BTN.value))
        smoothing_btn.config(command = lambda button=smoothing_btn: self.on_click_smoothing_btn(button))
        smoothing_btn.pack(side=LEFT, padx=10, pady=5)
        smoothing_btn.pack_propagate(FALSE)

        red_eye_btn = FeatureButton(parent, Strings.RED_EYE_BTN.value, "images\ic_red_eye_btn.png")
        red_eye_btn.config(command = lambda button=red_eye_btn: self.on_click_red_eye_btn(button))
        red_eye_btn.pack(side=LEFT, padx=10, pady=5)
        red_eye_btn.pack_propagate(FALSE)

        self.feature_btns.append(cut_btn)
        self.feature_btns.append(rotation_btn)
        self.feature_btns.append(resize_btn)
        self.feature_btns.append(brightness_btn)
        self.feature_btns.append(contrast_btn)
        self.feature_btns.append(saturation_btn)
        self.feature_btns.append(blur_btn)
        self.feature_btns.append(sharpen_btn)
        self.feature_btns.append(color_filter_btn)
        self.feature_btns.append(draw_btn)
        self.feature_btns.append(smoothing_btn)
        self.feature_btns.append(red_eye_btn)

        # for btn in self.feature_btns:
        #     btn.config(command = lambda button=btn: self.select_button(button))
    
    def on_click_cut_btn(self, button: FeatureButton):
        self.select_button(button)

    def on_click_rotate_btn(self, button: FeatureButton):
        self.select_button(button)

    def on_click_resize_btn(self, button: FeatureButton):
        self.select_button(button)

    def on_click_brightness_btn(self, button: FeatureButton):
        self.select_button(button)

    def on_click_contrast_btn(self, button: FeatureButton):
        self.select_button(button)

    def on_click_saturation_btn(self, button: FeatureButton):
        self.select_button(button)

    def on_click_blur__btn(self, button: FeatureButton):
        self.select_button(button)

    def on_click_sharpen_btn(self, button: FeatureButton):
        self.select_button(button)

    def on_click_smoothing_btn(self, button: FeatureButton):
        self.select_button(button)

    def on_click_red_eye_btn(self, button: FeatureButton):
        self.select_button(button)

    def select_button(self, btn: FeatureButton):
        if (self.selected_button != btn):
            self.selected_button = btn
        else:
            self.selected_button = None

        self.update_selected_btn_color()
    
    def update_selected_btn_color(self):
        for btn in self.feature_btns:
            if btn is self.selected_button:
                btn.config(bg = Colors.BTN_HIGHTLIGHT_COLOR.value)
                btn.show_frame()
            else:
                btn.config(bg = Colors.BTN_COLOR.value)
                btn.hide_frame()

    def select_image(self):
        self.edit_step = []
        file_path = selected_image_path()

        if file_path:
            self.selected_img_path = file_path
            image = get_image(self.selected_img_path)
            load_image(self.original_container, image, Sizes.ORIGINAL_FRAME.value)
            self.load_image_into_edit(image)

    def load_image_into_edit(self, image):
        self.select_image = load_image(self.edit_container, image, Sizes.EDIT_FRAME.value)
        self.edit_step.append(self.select_image)

    def export_image(self):
        if self.selected_img:
            file_path = selected_image_path()
            if file_path:
                self.selected_img.save(file_path, format='PNG')
                print(f"Image saved to {file_path}")

    def undo(self):
        if(len(self.edit_step) > 0):
            self.edit_step.pop()
            self.selected_img = self.edit_step.pop()
            self.load_image_into_edit(self.selected_img)

    def restart(self):
        self.selected_img = None
        self.selected_img_path = None
        self.edit_step = []
        self.edit_container.delete("all")
        self.original_container.delete("all")
        self.selected_button = None
        self.update_selected_btn_color()

    def run(self):
        self.mainloop()