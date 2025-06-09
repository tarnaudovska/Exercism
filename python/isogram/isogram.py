def is_isogram(string):
    string = string.lower()
    letters = [char for char in string if char.isalpha()]
    return len(letters) == len(set(letters))