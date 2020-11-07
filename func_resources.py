import random
import json
import time
import sys

import requests
from PIL import Image


def line_printer(line):
    for char in line:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.02)


def quote_generator(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        chosen_line = random.choice(lines)
        return chosen_line


def adjective_generator(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        chosen_adjec = []
        for i in range(0, 3):
            chosen_adjec.append(random.choice(lines).strip().lower())
        return chosen_adjec


def weather(location, api_key):
    weather_info_request = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={location.lower()}&appid={api_key}&units=metric")
    weather_info_dict = weather_info_request.json()
    temps = weather_info_dict['main']
    temp_list = [temps['temp'], temps['feels_like'],
                 temps['temp_min'], temps['temp_max']]
    day_night = weather_info_dict['sys']
    time_list = [day_night['sunrise'], day_night['sunset']]
    weather_desc = weather_info_dict['weather'][0]
    weather_type_list = [weather_desc['main'],
                         weather_desc['description'], weather_desc['icon'], weather_info_dict['clouds']['all']]

    return temp_list, time_list, weather_type_list


def image_ascii(identifier):
    image_path = f"resources/weather_pics/{identifier}@2x.png"
    img = Image.open(image_path)
    width, height = img.size
    aspect_ratio = height/width
    new_width = 50
    new_height = aspect_ratio * new_width*0.6
    img = img.resize((new_width, int(new_height)))
    # convert image to greyscale format
    img = img.convert('L')
    pixels = img.getdata()
    chars = [ch for ch in " .:-=+*#%@"]
    print(len(chars))
    new_pixels = [chars[pixel//26] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width]
                   for index in range(0, new_pixels_count, new_width) if new_pixels[index:index + new_width].count(' ') != new_width]
    ascii_image = "\n".join(ascii_image)
    return(ascii_image)
