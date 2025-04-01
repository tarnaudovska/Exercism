def response(hey_bob):
    hey_bob = str(hey_bob).strip()

    if not hey_bob:
        return "Fine. Be that way!"
    
    is_question = hey_bob.endswith('?') #boolean

    if is_question and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."
