def is_pangram(sentence):
    sentence = str(sentence).lower().replace(" ", "")
    alphabet = list(map(chr, range(ord('a'), ord('z')+1)))

    for i in sentence:
        if i in alphabet:
            alphabet.remove(i)

    return len(alphabet) == 0