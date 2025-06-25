from enum import Enum
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



class MahaStudent(object):
    def is_attribute_valid(self):
        # is name valid
        if self.

    def __init__(self, full_name: str, id: int, mail: str, recruit_date, profession: MahaProfession):
