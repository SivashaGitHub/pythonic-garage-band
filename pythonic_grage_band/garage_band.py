from abc import ABC, abstractmethod

class Musician(ABC):
    count = 0
    def __init__ (self,name="unknown",instrument="unknown"):
        self.name =name
        self.instrument = instrument 
        Musician.count += 1
        
    @abstractmethod
    def play_solo(self):
        pass

    def get_instrument(self):
        return instrument

    @classmethod
    def to_list (cls):
        return f"The number of band instance created is {cls.count}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance."

class Guitarist(Musician):
    def __init__ (self, name="unknown"):
        super().__init__(name,"Guitar")

    def play_solo(self):
        return "heart melting guitar wailing"

    def __str__(self):
        return f"I am Guitariest named {self.name}"

class Bassist(Musician):
    def __init__(self,name="unknown"):
        super().__init__(name,"Bass")

    def __str__(self):
        return f"I am Bassist named {self.name}"


    def play_solo(self):
        return "thum, thupy"

class Drummer(Musician):
    def __init__(self,name="unknown"):
        super().__init__(name,"Drumm")

    def __str__(self):
        return f"I am Drummer named {self.name}"

    def play_solo(self):
        return "crash boom"                

""" def some_band():
    nirvana = Band("Nirvana",[
        Guitarist ("Jimmy Page"),
        Bassist("Cliff Burton"),
        Drummer("John Bonhan")
         ])
    return nirvana """

if __name__ == "__main__":
   """  x= some_band()
    print (x) """