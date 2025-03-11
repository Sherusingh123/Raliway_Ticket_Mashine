class Sation:
    """model the each sation"""
    def __init__(self,name,distance,cost):
     self.name=name
     self.distance=distance
     self.cost=cost
     
     
     
class Sations:
    """model all the sations"""
    def __init__(self):
        self.Sations=[
            Sation(name="Pratap Nager", distance=2,cost=10,),
            Sation(name="GopalPua", distance=5,cost=50,),
            Sation(name="200fit", distance=4,cost=20,),
            Sation(name="Meera marg", distance=8,cost=30,),
            Sation(name="Sanganer", distance=3,cost=10,)
        ]    
        
        
       
            
            
    def get_Sation(self): 
        """Returns all the satrions"""
        Options="" 
        for sation in self.Sations:
            Options += f"Sation_Name:{sation.name} , Cost:{sation.cost}\n"
        return Options
    
    def find_Sation(self,sation_name):
        """Seach the sation it return the sation object if it is not found the return none"""
        for sation in self.Sations:
            if sation.name==sation_name:
               return sation
            return None
      
            
            
           
    
         
            
 