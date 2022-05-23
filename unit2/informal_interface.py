class Fruits:
    def __init__( self, element) :
        self.__element = element
        
    def __contains__( self, element) :
        return element in self.__element
    
    def __len__( self ):
        return len( self.__element)
    
    
Fruits_list = Fruits([ "Apple", "Banana", "Orange" ])
print(len(Fruits_list))
print("Apple" in Fruits_list)
print("Mango" in Fruits_list)
print("Orange" not in Fruits_list)


# import abc
# class FourWheelVehicle (abc.ABC):
#     @abc.abstractmethod
#     def SpeedUp( self ):
#         pass
# class Car(FourWheelVehicle) :
#     def SpeedUp(self):
#         print(" Running! ")
# class TwoWheelVehicle (abc.ABC) :
#     @abc.abstractmethod
#     def SpeedUp(self):
#         pass
# class Bike(TwoWheelVehicle) :
#     def SpeedUp(self) :
#         print(" Running!.. ")
# a = Bike ()
# s = Car()
# print( isinstance(s, FourWheelVehicle))
# print( isinstance(s, TwoWheelVehicle))
# print( isinstance(a, FourWheelVehicle))
# print( isinstance(a, TwoWheelVehicle))