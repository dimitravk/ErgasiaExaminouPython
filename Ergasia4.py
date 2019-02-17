myls= []
def plus(x): 
    myls = ['+',x]
    return myls

def minus(x):
    myls = ['-',x]
    return myls

def times(x):
    myls = ['*',x]
    return myls

def div(x):
    myls = ['/',x]
    if x==0:
        raise ValueError('Διαίρεση με το 0!')
    return myls

def zero(myls = None):
    num1=0
    if myls: 
        praksi = myls[0]
        num2 = myls[1]
        if praksi=='+':
            return num1 + num2
        elif praksi=='-':
            return num1 - num2
        elif praksi=='*':
            return num1 * num2
        elif praksi=='/':
            return num1 / num2
    else: 
        return num1


def one(my = None):
     num1=1
     if myls: 
        praksi = myls[0]
        num2 = myls[1]
        if praksi=='+':
            return num1 + num2
        elif praksi=='-':
            return num1 - num2
        elif praksi=='*':
            return num1 * num2
        elif praksi=='/':
            return num1 / num2
     else: 
        return num1

def two(myls = None):
    num1=2
    if myls:
        praksi = myls [0]
        num2 = myls[1]
        if praksi=='+':
            return num1 + num2
        elif praksi=='-':
            return num1 - num2
        elif praksi=='*':
            return num1 * num2
        elif praksi=='/':
            return num1 / num2
    else:
        return num1

def three(myls = None):
    num1=3
    if myls:
        praksi = myls [0]
        num2 = myls[1]
        if praksi=='+':
            return num1 + num2
        elif praksi=='-':
            return num1 - num2
        elif praksi=='*':
            return num1 * num2
        elif praksi=='/':
            return num1 / num2
    else:
        return num1


def four(myls = None):
    num1=4
    if myls:
        praksi = myls [0]
        num2 = myls[1]
        if praksi=='+':
            return num1 + num2
        elif praksi=='-':
            return num1 - num2
        elif praksi=='*':
            return num1 * num2
        elif praksi=='/':
            return num1 / num2
    else:
        return num1


def five(myls = None):
    num1=5
    if myls:
        praksi = myls [0]
        num2 = myls[1]
        if praksi=='+':
            return num1 + num2
        elif praksi=='-':
            return num1 - num2
        elif praksi=='*':
            return num1 * num2
        elif praksi=='/':
            return num1 / num2
    else:
        return num1

def six(myls = None):
    num1=6
    if myls:
        praksi = myls [0]
        num2 = myls[1]
        if praksi=='+':
            return num1 + num2
        elif praksi=='-':
            return num1 - num2
        elif praksi=='*':
            return num1 * num2
        elif praksi=='/':
            return num1 / num2
    else:
        return num1


def seven(myls = None):
    num1=7
    if myls:
        praksi = myls [0]
        num2 = myls[1]
        if praksi=='+':
            return num1 + num2
        elif praksi=='-':
            return num1 - num2
        elif praksi=='*':
            return num1 * num2
        elif praksi=='/':
            return num1 / num2
    else:
        return num1


def eight(myls = None):
    num1=8
    if myls:
        praksi = myls [0]
        num2 = myls[1]
        if praksi=='+':
            return num1 + num2
        elif praksi=='-':
            return num1 - num2
        elif praksi=='*':
            return num1 * num2
        elif praksi=='/':
            return num1 / num2
    else:
        return num1


def nine(myls = None):
    num1=9
    if myls:
        praksi = myls [0]
        num2 = myls[1]
        if praksi=='+':
            return num1 + num2
        elif praksi=='-':
            return num1 - num2
        elif praksi=='*':
            return num1 * num2
        elif praksi=='/':
            return num1 / num2
    else:
        return num1


print("six(plus(four())) =", six(plus(four())))
print("two(minus(one())) =", two(minus(one())))
print("five(times(four())) =",five(times(four())))
print("nine(div(three())) =", nine(div(three())))
#print("seven(div(zero())) =", seven(div(zero())))
