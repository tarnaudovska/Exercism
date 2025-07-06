import string 

def rotate(text, key):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    cipher = ""
    for letter in text:
        if letter in lowercase:
            letter_index = lowercase.index(letter)
            shifted_index = (letter_index + key) % 26
            cipher += lowercase[shifted_index]
        elif letter in uppercase:
            letter_index = uppercase.index(letter)
            shifted_index = (letter_index + key) % 26
            cipher += uppercase[shifted_index]
        else:
            cipher += letter
    return cipher