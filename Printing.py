class Printing:
    def __init__(self):
        self.resoucce={
            "Page": 100,
            "Ink" :  500
            
        }
        
        def Report(self):
            pass
        
    def is_resouce_sufficient(self):
            """return true if print the tiket else return false"""
            for key in self.resoucce:
                if self.resoucce[key] < 1:
                    print("not enough resouce {key}")
                    return False
                return True
        
        
    def Print_Ticket(self):
            pass