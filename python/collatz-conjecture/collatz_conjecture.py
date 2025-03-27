def steps(number):
    iterat = 0
    if number<1:
        raise ValueError("Only positive integers are allowed")
    while number!=1 and number>0:
        if number%2==0:
            number/=2
        elif number%2!=0:
            number=(number*3)+1
        iterat+=1
    return iterat
