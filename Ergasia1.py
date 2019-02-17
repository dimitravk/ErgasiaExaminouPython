import re
x  = ""
x1 = []
s=0
a = 0
b = 0
def sumIntervals(x,x1,a,b,s):
    x = input("Διαστήματα:")
    x1 = re.split('\s|(?!\d)[,.](?<!\d)|(?!\d)[[](?<!\d)|(?!\d)[]](?<!\d)', x)
    for i in range(0, len(x1)//2):

        a= int(x1[2*i])
        b= int(x1[2*i+1])
        s = s+(b-a)
    return s   
print("Αθροισμα: ",sumIntervals(x,x1,a,b,s))
