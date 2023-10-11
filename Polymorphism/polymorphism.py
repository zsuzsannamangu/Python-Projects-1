
#parent class
class Car:
    make = "unknown"
    model = "unknown"
    id_number = ""
    powertype = ""

    #we give two methods to the Car class:
    def information(self):
        msg = "\nmake: {}\nmodel: {}\nid_number: {}\npowertype:".format(self.make,self.model,self.id_number,self.powertype)
        return msg

    def owner(self):
        owner_name = input("Enter your name: ")
        print("Hello {}, your {} {} car is cool.".format(owner_name,self.make,self.model))
        

#child class instance #1
class Full_hybrid(Car):
    make = "Toyota"
    model = "Prius"
    id_number = "1234KF"
    powertype = "hybrid"

    def source(self):
        msg = "\nFull hybrid vehicles can run on the internal combustion engine alone, the electric motors alone, or a combination of both."
        return msg

#child class instance #2
class Mild_hybrid(Car):
    make = "Dodge"
    model = "Ram"
    id_number = "2829KB"
    powertype = "hybrid"

    def source(self):
        msg = "\nMild hybrid vehicles cannot run solely on either its internal combustion engine or its electric motors. "
        return msg

    #we give this child class the owner function but modified
    def owner(self):
        owner_name = input("Enter your name: ")
        owner_phone = input("Enter your number: ")
        print("Hello {}, your {} {} car is cool.".format(owner_name,self.make,self.model))

#child class instance #3
class Plugin_hybrid(Car):
    make = "BMW"
    model = "X5"
    id_number = "2191KB"
    powertype = "hybrid"

    def source(self):
        msg = "\nThey offer the possibility of driving on full-electric power without the worry of finding a charging station as it still has an internal combustion engine as a backup."
        return msg

    #we give this child class the owner function but modified again
    def owner(self):
        owner_question = input("Do you like this car? ")
        if (owner_question == "yes"):
            print ("Great.")
        else:
            print("Sorry to hear that.")

#instantiate all the above class objects:
    
if __name__ == "__main__":
    fullhybrid = Full_hybrid()
    print(fullhybrid.owner())
    print(fullhybrid.information())
    print(fullhybrid.source())

    mildhybrid = Mild_hybrid()
    print(mildhybrid.owner())
    print(mildhybrid.information())
    print(mildhybrid.source())

    pluginhybrid = Plugin_hybrid()
    print(pluginhybrid.owner())
    print(pluginhybrid.information())
    print(pluginhybrid.source())
    
    
    

    
