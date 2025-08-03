import numpy as np
from prettytable import PrettyTable

def scale_RGB(RGB, scale_factor=2.2):
    scaled_RGB = RGB ** scale_factor
    scaled_RGB = np.round(scaled_RGB, 4)
    return scaled_RGB

def RGB_dec_to_int(RGB_dec):
    return np.round(RGB_dec * 255, 4)

def RGB_int_to_dec(RGB_int):
    return np.round(RGB_int / 255, 4)

#color determined from the Colour python package
wKNb_colour_int = np.array([233, 233, 226])  # white sample
wRbNb_colour_int = np.array([194, 160, 119]) # white sample
wCsNb_colour_int = np.array([194, 160, 119]) # white sample

wKNb_colour_dec = RGB_int_to_dec(wKNb_colour_int)
wRbNb_colour_dec = RGB_int_to_dec(wRbNb_colour_int)
wCsNb_colour_dec = RGB_int_to_dec(wCsNb_colour_int)

wKNb_scale_dec = scale_RGB(wKNb_colour_dec)
wRbNb_scale_dec = scale_RGB(wRbNb_colour_dec)
wCsNb_scale_dec = scale_RGB(wCsNb_colour_dec)

wKNb_scale_int = RGB_dec_to_int(wKNb_scale_dec)
wRbNb_scale_int = RGB_dec_to_int(wRbNb_scale_dec)
wCsNb_scale_int = RGB_dec_to_int(wCsNb_scale_dec)

table = PrettyTable()

table.title = "RGB Color Codes"
table.field_names = ["Complex", "Colour Pack. RGB", "RGB (0-1)", "Scaled RGB", "Scaled RGB (0-1)", "Notes"]

# Add rows
table.add_row(["K3NbO8", f"{wKNb_colour_int[0]}", f"{wKNb_colour_dec[0]}", f"{wKNb_scale_int[0]}", f"{wKNb_scale_dec[0]}", ""])
table.add_row(["",      f"{wKNb_colour_int[1]}", f"{wKNb_colour_dec[1]}",  f"{wKNb_scale_int[1]}", f"{wKNb_scale_dec[1]}", ""])
table.add_row(["",      f"{wKNb_colour_int[2]}", f"{wKNb_colour_dec[2]}",  f"{wKNb_scale_int[2]}", f"{wKNb_scale_dec[2]}", ""])

print(table)
