from tkinter import *
from customtkinter import *
from Constraint import *
from Components import *
from ImageProcessor import *
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser

class PhotoshopApp(Tk):
    def __init__(self):
        super().__init__()
        self.title(Strings.APP_TITLE.value)
        self.geometry(f"{Sizes.WIDTH.value}x{Sizes.HEIGHT.value}")
        self.resizable(False, False)
        self.iconbitmap("images\logo.ico")
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
        self.show_selected()
        button.select_button()

    def on_click_customize_button(self, button: FeatureButton):
        self.show_selected()
        button.select_button()

    def on_click_cut_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()
    
    def cut_processing(self, var = None, index = None, mode = None):
        max_size = 100

        try:
            left = int(self.left_img.get())
            top = int(self.top_img.get())
            right = int(self.right_img.get())
            bottom = int(self.bottom_img.get())
            if max_size >= left >= 0 and max_size >= top >= 0 and max_size >= right >= left and max_size >= bottom >= top:
                self.temp_img = self.selected_img.crop((left, top, right, bottom))
                self.load_image_into_edit(self.temp_img)

                return
            else:
                messagebox.showwarning("Cảnh báo", f"Giá trị không hợp lệ. Vui lòng nhập lại với giá trị trong khoảng từ 0 đến {max_size}")
        except ValueError:
            pass

        # Nếu có lỗi xảy ra hoặc người dùng nhập giá trị không hợp lệ, giữ nguyên hình ảnh ban đầu
        # width, height = self.selected_img.size
        # self.left_img.set(str(0))
        # self.top_img.set(str(0))
        # self.right_img.set(str(width))
        # self.bottom_img.set(str(height))

    def on_click_rotate_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()

    def rotate_image(self, angle):
        if self.selected_img:
            rotated_image = self.selected_img.rotate(angle, expand=True)
            self.update_image_into_selected()
            self.temp_img = rotated_image
            self.load_image_into_edit(rotated_image)

    def on_click_rotate_minus_90_button(self, button: FeatureButton):
        self.show_selected()
        self.rotate_image(-90)
        button.select_button()
        self.update_image_into_selected_and_reset_button(button)

    def on_click_rotate_90_button(self, button: FeatureButton):
        self.show_selected()
        self.rotate_image(90)
        button.select_button()
        self.update_image_into_selected_and_reset_button(button)


    def on_click_resize_btn(self, button: FeatureButton):
        self.show_selected()
        w, h = self.selected_img.size
        self.w_img.set(int(w))
        self.h_img.set(int(h))
        button.select_button()

    def on_click_brightness_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()
    
    def brightness_processing(self, var = None, index = None, mode = None):
        result = brightness_feature(self.selected_img, self.brightness_btn.frame.get_value())
        self.load_image_into_edit(result)

    def on_click_contrast_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()
    
    def contrast_processing(self, var = None, index= None, mode= None):
        result = contrast_feature(self.selected_img, self.contrast_btn.frame.get_value())
        self.load_image_into_edit(result)

    def on_click_saturation_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()

    def saturation_processing(self, var = None, index= None, mode= None):
        result = saturation_feature(self.selected_img, self.saturation_btn.frame.get_value())
        self.load_image_into_edit(result)

    def on_click_blur__btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()

    def on_click_sharpen_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()

    def sharpen_processing(self, var = None, index= None, mode= None):
        result = sharpen_feature(self.selected_img, self.sharpen_btn.frame.get_value())
        self.load_image_into_edit(result)

    def on_click_smoothing_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()

    def on_click_draw_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()

    def on_click_color_filter_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()

    def on_click_blue_filter_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()

    def blue_filter_processing(self, var = None, index= None, mode= None):
        result = color_filter(self.selected_img, 0, 3, 1, self.blue_filter_btn.frame.get_value())
        self.load_image_into_edit(result)

    def on_click_pink_filter_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()

    def pink_filter_processing(self, var = None, index= None, mode= None):
        result = color_filter(self.selected_img, 2, 0, 1, self.pink_filter_btn.frame.get_value())
        self.load_image_into_edit(result)

    def on_click_yellow_filter_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()
    
    def yellow_filter_processing(self, var = None, index= None, mode= None):
        result = color_filter(self.selected_img, 2, 1, 1, self.yellow_filter_btn.frame.get_value())
        self.load_image_into_edit(result)

    def on_click_red_filter_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()

    def red_filter_processing(self, var = None, index= None, mode= None):
        result = color_filter(self.selected_img, 2, 3, 1, self.red_filter_btn.frame.get_value())
        self.load_image_into_edit(result)

    def on_click_green_filter_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()

    def green_filter_processing(self, var = None, index= None, mode= None):
        result = color_filter(self.selected_img, 1, 3, 1, self.green_filter_btn.frame.get_value())
        self.load_image_into_edit(result)

    def on_click_pen_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()

    def on_click_red_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()

    def on_click_blue_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()

    def on_click_yellow_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()

    def on_click_text_btn(self, button: FeatureButton):
        self.show_selected()
        button.select_button()

    # Basic button

    def select_image(self):
        self.restart()
        self.edit_step = []
        file_path = selected_image_path()

        if file_path:
            self.selected_img_path = file_path
            image = get_image(self.selected_img_path)
            self.set_selected_img(load_image(self.original_container, image, Sizes.ORIGINAL_FRAME.value, Sizes.ORIGINAL_FRAME.value))
            self.load_image_into_edit(image)

    def load_image_into_edit(self, image):
        if image is not None:
            self.temp_img = load_image(self.edit_container, image, Sizes.EDIT_FRAME.value, Sizes.EDIT_FRAME.value)

    def update_image_into_selected(self):
        if self.temp_img is not None and self.temp_img != self.selected_img:
            self.edit_step.append(self.selected_img)
            self.set_selected_img(load_image(self.original_container, self.temp_img, Sizes.ORIGINAL_FRAME.value, Sizes.ORIGINAL_FRAME.value))
            self.load_image_into_edit(self.temp_img)

    def update_image_into_selected_and_reset_button(self, button):
        self.update_image_into_selected()
        button.frame.draw()
                        
    def export_image(self):
        if self.selected_img:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                self.selected_img.save(file_path, format='PNG')
                print(f"Image saved to {file_path}")

    def undo(self):
        if(len(self.edit_step) > 0):
            self.set_selected_img(self.edit_step.pop())
            self.show_selected()
            print("Undo")

    def restart(self):
        self.set_selected_img(None)
        self.selected_img_path = None
        self.edit_step = []
        self.edit_container.delete("all")
        self.original_container.delete("all")
        self.inner_frame.destroy()
        self.selected_img_changed()

    def show_selected(self):
        self.set_selected_img(load_image(self.original_container, self.selected_img, Sizes.ORIGINAL_FRAME.value, Sizes.ORIGINAL_FRAME.value))
        self.load_image_into_edit(self.selected_img)
        self.temp_img = self.selected_img

    def run(self):
        self.mainloop()

    # Event

    def selected_img_changed(self):
        if self.selected_img != None:
            self.start_frame.pack_forget()
            self.processing_panel.pack(side="right", fill="both", expand=True)
            self.inner_frame.draw()
        else:
            self.processing_panel.pack_forget()
            self.start_frame.pack(side="right", fill="both", expand=True)
            self.inner_frame.destroy()

    def resize_processing(self):
        self.width_status.grid_forget()
        self.height_status.grid_forget()
        max = Sizes.MAX_IMG.value
        min = Sizes.MIN_IMG.value

        try:
            temp_w = int(self.w_img.get())
            temp_h = int(self.h_img.get())

            if max >= temp_w >= min and max >= temp_h >= min:
                self.temp_img = self.selected_img.resize((temp_w, temp_h), Image.BICUBIC)
                self.load_image_into_edit(self.temp_img)
                self.width_status.grid(row=2, column=2, padx=5, pady=5)
                self.height_status.grid(row=3, column=2, padx=5, pady=5)
                return
            else:
                messagebox.showwarning("Cảnh báo", f"Kích thước không phù hợp. Vui lòng nhập lại với kích thước trong khoảng {min} đến {max}")
        except ValueError:
            pass
             
        w, h = self.selected_img.size
        self.w_img.set(str(w))
        self.h_img.set(str(h))

    # Draw View

    def main_view(self):
        control_panel = CTkFrame(self, 
                              width=Sizes.WIDTH_LEFT.value, 
                              fg_color=Colors.BACKGROUND_V2.value)
        control_panel.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        control_panel.pack_propagate(False)
        self.draw_control_panel(control_panel)

        self.processing_panel = Frame(self, 
                                 width=Sizes.WIDTH_RIGHT.value,  
                                 bg=Colors.BACKGROUND.value)
        self.processing_panel.pack(side="right", fill="both", expand=True)
        self.processing_panel.pack_propagate(False)
        self.draw_processing_panel(self.processing_panel)
        self.processing_panel.pack_forget()
        
        self.draw_start_window()
        
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
        self.original_container.pack_propagate(False)

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
        self.edit_container.pack_propagate(False)

        self.choice_frame = Frame(parent, width=950, height=100,
                              bg=Colors.BACKGROUND.value)
        self.choice_frame.pack(side=BOTTOM)
        self.choice_frame.pack_propagate(False)

    def draw_feature_panel(self, parent):
        self.inner_frame = MultilFeature(parent)

        self.create_feature_button(self.inner_frame)

    def draw_start_window(self):
        self.start_frame = Frame(self, 
                                 width=Sizes.WIDTH_RIGHT.value,  
                                 bg=Colors.BACKGROUND.value)
        self.start_frame.pack(side="right", fill="both", expand=True)
        self.start_frame.pack_propagate(False)

        #Background
        load_gif_into_frame(self.start_frame, "gifs\_background.gif", Sizes.WIDTH_RIGHT.value)


        infor_frame = CTkFrame(self.start_frame, bg_color=Colors.BACKGROUND_V2.value)
        infor_frame.pack(expand = True, anchor = "se", pady = 20, padx = 20)

        infor_frame_right = CTkFrame(infor_frame) 
        infor_frame_right.pack(side = RIGHT, pady = 5, padx = 5)

        group_name = CTkLabel(infor_frame_right, text="--- Nhóm 7 ---", font=("Helvetica", 14, "bold"))
        group_name.grid(row=0, column=0, columnspan=2, padx=5, pady=2)

        member1 = CTkLabel(infor_frame_right, text="Nguyễn Hà Quỳnh Giao")
        member1.grid(row=1, column=0, padx=10, pady=2)

        member1_id = CTkLabel(infor_frame_right, text="21110171")
        member1_id.grid(row=1, column=1, padx=10, pady=2)

        member2 = CTkLabel(infor_frame_right, text="Lê Tân")
        member2.grid(row=2, column=0, padx=10, pady=2)

        member2_id = CTkLabel(infor_frame_right, text="21110296")
        member2_id.grid(row=2, column=1, padx=10, pady=2)

        member3 = CTkLabel(infor_frame_right, text="Hoàng Công Mạnh")
        member3.grid(row=3, column=0, padx=10, pady=2)

        member3_id = CTkLabel(infor_frame_right, text="21110839")
        member3_id.grid(row=3, column=1, padx=10, pady=2)

        infor_frame_left = CTkFrame(infor_frame)
        infor_frame_left.pack( pady = 5, padx = 5, side=LEFT)

        schoool_image = ImageTk.PhotoImage(Image.open("images\ic_school.png").resize((20, 25), Image.BICUBIC))

        schoool_label = Label(infor_frame_left, image=schoool_image, background=Colors.BACKGROUND_V4.value)
        schoool_label.grid(row=0, column=0, padx=10, pady=2)
        schoool_label.photo = schoool_image

        school_infor = CTkLabel(infor_frame_left, text="Trường Đại Học Sư Phạm Kỹ Thuật TP.HCM")
        school_infor.grid(row=0, column=1, padx=10, pady=2)

        subject_label = CTkLabel(infor_frame_left, text="Môn:")
        subject_label.grid(row=1, column=0, padx=10, pady=2)

        subject_infor = CTkLabel(infor_frame_left, text="Xử lý ảnh số")
        subject_infor.grid(row=1, column=1, padx=10, pady=2)

        teacher_label = CTkLabel(infor_frame_left, text="GVHD:")
        teacher_label.grid(row=2, column=0, padx=10, pady=2)

        teacher_infor = CTkLabel(infor_frame_left, text="PGS.TS Hoàng Văn Dũng")
        teacher_infor.grid(row=2, column=1, padx=10, pady=2)

        github_image = ImageTk.PhotoImage(Image.open("images\ic_github.png").resize((20, 20), Image.BICUBIC))

        github_label = Label(infor_frame_left, image=github_image, background=Colors.BACKGROUND_V4.value)
        github_label.grid(row=3, column=0, padx=10, pady=2)
        github_label.photo = github_image

        github_contact = CTkButton(infor_frame_left, text="Github", command=self.visit_github)
        github_contact.grid(row=3, column=1, padx=10, pady=2)
    
    def visit_github(self):
        webbrowser.open("https://github.com/ZaoQuynh/Photoshop-App")

    def create_feature_button(self, parent):
        format_btn = FeatureButton(parent, Strings.FORMAT_BTN.value, "images\ic_format_btn.png")
        format_multi_frame = MultilFeature(self.choice_frame)
        format_btn.set_frame(format_multi_frame)
        format_btn.config(command = lambda button=format_btn: self.on_click_format_button(button))

        format_btns = []

        self.left_img = StringVar()
        self.right_img = StringVar()
        self.top_img = StringVar()
        self.bottom_img = StringVar()
        self.left_img.set(str(0))
        self.right_img.set(str(0))
        self.top_img.set(str(0))
        self.bottom_img.set(str(0))

        cut_btn = FeatureButton(format_multi_frame, Strings.CUT_BTN.value, "images\ic_cut_btn.png")
        cut_edit_frame = MultilFeature(self.custom_container)
        cut_btn.set_frame(cut_edit_frame)
        cut_btn.config(command = lambda button=cut_btn: self.on_click_cut_btn(button))

        padding_left = Label(cut_edit_frame, text=Strings.PADDING_LEFT.value, background=Colors.BACKGROUND_V2.value, fg=Colors.TEXT_HIGHTLIGHT_COLOR.value)
        padding_left.grid(row=0, column=0, padx=5, pady=5)
        padding_left_input = CTkEntry(cut_edit_frame, textvariable=self.left_img)
        padding_left_input.grid(row=0, column=1, padx=5, pady=5)

        padding_top = Label(cut_edit_frame, text=Strings.PADDING_TOP.value, background=Colors.BACKGROUND_V2.value, fg=Colors.TEXT_HIGHTLIGHT_COLOR.value)
        padding_top.grid(row=1, column=0, padx=5, pady=5)
        padding_top_input = CTkEntry(cut_edit_frame, textvariable=self.top_img)
        padding_top_input.grid(row=1, column=1, padx=5, pady=5)

        padding_right = Label(cut_edit_frame, text=Strings.PADDING_RIGHT.value, background=Colors.BACKGROUND_V2.value, fg=Colors.TEXT_HIGHTLIGHT_COLOR.value)
        padding_right.grid(row=2, column=0, padx=5, pady=5)
        padding_right_input = CTkEntry(cut_edit_frame, textvariable=self.right_img)
        padding_right_input.grid(row=2, column=1, padx=5, pady=5)

        padding_bottom = Label(cut_edit_frame, text=Strings.PADDING_BOTTOM.value, background=Colors.BACKGROUND_V2.value, fg=Colors.TEXT_HIGHTLIGHT_COLOR.value)
        padding_bottom.grid(row=3, column=0, padx=5, pady=5)
        padding_bottom_input = CTkEntry(cut_edit_frame, textvariable=self.bottom_img)
        padding_bottom_input.grid(row=3, column=1, padx=5, pady=5)

        padding_bottom_input.bind("<Return>", lambda event: self.cut_processing())
        padding_top_input.bind("<Return>", lambda event: self.cut_processing())
        padding_right_input.bind("<Return>", lambda event: self.cut_processing())
        padding_left_input.bind("<Return>", lambda event: self.cut_processing())

        cut_btn.config(command = lambda button=cut_btn: self.on_click_cut_btn(button))
        
        rotation_btn = FeatureButton(format_multi_frame, Strings.ROTATION_BTN.value, "images\icon_rotate_btn.png")
        rotation_multi_frame = MultilFeature(self.custom_container)
        rotation_btn.set_frame(rotation_multi_frame)
        rotation_btn.config(command = lambda button=rotation_btn: self.on_click_rotate_btn(button))

        rotation_btns = []

        rotate_90_button  = FeatureButton(rotation_multi_frame, Strings.ROTATE_90_BTN.value, "images\ic_rotate_90.png")
        rotate_90_button .config(command = lambda button=rotate_90_button: self.on_click_rotate_90_button(button))

        rotate_minus_90_button = FeatureButton(rotation_multi_frame, Strings.ROTATE_MINUS_90_BTN.value, "images\ic_rotate_minus_90.png")
        rotate_minus_90_button .config(command = lambda button=rotate_minus_90_button: self.on_click_rotate_minus_90_button(button))

        rotation_btns.append(rotate_90_button)
        rotation_btns.append(rotate_minus_90_button)

        rotation_btn.get_frame().set_btns(rotation_btns)

        resize_btn = FeatureButton(format_multi_frame, Strings.SCALING_BTN.value, "images\icon_resize_btn.png")
        resize_edit_frame = MultilFeature(self.custom_container)
        resize_btn.set_frame(resize_edit_frame)
        resize_btn.config(command = lambda button=resize_btn: self.on_click_resize_btn(button))

        self.w_img = StringVar()
        self.h_img = StringVar()
        self.w_img.set(str(0))
        self.h_img.set(str(0))

        resize_edit_frame_label = Label(resize_edit_frame, text="Nhấn Enter để thiết lập giá trị biến đổi!", background = Colors.BACKGROUND_V2.value, fg=Colors.TEXT_HIGHTLIGHT_COLOR.value)
        resize_edit_frame_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        resize_edit_frame_note = Label(resize_edit_frame, text= f"Lưu ý: Nhập giá trị trong khoảng {Sizes.MIN_IMG.value} đến {Sizes.MAX_IMG.value}", background = Colors.BACKGROUND_V2.value, fg=Colors.TEXT_NOTE.value)
        resize_edit_frame_note.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        width_label = Label(resize_edit_frame, text=Strings.WIDTH_TEXT.value, background = Colors.BACKGROUND_V2.value, fg=Colors.TEXT_HIGHTLIGHT_COLOR.value)
        width_label.grid(row=2, column=0, padx=5, pady=5)
        width_input = CTkEntry(resize_edit_frame, textvariable=self.w_img)
        width_input.grid(row=2, column=1, padx=5, pady=5)

        status_image = ImageTk.PhotoImage(Image.open("images\ic_check.png").resize((20, 20), Image.BICUBIC))

        self.width_status = Label(resize_edit_frame, image=status_image, background = Colors.BACKGROUND_V2.value)
        self.width_status.photo = status_image

        height_label = Label(resize_edit_frame, text=Strings.HEIGHT_TEXT.value, background = Colors.BACKGROUND_V2.value, fg=Colors.TEXT_HIGHTLIGHT_COLOR.value)
        height_label.grid(row=3, column=0, padx=5, pady=5)
        height_input = CTkEntry(resize_edit_frame, textvariable=self.h_img)
        height_input.grid(row=3, column=1, padx=5, pady=5)

        self.height_status = Label(resize_edit_frame, image=status_image, background = Colors.BACKGROUND_V2.value)
        self.height_status.photo = status_image

        width_input.bind("<Return>", lambda event: self.resize_processing())
        height_input.bind("<Return>", lambda event: self.resize_processing())

        resize_btn.config(command = lambda button=resize_btn: self.on_click_resize_btn(button))

        format_btn_update = FeatureButton(format_multi_frame, Strings.UPDATE_BTN.value, "images\ic_update_btn.png")
        format_btn_update.config(command = lambda: self.update_image_into_selected())

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

        self.brightness_btn = FeatureButton(customize_multi_frame, Strings.BRIGHTNESS_BTN.value, "images\ic_brightness_btn.png")
        self.brightness_btn.set_frame(
            FeatureScaleFrame(
                self.custom_container,
                Strings.BRIGHTNESS_BTN.value, 
                lambda button=self.brightness_btn: self.update_image_into_selected_and_reset_button(button),
                lambda event, arg1, arg2: self.brightness_processing(),
                range = [-50, 50], 
                init_value = 0))
        
        self.brightness_btn.config(command = lambda button=self.brightness_btn: self.on_click_brightness_btn(button))

        self.contrast_btn = FeatureButton(customize_multi_frame, Strings.CONTRAST_BTN.value, "images\ic_contrast_btn.png")
        self.contrast_btn.set_frame(
            FeatureScaleFrame(
                self.custom_container, Strings.CONTRAST_BTN.value,
                lambda button= self.contrast_btn: self.update_image_into_selected_and_reset_button(button),
                lambda event, arg1, arg2: self.contrast_processing(),
                range = [-50, 50], 
                init_value = 0))
        self.contrast_btn.config(command = lambda button= self.contrast_btn: self.on_click_contrast_btn(button))

        self.saturation_btn = FeatureButton(customize_multi_frame, Strings.SATURATION_BTN.value, "images\ic_saturation_btn.png")
        self.saturation_btn.set_frame(
            FeatureScaleFrame(
                self.custom_container, 
                Strings.SATURATION_BTN.value, 
                lambda button=self.saturation_btn: self.update_image_into_selected_and_reset_button(button), 
                lambda event, arg1, arg2: self.saturation_processing(),
                range = [-50, 50], 
                init_value = 0))
        self.saturation_btn.config(command = lambda button=self.saturation_btn: self.on_click_saturation_btn(button))
        
        customize_btns.append(self.brightness_btn)
        customize_btns.append(self.contrast_btn)
        customize_btns.append(self.saturation_btn)

        customize_btn.get_frame().set_btns(customize_btns)

        blur_btn = FeatureButton(parent, Strings.BLUR_BTN.value, "images\ic_blur_btn.png")
        blur_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.BLUR_BTN.value, lambda button=blur_btn: self.update_image_into_selected_and_reset_button(button)))
        blur_btn.config(command = lambda button=blur_btn: self.on_click_blur__btn(button))

        self.sharpen_btn = FeatureButton(parent, Strings.SHARPEN_BTN.value, "images\ic_sharpen_btn.png")
        self.sharpen_btn.set_frame(
            FeatureScaleFrame(
                self.custom_container, 
                Strings.SHARPEN_BTN.value, 
                lambda button=self.sharpen_btn: self.update_image_into_selected_and_reset_button(button), 
                lambda event, arg1, arg2: self.sharpen_processing(),
                range = [0,50], 
                init_value = 0))
        self.sharpen_btn.config(command = lambda button=self.sharpen_btn: self.on_click_sharpen_btn(button))

        smoothing_btn = FeatureButton(parent, Strings.SMOOTHING_BTN.value, "images\ic_smoothing_btn.png")
        smoothing_btn.set_frame(FeatureScaleFrame(self.custom_container, Strings.SMOOTHING_BTN.value, lambda button=smoothing_btn: self.update_image_into_selected_and_reset_button(button)))
        smoothing_btn.config(command = lambda button=smoothing_btn: self.on_click_smoothing_btn(button))

        color_filter_btn = FeatureButton(parent, Strings.COLOR_FILTER_BTN.value, "images\ic_color_filter_btn.png")
        color_filter_multi_frame = MultilFeature(self.choice_frame)
        color_filter_btn.set_frame(color_filter_multi_frame)
        color_filter_btn.config(command = lambda button=color_filter_btn: self.on_click_color_filter_btn(button))

        color_filter_btns = []

        self.red_filter_btn = FeatureButton(color_filter_multi_frame, Strings.RED_FILTER_BTN.value, "images\ic_red_filter_btn.png")
        self.red_filter_btn.set_frame(
            FeatureScaleFrame(
                self.custom_container, 
                Strings.RED_FILTER_BTN.value, 
                lambda button=self.red_filter_btn: self.update_image_into_selected_and_reset_button(button),
                lambda event, arg1, arg2: self.red_filter_processing(),
                range = [0,15], 
                init_value = 0))
        self.red_filter_btn.config(command = lambda button=self.red_filter_btn: self.on_click_red_filter_btn(button))
        
        self.blue_filter_btn = FeatureButton(color_filter_multi_frame, Strings.BLUE_FILTER_BTN.value, "images\ic_blue_filter_btn.png")
        self.blue_filter_btn.set_frame(
            FeatureScaleFrame(
                self.custom_container, 
                Strings.BLUE_FILTER_BTN.value, 
                lambda button=self.blue_filter_btn: self.update_image_into_selected_and_reset_button(button),
                lambda event, arg1, arg2: self.blue_filter_processing(),
                range = [0,15], 
                init_value = 0))
        self.blue_filter_btn.config(command = lambda button=self.blue_filter_btn: self.on_click_blue_filter_btn(button))
        
        self.yellow_filter_btn = FeatureButton(color_filter_multi_frame, Strings.YELLOW_FILTER_BTN.value, "images\ic_yellow_filter_btn.png")
        self.yellow_filter_btn.set_frame(
            FeatureScaleFrame(
                self.custom_container, 
                Strings.YELLOW_FILTER_BTN.value, 
                lambda button=self.yellow_filter_btn: self.update_image_into_selected_and_reset_button(button),
                lambda event, arg1, arg2: self.yellow_filter_processing(),
                range = [0,15], 
                init_value = 0))
        self.yellow_filter_btn.config(command = lambda button=self.yellow_filter_btn: self.on_click_yellow_filter_btn(button))
        
        self.pink_filter_btn = FeatureButton(color_filter_multi_frame, Strings.PINK_FILTER_BTN.value, "images\ic_pink_filter_btn.png")
        self.pink_filter_btn.set_frame(
            FeatureScaleFrame(
                self.custom_container, 
                Strings.PINK_FILTER_BTN.value, 
                lambda button=self.pink_filter_btn: self.update_image_into_selected_and_reset_button(button),
                lambda event, arg1, arg2: self.pink_filter_processing(),
                range = [0,15], 
                init_value = 0))
        self.pink_filter_btn.config(command = lambda button=self.pink_filter_btn: self.on_click_pink_filter_btn(button))

        self.green_filter_btn = FeatureButton(color_filter_multi_frame, Strings.GREEN_FILTER_BTN.value, "images\ic_green_filter_btn.png")
        self.green_filter_btn.set_frame(
            FeatureScaleFrame(
                self.custom_container, 
                Strings.GREEN_FILTER_BTN.value, 
                lambda button=self.green_filter_btn: self.update_image_into_selected_and_reset_button(button),
                lambda event, arg1, arg2: self.green_filter_processing(),
                range = [0,15], 
                init_value = 0))
        self.green_filter_btn.config(command = lambda button=self.green_filter_btn: self.on_click_green_filter_btn(button))

        color_filter_btns.append(self.red_filter_btn)
        color_filter_btns.append(self.blue_filter_btn)
        color_filter_btns.append(self.yellow_filter_btn)
        color_filter_btns.append(self.pink_filter_btn)
        color_filter_btns.append(self.green_filter_btn)

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
        draw_btn_update.config(command = lambda: self.update_image_into_selected())

        draw_btns.append(pen_btn)
        draw_btns.append(text_btn)
        draw_btns.append(draw_btn_update)

        draw_btn.get_frame().set_btns(draw_btns)

        feature_btns = []
        feature_btns.append(format_btn)
        feature_btns.append(customize_btn)
        feature_btns.append(blur_btn)
        feature_btns.append(self.sharpen_btn)
        feature_btns.append(smoothing_btn)
        feature_btns.append(color_filter_btn)
        feature_btns.append(draw_btn)

        parent.set_btns(feature_btns)