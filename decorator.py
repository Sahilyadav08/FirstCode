def level1(c):
    def inner():
        print("Hello")
        c()
        print("Yadav")
        
    return inner  

@level1
def level2(name):
        print("L") 

#insider = level1(level2("Sahil")) 

x=level2("sahil")
print(x)