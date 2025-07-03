def get_rounds(number):
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    return number in rounds


def card_average(hand):
    return float(sum(hand) / len(hand))


def approx_average_is_average(hand):
    average_ends = (hand[0]+hand[-1])/2
    middle_card = hand[int((len(hand)-1)/2)]
    return average_ends == card_average(hand) or middle_card == card_average(hand)


def average_even_is_average_odd(hand):
    even_num = sum(hand[0::2]) / len(hand[0::2])
    odd_num = sum(hand[1::2]) / len(hand[1::2])
    return odd_num == even_num


def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand