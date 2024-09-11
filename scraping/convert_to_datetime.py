from datetime import date

month_to_number = {"jan": 1, "feb": 2, "mar": 3, "mrt": 3, "apr": 4, "mei": 5, "jun": 6,
                   "jul": 7, "aug": 8, "sep": 9, "okt": 10, "nov": 11, "dec": 12}

year = date.today().year


def convert_to_datetime(day: str, month: str, hour: str, minute: str):
    month = month.strip()[:3].lower()
    month = month_to_number[month]
    formatted_date_time = f"{year}-{month}-{day.strip()} {hour.strip()}:{minute.strip()}"
    return formatted_date_time
