from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Next Week Monday', 'Next Week Monday'] 
    d = defaultdict(list)
    d = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Next Week Monday': []}

    today = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо до типу date*
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            next_year_bd = birthday_this_year.replace(year=today.year + 1)
        else:
            delta_days = (birthday_this_year - today).days
            if delta_days < 7:
                weekday = birthday_this_year.weekday()
            else:
                continue
        result = []
        d[days[weekday]].append(name)
        
        for key_day, value_name in d.items():
            if value_name:
                result.append(f'{key_day}: {', '.join(value_name)}')
                

    return print('\n'.join(result))    #список користувачів у кого дн на цьому тижні


a = [{"name": "Bill Gates", "birthday": datetime(1955, 2, 28)},{"name": "Papa Johnes", "birthday": datetime(1995, 2, 27)}, {"name": "Bereza Ivanivna", "birthday": datetime(1995, 3, 1)} ]  #список словників

#print(get_birthdays_per_week(a))
get_birthdays_per_week(a)