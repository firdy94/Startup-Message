import art
import datetime
import time

from func_resources import quote_generator as quot
from func_resources import adjective_generator as adject
from func_resources import line_printer as lp
from func_resources import weather
from func_resources import image_ascii


def get_quotes():
    real_quote = quot('resources/quotes.txt').strip().split(sep='-')
    filler = "On a totally unrelated note, "
    movie_quote = quot(
        'resources/movie_quotes_cleaned.txt').strip().split(sep='-')
    quote_1 = f"{real_quote[1]} famously once said:\n\n{real_quote[0]}"
    if "," in movie_quote[1]:
        character, film = (movie_quote[1].split(','))
        quote_2 = f"Here's a quote by{character} from the film,{film}:\n\n{movie_quote[0]}\n\n"
    else:
        quote_2 = f"Here's a quote from the film, {movie_quote[1]}:\n\n{movie_quote[0]}\n\n"
    return "\n\n".join([quote_1, filler, quote_2])


def get_message():
    positive_adject = adject('resources/positive_adjectives_cleaned.txt')
    positive_msg = f"Remember you are a {positive_adject[0]}, {positive_adject[1]} and {positive_adject[2]} human being!\n\n"
    return positive_msg


def get_weather(location, api_key):
    temps, times, weather_info = weather(location, api_key)
    weather_identifier = weather_info[2]
    weather_line_1 = f"On this fine day in beautiful {location.title()}, this is what the weather looks like now: \n"
    weather_line_2 = image_ascii(weather_identifier)
    if weather_info[0] == 'Clear':
        weather_line_3 = f"There is a {weather_info[3]}% chance of a {weather_info[1]}.\n"
    else:
        weather_line_3 = f"There is a {weather_info[3]}% chance of some {weather_info[1]}.\n"
    weather_line_4 = f"The sun rose today at {datetime.datetime.fromtimestamp(times[0]).strftime('%X')} and will set at {datetime.datetime.fromtimestamp(times[1]).strftime('%X')} later in the evening. "
    weather_line_5 = f"The current temperatue is {temps[0]} degrees Celcius but it\
        feels more like{temps[0]} degrees Celcius \n\and throughout the day, it could \
            be anywhere from {temps[2]} degrees Celcius to {temps[3]} degrees Celcius "
    filler = "Now for your quote of the day: \n\n"
    return "\n\n".join([weather_line_1, weather_line_2, weather_line_3, weather_line_4, filler])


location = 'your location'
api_key = 'API key from openweather'
welcome_msg = 'WELCOME FIRDAUS!'
end_msg = "Now go and make (or break) something today!\n\n"

all_quotes = get_quotes()
p_msg = get_message()
weather_msg = get_weather(location, api_key)
list_of_lines = [weather_msg, all_quotes, p_msg]

art.tprint(welcome_msg, font="big")
time.sleep(1.0)
for line in list_of_lines:
    lp(line)
    time.sleep(1.0)
time.sleep(1.0)
print(end_msg)
