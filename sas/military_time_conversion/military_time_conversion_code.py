from dateutil import parser
from datetime import datetime


time_string = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
               14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 21: "twenty-one", 22: "twenty-two", 23: "twenty-three", 24: "twenty-four"}


def military_time_conversion(time: str) -> str:
    time = time.replace(".", ":")

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
    return time_string[hour]


def exact_hour(parse_time):
    # The hour is represented using the 24 hour clock
    hour = parse_time.hour
    return f"{time_string[hour]} hundred hours"


def not_exact_hour(parse_time)


print(military_time_conversion("12AM"))
