def classify(number):
    if number<=0:
        raise ValueError("Classification is only possible for positive integers.")
    num_sum = 0
    for n in range(1,number):
        if number%n==0:
            num_sum+=n
    if number==num_sum:  
        return "perfect" 
    elif number<num_sum:
        return "abundant"
    else:
        return "deficient"