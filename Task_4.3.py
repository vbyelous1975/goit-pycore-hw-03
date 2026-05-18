import re


def normalize_phone(phone_number):
    

    clean_number = re.sub(r"\D", "", phone_number)
    if len(clean_number) == 10:
        clean_number = "+38" + clean_number
    elif len(clean_number) == 12:
         clean_number = "+" + clean_number
    else:
        clean_number = None

    return clean_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     050345123",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = []
for num in raw_numbers:
    result=normalize_phone(num)
    print(result)
    if result:
        sanitized_numbers.append(result)
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
