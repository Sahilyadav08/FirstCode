 
def func(x):
    y=""
    for i in range(0,len(x)):
        print(i)
        if i%2 == 0:

            y=y+x[i].upper()
        else:
            y=y+x[i].lower()
    return y            

print(func("Anthropomorphism"))



print(range(25))