"""Functions for creating, transforming, and adding prefixes to strings."""

def add_prefix_un(word):
    return 'un' + word


def make_word_groups(vocab_words):
    
    new_vocab_words = [vocab_words[0] + word for word in vocab_words[1:]]
    prefixed_vocab_words = [vocab_words[0]]
    prefixed_vocab_words.extend(new_vocab_words)

    return ' :: '.join(prefixed_vocab_words)
   

def remove_suffix_ness(word):
    word = str(word[:-4])
    return word[:-1] + 'y' if word.endswith('i') else word
    

def adjective_to_verb(sentence, index):
    word = sentence.split()
    return word[index].strip('.') + 'en'
