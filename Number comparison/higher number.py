numbers=[]
try:
    for i in range (2):
        numbers+=[int (input ("Enter number "))]

except ValueError:
    print ("This is not a number with base 10")
    numbers+=[int (input ("Enter number "))]

if numbers [0]!=numbers[1]:
    print(max(numbers))
else :
    print("Numers are equal there is no higher number")