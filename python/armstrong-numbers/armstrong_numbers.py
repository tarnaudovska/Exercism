def is_armstrong_number(number):
    number_list = [int(i) for i in str(number)]
    lenght = len(number_list)
    total = 0

    for i in number_list:
        total += i**lenght

    return True if total == number else False