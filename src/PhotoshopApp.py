from tkinter import *
from customtkinter import *
from Constraint import *
from Components import *
from ImageProcessor import *

"""
Lớp giao diện chính của phần mềm
"""

class PhotoshopApp(Tk):
    def __init__(self):
        super().__init__()
        self.title(Strings.APP_TITLE.value)
        self.geometry(f"{Sizes.WIDTH.value}x{Sizes.HEIGHT.value}")
        self.resizable(False, False)
        self.config(bg= Colors.BACKGROUND.value)
        self.temp_img = None
        self.selected_img_path = None
        self.edit_step = []
        self.selected_button:Button = None

        self.main_view()


    def set_selected_img(self, value):
        self.selected_img = value
        self.selected_img_changed()

    # Click button

    def on_click_format_button(self, button: FeatureButton):
        button.select_button()

    def on_click_customize_button(self, button: FeatureButton):
        button.select_button()

    def on_click_cut_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_rotate_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_resize_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_brightness_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_contrast_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_saturation_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_blur__btn(self, button: FeatureButton):
        button.select_button()

    def on_click_sharpen_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_smoothing_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_draw_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_color_filter_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_blue_filter_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_pink_filter_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_yellow_filter_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_red_filter_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_green_filter_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_pen_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_red_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_blue_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_yellow_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_text_btn(self, button: FeatureButton):
        button.select_button()

    def on_click_red_eye_btn(self, button: FeatureButton):
        button.select_button()

    # Basic button

    def select_image(self):
        self.edit_step = []
        file_path = selected_image_path()

        if file_path:
            self.selected_img_path = file_path
            image = get_image(self.selected_img_path)
            self.set_selected_img(load_image(self.original_container, image, Sizes.ORIGINAL_FRAME.value))
            self.load_image_into_edit(image)

    def load_image_into_edit(self, image):
        if image is not None:
            self.temp_img = load_image(self.edit_container, image, Sizes.EDIT_FRAME.value)

    def update_image_into_selected(self):
        if self.temp_img is not None and self.temp_img != self.selected_img:
            self.set_selected_img(self.temp_img)
            self.edit_step.append(self.selected_img)
            
    def export_image(self):
        if self.selected_img:
            file_path = selected_image_path()
            if file_path:
                self.selected_img.save(file_path, format='PNG')
                print(f"Image saved to {file_path}")

    def undo(self):
        if(len(self.edit_step) > 0):
            self.edit_step.pop()
            self.set_selected_img(self.edit_step.pop())
            self.load_image_into_edit(self.selected_img)

    def restart(self):
        self.set_selected_img(None)
        self.selected_img_path = None
        self.edit_step = []
        self.edit_container.delete("all")
        self.original_container.delete("all")
        self.selected_img_changed()

    def run(self):
        self.mainloop()

    # Event

    def selected_img_changed(self):
        if self.selected_img != None:
            self.inner_frame.pack()
        else:
            self.inner_frame.pack_forget()

    # Draw View

    def main_view(self):
        control_panel = CTkFrame(self, 
                              width=Sizes.WIDTH_LEFT.value, 
                              fg_color=Colors.BACKGROUND_V2.value)
        control_panel.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        control_panel.pack_propagate(False)
        self.draw_control_panel(control_panel)

        processing_panel = Frame(self, 
                                 width=Sizes.WIDTH_RIGHT.value,  
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
                              relief=SOLID,
                              bg=Colors.BACKGROUND.value)
        main_panel.pack(side=TOP, fill=X)
        main_panel.pack_propagate(False)
        self.draw_main_panel(main_panel)
        
        feature_panel = CTkFrame(master = parent, 
                              height=Sizes.HEIGHT_BOTTOM.value, fg_color=Colors.BACKGROUND.value)
        feature_panel.pack(side=BOTTOM, fill=X, padx = 10, pady = 10)
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
                              bg=Colors.BACKGROUND.value, highlightthickness=0)
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
        self.inner_frame = MultilFeature(parent)

        self.create_feature_button(self.inner_frame)

    def create_feature_button(self, parent):
        format_btn = FeatureButton(parent, Strings.FORMAT_BTN.value, "images\ic_format_btn.png")
        format_multi_frame = MultilFeature(self.choice_frame)
        format_btn.set_frame(format_multi_frame)
        format_btn.config(command = lambda button=format_btn: self.on_click_format_button(button))

        format_btns = []

        cut_btn = FeatureButton(format_multi_frame, Strings.CUT_BTN.value, "images\ic_cut_btn.png")
        cut_btn.config(command = lambda button=cut_btn: self.on_click_cut_btn(button))
        
        rotation_btn = FeatureButton(format_multi_frame, Strings.ROTATION_BTN.value, "images\icon_rotate_btn.png")
        rotation_btn.config(command = lambda button=rotation_btn: self.on_click_rotate_btn(button))

        resize_btn = FeatureButton(format_multi_frame, Strings.SCALING_BTN.value, "images\icon_resize_btn.png")
        resize_btn.config(command = lambda button=resize_btn: self.on_click_resize_btn(button))
        
        format_btn_update = FeatureButton(format_multi_frame, Strings.UPDATE_BTN.value, "images\ic_update_btn.png")
        format_btn_update.config(command = lambda button=format_btn_update: self.update_image_into_selected())

        format_btns.append(cut_btn)
        format_btns.append(rotation_btn)
        format_btns.append(resize_btn)
        format_btns.append(format_btn_update)

        format_btn.get_frame().set_btns(format_btns)

        customize_btn = FeatureButton(parent, Strings.CUSTOMIZE_BTN.value, "images\ic_customize_btn.png")
        customize_multi_frame = MultilFeature(self.choice_frame)
        customize_btn.set_frame(customize_multi_frame)
        customize_btn.config(command = lambda button=customize_btn: self.on_click_customize_button(button))

        customize_btns = []

        brightness_btn = FeatureButton(customize_multi_frame, Strings.BRIGHTNESS_BTN.value, "images\ic_brightness_btn.png")
        brightness_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.BRIGHTNESS_BTN.value, lambda: self.update_image_into_selected()))
        brightness_btn.config(command = lambda button=brightness_btn: self.on_click_brightness_btn(button))

        contrast_btn = FeatureButton(customize_multi_frame, Strings.CONTRAST_BTN.value, "images\ic_contrast_btn.png")
        contrast_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.CONTRAST_BTN.value, lambda: self.update_image_into_selected()))
        contrast_btn.config(command = lambda button=contrast_btn: self.on_click_contrast_btn(button))

        saturation_btn = FeatureButton(customize_multi_frame, Strings.SATURATION_BTN.value, "images\ic_saturation_btn.png")
        saturation_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.SATURATION_BTN.value, lambda: self.update_image_into_selected()))
        saturation_btn.config(command = lambda button=saturation_btn: self.on_click_saturation_btn(button))

        customize_btns.append(brightness_btn)
        customize_btns.append(contrast_btn)
        customize_btns.append(saturation_btn)

        customize_btn.get_frame().set_btns(customize_btns)

        blur_btn = FeatureButton(parent, Strings.BLUR_BTN.value, "images\ic_blur_btn.png")
        blur_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.BLUR_BTN.value, lambda: self.update_image_into_selected()))
        blur_btn.config(command = lambda button=blur_btn: self.on_click_blur__btn(button))

        sharpen_btn = FeatureButton(parent, Strings.SHARPEN_BTN.value, "images\ic_sharpen_btn.png")
        sharpen_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.SHARPEN_BTN.value, lambda: self.update_image_into_selected()))
        sharpen_btn.config(command = lambda button=sharpen_btn: self.on_click_sharpen_btn(button))

        smoothing_btn = FeatureButton(parent, Strings.SMOOTHING_BTN.value, "images\ic_smoothing_btn.png")
        smoothing_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.SMOOTHING_BTN.value, lambda: self.update_image_into_selected()))
        smoothing_btn.config(command = lambda button=smoothing_btn: self.on_click_smoothing_btn(button))

        color_filter_btn = FeatureButton(parent, Strings.COLOR_FILTER_BTN.value, "images\ic_color_filter_btn.png")
        color_filter_multi_frame = MultilFeature(self.choice_frame)
        color_filter_btn.set_frame(color_filter_multi_frame)
        color_filter_btn.config(command = lambda button=color_filter_btn: self.on_click_color_filter_btn(button))

        color_filter_btns = []

        red_filter_btn = FeatureButton(color_filter_multi_frame, Strings.RED_FILTER_BTN.value, "images\ic_red_filter_btn.png")
        red_filter_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.BRIGHTNESS_BTN.value, lambda: self.update_image_into_selected()))
        red_filter_btn.config(command = lambda button=red_filter_btn: self.on_click_red_filter_btn(button))
        
        blue_filter_btn = FeatureButton(color_filter_multi_frame, Strings.BLUE_FILTER_BTN.value, "images\ic_blue_filter_btn.png")
        blue_filter_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.BRIGHTNESS_BTN.value, lambda: self.update_image_into_selected()))
        blue_filter_btn.config(command = lambda button=blue_filter_btn: self.on_click_blue_filter_btn(button))
        
        yellow_filter_btn = FeatureButton(color_filter_multi_frame, Strings.YELLOW_FILTER_BTN.value, "images\ic_yellow_filter_btn.png")
        yellow_filter_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.BRIGHTNESS_BTN.value, lambda: self.update_image_into_selected()))
        yellow_filter_btn.config(command = lambda button=yellow_filter_btn: self.on_click_yellow_filter_btn(button))
        
        pink_filter_btn = FeatureButton(color_filter_multi_frame, Strings.PINK_FILTER_BTN.value, "images\ic_pink_filter_btn.png")
        pink_filter_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.BRIGHTNESS_BTN.value, lambda: self.update_image_into_selected()))
        pink_filter_btn.config(command = lambda button=pink_filter_btn: self.on_click_pink_filter_btn(button))

        green_filter_btn = FeatureButton(color_filter_multi_frame, Strings.GREEN_FILTER_BTN.value, "images\ic_green_filter_btn.png")
        green_filter_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.BRIGHTNESS_BTN.value, lambda: self.update_image_into_selected()))
        green_filter_btn.config(command = lambda button=green_filter_btn: self.on_click_green_filter_btn(button))

        color_filter_btns.append(red_filter_btn)
        color_filter_btns.append(blue_filter_btn)
        color_filter_btns.append(yellow_filter_btn)
        color_filter_btns.append(pink_filter_btn)
        color_filter_btns.append(green_filter_btn)

        color_filter_btn.get_frame().set_btns(color_filter_btns)

        draw_btn = FeatureButton(parent, Strings.DRAW_BTN.value, "images\ic_draw_btn.png")
        draw_multi_frame = MultilFeature(self.choice_frame)
        draw_btn.set_frame(draw_multi_frame)
        draw_btn.config(command = lambda button=draw_btn: self.on_click_draw_btn(button))
        
        draw_btns = []
        
        pen_btn = FeatureButton(draw_multi_frame, Strings.PEN_BTN.value, "images\ic_pen_btn.png")
        pen_multi_frame = MultilFeature(self.custom_container)
        pen_btn.set_frame(pen_multi_frame)
        pen_btn.config(command = lambda button=pen_btn: self.on_click_pen_btn(button))

        pen_btns = []

        red_btn = FeatureButton(pen_multi_frame, Strings.RED_BTN.value, "images\ic_red_btn.png")
        red_btn.config(command = lambda button=red_btn: self.on_click_red_btn(button))

        blue_btn = FeatureButton(pen_multi_frame, Strings.BLUE_BTN.value, "images\ic_blue_btn.png")
        blue_btn.config(command = lambda button=blue_btn: self.on_click_blue_btn(button))

        yellow_btn = FeatureButton(pen_multi_frame, Strings.YELLOW_BTN.value, "images\ic_yellow_btn.png")
        yellow_btn.config(command = lambda button=yellow_btn: self.on_click_yellow_btn(button))

        pen_btns.append(red_btn)
        pen_btns.append(blue_btn)
        pen_btns.append(yellow_btn)

        pen_btn.get_frame().set_btns(pen_btns)

        text_btn = FeatureButton(draw_multi_frame, Strings.TEXT_BTN.value, "images\ic_text_btn.png")
        text_btn.config(command = lambda button=text_btn: self.on_click_text_btn(button))

        draw_btn_update = FeatureButton(draw_multi_frame, Strings.UPDATE_BTN.value, "images\ic_update_btn.png")
        draw_btn_update.config(command = lambda button=draw_btn_update: self.update_image_into_selected())

        draw_btns.append(pen_btn)
        draw_btns.append(text_btn)
        draw_btns.append(draw_btn_update)

        draw_btn.get_frame().set_btns(draw_btns)

        red_eye_btn = FeatureButton(parent, Strings.RED_EYE_BTN.value, "images\ic_red_eye_btn.png")
        red_eye_btn.config(command = lambda button=red_eye_btn: self.on_click_red_eye_btn(button))

        feature_btns = []
        feature_btns.append(format_btn)
        feature_btns.append(customize_btn)
        feature_btns.append(blur_btn)
        feature_btns.append(sharpen_btn)
        feature_btns.append(smoothing_btn)
        feature_btns.append(color_filter_btn)
        feature_btns.append(draw_btn)
        feature_btns.append(red_eye_btn)

        parent.set_btns(feature_btns)


    