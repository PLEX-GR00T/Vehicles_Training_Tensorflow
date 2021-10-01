"""
Name : Priyank Thakkar
Date : 30th September 2021
About code : This code takes input folder with different images and put it into output folders with resizing it. 
            Just change the "pathlib.path()" accordingly.  
"""
# Use this block of code for HeavyVehicles
from PIL import Image
import pathlib
for input_img_path in pathlib.Path("D:\SJSU_HW\GitHubSJSU\Vehicles_Training_Tensorflow\Datasets\heavyvehicle_input").iterdir():
    output_img_path = str(input_img_path).replace("D:\SJSU_HW\GitHubSJSU\Vehicles_Training_Tensorflow\Datasets\heavyvehicle_input","D:\SJSU_HW\GitHubSJSU\Vehicles_Training_Tensorflow\Datasets\heavyvehicle")
    with Image.open(input_img_path) as im:
        if im.mode != 'RGB':
            im = im.convert('RGB')
        ri = im.resize((416, 416))
        ri.save(output_img_path, "JPEG", dpi=(96,96))
        print(f"{input_img_path} resized...")

# Use this block of code for CARS
"""
from PIL import Image
import pathlib
for input_img_path in pathlib.Path("D:\SJSU_HW\GitHubSJSU\Vehicles_Training_Tensorflow\Datasets\car_input").iterdir():
    output_img_path = str(input_img_path).replace("D:\SJSU_HW\GitHubSJSU\Vehicles_Training_Tensorflow\Datasets\car","D:\SJSU_HW\GitHubSJSU\Vehicles_Training_Tensorflow\Datasets\car")
    with Image.open(input_img_path) as im:
        if im.mode != 'RGB':
            im = im.convert('RGB')
        ri = im.resize((416, 416))
        ri.save(output_img_path, "JPEG", dpi=(96,96))
        print(f"{input_img_path} resized...")
"""

# Use this block of code for BIKE
"""
from PIL import Image
import pathlib
for input_img_path in pathlib.Path("D:\SJSU_HW\GitHubSJSU\Vehicles_Training_Tensorflow\Datasets\car_input").iterdir():
    output_img_path = str(input_img_path).replace("D:\SJSU_HW\GitHubSJSU\Vehicles_Training_Tensorflow\Datasets\car","D:\SJSU_HW\GitHubSJSU\Vehicles_Training_Tensorflow\Datasets\car")
    with Image.open(input_img_path) as im:
        if im.mode != 'RGB':
            im = im.convert('RGB')
        ri = im.resize((416, 416))
        ri.save(output_img_path, "JPEG", dpi=(96,96))
        print(f"{input_img_path} resized...")
"""