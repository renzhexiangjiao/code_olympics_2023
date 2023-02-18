from military_time_conversion_code import military_time_conversion


def test_hour_represented_24_hour_clock():
    assert military_time_conversion("12AM") == "zero"
    assert military_time_conversion("7AM") == "seven"
    assert military_time_conversion("1PM") == "thirteen"
    assert military_time_conversion("11PM") == "twenty-three"


def test_exact_hour():
    assert military_time_conversion("4:00PM") == "sixteen hundred hours"
    assert military_time_conversion("11:00AM") == "eleven hundred hours"


def test_not_exact_hour():
    assert military_time_conversion("11:23AM") == "eleven twenty three"
    assert military_time_conversion("6:45PM") == "eighteen forty five"


def test_hour_min_single_digit():
    assert military_time_conversion("7:45AM") == "zero seven forty five"
    assert military_time_conversion("5.05PM") == "seventeen zero five"
    assert military_time_conversion("4.09AM") == "zero four zero nine"
