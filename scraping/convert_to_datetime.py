from datetime import timedelta, datetime

month_to_number = {"jan": 1, "feb": 2, "mar": 3, "mrt": 3, "apr": 4, "mei": 5, "jun": 6,
                   "jul": 7, "aug": 8, "sep": 9, "okt": 10, "nov": 11, "dec": 12}

year = datetime.today().year


def convert_to_datetime(day: str, month: str, hour: str, minute: str):
    month = month.strip()[:3].lower()
    month = month_to_number[month]

    date_time = datetime(year, month, int(day.strip()), int(hour.strip()), int(minute.strip()), 0)

    if date_time < datetime.now():
        date_time = date_time.replace(year=date_time.year + 1)

    formatted_date_time = f"{date_time.year}-{date_time.month}-{date_time.day} {date_time.hour}:{date_time.minute}"

    return formatted_date_time
