from dateutil import parser
from datetime import datetime


time_strings = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
                19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
                50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
                90: 'ninety', 0: 'zero'}


def num_to_words(number):
    # convert number to word representation
    try:
        return time_strings[number]
    except KeyError:
        return f"{time_strings[number-number % 10]} {time_strings[number % 10].lower()}"


def military_time_conversion(time: str) -> str:
    time = time.replace(".", ":")

    # parse string
    try:
        parse_time = parser.parse(time)
    except parser._parser.ParserError.ParserError:
        print("Unknown time format")

    if ":" in time:
        if parse_time.minute == 0 and parse_time.second == 0:
            military_time = exact_hour(parse_time)
        else:
            military_time = not_exact_hour(parse_time)
    else:
        military_time = hour_represented_24_hour_clock(parse_time)

    return military_time


def hour_represented_24_hour_clock(parse_time):
    # The hour is represented using the 24 hour clock
    hour = parse_time.hour
    return num_to_words(hour)


def exact_hour(parse_time):
    # The hour is represented using the 24 hour clock
    hour = parse_time.hour
    return f"{num_to_words(hour)} hundred hours"


def not_exact_hour(parse_time):
    hour = parse_time.hour

    if hour < 10:
        military_time = f"zero {num_to_words(hour)}"
    else:
        military_time = f"{num_to_words(hour)}"

    minute = parse_time.minute

    if minute < 10:
        military_time = f"{military_time} zero {num_to_words(minute)}"
    else:
        military_time = f"{military_time} {num_to_words(minute)}"

    return military_time
