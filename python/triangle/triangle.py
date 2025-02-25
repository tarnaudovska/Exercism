def equilateral(sides):
    a, b, c = sorted(sides)
    return a == b == c > 0
    

def isosceles(sides):
    a, b, c = sorted(sides)
    if a + b < c or a + c < b or b + c < a:
        return False
    return a == b or b == c or a == c


def scalene(sides):
    a, b, c = sorted(sides)
    if a + b < c or a + c < b or b + c < a:
        return False
    return not equilateral(sides) and not isosceles(sides)