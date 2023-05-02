brackets=input("Write brackets")
count=0
if brackets[0]==")" or brackets[-1]=="(":
    print("unbalanced")
    break
for i in brackets:
    if i=="(":
        count+=1
    elif i==")":
        count-=1
        if count<0:
            print (Unbalanced)
            break
if count==0:
    print ("balanced")