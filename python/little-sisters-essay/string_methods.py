"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    return str(title).title()
    

def check_sentence_ending(sentence):
    return str(sentence).endswith('.')


def clean_up_spacing(sentence):
    return str(sentence).strip()


def replace_word_choice(sentence, old_word, new_word):
    return str(sentence).replace(old_word, new_word)
