from abc import ABC, abstractmethod

class Band:

    instance_of_a_class =[]

    def __init__ (self,name,members=None):
        self.name =name
        self.members = members
        Band.instance_of_a_class.append(self)

        #print ("sivatest", self.instance_of_a_class)
         
    def __str__(self):
        return f"The Band {self.name}"

    def __repr__(self):
        return f"Band Instance. Name ={self.name},members ={self.members}"

    @classmethod
    def to_list (cls):
        return cls.instance_of_a_class

    def play_solos(self):
        solos =[]
        for member in self.members:
            solos.append(member.play_solo()) 
        return solos
 
        #return [member.play_solo() for member in self.members]

class Musician(ABC):
    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass

class Guitarist(Musician):
    def __init__ (self, name):
        self.name =name

    def __str__(self):
        return f"I am Guitariest named {self.name}"
    
    def __repr__(self):
        return f"Guitariest instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "Face melting guitar solo"    
    
class Bassist(Musician):
    def __init__ (self, name):
        self.name =name

    def __str__(self):
        return f"I am Bassist named {self.name}"
    
    def __repr__(self):
        return f"Bassist instance. Name ={self.name}"

    def get_instrument(self):
        return "Bass"
    
    def play_solo(self):
        return "bom dhu  bom bom"    

class Drummer(Musician):
    def __init__ (self, name):
        self.name =name

    def __str__(self):
        return f"I am Drummer named {self.name}"
    
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "Drums"

    def play_solo(self):
        return "rattle boom crash"     
    

if __name__ == "__main__":
   band =Band("The Supremes")
   assert band.name =="The Supremes"
   assert band.members == None

   print (repr(band))
   assert len(Band.to_list()) == 1

   print ("-----------sucess---------")
