def checkPrwtos(num):
    prwtos = True 
    for i in range(2, num):
            while prwtos:
               if (num % i) == 0:
                   prwtos = False
                   break
               else:
                   prwtos = True
                   break;
    return prwtos  


a, b = map(int, input("Τα a,b για το διάστημα [a,b] είναι= ").split())
d = int(input("Η διαφορά μεταξύ των δύο πρώτvν είναι= "))

x = False;
for num in range(a,b-d+1):
    if (x):
        break
    for i in range(2,num):
        if (checkPrwtos(num)):
            p = num
            q = p + d
            if (checkPrwtos(q)):
                print("To πρώτο ζεύγος πρώτων αριθμών στο δίαστημα [",a, ",", b,"] με μεταξύ τους διαφορά",d,"έιναι το (",p,",",q,")")
                x = True;
                break

           