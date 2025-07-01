def is_valid(isbn):
    clean_num = []
    for char in isbn:
        if char != "-":
            clean_num.append(char)

    if len(clean_num) != 10:
        return False

    isbn_sum = 0
    for i in range(10):
        char = clean_num[i]
        if i == 9 and char.upper() == "X":
            digit = 10
        elif char.isdigit():
            digit = int(char)
        else:
            return False  # Invalid character

        isbn_sum += digit * (10 - i)

    return isbn_sum % 11 == 0
