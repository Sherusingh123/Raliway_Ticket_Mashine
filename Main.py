import Station
import Printing

Station_instance=Station.Sations()
Printing_instance=Printing.Printing()

is_on=True
while is_on:
    print("Welcome to Railway Ticket Mashine")
    print("Select Your Sation")
    print(Station_instance.get_Sation())

    User_Choice=input("Where do you want to go:")
    
    if User_Choice=="off":
     is_on=False
    else:
        sation=Station_instance.find_Sation(User_Choice)
        if sation is None:
         print("not found ")
        else:
            if Printing_instance.is_resouce_sufficient():
                print("is enough resouce to print ticket")
       
          