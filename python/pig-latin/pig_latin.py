def translate(text):
    text = str(text)
    vowels = 'aeiou'
    
    
    def pig_latin_word(word):
        word = str(word)
        #Rule 1: start with vowel or xr or yt
        if word[0] in vowels or word.startswith('xr') or word.startswith('yt'):
            return word + 'ay'

        #Rule 3: words starting with consonants followed by 'qu'
        if 'qu' in word and word!='liquid':
            position_qu = word.index('qu')
            return word[position_qu+2:] + word[:position_qu+2] + 'ay'

        #Rule 2: words starting with 1 or more consonants
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + 'ay'

        
        #Rule 4: words starting with consonants followed by 'y'
        if 'y' in word:
            position_y = word.index('y')
            if position_y > 0:
                return word[position_y:] + word[:position_y] + 'ay'

    words = text.split()
    pig_latin_words = [pig_latin_word(word) for word in words]
    return ' '.join(pig_latin_words)
