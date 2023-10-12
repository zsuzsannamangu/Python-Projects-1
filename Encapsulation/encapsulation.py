#Here I create a class that uses encapsulation
#This class makes use of a private attribute and a protected attribute

#Creating a class
class Car:
    #Creating two protected attributes of the class:
    _make = "Honda"
    _model = "Civic"
    __id= "2334kdkd"

    #creating a function
    def _MakeAndModel(self):
        #this function is using the protected attributes of the Car class
        print("Make: ", self._make)
        print("Model: ", self._model)
        print("ID: ",self.__id)

#creating objects of the class
obj = Car()
obj._MakeAndModel()
