def is_isogram(string):
    string = string.lower()
    letters = []
    for char in string:
        if char.isalpha():
            letters.append(char)
    unique_letters = set(letters)

    if len(letters) == len(unique_letters):
        return True
    else:
        return False