from datetime import date

month_to_number = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "mei": 5, "jun": 6,
                   "jul": 7, "aug": 8, "sep": 9, "okt": 10, "nov": 11, "dec": 12}

year = date.today().year

def convert_to_datetime(datetime):
    datetime = datetime.split()[1:]
    day = datetime[0]
    month = month_to_number[datetime[1]]
    hour = datetime[2].split("u")[0]
    minute = datetime[2].split("u")[1]
    formatted_date_time = f"{year}-{month}-{day} {hour}:{minute}"
    return formatted_date_time

