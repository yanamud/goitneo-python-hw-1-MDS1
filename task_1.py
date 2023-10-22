import datetime
from datetime import datetime
from collections import defaultdict
import calendar

users = [{"name": "Bill Gates", "birthday": datetime(1955, 3, 30)},
         {"name": "Simon Gat", "birthday": datetime(1964, 10, 25)},
         {"name": "Alen Tes", "birthday": datetime(1982, 10, 22)},
         {"name": "Rick Gots", "birthday": datetime(1990, 10, 21)},
         {"name": "Sick Petes", "birthday": datetime(1980, 10, 23)},
         {"name": "Dick Petes", "birthday": datetime(1980, 10, 24)},
         {"name": "Lick Petes", "birthday": datetime(1980, 10, 25)},
         {"name": "Nick Petes", "birthday": datetime(1980, 10, 26)},
         {"name": "Pick Petes", "birthday": datetime(1980, 10, 27)}]

# display a list of colleagues who need to be congratulated on their birthdays during the week.
# display template:
#   Monday: Bill Gates, Jill Valentine
#   Friday: Kim Kardashian, Jan Koum

def get_birthdays_per_week(users):
    dic = defaultdict(list)

    today = datetime.today().date()
    for user in users:
        # analysis of birth date
        name = user["name"]
        birthday = user["birthday"].date()

        # check if the birthday has passed
        birthday_this_year = birthday.replace(
            year = today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(
                year=today.year+1)

        # Determine the difference between the birthday and the current day
        delta_days = (birthday_this_year - today).days

        # Day of the Week definition
        if delta_days < 7:
            if birthday_this_year.weekday() in (5,6):
                day =  "0" + "_" + calendar.day_name[0]
            else:
                day = str(birthday_this_year.weekday()) + "_" + calendar.day_name[birthday_this_year.weekday()]
            dic[day].append(name)

    # the week begins on Monday
    for key, value in sorted(dic.items()):
        new_key = key[2:]
        new_value = ", ".join(value)
        print(f"{new_key}: {new_value}")

get_birthdays_per_week(users)

