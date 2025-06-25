from calendar import month
from enum import Enum
from datetime import date, datetime

class MahaProfession(Enum):
    Elint = 0
    Commint = 1

def is_name_valid(full_name):
    name_l = full_name.split()
    flag = True
    if len(name_l) <= 1:
        flag = False
        print("Your input doesn't have a space. Make sure you type your full name")
    for e in name_l[1:-1]:
        if len(e) < 2:
            flag = False
            print("You cannot input a one digit name. Please type our full name")
        if not e.isalpha():
            flag = False
            print("Your need to enter a name with English letters and spaces only.")
    return flag

def is_id_valid(id):
    id_digits = list(map(int, str(id)))
    for i in range(9 - len(id_digits)):
        id_digits.insert(0, 0)
    sum_to_find_bikoret = 0
    for i, d in enumerate(id_digits):
        if i % 2 == 0 and i != 8:
            sum_to_find_bikoret += d
        else:
            weight = 2 * d
            if d > 4:
                sum_to_find_bikoret += (weight // 10) + (weight % 10)
            else:
                sum_to_find_bikoret += weight
    if id_digits[-1] == 10 - (sum_to_find_bikoret % 10):
        print("The ID you enter doesn't exist. Please pay attention to the Check digit")
        return False, None
    return True, int(''.join(map(str, id_digits)))

def is_mail_valid(mail):
    flag = True
    et_count = 0
    dot_count = 0
    for e in mail:
        if e == "@":
            et_count += 1
        elif e == ".":
            dot_count += 1
    if mail[0] == "@" or mail[0] == "." or ma2il[-1] == "@" or mail[-1] == ".":
        print("Your mail cannot have '.' or '@' in it's ends")
        flag = False
    if et_count != dot_count != 1:
        print("'.' and '@' may appear only once in your mail")
        flag = False
    return flag

def is_date_valid(recruit_date):
    flag = True
    today = datetime.now()
    slash_count = 0
    day = ""
    month = ""
    year = ""
    for char in recruit_date:
        if char != "/":
            if char not in "1234567890":
                print("You have not entered numbers and slashes only")
                return False, None
        if char == "/":
            slash_count += 1
        elif slash_count == 0:
            day += char
        elif slash_count == 1:
            month += char
        elif slash_count == 2:
            year += char
    if len(year) != 4:
        print("The year you have entered is not valid. Please enter in format 'dd/mm/yyyy'")
        flag = False
    if not 0 < int(month) <= 12:
        print("The month you have entered is not between 1 and 12. Please enter in format 'dd/mm/yyyy'")
        flag = False
    if flag:
        max_day = calendar.monthrange(int(year), int(month))[1]
        if not 0 < int(day) <= max_day:
            print(f"The day you have entered is not between 1 and maximum day of month({max_day}). Please enter in format 'dd/mm/yyyy'")
            flag = False
    if flag:
        recruit_date = datetime.strptime(recruit_date, "%d-%m-%Y")
        if today >= recruit_date:
            return True, recruit_date
    return False, None


class MahaStudent(object):
    def is_attribute_valid(self):
        # is name valid
        if self.

    def __init__(self, full_name: str, id: int, mail: str, recruit_date: str, profession: MahaProfession):
