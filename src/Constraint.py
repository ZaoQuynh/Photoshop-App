from enum import Enum

class Sizes(Enum):
    WIDTH = 1100
    HEIGHT = 730
    WIDTH_LEFT = 150
    HEIGHT_LEFT = 730
    WIDTH_RIGHT = 950
    HEIGHT_RIGHT = 730
    WIDTH_TOP = 950
    HEIGHT_TOP = 610
    WIDTH_BOTTOM = 950
    HEIGHT_BOTTOM = 120
    WIDTH_BTN = 130
    HEIGHT_BTN = 2
    WIDTH_FEATURE_BUTTON = 60
    ICON_BUTTON = 35
    ORIGINAL_FRAME = 300
    EDIT_FRAME = 480
    FEATURE_FRAME_WIDTH = 300
    FEATURE_FRAME_HEIGHT = 100

class Strings(Enum):
    APP_TITLE = "Photoshop App"
    LOAD_BTN = "Tải ảnh"
    EXPORT_BTN = "Xuất ảnh"
    UNDO_BTN = "Hoàn tác"
    RESTART_BTN = "Trở lại"
    CUT_BTN = "Cắt ảnh"
    ROTATION_BTN = "Xoay ảnh"
    SCALING_BTN = "Kích thước"
    BRIGHTNESS_BTN = "Sáng"
    CONTRAST_BTN = "Tương phản"
    SATURATION_BTN = "Bão hòa"
    BLUR_BTN = "Làm mờ"
    SHARPEN_BTN = "Làm rõ"
    COLOR_FILTER_BTN = "Lọc màu"
    DRAW_BTN = "Vẽ"
    SMOOTHING_BTN = "Làm mịn"
    RED_EYE_BTN = "Mắt đỏ"
    UPDATE_BTN = "Cập nhật"
    FORMAT_BTN = "Định dạng"
    CUSTOMIZE_BTN = "Điều chỉnh"
    TEXT_BTN = "Chữ"
    PEN_BTN = "Vẽ"
    RED_BTN = "Đỏ"
    BLUE_BTN = "Xanh dương"
    YELLOW_BTN = "Vàng"
    RED_FILTER_BTN = "Đỏ"
    BLUE_FILTER_BTN = "Xanh dương"
    YELLOW_FILTER_BTN = "Vàng"
    PINK_FILTER_BTN = "Hồng"
    GREEN_FILTER_BTN = "Xanh lá"

class Colors(Enum):
    INIT_COLOR = "#000000"
    BACKGROUND = "#2C3639"
    BACKGROUND_V2 = "#525455"
    BACKGROUND_V3 = "#A27B5C"
    TEXT_COLOR = "#000000"
    TEXT_HIGHTLIGHT_COLOR = "#DCD7C9"
    BTN_COLOR = "#525455"
    BTN_HIGHTLIGHT_COLOR = "#A27B5C"
    BTN_BORDER_COLOR = "#3F4E4F"
    BORDER_COLOR = "#00224D"