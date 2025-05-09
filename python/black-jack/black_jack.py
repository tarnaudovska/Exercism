def value_of_card(card):
    if card in ['J', 'Q', 'K']:
        return 10
    if card == 'A':
        return 1
    return int(card)


def higher_card(card_one, card_two):
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    if card_one_value > card_two_value:
        return card_one
    if card_two_value > card_one_value: 
        return card_two
    return (card_one, card_two)
    

def value_of_ace(card_one, card_two):
    if card_one == 'A' or card_two == 'A':
        return 1
    
    return 11 if value_of_card(card_one) + value_of_card(card_two) < 11 else 1
    


def is_blackjack(card_one, card_two):
    if value_of_card(card_one)==1 and value_of_card(card_two) == 10:
        return True
    if value_of_card(card_one)==10 and value_of_card(card_two) == 1:
        return True
    return False


def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    return False


def can_double_down(card_one, card_two):
    if value_of_card(card_one) + value_of_card(card_two) in [9,10,11]:
        return True
    return False