class Carparts:
    
    def __init__(self,EngineCC,gear,clutch):
       
       self.EngineCC=EngineCC
       self.gear=gear
       self.clutch=clutch
       print(clutch)

    def window(self): 
        print("window is fine")

    def viper(self): 
        print("Viper is also fine")

class Ford(Carparts) :
    #def suzuki(self):
        #print(f"My car Engine{self.EngineCC} and i have {self.gear} gear")

    def tire(self):
        print("I have stylish tire")


details=Ford(2000,4,'ok')

print(details.tire())




